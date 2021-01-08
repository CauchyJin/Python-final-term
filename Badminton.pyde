add_library('sound')
add_library('ttslib')
add_library('video')
add_library('ControlP5')

from decoration import floating

serveList = []
forecourtList = []
midcourtList = []
backcourtList = []
badmintonList = []

SkillName = ""
SkillDict = {"Serve":"In badminton, the serve must be hit in an upwards direction, with an underarm hitting action. You are not allowed to play a tennis style serve. The main rule here is that when you hit the shuttle, it must be below  your  waist. In other words, you can serve from a little higher than the top of your shorts, but not much.",
             "Forecourt":"forecourt skills include push\rush\lift\spin\net shot and cross court,Front court batting technique requires players to havea clear sense ofposition and choose what kind of batting technique in which position,which is very important for both the quality of the ball and the effect of tactics. The use of front court batting technology, must be based on their position at the time to choose the batting technology, only in the appropriate batting position, the rational use of appropriate batting technology, can receive good batting effect.",
             "Midcourt":"midcourt skills include drive smash and smash-defensemastering Mid Court takes more than having good accuracy, it takes good analysis as well as knowledge of what are your choices at that particular moment to hit a wonderful shot.",
             "Backcourt":"Back court skills include forehand backhand high claer and drop shout, among they ,forehand high is the most important technique in badmintonplaying.You’ll find yourself using this shot very oftenin a singles game.Beginners should learn how to hit Clears first before learning other shots."
             }

x = 0.1
music = None
flag1 = False
flag2 = False
flag3 = False
flag4 = False
flag5 = False
badmintonCount = 20

def setup():
    #setting
    imageMode(CENTER)
    rectMode(CENTER)
    textAlign(CENTER)
    f = loadFont("Chalkduster-32.vlw")
    textFont(f,15)
    frameRate(60)
    
    #draw a basic window
    size(1340,610)
    
    #play music
    global music
    music = SoundFile(this,"Shots.mp3")
    music.play()    
    
    #load floating decoration
    badmintonImg = loadImage("decoration.png")
    for i in range(badmintonCount):
        x = random(10,width/10)
        y = map(i,0,badmintonCount,0,height)
        badmintonList.append(floating(badmintonImg,x,y))
    
    for i in range(badmintonCount):
        x = random(9*width/10,width)
        y = map(i,0,badmintonCount,0,height)
        badmintonList.append(floating(badmintonImg,x,y))
        
    #load text 
    Serve = loadStrings('serve.txt')
    Forecourt = loadStrings('forecourt.txt')
    Midcourt = loadStrings('midcourt.txt')
    Backcourt = loadStrings('backcourt.txt')
    
    for line in Serve:
        serveList.append(line)
    for line in Forecourt:
        forecourtList.append(line)
    for line in Midcourt:
        midcourtList.append(line)
    for line in Backcourt:
        backcourtList.append(line)
    
    global ServeTxt,ForecourtTxt,MidcourtTxt,BackcourtTxt
    ServeTxt = "\n".join(serveList)
    ForecourtTxt = "\n".join(forecourtList)
    MidcourtTxt = "\n".join(midcourtList)
    BackcourtTxt = "\n".join(backcourtList)
    
    #load video
    global movie1,movie2,movie3,movie4,movie5
    movie1 = Movie(this,"Serve.mov")
    movie2 = Movie(this,"Forecourt.mov")
    movie3 = Movie(this,"Midcourt.mov")
    movie4 = Movie(this,"Backcourt.mov")
    movie5 = Movie(this,"KentoMomota.mp4")
    
    global cp5
    cp5 = ControlP5(this)
    cp5.addTextfield("Input Skill Name").setPosition(2*width/5+33, 560).setSize(
        100, 20).setFont(createFont("arial", 16)).setAutoClear(False)
    cp5.addBang("Describe It").setPosition(2*width/5+153, 560).setSize(
        60, 20).getCaptionLabel().align(ControlP5.CENTER, ControlP5.CENTER)
    cp5.addCallback(listenToSearch)
    
    global tts
    tts = TTS()
    
def movieEvent(movie_):
    movie_.read()
    
def draw():
    #refresh background every loop
    wallpaper = loadImage("wallpaper.png")
    image(wallpaper,width/2,height/2)
    
        
    #draw floating badminton
    for b in badmintonList:
        b.update()
        b.display()
        
    #print four kinds of skill on the screen,they can rotate
    global x,flag1,flag2,flag3,flag4,flag5,music
    pushMatrix()
    translate(width/4,height/6)
    rotate(x)
    fill(255)
    textSize(20)
    text("Serve",0,0)
    popMatrix()
    
    pushMatrix()
    translate(3*width/4,height/6)
    rotate(x)
    fill(255)
    textSize(20)
    text("Forecourt",0,0)
    popMatrix()
    
    pushMatrix()
    translate(width/4,5*height/6)
    rotate(x)
    fill(255)
    textSize(20)
    text("Midcourt",0,0)
    popMatrix()
    
    pushMatrix()
    translate(3*width/4,5*height/6)
    rotate(x)
    fill(255)
    textSize(20)
    text("Backcourt",0,0)
    popMatrix()
    
    x += 0.01
        
    #display the related Part if flag is True
    textSize(15)
    if flag1 == True:
        text(ServeTxt,4*width/5,3*height/8)
        image(movie1,width/5,height/2)
        movie1.loop()
    else:
        None
    if flag2 == True:
        text(ForecourtTxt,4*width/5,height/4)
        image(movie2,width/5,height/2)
        movie2.loop()
    else:
        None
    if flag3 == True:
        text(MidcourtTxt,4*width/5,3*height/8)
        image(movie3,width/5,height/2)
        movie3.loop()
    else:
        None
    if flag4 == True:
        text(BackcourtTxt,4*width/5,3*height/8)
        image(movie4,width/5,height/2)
        movie4.loop()
    else:
        None
    if flag5 == True:
        music.stop()
        image(movie5,width/2,height/2+30,640,360)
        movie5.loop()
    else:
        None
    
    #move your mouse to the area where the words are then click left button to display,or right button cancel
    if mousePressed:
        if mouseButton == LEFT:
           if dist(mouseX,mouseY,width/4,height/6) <= 50:
               flag1 = True
           if dist(mouseX,mouseY,3*width/4,height/6) <= 50:
               flag2 = True
           if dist(mouseX,mouseY,width/4,5*height/6) <= 50:
               flag3 = True
           if dist(mouseX,mouseY,3*width/4,5*height/6) <= 50:
               flag4 = True
           if dist(mouseX,mouseY,width/2,height/2) <= 50:
               flag5 = True
                   
        if mouseButton == RIGHT:
            if dist(mouseX,mouseY,width/4,height/6) <= 50:
               flag1 = False
               movie1.stop()
            if dist(mouseX,mouseY,3*width/4,height/6) <= 50:
               flag2 = False
               movie2.stop()
            if dist(mouseX,mouseY,width/4,5*height/6) <= 50:
               flag3 = False
               movie3.stop()
            if dist(mouseX,mouseY,3*width/4,5*height/6) <= 50:
               flag4 = False
               movie4.stop()
            if dist(mouseX,mouseY,width/2,height/2) <= 50:
               flag5 = False
               movie5.stop()
               music.loop()
    
    global SkillName,iIn
    SkillName = cp5.get(Textfield, "Input Skill Name").getText()
        
def listenToSearch(e):
    global SkillName
    if e.getAction() == ControlP5.ACTION_RELEASED and SkillName!="":
        # search in the dictionary       
        descript = SkillDict[SkillName]
        tts.speak(descript)
        SkillName = ""
        cp5.get(Textfield, "Input Skill Name").clear()
