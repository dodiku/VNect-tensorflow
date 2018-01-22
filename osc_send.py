from pythonosc import osc_message_builder
from pythonosc import udp_client

class OSCServer(object):

    def __init__(self, ip=None, port=None):

        if (ip == None):
            ip = '127.0.0.1'

        if (port == None):
            port = 7483

        try:
            self.client = udp_client.SimpleUDPClient(ip, port)
            print ('📡  OSC client is ready to send messages to {}:{}'.format(ip, port))
        except:
            print ('❌  could not initiate OSC client')


    def send(self, address, content):
        content = content.reshape(-1,content.shape[0]*content.shape[1]).astype(float).tolist()[0]
        self.client.send_message(address, content)

        return
