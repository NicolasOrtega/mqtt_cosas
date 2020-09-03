import paho.mqtt.client as mqtt
import time

def on_log(client, userdata, level, buf):
    print('log: '+buf)

def on_connect(client,userdata,flags,rc):
    if rc == 0:
        print('Conectado!')
    else:
        print('No conectado :(, codigo: ',rc)

def on_disconnect(client, userdata, flags, rc):
    print('Desconectado, codigo: '+str(rc))

def on_message(client,userdata,msg):
        topic = msg.topic
        print(topic)

broker = '192.168.0.49'
client = mqtt.Client('python1')
client.on_connect = on_connect
client.on_message = on_message

print('Conectando al broker',broker)

client.connect(broker)
client.subscribe([('camara1',0),('camara2',0),('camara3',0)])
client.loop_forever()
