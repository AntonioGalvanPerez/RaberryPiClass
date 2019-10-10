from sense_hat import SenseHat
import time

sense = SenseHat()
temp = sense.get_temperature()


#Colors
p = (204,0,204)
g = (0,102,102)

Heart1 = [
    g, g, g, g, g, g, g, g,
    g, p, p, g, g, p, p, g,
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    p, p, p, p, p, p, p, p,
    g, p, p, p, p, p, p, g,
    g, g, p, p, p, p, g, g,
    g, g, g, p, p, g, g, g,
    ]
    
Heart2 = [
    p, p, p, p, p, p, p, p,
    p, g, g, p, p, g, g, p,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    g, g, g, g, g, g, g, g,
    p, g, g, g, g, g, g, p,
    p, p, g, g, g, g, p, p,
    p, p, p, g, g, p, p, p,
    ]

#Flashes Heart 
for i in range (10):
    sense.set_pixels(Heart1)
    time.sleep(.5)
    sense.set_pixels(Heart2)
    time.sleep(.5)
    sense.set_pixels(Heart1)

#sense.show_message ("Love")