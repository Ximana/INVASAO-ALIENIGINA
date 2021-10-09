 
import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Inicializa o nave e defini a sua posico inicial"""
        self.screen = screen
        self.ai_settings = ai_settings
        
        #Carregar a imagem da nave 
        self.image = pygame.image.load('imagens/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        
        #Iniciar cada nova nave na parte central e baixa do ecra
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        #GUARDAR UM VALOR DECIMAL PARA O CENTRO DA NAVE
        self.center = float(self.rect.centerx)
        
        #MOVIMENTo FLAG
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """ATUALIZAR A POSICAO A NAV BASEADO NO MOVIMENTO FLAG"""
        #ATUALIAR O VALOR DO CENTRO DA NAVE, NAO O RECT
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        
        # Update rect object from self.center.
        self.rect.centerx = self.center
    
    def blitme(self):
        """Desenhar a nave na localizacao atual"""
        self.screen.blit(self.image, self.rect)