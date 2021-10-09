from bullet import Bullet
import sys
import pygame
from configuracoes import Configuracoes
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    # INICIALIZR O PYGAME, CONFIGURACOES E OBJECTOS DO ECRA
    pygame.init()
    ai_configuracoes = Configuracoes()
    screen = pygame.display.set_mode((ai_configuracoes.screen_width, ai_configuracoes.screen_height))
    pygame.display.set_caption("Invasao Alien")
    
    #CRIAR OBJETO NAVE
    ship = Ship(ai_configuracoes,screen)
    #CRIAR OBJECTO ALIEN
    alien = Alien(ai_configuracoes, screen)
    
    
    #FAZER UM GROUP PARA ARMAZENAR BALAS
    bullets = Group()
 
    
    # INICIAR O LOOP PRINCIPAL PARA O JOGO
    while True:
        
        # VER O EVENTO DO TECLADO E DO MOUSE
        gf.check_events(ai_configuracoes, screen, ship, bullets)    
        ship.update()     
        gf.update_bullets(bullets)
                         
        # REDESENHE O ECRA A CADA PASSO NO LOOP
        gf.update_screen(ai_configuracoes, screen, ship, alien, bullets)
    
run_game()