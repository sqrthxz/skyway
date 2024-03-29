import pygame, sys, os, ctypes
from pygame.locals import *


#set tamanho da tela do jogo
largura = 400
altura = 600
setTop = 20

# -------------------------------------- INIMIGOS ------------------------------------

class Enemy1(pygame.sprite.Sprite):
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

class Enemy3(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/enemy3.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)

class Enemy4(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/enemy4.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)

#-------------------------------- BOSS ----------------------------------------------

class BOSS(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load("images/boss.png")
        self.rect = self.ImageEnemy.get_rect()

        self.rect.top = posy
        self.rect.left = posx

    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)

#quando leva hit
class BOSS2(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load('images/boss2.png')
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)

#tiro boss
class BalaB(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImageEnemy = pygame.image.load("images/laser_boss.png")
        self.rect = self.ImageEnemy.get_rect()
        self.rect.top = posy
        self.rect.left = posx
    def put(self,superficie):
        superficie.blit(self.ImageEnemy, self.rect)


#------------------------------------------ PLAYER -----------------------------------------
#tiro
class Bala(pygame.sprite.Sprite):
    def __init__(self, posx, posy):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemBala = pygame.image.load("images/laser.png")
        self.rect = self.ImagemBala.get_rect()
        self.teste = self.ImagemBala.get_rect()
        self.velocidadeBala = 3
        self.rect.top = posy
        self.rect.left = posx
    def trajetoria(self):
        self.rect.top = self.rect.top - self.velocidadeBala
    def colocar(self,superficie):
        superficie.blit(self.ImagemBala, self.rect)

#player
class player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.ImagemNave = pygame.image.load("images/player.png")

        self.rect = self.ImagemNave.get_rect()
        #set posicao inicial
        self.rect.centerx = largura/2
        self.rect.centery = altura - 55
        self.listaDisparo = [] #add balas
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


#-----------------------------VARIAVEIS--------------------------

pygame.init()
tela = pygame.display.set_mode((largura, altura))#tamanho da tela
pygame.display.set_caption("Skyway")
cont = 0

#---------------------- altura dos inimigos ---------------------------
e1= -40
e2= -40
e3= -40
e4= -40
e5= -90
e6= -90
e7= -90
e8= -140
e9= -140
e10= -140
e11= -140

#-------------------- posicao dos inimigos ----------------------------
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

#-------------------------- posicao do boss------------------------------------------
boss = BOSS(-100,-100)
bp= 0 #altura do boss
bm= 135 #largura do boss
le= 0.5 #boss se movimentar na tela

#-----------------------velocidade I-------------------------------
con= 0.05 #velocidade inicial dos asteroides
vMode=0.10


#-------------------------------------------------------------------

dc= 0.3 #boss descer
fechar= 1 #count para fechar o jogo apos win/loss

ganhar= 0 #vida do boss
p= 475 #pos para perder

jogador = player()

bala = Bala(largura /2, altura - 55)

bC=0 #taxa de disparo do boss
bA=bp+166 #posicao da bala do boss

damage = 0  #vida do personagem
vidaboss = 10 #vida do boss

menucount=0
menucount1=0
menucount2=0
menu=0

#------------------ IMAGENS ---------------------------------------
vitoria = pygame.image.load("images/vitoria.png")
bg = pygame.image.load("images/bg.png")
menu1= pygame.image.load("images/menu1.png")
menu2= pygame.image.load("images/menu2.png")
menu3=pygame.image.load("images/menu3.png")
option=pygame.image.load("images/options.png")
option2=pygame.image.load("images/options2.png")
normal=pygame.image.load("images/normal.png")
hard=pygame.image.load("images/hard.png")
derrota= pygame.image.load('images/Derrota.png')
#----------------------------------------------------------


# relogio = pygame.time.Clock()

while True:
    # relogio.tick(5)

    #-------- menu principal --------------------------------
    while menu==0:

        if menucount==0:
            tela.blit(menu1,(0,0))
            pygame.display.update()

        if menucount>2:
            menucount=2
        if menucount<0:
            menucount=0

        if menucount==0:
            tela.blit(menu1,(0,0))
            pygame.display.update()
        elif menucount==1:
            tela.blit(menu2,(0,0))
            pygame.display.update()
        elif menucount==2:
            tela.blit(menu3,(0,0))
            pygame.display.update()

    #----- teclas no menu principal ------------------------------------------

        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key == K_DOWN :
                    menucount+=1
                if event.key == K_UP :
                    menucount-=1
                if event.key == K_RETURN and menucount==0:
                    menu=1
                if event.key == K_RETURN and menucount==1:
                    menu=2
                if event.key == K_RETURN and menucount==2:
                    pygame.quit()
                    sys.exit()

    #------------------ teclas em opcoes ------------------------------
    while menu==2:

        if menucount1==0:
            tela.blit(option,(0,0))
            pygame.display.update()

        if menucount1==1:
            tela.blit(option2,(0,0))
            pygame.display.update()



        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key == K_DOWN :
                    menucount1=1
                if event.key == K_UP :
                    menucount1=0
                if event.key == K_RETURN and menucount1==0:
                    menu=0
                if event.key == K_RETURN and menucount1==1:
                    menu=3

    #---------------teclas em dificuldades-----------------------------
    while menu==3:
        if menucount2==0:
            tela.blit(normal,(0,0))
            pygame.display.update()

        if menucount2==1:
            tela.blit(hard,(0,0))
            pygame.display.update()



        for event in pygame.event.get():
            if event.type== pygame.KEYDOWN:
                if event.key == K_DOWN :
                    menucount2=1
                if event.key == K_UP :
                    menucount2=0
                if event.key == K_RETURN and menucount2==0:#normal
                    menu=2
                    vMode=0.10
                    damage=0
                    vidaboss=10
                if event.key == K_RETURN and menucount2==1:#hard
                    menu=2
                    vMode=0.20
                    damage=3
                    vidaboss=20

    #--------------- game -------------------------------------
    while menu==1:


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
        parede1 = Enemy4(-25,120)
        parede2 = Enemy4(375,120)

        bL=bm+62
        tiro = BalaB(bL,bA)

        #------------- teclas em jogo ----------------------
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type== pygame.KEYDOWN:
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

        # ---------------set boss na tela-----------
        if cont == 11:
            boss = BOSS(bm,bp)
            boss.put(tela)
            bp+=dc

            if bp>70:
                dc=0
                bm+=le
                tiro.put(tela)
                boss.put(tela)

                if boss.rect.colliderect(parede2.rect):
                    le=-0.5
                if boss.rect.colliderect(parede1.rect):
                    le=0.5

                bC+=1
                if bC>5:
                    bA+=3 #velocidade da bala do boss
                    if bA>600:
                        bC=0
                        bA=bp+50
                if tiro.rect.colliderect(jogador.rect):
                    damage+=1
                    bA=100




        #------- set win -------
        if ganhar >= vidaboss:
            tela.blit(vitoria,(0,0))
            jogador.colocar(tela)
            bm= 5000
            bp= 5000
            fechar +=1

            if fechar >= 100:
                pygame.quit()




        #--- set inimigos na tela ---
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

#----------------------------------------------

        #att a tela apos disparo e verifica colisao dos asteroides
        if len(jogador.listaDisparo) > 0:
            for x in jogador.listaDisparo:
                x.colocar(tela)
                x.trajetoria()
                if x.rect.colliderect(enemy1.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e1= -10000
                    lado1= 500
                    con+=vMode

                elif x.rect.colliderect(enemy2.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e2= -10000
                    lado2= 500
                    con+=vMode

                elif x.rect.colliderect(enemy3.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e3= -10000
                    lado3= 500
                    con+=vMode

                elif x.rect.colliderect(enemy4.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e4= -10000
                    lado4= 500
                    con+=vMode


                elif x.rect.colliderect(enemy5.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e5= -10000
                    lado5= 500
                    con+=vMode


                elif x.rect.colliderect(enemy6.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e6= -10000
                    lado6= 500
                    con+=vMode


                elif x.rect.colliderect(enemy7.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e7= -10000
                    lado7= 500
                    con+=vMode

                elif x.rect.colliderect(enemy8.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    lado8= 500
                    e8= -10000
                    con+=vMode


                elif x.rect.colliderect(enemy9.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e9= -10000
                    lado9= 500
                    con+=vMode


                elif x.rect.colliderect(enemy10.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e10= -10000
                    lado10= 500
                    con+=vMode


                elif x.rect.colliderect(enemy11.rect):

                    jogador.listaDisparo.remove(x)
                    cont += 1
                    e11= -10000
                    lado11= 500
                    con+=vMode

                elif x.rect.top < -10:
                    jogador.listaDisparo.remove(x)

                elif cont>=11:
                    if x.rect.colliderect(boss.rect):
                        boss2 = BOSS2(bm,bp)
                        boss2.put(tela)
                        pygame.display.update()
                        jogador.listaDisparo.remove(x)
                        ganhar+=1
        #------------------------------------------------------------------

        #---- set derrota ----
        if damage>3 or e1 > p  or e2 > p or e3 > p or e4 > p or e5 > p or e6 > p or e7> p or e8 > p or e9 > p or e10 > p or e11 > p:
            tela.blit(derrota,(0,0))
            fechar+=1
            if fechar>100:
                pygame.quit()

        pygame.display.update()
        parede1.put(tela)
        parede2.put(tela)
