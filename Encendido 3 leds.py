from machine import Pin
from time import sleep

# Configuración de los pines
led1 = Pin(12, Pin.OUT)  # Conectar el LED1 al pin 2
led2 = Pin(27, Pin.OUT)  # Conectar el LED2 al pin 4
led3 = Pin(25, Pin.OUT)  # Conectar el LED3 al pin 5

# Tiempo en segundos entre cada encendido/apagado
delay = 0.5

while True:
    # Encender LEDs de forma secuencial
    led1.on()
    sleep(delay)
    led2.on()
    sleep(delay)
    led3.on()
    sleep(delay)
    
    # Apagar LEDs de forma secuencial
    led1.off()
    sleep(delay)
    led2.off()
    sleep(delay)
    led3.off()
    sleep(delay)