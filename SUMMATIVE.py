#Sahij Hayer, ICS3U0 SUMMATIVE - RANSOMWARE
#importing tkiner pygame PIL and webbrowser
from tkinter import *
from tkinter import messagebox
import pygame, sys, time, random, webbrowser
from PIL import Image, ImageTk
#variable used to prevent tkinter error with forgetting a placement of button
gameCheck = False
#functions for webrowser module and linking to happy/sad animation and the html website for later on
def happyman():
    messagebox.showinfo('Results', 'Congrats! You have got at least 80%!('+str((right/5*100))+'%)')
    webbrowser.open('happyman.py')
def sadman():
    messagebox.showinfo('Results', 'You\'re stupid! You got less than 80%('+str((right/5*100))+'%)')
    webbrowser.open('sadman.py')
def website():
    webbrowser.open('file:///C:/Users/sahij/Desktop/Python/Summative/Webpage.html')
#multiple variables used to being global and preventing errors
btPayment = ''
right = 0
y = []
tryAgain = 0
#naming Tkinter variable as root
root = Tk()
#tkinter title
root.title('Ransomware Demonstration')
bg1 = ''
image1 = ''
#loading a gif file for mainscreen
bg = PhotoImage(file="virus.gif")
canvas = Canvas(root, width = 1000, height = 500, bg = 'white')
canvas.pack()
image = canvas.create_image(500, 250,image=bg)
#title "ransomware" and a small slogan underneath
canvas.create_text(500, 50, text = 'Ransomware', font = 'Times 24 bold')
canvas.create_text(500, 400, text = 'Simulation of a true NIGHTMARE', font = 'Times 12 italic')
#start for quiz function
def quiz():
    #destroying root
    global root
    root.destroy()
    root = Tk()
    root.title('Quiz')
    #canvas
    canvas = Canvas(root, width = 1100, height = 500, bg = 'orange')
    canvas.pack()
    #functions for right and wrong
    def right():
        global right
        right += 1 
    def wrong():
        pass
    #checkbutton for each answer for the question
    #FROM HERE ON, ALL CODE IS COPY PASTED AND ONLY CHANGES WITH TEXT AND placement of buttons
    a = canvas.create_text(150,20,text='What is ransomware based on?',font='comic 10 bold',fill='white')
    bt1 = Checkbutton(root, text = "Fear of hackers", width=30, bg="yellow",command=wrong)
    bt1.place(x=20, y=50)
    bt2 = Checkbutton(root, text = "Fear of losing important files", width=30, bg="yellow",command=right)
    bt2.place(x=20, y=80)
    bt3 = Checkbutton(root, text = "Fear of the Internet", width=30, bg="yellow", command=wrong)
    bt3.place(x=20, y=110)
    bt4 = Checkbutton(root, text = "Fear of spywares", width=30, bg="yellow",command=wrong)
    bt4.place(x=20, y=140)

    a = canvas.create_text(200,200,text='According to the FBI,\n how many businesses globally become infected with\n ransomware every hour?',font='comic 10 bold',fill='white')
    bt1 = Checkbutton(root, text = "4000", width=30, bg="yellow",command=right)
    bt1.place(x=20, y=250)
    bt2 = Checkbutton(root, text = "2500", width=30, bg="yellow",command=wrong)
    bt2.place(x=20, y=280)
    bt3 = Checkbutton(root, text = "3500", width=30, bg="yellow", command=wrong)
    bt3.place(x=20, y=310)
    bt4 = Checkbutton(root, text = "5000", width=30, bg="yellow",command=wrong)
    bt4.place(x=20, y=340)

    a = canvas.create_text(500,20,text='What percentage of UK companies \nare confident in dealing with ransomware?',font='comic 10 bold',fill='white')
    bt1 = Checkbutton(root, text = "25%", width=30, bg="yellow",command=wrong)
    bt1.place(x=400, y=50)
    bt2 = Checkbutton(root, text = "93%", width=30, bg="yellow",command=wrong)
    bt2.place(x=400, y=80)
    bt3 = Checkbutton(root, text = "19%", width=30, bg="yellow", command=wrong)
    bt3.place(x=400, y=110)
    bt4 = Checkbutton(root, text = "4%", width=30, bg="yellow",command=right)
    bt4.place(x=400, y=140)

    a = canvas.create_text(500,200,text='In 2016, what percentage of businesses\n were attacked worldwide?',font='comic 10 bold',fill='white')
    bt1 = Checkbutton(root, text = "10%", width=30, bg="yellow",command=wrong)
    bt1.place(x=400, y=250)
    bt2 = Checkbutton(root, text = "20%", width=30, bg="yellow",command=right)
    bt2.place(x=400, y=280)
    bt3 = Checkbutton(root, text = "25%", width=30, bg="yellow", command=wrong)
    bt3.place(x=400, y=310)
    bt4 = Checkbutton(root, text = "5%", width=30, bg="yellow",command=wrong)
    bt4.place(x=400, y=340)

    a = canvas.create_text(850,20,text='If you do not have the required amount of money,\n what will the hacker do?',font='comic 10 bold',fill='white')
    bt1 = Checkbutton(root, text = "Never decrypt your files.", width=30, bg="yellow",command=wrong)
    bt1.place(x=780, y=50)
    bt2 = Checkbutton(root, text = "Attack other devices on your network.", width=30, bg="yellow",command=wrong)
    bt2.place(x=780, y=80)
    bt3 = Checkbutton(root, text = "Use your computer as a bitcoin miner.", width=30, bg="yellow", command=wrong)
    bt3.place(x=780, y=110)
    bt4 = Checkbutton(root, text = "Tell you to spread the ransomware to\n your friends to decrypt your files.", width=30, bg="yellow",command=right)
    bt4.place(x=780, y=140)
    #function for submitting answers
    def submit():
        global right
        if right >= 4:
            happyman()
        elif right <= 3:
            sadman()
        root.destroy()
    btSubmit = Button(root, text = 'Submit', width = 30, command = submit)
    btSubmit.pack()
#function for everything after the title page
def proceed():
    #globalling variables since I need to destroy the root and etc..
    global canvas
    global bg
    global image
    global bg1
    global image1
    #setting up the option for choosing between game or payment
    canvas.delete('all')
    bg = Image.open('money.jpg')
    bg1 = Image.open('game.png')
    bg = bg.resize((500, 400))
    bg1 = bg1.resize((500, 400))
    image = ImageTk.PhotoImage(bg)
    image1 = ImageTk.PhotoImage(bg1)
    imagesprite = canvas.create_image(250,200,image=image)
    imagesprite1 = canvas.create_image(750,200,image=image1)
    canvas.create_text(250,450, text = 'You will either be forced to pay your hard earned money', font = 'Times 16 bold italic')
    canvas.create_text(650,475, text = 'Or you will sweat blood and tears playing an unbeatable(almost) video game.', font = 'Times 16 bold italic')
    root.geometry('1200x500')
    #payment webpage
    def money():
        global canvas
        global gameCheck
        global root
        #gameCheck for avoiding errors since you can start the payment function from the game over screen and the option screen as well
        if not gameCheck:
            btGame.place_forget()
            btMoney.place_forget()
        elif gameCheck:
            root.destroy()
            root = Tk()
            root.title('Ransomware Demonstration')
            canvas = Canvas(root, width = 1000, height = 500, bg = 'white')
            canvas.pack()
        #small description introducing the payment
        root.geometry('1000x500')
        canvas.delete('all')
        canvas.create_text(500,150, text = 'When money is required,\n the program will link the computer owner to a site\n where they can enter their credit card information.', font = 'gyparody 20 bold', fill = 'red')
        def proceed1():
            #multiple entries being packed for entering the credit card, e.get() is never used since the what is typed does not matter
            canvas.delete('all')
            btProceed1.place_forget()
            d = Entry(root, width = 75)
            d.pack()
            d.place(x = 300, y = 0, height = 100, width = 500)
            d.insert(0, 'What is your full name?')
            e = Entry(root)
            e.pack()
            e.place(x = 300, y = 100, height = 100, width = 500)
            e.insert(0, 'What is your credit card number?')
            f = Entry(root)
            f.pack()
            f.place(x = 300, y = 200, height = 100, width = 500)
            f.insert(0, 'What is the expiry date?')
            g = Entry(root)
            g.pack()
            g.place(x = 300, y = 300, height = 100, width = 500)
            g.insert(0, 'What is the CVC?')
            #error message after clicking proceed
            def proceed2():
                #unpacking all the entries and the button
                canvas.delete('all')
                d.place_forget()
                e.place_forget()
                f.place_forget()
                g.place_forget()
                btProceed2.place_forget()
                messagebox.showerror("Error", "Error")
                def tryAgain():
                    #using an if loop for each time tryagain button is clicked, and after 10 times, the user will proceed
                    global tryAgain
                    canvas.delete('all')
                    tryAgain += 1
                    messagebox.showerror("Error", "Error")
                    if tryAgain == 10:
                        canvas.delete('all')
                        btTryAgain.place_forget()
                        canvas.create_text(500,250, text = 'This is a demonstration of how even though you have paid the correct amount,\n there are some ransomwares which try to play it off like you didn\'t.\n They will run away with your money. \nRemember not to give your money to the people who put the virus on your computer\n because even though sometimes they may not be lying, you can never trust them.', font = 'Times 16', fill = 'purple')
                        root.geometry('1000x550')
                        #function for going to the website
                        def html():
                            #function from the top of the code
                            website()
                        #one button for the webpage with info, one with testing knowledge from the website
                        btLearn = Button(root, text = 'Learn Knowledge', command = html)
                        btLearn.pack()
                        btQuiz = Button(root, text = 'Test Knowledge', command = quiz)
                        btQuiz.pack()
        #buttons
                btTryAgain = Button(root, text = 'Try Again', command = tryAgain)
                btTryAgain.pack()
                btTryAgain.place(x = 0, y = 0, height = 500, width = 1000)
            btProceed2 = Button(root, text = 'Proceed', command = proceed2)
            btProceed2.pack()
            btProceed2.place(x = 300, y = 400, height = 100, width = 500)
        btProceed1 = Button(root, text = 'Proceed', command = proceed1)
        btProceed1.pack()
        btProceed1.place(x = 300, y = 400, height = 100, width = 500)
    def game():
        global gameCheck
        global y
        global dead
        global t
        global f
        global option
        global categories
        global pdsitribution
        global points
        global option1
        global root
        root.destroy()
        #using an old assignment for the choosing stats of the user
        #Sahij Hayer, RPG ASSIGNMENT
        #printing the rules
        print('You have 100 points to spend on the 3 categories: Strength, Wisdom, and Dexterity')
        a = 0
        re = 0
        option1 = ''
        #defining function for foolproofing the input by the user
        def check():
            global option1
            while not option1.isnumeric():
              print('Please input a number..')
              option1 = input('How many of your 100 points do you which to spend?')
            if option1.isnumeric():
              option1 = int(option1)
              while option1 < 0 or option1 > 100:
                print('The points must be in between 0 and 30')
                option1 = input('How many of your 100 points do you which to spend?')
                while not option1.isnumeric():
                  print('Please input a number..')
                  option1 = input('How many of your 100 points do you which to spend?')
                if option1.isnumeric():
                  option1 = int(option1)
        #defining function for the adding of the points
        def adding():
            global option
            global categories
            global pdsitribution
            global points
            global option1
            re = points
            option = input('Which category do you wish to add a point to?').upper()
            while option not in categories:
              print('This is not one of the attributes that points can be added to.')
              option = input('Which category do you wish to add a point to?').upper()
            while option in categories:
              option1 = input('How many of your 100 points do you which to spend?')
              check()
              if option == 'STRENGTH':
                pdistribution[0] = option1
                points -= option1
                categories.remove('STRENGTH')
              elif option == 'WISDOM':
                pdistribution[1] = option1
                points -= option1
                categories.remove('WISDOM')
              elif option == 'DEXTERITY':
                pdistribution[2] = option1
                points -= option1
                categories.remove('DEXTERITY')
              if categories == []:
                break
              if points < 0:
                print('The total of 100 points has been surpassed. Please begin all over again.')
                points = re
                categories = ['STRENGTH', 'WISDOM', 'DEXTERITY']
              option = input('Which category do you wish to add a point to?').upper()
              while option not in categories:
                print('This is not one of the attributes that points can be added to.')
                option = input('Which category do you wish to add a point to?').upper()
                while option not in categories:
                  print('This is not one of the attributes that points can be added to.')
                  option = input('Which category do you wish to add a point to?').upper()
        #setting variables: points amount, list for attributes, backup list for attributes, and the list for the point distribution
        points = 100
        categories = ['STRENGTH', 'WISDOM', 'DEXTERITY']
        bcategories = ['STRENGTH', 'WISDOM', 'DEXTERITY']
        pdistribution = [0, 0, 0, 0]
        #using the adding of points function
        adding()
        #setting variables for all of the points for attributes
        strength = pdistribution[0]
        wisdom = pdistribution[1]
        dexterity = pdistribution[2]
        #setting FPS to a solid 60 frames
        FPS = 60
        fpsClock = pygame.time.Clock()
        #initiating pygame
        pygame.init()
        #loading all the images: boss, boss 3rd phase, boss shot, player, player shot, dead boss, icicle shot, background
        bg = pygame.image.load('bg.png')
        bg = pygame.transform.scale(bg, (800,600))
        prot = pygame.image.load('veigar.png')
        prot = pygame.transform.scale(prot, (90, 90))
        boss = pygame.image.load('arcus.png')
        boss = pygame.transform.scale(boss, (275, 225))
        boss2 = pygame.image.load('arcus2.png')
        boss2 = pygame.transform.scale(boss2, (300, 450))
        deadBoss = pygame.image.load('deadboss.png')
        deadBoss = pygame.transform.scale(deadBoss, (275, 225))
        protShot = pygame.image.load('veigarshot.png')
        protShot = pygame.transform.scale(protShot, (25, 25))
        bossShot1 = pygame.image.load('p1laser.png')
        bossShot1 = pygame.transform.scale(bossShot1, (240,40))
        bossShot2 = pygame.image.load('p2laser.png')
        bossShot2 = pygame.transform.scale(bossShot2, (400, 250))
        icicle = pygame.image.load('icicle.png')
        icicle = pygame.transform.scale(icicle, (50,100))
        #setting boss x and y value default
        bossx = 550
        bossy = 25
        #speed, power, and shotspped based on the stat values chosen
        speed = 1 + 0.25 * dexterity
        power = 0.125 * strength
        shotSpeed = 2+wisdom
        #setting boss speed
        bspeed = 25
        #setting user x and y value default
        protx = 10
        proty = 400
        #getting rectangles for the boss, player, shots so collisions can be used to damage the boss or end the game
        protRect = prot.get_rect()
        bossRect = boss.get_rect()
        boss2Rect = boss2.get_rect()
        protShotRect = protShot.get_rect()
        protRect.move_ip(protx, proty)
        bossRect.move_ip(bossx, bossy)
        boss2Rect.move_ip(500000,500000)
        gameDisplay = pygame.display.set_mode((800,600))
        pygame.display.set_caption('Good Luck')
        #setting boss health
        bossHealth = 100
        #setting booleans for the game existing, phases, and different variables used for the player shooting
        gameExist = True
        phaseOne = True
        phaseTwo = False
        phaseThree = False
        shotMeasure = 0
        shotCheck = False
        positionCheck = False
        bossMeasure = 0
        bossCheck = False
        charge = False
        newBoss = False
        #initiating the mixer(for sound) and making variables for the different sounds and the music
        pygame.mixer.init()
        pygame.mixer.music.load('background.mid')
        pygame.mixer.music.play(-1, 0.0)
        phase3sound = pygame.mixer.Sound('phase3.wav')
        chargesound = pygame.mixer.Sound('charge.wav')
        shotsound = pygame.mixer.Sound('shot.wav')
        laughsound = pygame.mixer.Sound('laugh.wav')
        #loop which only ends once player dies (game starts here)
        while gameExist:
            #open text file which holds the number of deaths by the user
            f = open('deaths.txt','r+')
            #read the file
            t = f.read()
            f.close()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameExit = True
            #display the background picture
            gameDisplay.blit(bg, (0, 0))
            #move up left right and down with arrow keys and space makes the shotCheck true
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    protx -= speed
                elif event.key == pygame.K_RIGHT:
                    protx += speed
                elif event.key == pygame.K_UP:
                    proty -= speed
                elif event.key == pygame.K_DOWN:
                    proty += speed
                elif event.key == pygame.K_SPACE:
                    shotCheck = True
                    pygame.mixer.Sound.play(shotsound)
                #limitting movement off the screen
                if proty > 500:
                    proty = 500
                if protx < 0:
                    protx = 0
            if phaseOne:
                #death by colliding with boss
                if protRect.colliderect(bossRect):
                    pygame.mixer.Sound.play(laughsound)
                    time.sleep(2)
                    if t != '':
                        f = open('deaths.txt', 'w')
                        t = str(int(t)+1)
                        f.write(t)
                        f.close()
                    elif t == '':
                        f = open('deaths.txt', 'w')
                        f.write('1')
                        f.close()
                    gameExist = False
                #random movement of the boss up and down using randint
                if True:
                    x = random.randint(1,15)
                    if x == 1:
                        bossy += 3*bspeed
                    elif x == 2:
                        bossy -= 3*bspeed
                    else:
                        pass
                    if bossy > 200:
                        bossy = 200
                    if bossy < 0:
                        bossy = 0
                    #next phase starts if health than 66
                    if bossHealth < 66:
                        phaseOne = False
                        phaseTwo = True
                    x = random.randint(1,4)
                    y.append(x)
                    #boss shooting
                    if y[0] == 1:
                        if bossCheck == False:
                            currentXb = bossx
                            currentYb = bossy
                            bossCheck = True
                        bossMeasure += 1
                        gameDisplay.blit(bossShot1, (currentXb-20*bossMeasure,currentYb+200))
                        bossShotRect = bossShot1.get_rect()
                        #shot moves horizontally
                        bossShotRect.move_ip(currentXb-20*bossMeasure,currentYb+200)
                        #death by collision with boss shot
                        if bossShotRect.colliderect(protRect):
                            pygame.mixer.Sound.play(laughsound)
                            time.sleep(2)
                            if t != '':
                                f = open('deaths.txt', 'w')
                                t = str(int(t)+1)
                                f.write(t)
                                f.close()
                            elif t == '':
                                f = open('deaths.txt', 'w')
                                f.write('1')
                                f.close()
                            gameExist = False
                        elif currentXb-10*bossMeasure < -100:
                            bossCheck = False
                            bossMeasure = 0
                            y = []
                    else:
                        y = []
            if phaseTwo:
                #death by colliding with boss
                if protRect.colliderect(bossRect):
                    pygame.mixer.Sound.play(laughsound)
                    time.sleep(2)
                    if t != '':
                        f = open('deaths.txt', 'w')
                        t = str(int(t)+1)
                        f.write(t)
                        f.close()
                    elif t == '':
                        f = open('deaths.txt', 'w')
                        f.write('1')
                        f.close()
                    gameExist = False
                if True:
                    z = random.randint(1,80)
                    y.append(z)
                    if y[0] == 1:
                        if charge == False:
                            time.sleep(0.25)
                            charge = True
                            pygame.mixer.Sound.play(chargesound)
                        if bossCheck == False:
                            currentXb = bossx
                            currentYb = bossy
                            bossCheck = True
                        bossMeasure += 1
                        gameDisplay.blit(bossShot2, ((currentXb+150)-7*bossMeasure,currentYb))
                        bossShotRect = bossShot2.get_rect()
                        #shot moves horizontally
                        bossShotRect.move_ip((currentXb+150)-7*bossMeasure,currentYb)
                        #death by collision with boss shot
                        if bossShotRect.colliderect(protRect):
                            if t != '':
                                pygame.mixer.Sound.play(laughsound)
                                time.sleep(2)
                                f = open('deaths.txt', 'w')
                                t = str(int(t)+1)
                                f.write(t)
                                f.close()
                            elif t == '':
                                f = open('deaths.txt', 'w')
                                f.write('1')
                                f.close()
                            gameExist = False
                        elif (currentXb+150)-7*bossMeasure < -100:
                            bossCheck = False
                            bossMeasure = 0
                            charge = False
                            y = []
                    else:
                            y = []
                            x = random.randint(1,10)
                            if x == 1:
                                bossy += 4*bspeed
                            elif x == 2:
                                bossy -= 4*bspeed
                            else:
                                pass
                            if bossy > 200:
                                bossy = 200
                            if bossy < 0:
                                bossy = 0
                    #last phase, new boss sprite loads up
                    if bossHealth < 33:
                        gameDisplay.blit(deadBoss, (bossx, bossy))
                        bossx = -500
                        bossy = -500
                        time.sleep(1)
                        newBoss = True
                        phaseTwo = False
                        phaseThree = True
                        pygame.mixer.Sound.play(phase3sound)
            if phaseThree:
                #death by colliding with boss
                if protRect.colliderect(boss2Rect):
                    pygame.mixer.Sound.play(laughsound)
                    time.sleep(2)
                    if t != '':
                        f = open('deaths.txt', 'w')
                        t = str(int(t)+1)
                        f.write(t)
                        f.close()
                    elif t == '':
                        f = open('deaths.txt', 'w')
                        f.write('1')
                        f.close()
                    gameExist = False
                if True:
                    if bossCheck == False:
                        currentXb = random.randint(1,600)
                        bossCheck = True
                    bossMeasure += 1
                    gameDisplay.blit(icicle, (currentXb,12*bossMeasure))
                    icicleRect = icicle.get_rect()
                    #shot moves vertically
                    icicleRect.move_ip(currentXb,12*bossMeasure)
                    #death by collision with boss shot
                    if icicleRect.colliderect(protRect):
                        pygame.mixer.Sound.play(laughsound)
                        time.sleep(2)
                        if t != '':
                            f = open('deaths.txt', 'w')
                            t = str(int(t)+1)
                            f.write(t)
                            f.close()
                        elif t == '':
                            f = open('deaths.txt', 'w')
                            f.write('1')
                            f.close()
                        gameExist = False
                    elif 12*bossMeasure > 700:
                        bossCheck = False
                        bossMeasure = 0
                        charge = False
                        y = []
                if bossHealth <= 0:
                    #win game, no reward
                    f = open('deaths.txt', 'r')
                    print('Wow you won! That\'s a surprise... Sucks that it doesn\'t matter, your files are going to stay encrypted until you pay me that $'+str(int(f.read())*1000)+' that you owe me, or I might have to resort to making you give this to your friends.')
                    f.close()
            #user shot
            if shotCheck == True:
                if positionCheck == False:
                    currentX = protx
                    currentY = proty
                    positionCheck = True
                shotMeasure += 1
                gameDisplay.blit(protShot, (currentX+shotSpeed*shotMeasure,currentY+30))
                protShotRect = protShot.get_rect()
                protShotRect.move_ip(currentX+shotSpeed*shotMeasure,currentY+10)
                if protShotRect.colliderect(bossRect) or protShotRect.colliderect(boss2Rect):
                    shotCheck = False
                    positionCheck = False
                    shotMeasure = 0
                    bossHealth -= power
                elif currentX+shotSpeed*shotMeasure > 800:
                    shotCheck = False
                    positionCheck = False
                    shotMeasure = 0
            #constant things always happening at the end of each frame
            protRect = prot.get_rect()
            bossRect = boss.get_rect()
            boss2Rect = boss2.get_rect()
            protRect.move_ip(protx, proty)
            bossRect.move_ip(bossx, bossy)
            if not phaseThree:
                boss2Rect.move_ip(5000,5000)
            if phaseThree:
                boss2Rect.move_ip(bossx, bossy)
            if newBoss:
                gameDisplay.blit(boss2, (650, 20))
            gameDisplay.blit(prot, (protx,proty))
            gameDisplay.blit(boss, (bossx,bossy))
            deaths = t
            pygame.display.update()
            fpsClock.tick(FPS)
        pygame.quit()
        #once out of loop (collision with boss or bossshot)
        f = open('deaths.txt', 'r')
        #new page for game over screen
        root = Tk()
        root.title('Ransomware Demonstration')
        canvas = Canvas(root, width = 1000, height = 500, bg = 'black')
        canvas.pack()
        canvas.create_text(500, 150, text = 'GAME OVER', font = 'comic 36 bold', fill = 'white')
        canvas.create_text(500, 350, text = 'You owe me $'+str(int(f.read())*1000)+' dollars to save your computer now!', font = 'comic 24 underline italic', fill = 'red')
        #payment owed (based on how many deaths)
        #button to payment seciont
        global btPayment
        btPayment = Button(root, text = 'Pay', command = money)
        btPayment.pack()
        btGameAgain = Button(root, text = 'Play Again', command = game)
        btGameAgain.pack()
        gameCheck = True

    btGame = Button(root, text = 'Video Game', command = game)
    btMoney = Button(root, text = 'Ransom', command = money)
    btGame.pack()
    btGame.place(x = 1100, y = 0, height = 500, width = 100)
    btMoney.pack()
    btMoney.place(x = 0, y = 0, height = 500, width = 100)
    btProceed.pack_forget()
btProceed = Button(root, text = 'Proceed', command = proceed)
btProceed.pack()
