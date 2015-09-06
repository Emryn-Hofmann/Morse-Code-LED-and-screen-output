#use pins 15 and GND for the GPIO

import RPi.GPIO as GPIO
import time
# to use Raspberry Pi board pin numbers
Rate = 0.33

GPIO.setmode(GPIO.BCM)
GPIO.setup(15, GPIO.OUT)

conversion = {"A" : ".-", "B" : "-...", "C" : "-.-.", "D" : "-..", "E" : ".", "F" : "..-.", "G" : "--.", "H" : "....", "I" : "..", "J" : ".---", "K" : "-.-", "L" : ".-..", "M" : "--", "N" : "-.", "O" : "---", "P" : ".--.", "Q" : "--.-", "R" : ".-.", "S" : "...", "T" : "-", "U" : "..-", "V" : "...-", "W" : ".--", "X" : "-..-", "Y" : "-.--", "Z" : "--..", "1" : ".----", "2" : "..---", "3" : "...--", "4" : "....-", "5" : ".....", "6" : "-....", "7" : "--...", "8" : "---..", "9" : "----.", "0" : "-----", "." : ".-.-.-", "," : "--..--"}

def morse_line():
        GPIO.output(15, GPIO.HIGH)
        time.sleep(3*Rate)
        GPIO.output(15,GPIO.LOW)
        time.sleep(Rate)


def morse_dot():
        GPIO.output(15,GPIO.HIGH)
        time.sleep(Rate)
        GPIO.output(15,GPIO.LOW)
        time.sleep(Rate)

text = raw_input("Morse code: ").upper()

for i in range(len(text)):
    morseCode = conversion[text[i]]
#Uncomment this if you want to see the morse code in the shell, in the form of dots (.) and dashes (-)
#    print(morseCode)
    for j in range(len(morseCode)):
        character = morseCode[j]
        if (character == '-'):
                morse_line()
        elif (character == '.'):
                morse_dot()
        elif (character == ' '):
                time.sleep(7*Rate)
        else:
                print("invalid character - use dots and dashes (. and -)")
