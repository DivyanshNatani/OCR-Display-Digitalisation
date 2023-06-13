## Python Server

These folder contains python files which can constitute as a server and can act as bridge between IP Camera and Database as well as doing the hard task of recoganising the digits.

- **python_server.py** : This is the main file which is used in Demos in presentation. This file contains a for loop which runs after specific period of time (it is an hyper paramenter, currently set to 15s). In this loop, it first calls IP Camera API and stores image from the video feed and then applies seven segment algorithm to retrieve numerical reading. It then connects to Django API and sends the data to the localhosted(or cloud, dependig upon where the django is hosted) database, where these readings are stored.

- **loop_reading.py** : It mimics the same above procedure except it does not connects to IP Camera but randomly assumes a value of reading and sends it to database.

- **api_system.py** : This file considers a different senerio when we cannot place high processing computer system on wifi through which IP Camera is connected. In that case, a possible solution will be connecting a simple arduino chip which can connect to some central computer(star topology), where central computer has comperitively high processing power and can afford seven-segement algorithm. This file uses flask to make that central system, which will provide an API endpoint to small chips which can collect images from the IP camera and send it to central systems using these endpoints. Central flask system can then process these images and then send it to Django database(Django API not connected in this code currently) 
