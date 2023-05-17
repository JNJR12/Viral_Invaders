from tkinter import Canvas, PhotoImage, Tk, Label, Button
from random import randint as rand
from tkinter.constants import NW
#Screen Resolution is 1280x720
#Image Resources : 
#   https://www.shutterstock.com/image-vector/red-blood-cell-character-design-vector-1592291989 (rbc image)
#   https://thumbs.dreamstime.com/b/basic-rgb-175103310.jpg (virus image)
#   https://unsplash.com/photos/m3hn2Kn5Bns (mainMenu image)

def virusRollOut():
    virusMove()
    virus2Move()
    virus3Move()
    virus4Move()
    virus5Move()

#moves Viruses
def virusMove():
    global virusSpeed1,virusSpeed2,virusSpeed3,virusSpeed4,stop,virus
    if stop == False:
        posx = rand(-40,40)
        posy = rand(5,15)
        game_area.move(virus,posx,posy)
    pos = game_area.coords(virus)
    if stop == True:
        game_area.delete(virus)
        virus = game_area.create_image(pos[0],pos[1],image=virusImage)
    if (virus):
        collisions()
        virusCoords = game_area.bbox(virus)
        if (virusCoords):
            if virusCoords[1]>550:
                game_area.coords(virus,600,25)
                scoreboard()
    if score <= 20: 
        canvas.after(virusSpeed1,virusMove)
    if 20<score<40:
        canvas.after(virusSpeed2,virusMove)
    if 39<score<50:
        canvas.after(virusSpeed3,virusMove)
    if score > 49:
        canvas.after(virusSpeed4,virusMove)
def virus2Move():
    global virusSpeed1,stop,virus2
    if stop == False:
        posx = rand(-40,40)
        posy = rand(5,15)
        game_area.move(virus2,posx,posy)
    pos2 = game_area.coords(virus2)
    if stop == True:
        game_area.delete(virus2)
        virus2 = game_area.create_image(pos2[0],pos2[1],image=virusImage)
    if virus2:
        collisions()
        virusCoords = game_area.bbox(virus2)
        if (virusCoords):
            if virusCoords[1]>550:
                game_area.coords(virus2,200,25)
                scoreboard()
    if score <= 20: 
        canvas.after(virusSpeed1,virus2Move)
    if 20<score<40:
        canvas.after(virusSpeed2,virus2Move)
    if 39<score<50:
        canvas.after(virusSpeed3,virus2Move)
    if score > 49:
        canvas.after(virusSpeed4,virus2Move)
def virus3Move():
    global virusSpeed1,stop,virus3
    if stop == False:
        posx = rand(-40,40)
        posy = rand(5,15)
        game_area.move(virus3,posx,posy)
    pos3 = game_area.coords(virus3)
    if stop == True:
        game_area.delete(virus3)
        virus3 = game_area.create_image(pos3[0],pos3[1],image=virusImage)

    if virus3:
        collisions()
        virusCoords = game_area.bbox(virus3)
        if (virusCoords):
            if virusCoords[1]>550:
                game_area.coords(virus3,1000,25)
                scoreboard()
    if score <= 20: 
        canvas.after(virusSpeed1,virus3Move)
    if 20<score<40:
        canvas.after(virusSpeed2,virus3Move)
    if 39<score<50:
        canvas.after(virusSpeed3,virus3Move)
    if score > 49:
        canvas.after(virusSpeed4,virus3Move)
def virus4Move():
    global virusSpeed1,stop,virus4
    if stop == False:
        posx = rand(-40,40)
        posy = rand(5,15)
        game_area.move(virus4,posx,posy)
    pos4 = game_area.coords(virus4)
    if stop == True:
        game_area.delete(virus4)
        virus4 = game_area.create_image(pos4[0],pos4[1],image=virusImage)
    if virus4:
        collisions()
        virusCoords = game_area.bbox(virus4)
        if (virusCoords):
            if virusCoords[1]>550:
                game_area.coords(virus4,400,25)
                scoreboard()
    if score <= 20: 
        canvas.after(virusSpeed1,virus4Move)
    if 20<score<40:
        canvas.after(virusSpeed2,virus4Move)
    if 39<score<50:
        canvas.after(virusSpeed3,virus4Move)
    if score > 49:
        canvas.after(virusSpeed4,virus4Move)

def virus5Move():
    global virusSpeed1,stop,virus5
    if stop == False:
        posx = rand(-40,40)
        posy = rand(5,15)
        game_area.move(virus5,posx,posy)
    pos5 = game_area.coords(virus5)
    if stop == True:
        game_area.delete(virus5)
        virus5 = game_area.create_image(pos5[0],pos5[1],image=virusImage)

    if virus5:
        collisions()
        virusCoords = game_area.bbox(virus5)
        if (virusCoords):
            if virusCoords[1]>550:
                game_area.coords(virus5,800,25)
                scoreboard()
    if score <= 20: 
        canvas.after(virusSpeed1,virus5Move)
    if 20<score<40:
        canvas.after(virusSpeed2,virus5Move)
    if 39<score<50:
        canvas.after(virusSpeed3,virus5Move)
    if score > 49:
        canvas.after(virusSpeed4,virus5Move)
def pau(event):
    global stop,gamePaused, startText
    if stop == True:
        stop = False
        startText.destroy()
        gamePaused.destroy()
        UI_area.bind_all("<Right>", moveRight)
        UI_area.bind_all("<Left>", moveLeft)
        UI_area.bind_all("<Up>", moveUp)
        UI_area.bind_all("<Down>", moveDown)
    elif stop == False:
        stop = True
        gamePaused = Label(game_area,text="Paused",fg="black")
        gamePaused.place(x=600,y=200)
        UI_area.unbind_all("<Right>")
        UI_area.unbind_all("<Left>")
        UI_area.unbind_all("<Up>")
        UI_area.unbind_all("<Down>")

#stop time cheatkey(allows rbc to move freely when paused)
#by pressing <return> instead of <space> to start and pause
def NeoTheRBC(event):
    global stop,gamePaused,startText
    if stop == True:
        stop = False
        startText.destroy()
        gamePaused.destroy()
        UI_area.bind_all("<Right>", moveRight)
        UI_area.bind_all("<Left>", moveLeft)
        UI_area.bind_all("<Up>", moveUp)
        UI_area.bind_all("<Down>", moveDown)
        NeoMode = Label(top,text="Matrix Mode Activated, press <Return> to go full Neo",bg="green",fg="black")
        NeoMode.place(x=450, y=10)
    elif stop == False:
        stop = True
        gamePaused = Label(game_area,text="Paused",fg="black")
        gamePaused.place(x=600,y=200)

def startGame():
    global start, label1,startButton
    if start == False:
        start = True
        label1.destroy()
        startButton.destroy()
        label2.destroy()

#keybinding functions
def moveRight(event):
    game_area.move(rbc,+10,0)
def moveLeft(event):
    game_area.move(rbc,-10,0)
def moveUp(event):
    game_area.move(rbc,0,-10)
def moveDown(event):
    game_area.move(rbc,0,+10)

#detects if virus collide with rbc
def collisions():
    global health,lose
    rbcCoords = game_area.bbox(rbc)
    virusCoords = game_area.bbox(virus)
    virus2Coords = game_area.bbox(virus2)
    virus3Coords = game_area.bbox(virus3)
    virus4Coords = game_area.bbox(virus4)
    virus5Coords = game_area.bbox(virus5)
    if (virusCoords and virus2Coords and virus3Coords and virus4Coords and virus5Coords):

        if (rbcCoords[1]<virusCoords[3]<rbcCoords[3] and rbcCoords[2]>virusCoords[0]>rbcCoords[0]):
            print ("Incoming!")
            game_area.coords(virus,600,25)
            health -= 1
            collisionEffect()
          
        if (rbcCoords[1]<virus2Coords[3]<rbcCoords[3] and rbcCoords[2]>virus2Coords[0]>rbcCoords[0]):
            print ("Incoming!")
            game_area.coords(virus2,200,25)
            health -= 1
            collisionEffect()
            
        if (rbcCoords[1]<virus3Coords[3]<rbcCoords[3] and rbcCoords[2]>virus3Coords[0]>rbcCoords[0]):
            print ("Incoming!")
            game_area.coords(virus3,1000,25)
            health -= 1
            collisionEffect()

        if (rbcCoords[1]<virus4Coords[3]<rbcCoords[3] and rbcCoords[2]>virus4Coords[0]>rbcCoords[0]):
            print ("Incoming!")
            game_area.coords(virus4,400,25)
            health -= 1
            collisionEffect()

        if (rbcCoords[1]<virus5Coords[3]<rbcCoords[3] and rbcCoords[2]>virus5Coords[0]>rbcCoords[0]):
            print ("Incoming!")
            game_area.coords(virus5,800,25)
            health -= 1
            collisionEffect()

#tracks score     
def scoreboard():
    global score
    if health>0:
        score += 1
        scoreText.configure(text="Score :" + str(score))

#determines if game has or hasnt been lost
def collisionEffect():
    global lose, reset
    if health < 1: 
            lose = True
            healthText.configure(text="GAME OVER", bg="black",fg="red")
            gameOver= Label(game_area,text="Game Over!!", bg = "red", fg="white", font=(50))
            gameOver.place(x=600, y=250)
            staySafe = Label(game_area,text="Stay Safe :)", bg = "red", fg="white", font=(50))
            staySafe.place(x=600,y=300)
            scoreFinal = Label(game_area,text="Score: " + str(score), bg = "red", fg="white", font=(50))
            scoreFinal.place(x=620, y=400)
            resetButton = Button(game_area, text="Restart", command=ResetGame)
            resetButton.place(x=640, y=500)        
            game_area.delete(virus)
            game_area.delete(virus2)
            game_area.delete(virus3)
            game_area.delete(virus4)
            game_area.delete(virus5)
            if reset == True:
            
                game_area.delete(gameOver)
                game_area.delete(staySafe)
                game_area.delete(scoreFinal)
                game_area.delete(resetButton)

    else:
            healthText.configure(text="Health: " + str(health), bg="green",fg="white")

def ResetGame():
    reset = True
    virus = game_area.create_image(600,25,image=virusImage)
    virus2 = game_area.create_image(200,25,image=virusImage)
    virus3 = game_area.create_image(1000,25,image=virusImage)
    virus4 = game_area.create_image(400,25,image=virusImage)
    virus5 = game_area.create_image(800,25,image=virusImage)

#4 phases of virus speeds
virusSpeed1 = 200
virusSpeed2 = 150
virusSpeed3 = 100
virusSpeed4 = 75

#other variables
global stop
stop = True # change to make start of game paused
pause_text = ''
start = False
lose = False
reset = False

# Makes canvas for game
canvas=Tk()
canvas.geometry("1280x720")
canvas.title("Viral Invaders")

#Canvas Segments
top = Canvas(canvas, width=1280, height=40,bg="black") 
top.grid(column=0, row=0)
UI_area = Canvas(canvas, width=1280, height=100, bg="black")
UI_area.grid(column=0,row=2)
game_area = Canvas(canvas, width=1280, height=550, bg="#FF7A5E")
game_area.grid(column=0,row=1)

#pause text
gamePaused = Label(game_area,text="Paused",fg="black")

#Health & Score
global health
health = 3
global score 
score = 0
healthText = Label(top, text="Health: " + str(health), bg="green", fg="white")
healthText.place(x=12, y = 12)
scoreText = Label(top, text="Score: " + str(score), bg="red", fg="white")
scoreText.place(x=1220, y=12)

#Key Bindings
RightButton=Button(UI_area, text=">>")
RightButton.grid(column=2,row=1)
LeftButton=Button(UI_area, text="<<")
LeftButton.grid(column=0,row=1)
UpButton=Button(UI_area, text="^^")
UpButton.grid(column=1,row=0)
DownButton=Button(UI_area, text="vv")
DownButton.grid(column=1,row=2)
UI_area.bind_all("<space>", pau)

#cheatkey bind
UI_area.bind_all("<Return>",NeoTheRBC)

#rbc & virus image
rbcImage = PhotoImage(file="rbcf1.png")
rbc = game_area.create_image(600,400,image=rbcImage)
virusImage = PhotoImage(file="virus.png")
virus = game_area.create_image(600,25,image=virusImage)
virus2 = game_area.create_image(200,25,image=virusImage)
virus3 = game_area.create_image(1000,25,image=virusImage)
virus4 = game_area.create_image(400,25,image=virusImage)
virus5 = game_area.create_image(800,25,image=virusImage)
startText = Label(game_area,text="Press <Space> to begin or to pause")
startText.place(x=580,y=250)

#makes Main Menu page before going into game screen
img = PhotoImage(file="mainMenu.png")
label1 = Label(canvas,image=img)
label1.place(x=0,y=0)
startButton = Button(canvas, text="Start",command = startGame)
startButton_window = game_area.create_window(600,300,anchor=NW, window=startButton)

#Unlike its space counterpart, there were lack of virus-themed arcade images
#for the main menu due to the lockdown of several arcade places, so a classic retro arcade image is used
label2 = Label(canvas, text="Welcome to Viral Invaders! \n You will play as a Red Blood Cell trying to survive \n the endless horde of viruses that threaten \n your very existence. \n Survive at all costs! \n Use arrow keys to navigate yourself around \n and use <space> to pause the game. \n Good luck and stay safe!")
label2.place(x=480, y=400)
virusRollOut()
canvas.mainloop()
