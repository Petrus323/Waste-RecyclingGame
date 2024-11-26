# This is a representation of the waste vehicle

import pygame

from enum import Enum

class vehicleModel:
    
    Directions = Enum('Direction', [('LEFT', 0), ('UP', 1), ('RIGHT', 2), ('DOWN', 3)])
    
    vehicleSurface = pygame.Surface
    vehicleRect = pygame.Rect
    vehiclePosition = [100,100]
    vehicleImages = []
    vehicleDirection = Directions.RIGHT
    vehicleSpeed = 0.5

    def __init__(self):    
        self.vehicleImages = ["GameAssets/vehicle/vehicle_left.png", "GameAssets/vehicle/vehicle_up.png", "GameAssets/vehicle/vehicle_right.png", "GameAssets/vehicle/vehicle_down.png"]
    
    def getVehicleSurface(self):
        self.vehicleSurface = pygame.image.load(self.vehicleImages[self.vehicleDirection.value]).convert_alpha()
        self.vehicleRect = self.vehicleSurface.get_rect()
        self.vehicleRect.center = self.vehiclePosition
        return self.vehicleSurface
    
    def setVehicleDirection(self, newDirection : Directions):
        self.vehicleDirection = newDirection
        
    def getVehicleDirection(self):
        return self.vehicleDirection
        
    def getVehicleRect(self):
        return self.vehicleRect
    
    def moveVehiclePosition(self, addX, addY):
        self.vehiclePosition[0] += addX
        self.vehiclePosition[1] += addY
        
    def getVehiclePosition(self):
        return self.vehiclePosition   
    
    def getVehicleSpeed(self):
        return self.vehicleSpeed
    