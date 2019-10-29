from serial import Serial
import time

arduino = Serial('COM3',9600)




while(1):

    c=input()

    if c =='q':

        break

    else:

        c=c.encode('utf-8')

        arduino.write(70)

