from pythonosc import osc_message_builder
from pythonosc import udp_client
import numpy as np
import math

class OSCServer(object):

    def __init__(self, ip=None, port=None):

        if (ip == None):
            self.ip = '127.0.0.1'
        else:
            self.ip = ip

        if (port == None):
            self.port = 7483
        else:
            self.port = port

        try:
            self.client = udp_client.SimpleUDPClient(ip, port)
            print ('📡  OSC client is ready to send messages to {}:{}'.format(ip, port))
        except:
            print ('❌  could not initiate OSC client')


    def send(self, address, content, hm=0):

        print ('👫  Predicted {} joints from {}x{} heatmap'.format(content.shape[0], hm.shape[1], hm.shape[2]))

        # creating 90 degrees rotation matrix
        rotation = np.array(([math.cos(1.5708), (-1)*math.sin(1.5708)], [math.sin(1.5708), math.cos(1.5708)]))

        # rotating the content
        content = np.dot(content, rotation)

        # creating a list for OSC purposes
        content = content.reshape(-1,content.shape[0]*content.shape[1]).astype(float).tolist()[0]

        self.client.send_message(address, content)
        print ('📡  Joints data was sent successfully over OSC to {}:{}'.format(self.ip, self.port))
        print (content[0], content[1])
        print (content[2], content[3], '\n')

        return
