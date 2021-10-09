from ship import Ship
import sys
import pygame
from pygame.constants import KEYUP, QUIT
from bullet import Bullet


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """QUANDO UM BOTAO E PRESSIONADO"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
    elif event.key == pygame.K_q:
        sys.exit()
        
        
def fire_bullet(ai_settings, screen, ship, bullets):
    """CRIAR NOVA BALA E ADICIONAR AO GRUPO DE BALAS SE LIMITE NAO ALCANCADO"""
    if len(bullets) < ai_settings.bullets_allowed:#LIMITA O NUMERO DE BALAS A 3
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
        
        

def check_keyup_events(event, ship):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Responder ao teclado e ao mouse"""
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
            
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
            #check_keydown_events(event, ship)
                
        elif event.type == KEYUP:
            check_keyup_events(event, ship)

            
# REDESENHE O ECRA A CADA PASSO NO LOOP
def update_screen(ai_settings, screen, ship, alien, bullets):
    """Atualizar a imagem no ecra e mover para o novo ecra"""
    screen.fill(ai_settings.bg_color)
    #REDESENHE TODAS AS BALAS ATRAS DA NAVE E DOS ALIENNS
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    
    ship.blitme()
    alien.blitme()
    
    # MOSTAR O DESENHO RECENT NO ECRA   
    pygame.display.flip()
    
    
    
def update_bullets(bullets):
    """ATUALIZAR A POSICAO DA BULA E APAGAR AS ANTIGAS"""
    #ATUALIZAR A POSICAO DA BALA
    bullets.update()  
        
    #ELIMINAR AS BALAS QUE DESAPARECERAM
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #print(len(bullets))    