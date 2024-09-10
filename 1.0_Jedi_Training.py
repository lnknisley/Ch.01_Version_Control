'''
1.0 Jedi Training (17pts)  Name: Logan Knisley


1. Define Forking (1pt): Forking is the term for creating a new repo based off an existing repository.

2. Define Cloning (1pt): Cloning is the term for downloading a copy of a repo onto your system.

3. Define Branching (1pt): Branching is the term for the creation of repos that spread from a
 main/master branch (akin to the branches of a tree coming from a tree's truck, hence the term's name).

4. Define Committing (1pt): Commiting is the name for pushing new code into an existing repo.

5. Define Merging (1pt): Merging is the merging the changes of a forked branch into the master repository.

6. Define Pushing (1pt): Pushing is the name for pushing changes into a codebase. Force pushing is pushing without any need for approval.

7. Define Pull Request (1pt): A pull request is a request for someone's changes to be merged into the master branch.

8. TURTORIAL ART (10pts.)

Modify the starter code below to create your own cool drawing. 
Make sure you keep the last two lines of code!!!! 
Your first and last name must be written on your art.
The last line keeps the window open until you click to close.
Turtle Documentation: https://docs.python.org/3.3/library/turtle.html?highlight=turtle
'''
import turtle
snake = turtle.Turtle()

screen = turtle.Screen()
screen.screensize(200, 200)
screen.bgcolor("#cccccc")

snake.pensize(8)
snake.color("grey")
#Array indexs
slither = [4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3, 4, 3]
circle = [4, 4, 4, 4, 4, 3, 3, 5, 3, 7]
y = [5, 4, 3]
ux = [1, 2, 3, 4, 5, 6, 7]

#Function declarations
def zig(x):
  snake.pendown()
  if x % 2 == 0:
    snake.goto(snake.xcor() + 20, snake.ycor() + 20)
  else:
    snake.goto(snake.xcor() - 20, snake.ycor() + 20)
    
def zag():
  snake.pendown()
  snake.goto(snake.xcor() - 40, snake.ycor() - 20)
    
def ball(x):
  snake.pendown()
  if x % 2 == 0:
    snake.goto(snake.xcor() + 40, snake.ycor() + 20)
  else:
    snake.goto(snake.xcor() + 40, snake.ycor() - 20)

for i in y:
  #Cage outline
  snake.penup()
  snake.setpos(-200, -175 + (i * 12))
  snake.pendown()

  for cir in circle:
    ball(cir)
    
#Reptile setup
snake.pensize(24)
snake.penup()
snake.color("#365ab3")
snake.setpos(0, -200)

for slith in slither:
  #Draws the snake itself
  zig(slith)

#Draws the snake's face
snake.pensize(12)
snake.penup()
snake.goto(snake.xcor() - 10, snake.ycor() + 10)
snake.color("red")
snake.pendown()
snake.goto(snake.xcor() - 15, snake.ycor() + 15)
snake.penup()
snake.goto(snake.xcor() + 25, snake.ycor() - 25)
snake.color("white")
snake.pendown()
snake.goto(snake.xcor() + 1, snake.ycor() - 1)

snake.pensize(8)
snake.color("grey")

for j in ux:
  #Cage bars
  snake.penup()
  snake.setpos(0 + (j * 40), -20 - (j * 20))
  snake.pendown()
  
  for cir in circle:
    zag()

snake.penup()
snake.goto(0, 200)
snake.write('Logan Knisley',font=("Arial", 16, "normal")) # signs your name to your art
turtle.exitonclick() #Keeps pycharm window open so we can see the drawing
