import os
os.environ['SDL_VIDEO_WINDOW_POS'] = '100,100'
import random
import pgzrun
import pygame

random.seed()

pygame.mixer.music.load("song.ogg") #Jan125
pygame.mixer.music.play(-1)

level=-1
vokale = ["a","e","i","o","u","ä","ö","ü"]
text1=""
text2list = []
code=""
target=""
gemacht=False

def kalle(text1):
    global text2list,code,vokale
    for i in range(len(text1)):
        text2list.append(" ")
        if text1[i] in vokale:
            text2list.append(text1[i])
        else:
            text2list.append(text1[i])
            text2list.append("o")
            text2list.append(text1[i])
    code = "".join(text2list)

def draw():
    global level, target,code,vokale
    screen.clear()
    if level == -1:
        screen.blit("title", (0, 0))
    elif level == 0:
        screen.blit("intro",(0,0))
    elif level == 1:
        screen.blit("back", (0, 0))
        screen.draw.text("Word to encrypt:", center=(400, 130), fontsize=24, color=(25, 20, 55))
        screen.draw.text(target, center=(400, 180), fontsize=24, color=(55, 55, 0))
    elif level == 2:
        screen.blit("back",(0,0))
        screen.draw.text(target, center=(400, 180), fontsize=24, color=(25, 55, 0))
        screen.draw.text(" is ", center=(400, 280), fontsize=24, color=(25, 55, 0))
        screen.draw.text(code, center=(400, 380), fontsize=24, color=(25, 55, 0))
        
def on_key_down(key, unicode=None):
    global level, target
    if key==keys.ESCAPE:
        pygame.quit()
    if key == keys.BACKSPACE:
        target = ""
    elif key == keys.RETURN and level == 1:
        level = 2
    elif unicode and key != keys.RETURN and level==1:
        target += unicode

def update():
    global level,gemacht,target,text1,text2list,code
    if (level == 0 or level==-2) and keyboard.RETURN:
        level +=1
    elif level == -1 and keyboard.space:
        level = 0
    if level==0:
        text1=""
        text2list = []
        code=""
        target=""
        gemacht=False
    if level==2:
        if not gemacht:
            kalle(target)
            gemacht=True
        if keyboard.space:
            level=0
        

pgzrun.go()

