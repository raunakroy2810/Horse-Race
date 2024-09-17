from turtle import Turtle, Screen  # Import Turtle and Screen classes from the turtle module
import turtle  # Import the turtle module
import random  # Import random module to generate random choices


# Function to send the horses back to the starting line
def starting_line(n, x):
    n.penup()  # Lift the pen so the turtle doesn't draw a line while moving
    n.shape("minihorsebgls.gif")  # Set the turtle's shape to the horse image
    n.goto(-425, x)  # Move the turtle to the starting position (x-coordinate = -425)


# Function to move the horse forward randomly
def move_forward(n):
    n.speed('slow')  # Set the movement speed to slow
    x = [10, 20, 30]  # Create a list of possible step sizes
    n.forward(random.choice(x))  # Move forward by randomly selecting one of the step sizes


# Register the custom horse shape
turtle.register_shape("minihorsebgls.gif")

# Defining all the turtle objects (5 horses)
horse_1 = Turtle()
horse_2 = Turtle()
horse_3 = Turtle()
horse_4 = Turtle()
horse_5 = Turtle()

# Set up the screen
sc = Screen()
turtle.bgpic("HorseTrack.png")  # Set the background image as a race track
sc.setup(1000, 800)  # Set up the screen size to 1000x800 pixels

# Send all the horses to their starting positions
starting_line(horse_1, x=320)  # Position horse 1 at y-coordinate = 320
starting_line(horse_2, x=160)  # Position horse 2 at y-coordinate = 160
starting_line(horse_3, x=0)  # Position horse 3 at y-coordinate = 0
starting_line(horse_4, x=-160)  # Position horse 4 at y-coordinate = -160
starting_line(horse_5, x=-320)  # Position horse 5 at y-coordinate = -320

# Get the player's bet by asking for input through a dialog box
bet = sc.textinput(prompt="Choose the horse you want to bet on [1,2,3,4,5]", title="Bet")

# Initialize the race condition
X = True  # Control variable for the race loop

# Main loop for the horse race
while X:
    # Move each horse forward by a random amount
    move_forward(horse_1)
    move_forward(horse_2)
    move_forward(horse_3)
    move_forward(horse_4)
    move_forward(horse_5)

    # Check if any horse crosses the finish line (x-coordinate >= 425)
    if horse_1.xcor() >= 425:
        c = 1  # Horse 1 wins
        X = False  # End the race loop
    elif horse_2.xcor() >= 425:
        c = 2  # Horse 2 wins
        X = False
    elif horse_3.xcor() >= 425:
        c = 3  # Horse 3 wins
        X = False
    elif horse_4.xcor() >= 425:
        c = 4  # Horse 4 wins
        X = False
    elif horse_5.xcor() >= 425:
        c = 5  # Horse 5 wins
        X = False

# After the race ends, check if the player's bet matches the winning horse
if int(bet) == c:
    print("You WON")  # Player wins the bet
else:
    print("You LOSE")  # Player loses the bet

# Announce which horse won the race
if c == 1:
    print("1st horse wins")
elif c == 2:
    print("2nd horse wins")
elif c == 3:
    print("3rd horse wins")
elif c == 4:
    print("4th horse wins")
elif c == 5:
    print("5th horse wins")

# Wait for a click to exit the game
sc.exitonclick()
