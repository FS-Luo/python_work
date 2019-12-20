import pygame

class Ship:
    """创建一个飞船的类"""
    def __init__(self, ai_settings, screen):
        """初始化飞船并设置其初始位置"""
        self.screen = screen
        self.ai_settings = ai_settings
    
        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在飞船的属性 center 中存储浮点值
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)


        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        # 更新飞船的 self.center 值，而不是 rect
        # 更新左右位移        
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed

        # 更新上下位移
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed


        # 根据 self.center 更新 rect 对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)
