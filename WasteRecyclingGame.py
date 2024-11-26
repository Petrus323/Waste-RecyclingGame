import pygame
import random
import GameObjects
import GameObjects.MapModel
import GameObjects.VehicleModel
#import tkinter as tk
#from tkinter import Menu

pygame.init()

screen = pygame.display.set_mode( (800, 600) )
pygame.display.set_caption("Waste & Recycling")
game_running = True
keyPressedCounter = 0 #to avoid getting stop after a first key beeing up, this is an int and the vehicle will stop when this has the value 0

vehicle = GameObjects.VehicleModel.vehicleModel()

map = GameObjects.MapModel.mapModel()

screen.blit(map.getMapSurface(), map.getMapPosition())
screen.blit(vehicle.getVehicleSurface(), vehicle.getVehiclePosition())

while game_running:
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                keyPressedCounter += 1
                vehicle.setVehicleDirection(vehicle.Directions.LEFT)
            if event.key == pygame.K_UP:
                keyPressedCounter += 1
                vehicle.setVehicleDirection(vehicle.Directions.UP)
            if event.key == pygame.K_RIGHT:
                keyPressedCounter += 1
                vehicle.setVehicleDirection(vehicle.Directions.RIGHT)
            if event.key == pygame.K_DOWN:
                keyPressedCounter += 1
                vehicle.setVehicleDirection(vehicle.Directions.DOWN)
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                keyPressedCounter -= 1
                screen.blit(vehicle.getVehicleSurface(), vehicle.getVehiclePosition())
            
    #updates the screen when the vehicle is moving
    if keyPressedCounter > 0:
        screen.fill("black")
                
        #check if the vehicle is moving to the left
        if vehicle.vehicleDirection == vehicle.Directions.LEFT:
            #check if the vehicle is on the middle of the screen width
            if vehicle.getVehiclePosition()[0] > screen.get_width()/2 and map.getMapPosition()[0] <= 0:
                #move the map to the right
                map.moveMapPosition(vehicle.getVehicleSpeed(), 0)
            else:
                #move the vehicle to the left
                vehicle.moveVehiclePosition(-vehicle.getVehicleSpeed(), 0)
        #check if the vehicle is moving up
        if vehicle.vehicleDirection == vehicle.Directions.UP:
            #check if the vehicle is on the middle of the screen height
            if vehicle.getVehicleRect()[1] > screen.get_height()/2:
                #move the map down
                map.moveMapPosition(0, vehicle.getVehicleSpeed())
            else:
                #move the vehicle up
                vehicle.moveVehiclePosition(0, -vehicle.getVehicleSpeed())
        #check if the vehicle is moving to the right
        if vehicle.vehicleDirection == vehicle.Directions.RIGHT:
            #check if the vehicle is on the middle of the screen width
            if vehicle.getVehiclePosition()[0] > screen.get_width()/2:
                #move the map to the left
                map.moveMapPosition(-vehicle.getVehicleSpeed(), 0)
            else:
                #move the vehicle to the right
                vehicle.moveVehiclePosition(vehicle.getVehicleSpeed(), 0)
        #check if the vehicle is moving down
        if vehicle.vehicleDirection == vehicle.Directions.DOWN:
            #check if the vehicle is on the middle of the screen height
            if vehicle.getVehicleRect()[1] > screen.get_height()/2:
                #move the map up
                map.moveMapPosition(0, -vehicle.getVehicleSpeed())
            else:
                #move the vehicle down
                vehicle.moveVehiclePosition(0, vehicle.getVehicleSpeed())
            
        screen.blit(map.getMapSurface(), map.getMapPosition())
        screen.blit(vehicle.getVehicleSurface(), vehicle.getVehiclePosition() )
            
pygame.quit()

