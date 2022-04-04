import ssl

import paho.mqtt.client as mqtt
import json


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print(str(rc))


def on_publish(client, userdata, mid):
    print("In on_pub callback mid= ", mid)

def on_message(client, userdata, msg):

    print(str(msg.payload.decode("utf-8")))

def on_subscribe(client, userdata, mid, granted_qos):

    print("subscribed: " + str(mid) + " " + str(granted_qos))

# 새로운 클라이언트 생성
client = mqtt.Client("algo_result")
# client.tls_set("/home/autoever/bin/cmsAbasic/certs/ca.crt", cert_reqs = ssl.CERT_NONE)
# 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지
# 발행)

client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_subscribe = on_subscribe
client.on_message = on_message

client.connect("localhost" , 1883)
client.loop_start()
client.publish('cms/algo/cms_algo/cms_daq',

               json.dumps({"HAEcms":
                   [{"fr": "CMS_ALG",
                     "to": "CMS_DMC",
                     "model": 'lof2.model',
                     "si": "",
                     "ct": "20211008113017"
                     }]
                           }), 1)

client.loop_stop()
client.disconnect()