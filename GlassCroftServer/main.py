from fastapi import FastAPI
from mycroft_bus_client import MessageBusClient, Message
from pydantic import BaseModel
from time import sleep
app = FastAPI()
mbusc = MessageBusClient()
mbusc.run_in_thread()
class Request(BaseModel):
    request: str
global x
x = []
def create_response(message):
    global x
    print('meme response' + message.data.get('utterance'))
    x.append(message.data.get('utterance'))
@app.post("/verysecurekey/getmcresponse/")
async def mcresp(request: Request):
    global x
    x = []
    mbusc.emit(Message("recognizer_loop:utterance",{'utterances': [request.request]},{'client_name': 'mycroft_simple_cli','source': 'debug_cli','destination': ["skills"]}))
    print("message sent")
    mbusc.on('speak',create_response)
    sleep(7)
    print(x)
    troll = 0
    gamer = ""
    while (troll < len(x)):
        print(x[troll])
        gamer = gamer + "^" + x[troll]
        troll += 1
        print("gamer value ", gamer)
    gamer.replace("*^", "")
    print("gamer final val", gamer)
    return gamer
    x = []
    print("X val reset")