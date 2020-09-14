import cv2
from human_detector import HumanDetector
import paho.mqtt.client as mqtt

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
        
        if __name__ == '__main__':
            models_dir = '../data/models/yolo-v4/'
            object_detector = HumanDetector(models_dir)
            frame = cv2.imread('../data/sample-images/crowd.jpg')
            bboxes, labels, confidences = object_detector.detect_objects(frame)
            for bbox, label in zip(bboxes, labels):
                start_point = tuple(bbox[:2])
                end_point = tuple(bbox[2:])
                color = (255, 0, 0)
                thickness = 2
                frame = cv2.rectangle(frame, start_point, end_point, color, thickness)
                font = cv2.FONT_HERSHEY_SIMPLEX
                fontScale = 0.7
                frame = cv2.putText(frame, label, start_point, font,
                            fontScale, color, thickness, cv2.LINE_AA)
            cv2.imwrite('../data/output/result.png', frame)
            
broker = '192.168.0.49'
client = mqtt.Client('python1')
client.on_connect = on_connect
client.on_message = on_message

print('Conectando al broker',broker)

client.connect(broker)
client.subscribe([('camara1',0),('camara2',0),('camara3',0)])
client.loop_forever()





