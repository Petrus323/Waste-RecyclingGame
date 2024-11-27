import pygame
import random
import GameObjects
import GameObjects.GameModel
import GameObjects.MapModel
import GameObjects.VehicleModel
import pygame_menu
from pygame_menu import themes

game = GameObjects.GameModel.gameModel("Waste & Recycling", (800, 600))

#menu
mainmenu = pygame_menu.Menu(game.gameTitle, game.screenDimensions[0], game.screenDimensions[1], theme=themes.THEME_SOLARIZED)
mainmenu.add.button('Play', game.startGame)
mainmenu.add.button('Quit', pygame_menu.events.EXIT)

mainmenu.mainloop(game.screen)