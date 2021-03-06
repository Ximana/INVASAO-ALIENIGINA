

class Configuracoes():
    """Classe para gurdar todas as definicoes do jogo Invasao Alien."""
    
    def __init__(self):
        """Inicializa as configuracoes do jogo."""
        
        # CONFIGURACOES DO ECRA
        self.screen_width = 1200
        self.screen_height = 700
        self.bg_color = (230, 230, 230)
        
        #CONFIGURACOES DA NAVE
        self.ship_speed_factor = 1.5
        
        #CONFIGURACOES DA BALA(BULLET)
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
        