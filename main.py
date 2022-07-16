import turtle
import time
import random

#Delay
delay=0.1


#Score
score=0
high_score=0


#Set up the screen
wn=turtle.Screen()
wn.title("Snake Game by @zkakhetelidze")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0) #Turns off the screen updates


#Snake head
head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0,0)
head.direction="stop"


#Snake food
food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)


#List for the snake segments
segments=[]


#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))


#Functions
def go_up():
    if head.direction != "down": #it won't go down if it's going up
        head.direction="up"

def go_down():
    if head.direction != "up":
        head.direction="down"

def go_left():
    if head.direction != "right":
        head.direction="left"

def go_right():
    if head.direction != "left":
        head.direction="right"            


def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)

    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)

    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)            


#Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


#Main game loop
while True:
    wn.update()

    #Check for collison with the border
    if head.xcor() > 290 or head.xcor() <-290 or head.ycor()>290 or head.ycor( )<-290: #if head goes off the screen to the right, left,top or the bottom  
        time.sleep(0.4) #pauses the game for 1 second
        head.goto(0,0) 
        head.direction="stop"

        #Hide the segments
        for segment in segments:
            segment.goto(1000,1000) #moves segments off the screen

        #Clear the segments list
        segments.clear()  

        #Reset the score
        score=0 

        #Reset the delay
        delay=0.1

        #Update the score display
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("Courier", 24, "normal"))    
         

    #Check for a collision with the food
    if head.distance(food)<20: #every basic turtle shape is 20x20 pixels        
        #Move the food to the random spot
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)

        #Add a segment
        new_segment=turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("blue")
        new_segment.penup()
        segments.append(new_segment)

        #Shorten the delay
        delay-=0.001

        #Increase the score
        score+=1

        if score >high_score:
            high_score=score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("Courier", 24, "normal"))    

    #Move the end segments first in reverse order
    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    #Move segment 0 to where the head is 
    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)    


    move()

    
    #Check for the head collision with the body segments
    for segment in segments:    
        if segment.distance(head)<20:
            time.sleep(0.4)
            head.goto(0,0)
            head.direction="stop"

            #Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)
           
            #Clear the segments list
            segments.clear() 

            #Reset the score
            score=0 

            #Reset the delay
            delay=0.1
        
            #Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score,high_score),align="center", font=("Courier", 24, "normal"))     

    time.sleep(delay)


wn.mainloop()