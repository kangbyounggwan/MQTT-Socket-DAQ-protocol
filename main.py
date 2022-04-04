import socket
import ssl

from model import rrcf, lof
# from mqtt_pub
from preprocessing import fft_t_sum
import time
import json
import paho.mqtt.client as mqtt
from queue import Queue
import warnings
warnings.filterwarnings('ignore')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
recv_address = ('localhost', 30010)
sock.bind(recv_address)
print('socket OK')
sock.listen(1)
conn, addr = sock.accept()
# recv and send loop
# print(model_name)
raw_data = []
while True:
    loof_input = raw_data.append
    data = conn.recv(32000)
    print('input data len:',len(data))
    if len(data) != 32000:
        continue
    # 받고 data를 돌려줌
    infer_start = time.time()
    for i in range(4000):
        loof_input(data[i])
    print('test len:',len(raw_data))
    if len(raw_data) == 8000:


        t_sum_raw = fft_t_sum(raw_data)
        # rcf_score, rcf_predict = rrcf(t_sum_raw)
        lof_predict, lof_score = lof(t_sum_raw)
        print('end')

        client = mqtt.Client("algo_result")
        client.tls_set("/home/autoever/bin/cmsAbasic/certs/ca.crt", cert_reqs = ssl.CERT_NONE)
        # 콜백 함수 설정 on_connect(브로커에 접속), on_disconnect(브로커에 접속중료), on_publish(메세지
        # 발행)

        client.connect("localhost", 8883)
        client.publish('cms/algo/cms_dmc/cms_algo',

                       json.dumps({"HAEcms":
                                       [{"fr": "CMS_ALG",
                                         "to": "CMS_DMC",
                                         "rt": {'score':lof_score.tolist(),
                                                'predict':lof_predict.tolist()},
                                         "si": "",
                                         "ct": "20211008113017"
                                         }]
                                   }), 1)
        raw_data = []
        print("inference time :", time.time() - infer_start, 's')
    continue





