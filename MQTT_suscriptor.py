import paho.mqtt.client as mqtt
import time

# Esta funcion es la que definen los locos en internet para tener respuesta de lo que está haciendo el cliente MQTT
def on_log(client, userdata, level, buf):
    print('log: '+buf)

# Con esta función se verifica que el cliente conecte.
def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print('Conectado!')
    else:
        print('No conectado :(, codigo: ',rc)

# Esta función se ejecuta si el cliente se desconecta
def on_disconnect(client, userdata, flags, rc):
    print('Desconectado, codigo: '+str(rc))

# Esta función se ejecuta cada vez que llega un mensaje. En este caso la hago imprimir el tópico del mensaje recibido.
def on_message(client,userdata,msg):
        topic = msg.topic
        print(topic)

broker = '192.168.0.49'
client = mqtt.Client('python1')
client.on_connect = on_connect
client.on_message = on_message

print('Conectando al broker',broker)

# La secuencia que sigue permite que el cliente esté conectado siempre. Hay otras formas también, en las que el cliente se conecta y reconecta dados ciertos intervalos de tiempo.
# Esas cosas salen en la documentación de la libreria paho.mqtt
client.connect(broker)
client.subscribe([('camara1',0),('camara2',0),('camara3',0)])
client.loop_forever()
