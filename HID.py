#----------Code by Arwaz Khan | Wishing you Happy Independence Day 2020 -------------------------------
import turtle
import winsound #pip install winsound
winsound.PlaySound('sound.wav',winsound.SND_ASYNC)  # play audio

t=turtle.Turtle()  #t variable 

s=turtle.Screen()
s.title("Happy Independance Day ")   #title
s.bgpic("image.gif")    #set india map bg image
s.bgcolor("black")



t.speed(5)  # speed of drawing   
t.ht()  #hiding turtle pen

#Comments are the position of turtle pen
#-------functions-------------
def startpoint():
    t.up()
    t.rt(90)
    t.fd(200)
    t.rt(90)
    t.fd(200)
    t.rt(180)    #start point of bottom stair

def stair():
    t.pencolor("orange")
    t.down()
    t.pensize(25)
    t.fd(150)   #bottom stair end 
    t.up()
    t.lt(90)
    t.fd(25)
    t.lt(90)
    t.fd(25)
    t.down()
    t.fd(100)   #middle stair end 
    t.up()
    t.rt(90)
    t.fd(25)
    t.rt(90)
    t.fd(25)
    t.down()
    t.fd(50)  #top stair end 
    t.up()
    t.rt(180)
    t.fd(25)
    t.rt(90)  #middle of the top stair

    
def pole():
    t.down()
    t.fd(5)
    t.pensize(10)
    t.pencolor("grey") 
    t.fd(345)      #top of pole
    t.pencolor("gold")
    t.circle(0.3)
    t.up()
    t.rt(180)
    t.fd(20)
    t.lt(90)
    t.fd(5)  #positon to draw the flag
    
def flag():
    t.down()
    def onerec(color):       #This function is used to draw one of the tricolor of rectangle shape 
        t.pencolor("black")
        t.fillcolor(color)
        t.begin_fill()   #start filling color -orange|white|green
        t.pensize(1)
        t.fd(200)
        t.rt(90)
        t.fd(33.3)
        t.rt(90)
        t.fd(200)
        t.end_fill()    #end filling  color
        t.pencolor("grey")
        t.fd(5)
        t.rt(90)
        t.fd(33.3)
        t.rt(90)
        t.fd(5)
        
    def setpoint():  #This function sets the postion of pen to draw one flag color
        t.rt(90)
        t.fd(33.3)
        t.lt(90)
        
    def cakr():   # function - drawing Ashoka Chakra
        t.down()
        t.pencolor("blue")
        t.pensize(1)
        t.circle(16.65)
        t.lt(90)
        t.up()
        t.fd(16.65)
        t.dot(5,"blue")
        def lines():              # function - drawing lines in chakra
            t.down()
            for i in range(24):
                t.fd(16.65)
                t.up()
                t.bk(16.65)
                t.rt(15)
                t.down()
        lines()
        t.up()
     #### calling function onrec() for different colors--------  
    onerec("orange")  
    setpoint()
    onerec("white")
    setpoint()
    onerec("green")
    ###---------
    t.up()
    t.fd(120)
    t.lt(90)
    t.fd(16.65)

    cakr()    #calling  functio cakr() to draw Chakra

def hid():   #function - writing HID2020
    t.goto(0,-90)
    t.pencolor("orange")
    t.write("Happy",font=('Courier',30,'bold'))
    t.goto(-50,-120)
    t.pencolor("white")
    t.write("Independence",font=('Courier',30,'bold'))
    t.goto(0,-150)
    t.pencolor("green")
    t.write("Day",font=('Courier',30,'bold'))
    t.goto(-10,-180)
    t.pencolor("white")
    t.write("2020",font=('Courier',30,'bold'))   
#----------main function-------
def MAIN():
    startpoint() #goto bottom from
    stair() #drawing stair
    pole() #drawing pole
    flag() #drawing flag
    hid() #writing happy independance day 2020
#--------function end ---------------


MAIN()   # ---calling main function---------

t.goto(100,300)
t.pencolor("white")
t.write("❗Click on screen to exit",font=('Courier',10,'bold'))
turtle.exitonclick()    #exit on click
winsound.PlaySound(None,winsound.SND_ASYNC)  # Stop audio

turtle.done()
 
