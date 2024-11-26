import pygame

class mapModel:
    mapSurface = pygame.Surface
    mapPosition = [0, 0]
    
    def __init__(self):
        mapSurface = pygame.image.load("GameAssets/map/map.png").convert_alpha()
        self.mapSurface = mapSurface.subsurface(350, 750, 2000, 2000) #delete this after the map beeing finish
        
    def getMapSurface(self):
        return self.mapSurface
    
    def moveMapPosition(self, addX, addY):
        self.mapPosition[0] += addX
        self.mapPosition[1] += addY
        
    def getMapPosition(self):
        return self.mapPosition   
