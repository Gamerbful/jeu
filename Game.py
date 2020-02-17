import keyboard
import pygame
from pygame.locals import *
class Game:
    def __init__(self):
        pygame.init()
        self.windows=pygame.display.set_mode((1720, 900))
        self.svg=[]
        self.background_music="test.mp3"
        self.background_image="Background.png"
        self.fond=pygame.image.load(self.background_image).convert()
        self.windows.blit(self.fond, (0,0))
        self.font=pygame.font.SysFont("sitkasmallsitkatextbolditalicsitkasubheadingbolditalicsitkaheadingbolditalicsitkadisplaybolditalicsitkabannerbolditalic", 60)
        self.current_text=Text()
        self.game_running=True



    def run(self):
        pygame.display.set_caption('The mysterious journey')
        pygame.mixer.init()
        pygame.mixer.music.load(self.background_music)
        pygame.mixer.music.set_volume(0.1)
        pygame.mixer.music.play()
        icon = pygame.image.load("icon.png")
        pygame.display.set_icon(icon)

        text = self.font.render("Aventurier qui êtes vous?", True, (148,68,68))
        text2 = self.font.render("A : Femme  B : Homme", True, (148,68,68))
        self.windows.blit(text,(400,380))
        self.windows.blit(text2,(550,450))
        pygame.display.flip()

        continuer = True
        ispressed=True
        while continuer:
            for event in pygame.event.get():
                if event.type == KEYDOWN and ispressed:
                    if event.key == K_q:
                        self.fade()
                        self.game(0)
                    if event.key == K_b:
                        self.fade()
                        self.game(1)

                if event.type == QUIT:
                    continuer=False

    def game(self,y):
        self.appear(self.current_text.history())


    def fade(self):
        for alpha in range(0,100):
            self.fond.set_alpha(alpha)
            self.windows.blit(self.fond,(0,0))
            pygame.display.update()
            pygame.time.delay(15)



    def appear(self,text):
        effect = pygame.mixer.Sound("sound.wav")
        effect.play()
        dx=270
        dy=300
        self.windows.blit(self.fond, (0,0))
        for i in range (0,len(text)):
            t1,t2 = self.font.size(text[i])
            if dx>1400:
                dy+=60
                dx=270
            t=self.font.render(text[i], True, (148,68,68,0))
            self.windows.blit(t,(dx,dy))
            if t1>50:
                div=t1/2
            else:
                div=t1/3
            dx=dx+26+div

            pygame.display.update()
            pygame.time.delay(300)
        effect.stop()
        troll=pygame.image.load("th.jpg").convert()
        for i in range(0,100):
            troll.set_alpha(i)
            self.windows.blit(troll,(0,0))
            pygame.display.update()
            pygame.time.delay(100)

class Text:
    def __init__(self):
        self.script=["Bienvenue aventurier avez vous fait bon voyage, laissez moi me présenter je suis Normal Man","Hipipipi Houra! ah ah ah ah","Naniiiiiiiiiiiiii"]
        self.step=-1

    def inc_step(self):
        self.step+=1

    def get_script(self,x):
        return self.script[x]

    def history(self):
        self.inc_step()
        return self.get_script(self.step)


Game().run()
