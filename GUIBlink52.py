  # if it is lit, turn it off, change the button text, and deselect the radial
    if led.is_lit:
        led.off()
        button["text"]="Turn " + buttonColour.get() + " LED on" # Change only the button text property
        button.deselect()
    # if it is off, turn all led's off, reest all the button text's, and then turn on the specified led and change the appropiate
    # button text
    else:
        for LED in LEDs:
            LED.off()
        for clearButton in buttons:
            resetButtonText(clearButton)
        led.on()
        button["text"]="Turn " + buttonColour.get() + " LED off"


# elegantly closes the program
def close():
    RPi.GPIO.cleanup()
    window.destroy()
# SIT210 5.2C
## Code template used from core-electronics.com.au, thanks heaps! ##
## Toggle an LED when the GUI button is pressed ##

# import the required libraries
from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
redLED=LED(15)
greenLED=LED(18)
blueLED=LED(17)
LEDs=[redLED, blueLED, greenLED]

### GUI DEFINITIONS ###
window = Tk()
window.title("LED Toggler")
windowFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

### Strings for the buttons ###
redDefaultText="Turn red LED on"
greenDefaultText="Turn green LED on"
blueDefaultText="Turn blue LED on"

# shared variable for the buttons
buttonColour=tkinter.StringVar()

### Event Functions ###
# toggles a led off if it's on, otherwise turns all off and turns the specified led on
def ledToggle(led, button):
    # if it is lit, turn it off, change the button text, and deselect the radial
    if led.is_lit:
        led.off()
        button["text"]="Turn " + buttonColour.get() + " LED on" # Change only the button text property
        button.deselect()
    # if it is off, turn all led's off, reest all the button text's, and then turn on the specified led and change the appropiate
    # button text
    else:
        for LED in LEDs:
            LED.off()
        for clearButton in buttons:
            resetButtonText(clearButton)
        led.on()
        button["text"]="Turn " + buttonColour.get() + " LED off"

# elegantly closes the program
def close():
    RPi.GPIO.cleanup()
    window.destroy()

# resets the button text to the strings defined
def resetButtonText(button):
    if button == redLEDButton:
        button["text"]=redDefaultText
    elif button == blueLEDButton:
        button["text"]=blueDefaultText
    elif button == greenLEDButton:
        button["text"]=greenDefaultText

### WIDGETS ###

# Button, triggers the connected command when it is pressed
redLEDButton = Radiobutton(window, text=redDefaultText, font=windowFont, variable=buttonColour, command=lambda: ledToggle(redLED, redLEDButton), bg='tomato', height=1, $
redLEDButton.grid(row=0,column=1)


blueLEDButton = Radiobutton(window, text=blueDefaultText, font=windowFont, command=lambda: ledToggle(blueLED, blueLEDButton), bg='DodgerBlue2', height=1, width=20, vari$
blueLEDButton.grid(row=1,column=1)

greenLEDButton = Radiobutton(window, text=greenDefaultText, font=windowFont, command=lambda: ledToggle(greenLED, greenLEDButton), bg='palegreen', height=1, width=20, va$
greenLEDButton.grid(row=2,column=1)

# used to change all the button texts
buttons=[redLEDButton, blueLEDButton, greenLEDButton]

# used to close the program
exitButton = Button(window, text='Exit', font=windowFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=3, column=1)

window.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

window.mainloop() # Loops forever


