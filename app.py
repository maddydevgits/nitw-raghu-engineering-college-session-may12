# package has to be imported if you want to connected with aws broker
from AWSIoTPythonSDK.MQTTLib import AWSIoTMQTTClient
import time
from generate_some_random_data import *

# create a MQTT Client Object
client=AWSIoTMQTTClient('nitw_client')

# configure the endpoint (broker) - paste it from interact(view settings)
client.configureEndpoint('a366shaagepcsd-ats.iot.ap-south-1.amazonaws.com',8883)

# configure the device credentials
# Root Certificate, Device Private Key, Device Certificate
client.configureCredentials('AmazonRootCA1.pem','device-private.pem.key','device-certificate.pem.crt')

# configure the queueing 
client.configureOfflinePublishQueueing(-1)

#configure the data transfer
client.configureDrainingFrequency(2)

#configure discconect connect timeout
client.configureConnectDisconnectTimeout(10)

#configure operation timeout
client.configureMQTTOperationTimeout(5)

try:
    client.connect() # connected with broker
    print('Connected with AWS')
    while True:
        h,t=readDataRandom() # reading data 
        print('Connected with AWS')
        payload='{"temperature": '+str(t) +',"humidity": '+str(h)+'}' # prepare a string
        #print(payload)
        client.publish('nitw/rec',payload,0)
        print('Data Published to AWS Broker')
        time.sleep(4)
except:
    print('Failed in connecting with AWS')


