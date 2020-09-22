# publisher
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('192.168.0.48', 1883) # Aqui te conectas a la IP del broker, sea cual sea, uno público o la misma jetson.

# Esta secuencia es de prueba para enviar mensajes ingresados por la consola a los tópicos que aparecen en el primer argumento.
while True:
    client.publish("camara1", input('Message : '))
    client.publish("camara2", input('Message : '))
    client.publish("camara3", input('Message : '))
    client.publish("camara1", input('Message : '))
    client.publish("asdsda", input('Message : '))
