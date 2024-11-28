import pygame
import GameObjects.MapModel
import GameObjects.VehicleModel
import pygame_menu
from datetime import timedelta

class gameModel:
    
    screenDimensions = (0,0)
    gameTitle = ""
    screen = pygame.Surface
    gameRunning = False
    keyPressedCounter = 0 #to avoid getting stop after a first key beeing up, this is an int and the vehicle will stop when this has the value 0
    vehicleSurface = GameObjects.VehicleModel
    mapSurface = GameObjects.MapModel
    playerScore = 0
    timerFont = pygame.font
    timerPosition = (100, 100)
    maxLevelTime = timedelta(minutes=2)

    def __init__(self, gameTitle, screenDimensions):
        pygame.init()
        
        self.gameTitle = gameTitle
        self.screenDimensions = screenDimensions
        
        self.screen = pygame.display.set_mode( screenDimensions )
        pygame.display.set_caption(gameTitle)
        
        self.timerFont = pygame.font.SysFont("freesans", 32)
        
        self.vehicleSurface = GameObjects.VehicleModel.vehicleModel()
        self.mapSurface = GameObjects.MapModel.mapModel()

    def startGame(self):
        self.game_running = True
        self.screen.fill("black")
        self.screen.blit(self.mapSurface.getMapSurface(), self.mapSurface.getMapPosition())
        self.screen.blit(self.vehicleSurface.getVehicleSurface(), self.vehicleSurface.getVehiclePosition())
        
        while self.game_running:
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    
                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_LEFT:
                        self.keyPressedCounter += 1
                        self.vehicleSurface.setVehicleDirection(self.vehicleSurface.Directions.LEFT)
                    if event.key == pygame.K_UP:
                        self.keyPressedCounter += 1
                        self.vehicleSurface.setVehicleDirection(self.vehicleSurface.Directions.UP)
                    if event.key == pygame.K_RIGHT:
                        self.keyPressedCounter += 1
                        self.vehicleSurface.setVehicleDirection(self.vehicleSurface.Directions.RIGHT)
                    if event.key == pygame.K_DOWN:
                        self.keyPressedCounter += 1
                        self.vehicleSurface.setVehicleDirection(self.vehicleSurface.Directions.DOWN)
                        
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_UP or event.key == pygame.K_RIGHT or event.key == pygame.K_DOWN:
                        self.keyPressedCounter -= 1
                        self.screen.blit(self.vehicleSurface.getVehicleSurface(), self.vehicleSurface.getVehiclePosition())
                    
            #updates the screen when the vehicle is moving
            if self.keyPressedCounter > 0:
                self.screen.fill("black")        
                #check if the vehicle is moving to the left
                if self.vehicleSurface.vehicleDirection == self.vehicleSurface.Directions.LEFT:
                    #check if the vehicle is on the middle of the screen width
                    if self.vehicleSurface.getVehiclePosition()[0] > self.screen.get_width()/2 and self.mapSurface.getMapPosition()[0] <= 0:
                        #move the map to the right
                        self.mapSurface.moveMapPosition(self.vehicleSurface.getVehicleSpeed(), 0)
                    else:
                        #move the vehicle to the left
                        self.vehicleSurface.moveVehiclePosition(-self.vehicleSurface.getVehicleSpeed(), 0)
                #check if the vehicle is moving up
                if self.vehicleSurface.vehicleDirection == self.vehicleSurface.Directions.UP:
                    #check if the vehicle is on the middle of the screen height
                    if self.vehicleSurface.getVehicleRect()[1] > self.screen.get_height()/2:
                        #move the map down
                        self.mapSurface.moveMapPosition(0, self.vehicleSurface.getVehicleSpeed())
                    else:
                        #move the vehicle up
                        self.vehicleSurface.moveVehiclePosition(0, -self.vehicleSurface.getVehicleSpeed())
                #check if the vehicle is moving to the right
                if self.vehicleSurface.vehicleDirection == self.vehicleSurface.Directions.RIGHT:
                    #check if the vehicle is on the middle of the screen width
                    if self.vehicleSurface.getVehiclePosition()[0] > self.screen.get_width()/2:
                        #move the map to the left
                        self.mapSurface.moveMapPosition(-self.vehicleSurface.getVehicleSpeed(), 0)
                    else:
                        #move the vehicle to the right
                        self.vehicleSurface.moveVehiclePosition(self.vehicleSurface.getVehicleSpeed(), 0)
                #check if the vehicle is moving down
                if self.vehicleSurface.vehicleDirection == self.vehicleSurface.Directions.DOWN:
                    #check if the vehicle is on the middle of the screen height
                    if self.vehicleSurface.getVehicleRect()[1] > self.screen.get_height()/2:
                        #move the map up
                        self.mapSurface.moveMapPosition(0, -self.vehicleSurface.getVehicleSpeed())
                    else:
                        #move the vehicle down
                        self.vehicleSurface.moveVehiclePosition(0, self.vehicleSurface.getVehicleSpeed())
                    
                self.screen.blit(self.mapSurface.getMapSurface(), self.mapSurface.getMapPosition())
                self.screen.blit(self.vehicleSurface.getVehicleSurface(), self.vehicleSurface.getVehiclePosition() )
                
            #calculate and show the count down
            #show the score if the time is over
            if self.calcCountDown():
                self.showScore('GAME OVER')

        self.showScore('')
        
    def calcCountDown(self):
        #draw a timer board
        timerBoard = pygame.Surface((100, 50))
        timerBoard.fill("black")
        timerBoardRect = timerBoard.get_rect() 
        timerBoardRect.center = self.timerPosition
        self.screen.blit(timerBoard, timerBoardRect)
        
        #calculate the time and show it over the timer board
        millis = timedelta(milliseconds=pygame.time.get_ticks())
        timeLeft = (self.maxLevelTime - millis)
        result = ("%s:%s" % (str(int(timeLeft.seconds/60)), str(f"{timeLeft.seconds%60:02}")))
        timerSurface = self.timerFont.render(result, True, "white")
        timerSurfaceRect = timerSurface.get_rect()
        timerSurfaceRect.center = self.timerPosition
        self.screen.blit(timerSurface, timerSurfaceRect)
        
        return timeLeft.seconds == 0
    
    def quitGame(self):
        exit()
        
    def showScore(self, title):
        mainmenu = pygame_menu.Menu(title, width = 400, height = 300)
        mainmenu.add.label('Score: ' + str(self.playerScore))
        mainmenu.add.label("")
        mainmenu.add.button('Quit', pygame_menu.events.EXIT)

        mainmenu.mainloop(self.screen)
        
        
    # def pickContainer():
        