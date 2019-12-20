import sys, pygame
from bullet import Bullet

def check_key_down(event, ai_settings, screen, ship, bullets):
    """响应按下键盘"""
    # 响应 Esc 退出游戏
    if event.key == pygame.K_ESCAPE:
        pygame.quit()
        exit()
    # 响应按下左右键
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 响应按下上下键
    if event.key == pygame.K_UP:
        ship.moving_up = True
    if event.key == pygame.K_DOWN:
        ship.moving_down = True
    # 响应空格键 开火
    if event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def check_key_up(event, ship):
    """响应松开键盘"""
    # 响应松开左右键 
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    
    # 响应松开上下键
    if event.key == pygame.K_UP:
        ship.moving_up = False
    if event.key == pygame.K_DOWN:
        ship.moving_down = False

def fire_bullet(ai_settings, screen, ship, bullets):
    """如果还没有达到限制， 就发射一颗子弹"""
    # 创建新子弹，并将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)     

def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.KEYDOWN:
            check_key_down(event, ai_settings, screen, ship, bullets)
        if event.type == pygame.KEYUP:
            check_key_up(event, ship)
        
def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 让最近绘制的屏幕可见
    pygame.display.flip()

def update_bullets(bullets):
    """更新子弹的位置，并删除已消失的子弹"""
    # 更新子弹的位置
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
