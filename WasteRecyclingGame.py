import pygame
import random
import GameObjects
import GameObjects.VehicleModel
#import tkinter as tk
#from tkinter import Menu

pygame.init()

screen = pygame.display.set_mode( (800, 600) )
pygame.display.set_caption("Waste & Recycling")
game_running = True

vehicle = GameObjects.VehicleModel.vehicleModel()
vehiclePosition = [100,100]
moveVehicle = 0 #to avoid getting stop after a first key beeing up, this is an int and the vehicle will stop when this has the value 0
vehicleDirection = GameObjects.VehicleModel.Directions

screen.blit(vehicle.getVehicleSurface(GameObjects.VehicleModel.Directions.RIGHT), vehiclePosition )

while game_running:
    
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False
            
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_LEFT:
                moveVehicle += 1
                vehicleDirection = GameObjects.VehicleModel.Directions.LEFT
            if event.key == pygame.K_UP:
                moveVehicle += 1
                vehicleDirection = GameObjects.VehicleModel.Directions.UP
            if event.key == pygame.K_RIGHT:
                moveVehicle += 1
                vehicleDirection = GameObjects.VehicleModel.Directions.RIGHT
            if event.key == pygame.K_DOWN:
                moveVehicle += 1
                vehicleDirection = GameObjects.VehicleModel.Directions.DOWN
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                moveVehicle -= 1
                screen.blit(vehicle.getVehicleSurface(vehicleDirection), vehiclePosition)
            
    if moveVehicle > 0:
        screen.fill("black")
        if vehicleDirection == GameObjects.VehicleModel.Directions.LEFT:
            vehiclePosition[0] -= 0.1
            screen.blit(vehicle.getVehicleSurface(GameObjects.VehicleModel.Directions.LEFT), vehiclePosition )
        if vehicleDirection == GameObjects.VehicleModel.Directions.UP:
            vehiclePosition[1] -= 0.1
            screen.blit(vehicle.getVehicleSurface(GameObjects.VehicleModel.Directions.UP), vehiclePosition)
        if vehicleDirection == GameObjects.VehicleModel.Directions.RIGHT:
            vehiclePosition[0] += 0.1
            screen.blit(vehicle.getVehicleSurface(GameObjects.VehicleModel.Directions.RIGHT), vehiclePosition )
        if vehicleDirection == GameObjects.VehicleModel.Directions.DOWN:
            vehiclePosition[1] += 0.1
            screen.blit(vehicle.getVehicleSurface(GameObjects.VehicleModel.Directions.DOWN), vehiclePosition )
            
            
pygame.quit()

