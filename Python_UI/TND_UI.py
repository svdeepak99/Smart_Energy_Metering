import pygame as pg
import numpy
import serial
import time
from pygame.locals import*

win_H=720
win_W=1280
bc=(150,255,205)
bt=10

real_e=0
img_e=0

def draw_borders():
    #Draw outer border
    pg.draw.polygon(win, bc, [(0,0),(win_W,0),(win_W,win_H),(0,win_H)], bt)
    #Draw Rows
    pg.draw.line(win, bc, (0,144), (win_W,144), bt)
    pg.draw.line(win, bc, (0,540), (win_W,540), bt)

class Text:
    def __init__(self,window):
        pg.font.init()
        self.screen=window
        
    def text_objects(self,text,font,__color):
        txtsurf = font.render(text,True,__color)
        return txtsurf, txtsurf.get_rect()

    def write(self,_text,x,y,_size=20,_color=(0,0,0)):
        font = pg.font.Font('freesansbold.ttf',_size)
        txtsf, txtre = self.text_objects(_text,font,_color)
        txtre.center = (x,y)
        self.screen.blit(txtsf,txtre)

def readValues():

    Volt=0
    Curr=0
    Freq=0
    Pf=0
    
    while True:
        if ard.inWaiting()!=0:
            break
    word=ard.readline().decode()
    word_limit=len(word)-1

    i=0
    while True:
        if (i>word_limit):
            return (0,0,0,0)
        elif( (word[i]=='\t') ):
            i+=1
            break
        if(i==0):
            Volt=word[i]
        else:
            Volt+=word[i]
        i+=1
    last_val=i

    while True:
        if (i>word_limit):
            return (0,0,0,0)
        elif( (word[i]=='\t') ):
            i+=1
            break
        if (i==last_val):
            Curr=word[i]
        else:
            Curr+=word[i]
        i+=1
    last_val=i

    while True:
        if (i>word_limit):
            return (0,0,0,0)
        elif( (word[i]=='\t') ):
            i+=1
            break
        if (i==last_val):
            Freq=word[i]
        else:
            Freq+=word[i]
        i+=1
    last_val=i

    while True:
        if (i>word_limit):
            return (0,0,0,0)
        elif( word[i]=='\t' ):
            i+=1
            break
        if(i==last_val):
            Pf=word[i]
        else:
            Pf+=word[i]
        i+=1
    
    volt_f=float(Volt)
    curr_f=float(Curr)
    freq_f=float(Freq)
    pf_f=float(Pf)

    return (volt_f,curr_f,freq_f,pf_f)


#creating a pygame window
win = pg.display.set_mode((win_W,win_H))
running = True

text=Text(win)

prev_t=time.time()

ard=serial.Serial('com4',2000000)
while True:
        if ard.inWaiting()!=0:
            break

#To avoid python shell crash after closing a pygame window
while running:
    for event in pg.event.get():
        if(event.type == QUIT):
            running = False

    #Get values from Serial
    volt,curr,freq,pf=readValues()

    real_p=volt*curr*pf*0.001
    imaginary_p=volt*curr*numpy.sqrt(1-(pf*pf))*0.001

    curr_t=time.time()
    Dt=curr_t-prev_t
    real_e += real_p*Dt
    img_e += imaginary_p*Dt
    prev_t=curr_t

    #Clear Screen
    win.fill((0,0,0))

    draw_borders()

    if(imaginary_p>=0):
        ch='+'
    else:
        ch=''

    if(img_e>=0):
        ch_e='+'
    else:
        ch_e=''

    #Texts
    text.write('Smart Energy Metering' ,640,72,45,(255,255,255) )
    text.write('Net Energy Consumption ',640,243,35,(0,0,255) )
    text.write('Real : '+str(real_e)+' J',640,342,30,(0,255,0) )
    text.write('Apparent : '+ str(int(real_e)) + str(ch_e) + str(int(img_e)) + 'j J',640,441,30,(255,0,0) )
    text.write('Instantaneous Power Consumption : ' +str(int(real_p*1000))+' ' + str(ch) + ' ' + str(int(imaginary_p*1000))+'j mW',640,600,30,(255,255,0) )
    text.write('Frequency : '+str(freq)+' Hz'+'    Power Factor: '+str(pf),640,660,30,(255,255,0) )
    
    #Refresh Screen
    pg.display.update()
    pg.time.delay(1)
