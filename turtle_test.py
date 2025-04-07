import turtle
import time
import os
import sys

# Suppress deprecation warnings
os.environ['TK_SILENCE_DEPRECATION'] = '1'

try:
    # Setup the screen
    screen = turtle.Screen()
    screen.title("Turtle Graphics Test")
    screen.setup(400, 400)
    
    # Force a screen update and short delay
    screen.update()
    time.sleep(0.5)
    
    # Create a turtle
    t = turtle.Turtle()
    t.shape("turtle")
    t.pensize(3)
    
    # Draw a simple square
    for _ in range(4):
        t.forward(100)
        t.right(90)
        # Short delay to ensure graphics render properly
        time.sleep(0.1)
    
    # Move to another position
    t.penup()
    t.goto(-50, -50)
    t.pendown()
    
    # Draw a triangle
    t.color("blue")
    for _ in range(3):
        t.forward(100)
        t.left(120)
        time.sleep(0.1)
    
    # Show text on screen
    t.penup()
    t.goto(0, 150)
    t.write("Turtle Test Complete", align="center", font=("Arial", 12, "normal"))
    
    # Keep the window open
    print("Turtle test running - close the window to exit")
    screen.mainloop()
    
except Exception as e:
    print(f"Error occurred: {e}")
    print("There might be an issue with your turtle graphics setup.")
    sys.exit(1)

