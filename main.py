from turtle import width
import pygame
import time
from pygame.locals import *
import random



class Game:
    # Initializing the game and creating the window
    def __init__(self):
        pygame.init()

    def play(self):
        self.surface = pygame.display.set_mode((600,700))
        self.surface.fill((255,255,255))
        bg = pygame.image.load('resources\Sunset.png')
        self.surface.blit(bg, (0,0))
        pygame.display.set_caption("Green Screen Game")
        pygame.display.update()
        game.draw_tiles()

    def home(self):
        self.surface = pygame.display.set_mode((600,700))
        self.surface.fill((255,255,255))
        homescreen = pygame.image.load('resources\Homescreen.png')
        self.surface.blit(homescreen, (0,0))
        pygame.display.set_caption("Green Screen Game")
        self.home = 0
        play_again = pygame.image.load('resources\Play.png')
        self.surface.blit(play_again,(253,100))
        pygame.display.update()
        game.run()
    
    def run(self):
        #Event loop condition
        isrunning = True
        self.victory = False
        self.color = (13, 111, 209)
        self.click = 0
        self.font = pygame.font.SysFont('rockwellextra', 32)

        #Event loop
        while isrunning:
            #Exit condition
            for event in pygame.event.get():
                #finding the exact position of the mouse
                self.mouse = pygame.mouse.get_pos()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.home == 0:
                        if 253 <= self.mouse[0] <= 253+95 and 100 <= self.mouse[1] <= 100+75:
                            self.home = 1
                            game.full_fade()
                            game.play()
                    else:       
                        if self.victory == False:
                            game.colorswitch()
                            game.clicks()
                            #game.restart
                            game.vict()
                        else: 
                            game.endscreen()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:

                        isrunning = False
                elif event.type == QUIT:
                    isrunning = False

    def clicks(self):
        s_click = "Clicks:" + str(self.click)
        text = self.font.render(s_click, True, (255,255,255), (115,10,52))
        textRect = text.get_rect()
        textRect.center = (100 ,650)
        self.surface.blit(text, textRect)
        pygame.display.update()

    def endscreen(self):
        if 150 <= self.mouse[0] <= 150+95 and 550 <= self.mouse[1] <= 550+75:
            game.full_fade()
            game.play()

    def half_fade(self):
        fade = pygame.Surface((600,700))
        fade.fill((136, 67, 209))
        for alpha in range (0,25):
            fade.set_alpha(alpha)
            self.surface.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(15)

    def full_fade(self):
        fade = pygame.Surface((600,700))
        fade.fill((0,0,0))
        for alpha in range (0,300):
            fade.set_alpha(alpha)
            self.surface.blit(fade, (0,0))
            pygame.display.update()
            pygame.time.delay(5)

    def vict(self):
        check =0
        for num in self.counter:
            check = (num%2) + check
        if check == 9:
            game.half_fade()
            victory_screen = pygame.image.load('resources\Victory.png')
            play_again = pygame.image.load('resources\Play.png')
            white_space = pygame.Surface((373,112))
            white_space.fill((255,255,255))
            self.victory = True

            for alpha in range(0,300):
                victory_screen.set_alpha(alpha)
                play_again.set_alpha(alpha)
                white_space.set_alpha(alpha)
                self.surface.blit(white_space, (104, 530))
                self.surface.blit(play_again, (150, 550))
                self.surface.blit(victory_screen, (58,273))
                pygame.display.update()
                pygame.time.delay(5)

    def randomize_tiles(self):
        self.counter = []
        x = 0
        while x in range(0,9):
            x = x + 1
            self.counter.append(random.randint(0,1))

    def draw_tiles(self):
        #setting colors of buttons
        self.bcolor = (13, 111, 209)
        self.gcolor = (5, 153, 50)

        game.randomize_tiles()
        
        pygame.draw.rect(self.surface,(0,0,0), [95,95,395,395])

        if self.counter[0] % 2 == 1:
            color = self.gcolor
            pygame.draw.rect(self.surface,color,[100,100, 125,125])
        else:
            color = self.bcolor
            pygame.draw.rect(self.surface,color,[100,100, 125,125])
        if self.counter[1] % 2 == 1:
            color = self.gcolor
            pygame.draw.rect(self.surface,color,[230,100, 125,125])
        else:
            color = self.bcolor
            pygame.draw.rect(self.surface,color,[230,100, 125,125])
        if self.counter[2] % 2 == 1:
            color = self.gcolor
            pygame.draw.rect(self.surface,color,[360,100, 125,125])
        else:
            color = self.bcolor
            pygame.draw.rect(self.surface,color,[360,100, 125,125])
        if self.counter[3] % 2 == 1:
            color = self.gcolor
            pygame.draw.rect(self.surface,color,[100,230, 125,125])
        else:
            color = self.bcolor
            pygame.draw.rect(self.surface,color,[100,230, 125,125])
        if self.counter[4] % 2 == 1:
            color = self.gcolor
            pygame.draw.rect(self.surface,color,[230,230, 125,125])
        else:
            color = self.bcolor
            pygame.draw.rect(self.surface,color,[230,230, 125,125])
        if self.counter[5] % 2 == 1:
            color = self.gcolor
            pygame.draw.rect(self.surface,color,[360,230, 125,125])
        else:
            color = self.bcolor
            pygame.draw.rect(self.surface,color,[360,230, 125,125])
        if self.counter[6] % 2 == 1:
            color = self.gcolor
            pygame.draw.rect(self.surface,color,[100,360, 125,125])
        else:
            color = self.bcolor
            pygame.draw.rect(self.surface,color,[100,360, 125,125])
        if self.counter[7] % 2 == 1:
            color = self.gcolor
            pygame.draw.rect(self.surface,color,[230,360, 125,125])
        else:
            color = self.bcolor
            pygame.draw.rect(self.surface,color,[230,360, 125,125])
        if self.counter[8] % 2 == 1:
            color = self.gcolor
            pygame.draw.rect(self.surface,color,[360,360, 125,125])
        else:
            color = self.bcolor
            pygame.draw.rect(self.surface,color,[360,360, 125,125])
        
        pygame.display.update()
        game.run()

    def colorswitch(self):
        if 100 <= self.mouse[0] <= 100+125 and 100 <= self.mouse[1] <= 100+125:
            if self.counter[0] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,100, 125,125])
                self.counter[0] = self.counter[0] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,100, 125,125])
                self.counter[0] = self.counter[0] + 1
            if self.counter[1] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,100, 125,125])
                self.counter[1] = self.counter[1] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,100, 125,125])
                self.counter[1] = self.counter[1] + 1
            if self.counter[3] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,230, 125,125])
                self.counter[3] = self.counter[3] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,230, 125,125])
                self.counter[3] = self.counter[3] + 1
            self.click = self.click +1

        if 230 <= self.mouse[0] <= 230+125 and 100 <= self.mouse[1] <= 100+125:
            self.click = self.click +1
            if self.counter[0] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,100, 125,125])
                self.counter[0] = self.counter[0] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,100, 125,125])
                self.counter[0] = self.counter[0] + 1
            if self.counter[1] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,100, 125,125])
                self.counter[1] = self.counter[1] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,100, 125,125])
                self.counter[1] = self.counter[1] + 1
            if self.counter[2] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,100, 125,125])
                self.counter[2] = self.counter[2] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,100, 125,125])
                self.counter[2] = self.counter[2] + 1
            if self.counter[4] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1        
        if 360 <= self.mouse[0] <= 360+125 and 100 <= self.mouse[1] <= 100+125:
            self.click = self.click +1
            if self.counter[1] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,100, 125,125])
                self.counter[1] = self.counter[1] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,100, 125,125])
                self.counter[1] = self.counter[1] + 1
            if self.counter[2] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,100, 125,125])
                self.counter[2] = self.counter[2] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,100, 125,125])
                self.counter[2] = self.counter[2] + 1
            if self.counter[5] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,230, 125,125])
                self.counter[5] = self.counter[5] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,230, 125,125])
                self.counter[5] = self.counter[5] + 1

        if 100 <= self.mouse[0] <= 100+125 and 230 <= self.mouse[1] <= 230+125:
            self.click = self.click +1
            if self.counter[3] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,230, 125,125])
                self.counter[3] = self.counter[3] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,230, 125,125])
                self.counter[3] = self.counter[3] + 1
            if self.counter[0] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,100, 125,125])
                self.counter[0] = self.counter[0] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,100, 125,125])
                self.counter[0] = self.counter[0] + 1
            if self.counter[4] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1
            if self.counter[6] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,360, 125,125])
                self.counter[6] = self.counter[6] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,360, 125,125])
                self.counter[6] = self.counter[6] + 1
            
        if 230 <= self.mouse[0] <= 230+125 and 230 <= self.mouse[1] <= 230+125:
            self.click = self.click +1
            if self.counter[4] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1
            if self.counter[1] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,100, 125,125])
                self.counter[1] = self.counter[1] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,100, 125,125])
                self.counter[1] = self.counter[1] + 1
            if self.counter[3] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,230, 125,125])
                self.counter[3] = self.counter[3] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,230, 125,125])
                self.counter[3] = self.counter[3] + 1
            if self.counter[5] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,230, 125,125])
                self.counter[5] = self.counter[5] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,230, 125,125])
                self.counter[5] = self.counter[5] + 1
            if self.counter[7] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,360, 125,125])
                self.counter[7] = self.counter[7] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,360, 125,125])
                self.counter[7] = self.counter[7] + 1
        if 360 <= self.mouse[0] <= 360+125 and 230 <= self.mouse[1] <= 230+125:
            self.click = self.click +1
            if self.counter[5] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,230, 125,125])
                self.counter[5] = self.counter[5] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,230, 125,125])
                self.counter[5] = self.counter[5] + 1
            if self.counter[2] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,100, 125,125])
                self.counter[2] = self.counter[2] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,100, 125,125])
                self.counter[2] = self.counter[2] + 1
            if self.counter[4] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1
            if self.counter[8] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,360, 125,125])
                self.counter[8] = self.counter[8] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,360, 125,125])
                self.counter[8] = self.counter[8] + 1

        if 100 <= self.mouse[0] <= 100+125 and 360 <= self.mouse[1] <= 360+125:
            self.click = self.click +1
            if self.counter[6] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,360, 125,125])
                self.counter[6] = self.counter[6] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,360, 125,125])
                self.counter[6] = self.counter[6] + 1
            if self.counter[7] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,360, 125,125])
                self.counter[7] = self.counter[7] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,360, 125,125])
                self.counter[7] = self.counter[7] + 1
            if self.counter[3] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,230, 125,125])
                self.counter[3] = self.counter[3] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,230, 125,125])
                self.counter[3] = self.counter[3] + 1
        if 230 <= self.mouse[0] <= 230+125 and 360 <= self.mouse[1] <= 360+125:
            self.click = self.click +1
            if self.counter[7] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,360, 125,125])
                self.counter[7] = self.counter[7] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,360, 125,125])
                self.counter[7] = self.counter[7] + 1
            if self.counter[8] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,360, 125,125])
                self.counter[8] = self.counter[8] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,360, 125,125])
                self.counter[8] = self.counter[8] + 1
            if self.counter[6] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[100,360, 125,125])
                self.counter[6] = self.counter[6] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[100,360, 125,125])
                self.counter[6] = self.counter[6] + 1
            if self.counter[4] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,230, 125,125])
                self.counter[4] = self.counter[4] + 1
        if 360 <= self.mouse[0] <= 360+125 and 360 <= self.mouse[1] <= 360+125:
            self.click = self.click +1
            if self.counter[8] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,360, 125,125])
                self.counter[8] = self.counter[8] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,360, 125,125])
                self.counter[8] = self.counter[8] + 1
            if self.counter[5] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[360,230, 125,125])
                self.counter[5] = self.counter[5] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[360,230, 125,125])
                self.counter[5] = self.counter[5] + 1
            if self.counter[7] % 2 == 0:
                color = self.gcolor
                pygame.draw.rect(self.surface,color,[230,360, 125,125])
                self.counter[7] = self.counter[7] + 1
            else:
                color = self.bcolor
                pygame.draw.rect(self.surface,color,[230,360, 125,125])
                self.counter[7] = self.counter[7] + 1

        pygame.display.update()

 
if __name__ == "__main__":
    game = Game()
    game.home()