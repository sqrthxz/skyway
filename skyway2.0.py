import pygame, sys, os, ctypes
from pygame.locals import *


#set tamanho da tela do jogo
largura = 400
altura = 600
setTop = 20

# -------------------------------------- INIMIGOS ------------------------------------

class Enemy1(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load("images/enemy1.png")
        self.rect = self.ImageEnemy.get_rect()

        self.rect.top = posy
        self.rect.left = posx

    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)

class Enemy2(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/enemy2.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)

class Enemy3(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/enemy3.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie): #coloca img na tela
        superficie.blit(self.ImageEnemy, self.rect)

class Enemy4(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/enemy4.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)


# ------------------------------------------------------------------------------------



class Bala(pygame.sprite.Sprite): #set projetil
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load("images/laser.png")
        self.rect = self.ImagemBala.get_rect()
        self.teste = self.ImagemBala.get_rect()
        self.velocidadeBala = 10
        self.rect.top = posy
        self.rect.left = posx


    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeBala

    def colocar(self,superficie): #coloca img na tela
        superficie.blit(self.ImagemBala, self.rect)



#----------------------------------------------------
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load("images/player.png")

        self.rect = self.ImagemNave.get_rect()
        #set posicao inicial
        self.rect.centerx = largura/2
        self.rect.centery = altura - 55
        self.listaDisparo = [] #onde add bullets
        self.vida = True
        self.velocidade= 70 #vel de mov player

    def movimento(self): #set limite do movimento do player
        if self.vida == True:
            if self.rect.left < 4: #esquerda
                self.rect.left = 4
            elif self.rect.right > 395: #direita
                self.rect.right = 395

    def disparar(self, x, y): #set dispara o projetil
        minhaBala = Bala(x,y)
        self.listaDisparo.append(minhaBala)

    def colocar(self, superficie):
        superficie.blit(self.ImagemNave, self.rect)

def invasaoEspaco():
    pygame.init()
    tela = pygame.display.set_mode((largura, altura))#tamanho da tela
    pygame.display.set_caption("Skyway")
    cont = 0

    e1= 20
    e2= 20
    e3= 20
    e4= 20
    e5= 90
    e6= 90
    e7= 90
    e8= 160
    e9= 160
    e10= 160
    e11= 160
    con= 0.10


    lado1=40
    lado2=130
    lado3=220
    lado4=310
    lado5=85
    lado6=177
    lado7=269
    lado8=40
    lado9=130
    lado10=220
    lado11=310

    p= 475 #pos para perder
    jogador = player()
    bala = Bala(largura /2, altura - 55)






    jogando = True
    bg = pygame.image.load("images/bg.png")
    relogio = pygame.time.Clock()

    def win():
        if cont == 11 and len(jogador.listaDisparo) >= 1:
            ctypes.windll.user32.MessageBoxW(0, "You win!", "Congrats!", 1)
            pygame.quit()

    def lose():
        if e1 > p  or e2 > p or e3 > p or e4 > p or e5 > p or e6 > p or e7> p or e8 > p or e9 > p or e10 > p or e11 > p:
            ctypes.windll.user32.MessageBoxW(0, "Perdi XD!", "Congrats!", 1)
            pygame.quit()
    while True:

        relogio.tick(60) #fps
        jogador.movimento()
        #-------------posicao dos inimigos------------
        enemy1 = Enemy3(lado1,e1)
        enemy2 = Enemy2(lado2,e2)
        enemy3 = Enemy4(lado3,e3)
        enemy4 = Enemy1(lado4,e4)
        enemy5 = Enemy4(lado5,e5)
        enemy6 = Enemy3(lado6,e6)
        enemy7 = Enemy1(lado7,e7)
        enemy8 = Enemy2(lado8,e8)
        enemy9 = Enemy3(lado9,e9)
        enemy10 = Enemy1(lado10,e10)
        enemy11 = Enemy4(lado11,e11)

        e1+=con
        e2+=con
        e3+=con
        e4+=con
        e5+=con
        e6+=con
        e7+=con
        e8+=con
        e9+=con
        e10+=con
        e11+=con
        #------------------------------------------------

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN: #pega tecla pressionada
                if event.key == K_LEFT :
                    jogador.rect.left -= jogador.velocidade
                if event.key== K_RIGHT:
                    jogador.rect.right += jogador.velocidade
                if event.key== K_SPACE:
                    x,y= jogador.rect.center
                    jogador.disparar(x-13,y-50)


        bala.trajetoria()
        tela.blit(bg,(0,0))

        jogador.colocar(tela)

        enemy1.put(tela)
        enemy2.put(tela)
        enemy3.put(tela)
        enemy4.put(tela)
        enemy5.put(tela)
        enemy6.put(tela)
        enemy7.put(tela)
        enemy8.put(tela)
        enemy9.put(tela)
        enemy10.put(tela)
        enemy11.put(tela)

        #att a tela apos disparo
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.colliderect(enemy1.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e1= -10000
                    lado1= 500
                    con+=0.15

                elif x.rect.colliderect(enemy2.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e2= -10000
                    lado2= 500
                    con+=0.15

                elif x.rect.colliderect(enemy3.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e3= -10000
                    lado3= 500
                    con+=0.15

                elif x.rect.colliderect(enemy4.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e4= -10000
                    lado4= 500
                    con+=0.15


                elif x.rect.colliderect(enemy5.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e5= -10000
                    lado5= 500
                    con+=0.15


                elif x.rect.colliderect(enemy6.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e6= -10000
                    lado6= 500
                    con+=0.15


                elif x.rect.colliderect(enemy7.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e7= -10000
                    lado7= 500
                    con+=0.15

                elif x.rect.colliderect(enemy8.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    lado8= 500
                    e8= -10000
                    con+=0.15


                elif x.rect.colliderect(enemy9.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e9= -10000
                    lado9= 500
                    con+=0.15


                elif x.rect.colliderect(enemy10.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e10= -10000
                    lado10= 500
                    con+=0.15


                elif x.rect.colliderect(enemy11.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e11= -10000
                    lado11= 500
                    con+=0.15

                elif x.rect.top < -10:
                    jogador.listaDisparo.remove(x)
        win()
        lose()
        pygame.display.update()


invasaoEspaco()
