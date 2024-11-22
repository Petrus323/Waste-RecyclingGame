# This is a representation of the waste vehicle

import pygame

from enum import Enum

class Directions(Enum):
    LEFT = 0
    UP = 1
    RIGHT = 2
    DOWN = 3

class vehicleModel:
    vehicleImages = []

    def __init__(self):    
        self.vehicleImages = ["GameAssets/vehicle/vehicle_left.png", "GameAssets/vehicle/vehicle_up.png", "GameAssets/vehicle/vehicle_right.png", "GameAssets/vehicle/vehicle_down.png"]
        
    def getVehicleSurface(self, direction: Directions) -> pygame.Surface:
        return pygame.image.load(self.vehicleImages[direction.value]).convert_alpha()
    