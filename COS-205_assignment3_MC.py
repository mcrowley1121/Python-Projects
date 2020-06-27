#   COS-205_assignment3_MC.py
#   This program will request inputs for the radius of a circle and the y-intercept at which a horizontal line will intersect it.
#   The program will then draw the circle and intersecting line, displaying red dots at the intersecting points.
#   The program print out the x coordinates for the intersecting points at the top left of the graphic window that was created.
#   The program will close when the user clicks their mouse within the graphics window.
#   by: Mike Crowley

#Importing entire graphics module to this assignment allowing us to utilize functions and objects from graphics.py
from graphics import *
#Importing math to allow use of the square root function
import math

#Defining main function of program.
def main():

    #Creating graphic window for user interface
    win = GraphWin("COS-205_assignment3_MC", 400, 400)

    #Reminding user that the circle's radius determines its length along the y-axis
    print("Please be advised that if your circle has a small radius, it may not intersect with your desired y-intercept.")

    #Asking the user to input the value they would like for the circle's radius and storing it in the variable 'radius'
    radius = float(input("Please enter the desired radius of your circle (valid entries range from greater than 0 through 10)) : "))
    #Asking the user to input the value they would like for the y-intercept and storing it in the variable 'y_intercept'
    y_intercept = float(input("Please enter where on the y-axis you would like the horizontal line to intercept your circle (valid entries may range from -10 through 10 depending on radius): "))

    #Setting the coordinates of the graphical window to lower left value of (-10, -10) and upper right value of (10, 10)
    #This allows for the program's graphics to scale accordingly instead of
    #requiring the programmer to adjust pixel position if changes are made to the dimensions of the window
    win.setCoords(-10,-10, 10, 10)

    #Creating a circle with a center point (0, 0) and the radius from the user's input and assigning it to variable 'circ'
    circ = Circle(Point(0, 0), radius)
    #Drawing the circle to the graphic window
    circ.draw(win)

    #Assiging the value of the intersecting line to variable 'intersecting_line' based on the user's given y-intercept.
    intersecting_line = Line(Point(-10, y_intercept), Point(10, y_intercept))
    #Drawing the horizontal intersecting line
    intersecting_line.draw(win)

    #Inputting error handling in case the user chooses an intercept that is outside of their circle's reach
    #Attempting to take x coordinates for left and right intersecting Points
    #Program will try to complete the equation below. If it is not possible, it will run the 'except' portion.
    try:
        x_of_left_intersection = (math.sqrt(radius ** 2 - y_intercept ** 2)) * -1
        x_of_right_intersection = (math.sqrt(radius ** 2 - y_intercept ** 2))
    #Printing a message for the user asking them to try again as they did not input valid values
    except:
        #Printing blank line for readability, followed by error handling message.
        print()
        print("It appears your circle is not large enough to intersect your desired y-intercept.")
        print("Please enter a larger radius or a y-intercept closer to 0 and try again.")

    #Creating variables to store location of left and right intersections
    left_intersection = Point(x_of_left_intersection, y_intercept)
    right_intersection = Point(x_of_right_intersection, y_intercept)

    #Adjusting the color of the intersecting points to be red
    left_intersection.setFill("red")
    right_intersection.setFill("red")

    #Drawing the red dots at the left and right intersecting points
    left_intersection.draw(win)
    right_intersection.draw(win)

    #Converting x coordinates to strings and rounding to 2 decimal places so that they may be shown as text in the graphical window.
    string_left_intersection_x_value = str(round(left_intersection.getX(), 2))
    string_right_intersection_x_value = str(round(right_intersection.getX(), 2))

    #Displaying text showing message and x values of left and right intersecting points
    #Condensed strings and assigned to one variable 'message' to successfully meet syntax requirements for Text()
    message = "Your intersecting X-coordinates (L and R respectively):", string_left_intersection_x_value, ";", string_right_intersection_x_value
    #Created text anchor and included the message above
    message_1 = Text(Point(-1.5, 9), message)
    #Drew message in the graphical window
    message_1.draw(win)

    #Waiting for user to click mouse to close window
    win.getMouse()
    #Closed window after user input
    win.close()

#Running main function
main()