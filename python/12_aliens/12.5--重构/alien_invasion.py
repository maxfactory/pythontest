import pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	"""初始化pygame，设置和屏幕对象"""
	ai_settings = Settings()
	screen = pygame.display.set_mode(
		(ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")

	# 创建一般飞船
	ship = Ship(screen)

	while True:
		gf.check_events()
		gf.update_screen(ai_settings,screen,ship)

		# 让最近绘制的屏幕可见
		# 每次循环时都重绘屏幕
		# screen.fill(ai_settings.bg_color)
		# ship.blitme()

		# 让最近绘制的屏幕可见
		pygame.display.flip()

run_game()