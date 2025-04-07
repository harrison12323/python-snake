import turtle
import time
import random
import pygame
import os

# Set TK_SILENCE_DEPRECATION to suppress Tk deprecation warning on macOS
os.environ['TK_SILENCE_DEPRECATION'] = '1'

# Game variables
delay = 0.1
score = 0
high_score = 0

# Initialize screen with error handling
try:
    # Screen setup
    wn = turtle.Screen()
    wn.title("Snake Game by harrison")
    wn.bgcolor("#000000")
    wn.setup(width=725, height=725)
    wn.tracer(0)
    
    # Force a screen update and add a small delay for macOS compatibility
    wn.update()
    time.sleep(0.5)
    
    # Initialize the snake head
    head = turtle.Turtle()
    head.speed(0)
    head.shape("circle")
    head.color("#0000FF")
    head.penup()
    head.goto(0, 0)
    head.direction = "stop"
    
    food = turtle.Turtle()
    food.speed(0)
    food.shape("square")
    food.color("#FFFF00")
    food.penup()
    food.goto(0, 100)
    segments = []
    
    pen = turtle.Turtle()
    pen.speed(0)
    pen.shape("triangle")
    pen.color("#0000FF")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))
    # Define game functions
    def go_up():
        if head.direction != "down":
            head.direction = "up"
    
    def go_down():
        if head.direction != "up":
            head.direction = "down"
    
    def go_left():
        if head.direction != "right":
            head.direction = "left"
    
    def go_right():
        if head.direction != "left":
            head.direction = "right"
    
    def move():
        if head.direction == "up":
            y = head.ycor()
            head.sety(y + 20)
        if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
        if head.direction == "left":
            x = head.xcor()
            head.setx(x - 20)
        if head.direction == "right":
            x = head.xcor()
            head.setx(x + 20)
    
    def cheat_increase_score():
        global score, high_score
        score += 50  
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
    
    # Set up keyboard bindings
    wn.listen()
    wn.onkeypress(go_up, "w")
    wn.onkeypress(go_down, "s")
    wn.onkeypress(go_left, "a")
    wn.onkeypress(go_right, "d")
    wn.onkeypress(cheat_increase_score, "c")
    # Main game loop
    while True:
        wn.update()
        
        # Check for collision with border
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        # Check for collision with food
        if head.distance(food) < 20:
            # Move food to random position
            x = random.randint(-290, 290)
            y = random.randint(-290, 290)
            food.goto(x, y)
            
            # Add a segment to the snake
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("#0000FF")
            new_segment.penup()
            segments.append(new_segment)
            
            # Shorten the delay to speed up game
            delay -= 0.001
            
            # Increase the score
            score += 10
            
            # Update high score if needed
            if score > high_score:
                high_score = score
            
            # Update the score display
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        # Move the end segments first in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)
        
        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)
        
        # Move the snake
        move()
        
        # Check for collision with body segments
        for segment in segments:
            if segment.distance(head) < 20:
                time.sleep(1)
                head.goto(0, 0)
                head.direction = "stop"
                
                # Hide the segments
                for segment in segments:
                    segment.goto(1000, 1000)
                
                # Clear the segments list
                segments.clear()
                
                # Reset the score
                score = 0
                
                # Reset the delay
                delay = 0.1
                
                # Update the score display
                pen.clear()
                pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        
        # Add a small delay between frames
        time.sleep(delay)
except Exception as e:
    print(f"Error initializing game: {e}")
    print("If you're on macOS, try running with python3 and ensure you have proper permissions.")
    import sys
    sys.exit(1)

# Start the game event loop if everything initialized correctly
wn.mainloop()
