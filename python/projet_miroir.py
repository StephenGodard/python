# Module de lecture/ecriture du port série
from serial import *
import time
# Port série ttyACM0
# Vitesse de baud : 9600
# Timeout en lecture : 1 sec
# Timeout en écriture : 1 sec
with Serial(port="/dev/ttyUSB2", baudrate=9600, timeout=1, writeTimeout=1) as port_serie:
    while True:
        ligne = port_serie.readline()
        print(ligne.decode('utf-8'))

