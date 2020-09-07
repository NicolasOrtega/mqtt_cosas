# publisher
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect('192.168.0.48', 1883)

while True:
    client.publish("camara1", input('Message : '))
    client.publish("camara2", input('Message : '))
    client.publish("camara3", input('Message : '))
    client.publish("camara1", input('Message : '))
    client.publish("asdsda", input('Message : '))