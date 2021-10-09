import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """CLASSE PARA CONFIGURAR A BALA DA NAVE"""
    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        
        #CRIAR UMA BALA RECT(0, 0) A DEFINIR A POSICAO CORRETA
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        
        #GUARDAR A POSICAO DA BALA COMO VALOR DECIMAL
        self.y = float(self.rect.y)
        
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
        
    def update(self):
        """MOVER A BALA PARA O TOPO DO ECRA"""
        #ATUALIZAR A POSICAO DECIMAL DA BALA
        self.y -= self.speed_factor
        #ATUALIZA A POSICAO DO RECT
        self.rect.y = self.y
        
    def draw_bullet(self):
        """DESENHAR A BALA NO ECRA"""
        pygame.draw.rect(self.screen, self.color, self.rect)