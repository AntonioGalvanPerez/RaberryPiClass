#Change the Shape arrays to display two shapes that will alternate back and forth
#By either using the colors provided or by creating custom collors from: https://www.rapidtables.com/web/color/RGB_Color.html
#At the end change the default text to a new message

from sense_hat import SenseHat
import time

sense = SenseHat()

#Color Variables
O = (0,0,0)       #Black
R = (255,0,0)     #Red
G = (0,255,0)     #Green
B = (0,0,255)     #Blue
Y = (255,55,0)    #Yellow
P = (255,51,153)  #Pink



#Example with no Variables
Shape1 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

Shape1 = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    ]

#Flashes Shapes 
for i in range (10):
    sense.set_pixels(Shape1)
    time.sleep(.5)
    sense.set_pixels(Shape2)
    time.sleep(.5)
    sense.set_pixels(Shape1)

 sense.show_message ("ENTER TEXT HERE")
