import requests
import random
import time
from datetime import datetime 
for i in range(5):
    a=random.randint(10, 100)
    read=30+a/10
    # print(datetime.now())
    # print(read)
    req={
        'data': read,
        'time_of_reading': str(datetime.now())[:19]
    }
    print('request=', req)
    print('----------------')
    r=requests.get(url='http://127.0.0.1:8000/adddata', params=req)
    print('response', r.json())
    print("============================")
    # print(r.json())
    time.sleep(30)