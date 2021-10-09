import pygame
from pygame import sprite
from pygame.sprite import Sprite

class Alien(Sprite):
    """CLASSE PARA REPRESENTAR UMA ALIEN NA FROTA"""
    def __init__(self, ai_settings, screen):
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
        #CARREGAR A IMAGEM DO ALIEN E E CONFIGURAR O SEU RECT
        self.image = pygame.image.load('imagens/alien.png')
        self.rect = self.image.get_rect()
        
        #COMECAR CADA NOVO ALIEN NO CANTO SUPERIOR ESQUERDO DO ECRA
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        #GUARGAR A POSICAO EXATA DO ALIEN
        self.x = float(self.rect.x)
        
    def blitme(self):
        """DESENHAR O ALIEN NA SUA POSICAO ATUAL"""
        self.screen.blit(self.image, self.rect)
            
        
        
        