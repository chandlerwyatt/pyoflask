from time import sleep
import pyo
import json


with open('config.json', 'r') as fp:
    config = json.load(fp)

# r = redis.Redis(host='localhost', port=6379, db=0)

server = pyo.Server().boot()
sf = pyo.SfPlayer(config['wav_file'], loop=True)  # replace <filename>
sh = pyo.FreqShift(sf)
sh.ctrl()
hr = pyo.Harmonizer(sh).out()
hr.ctrl()
ch = pyo.Chorus(sh).out()
ch.ctrl()
dly = pyo.Delay(sh).out()
dly.ctrl()
server.gui(locals())
'''
while True:
    temp = r.rpop('temp')
    if temp is None:
        print("Queue is empty")
        sleep(1)
    else:
        print(f'got {temp} on a worker')
        mod = (int(temp) - 19000) / 1000  # range between -14 and 14
        print(f'using mod {mod}')
        hr.transpo = mod - 7
        print(f"set transpo to {hr.transpo}")
        dly.delay = (mod + 14) * 0.05
        print(f"set delay to {dly.delay}")
        sh.setShift((mod + 14) * 16)
        print(f"set shift to {sh.shift}")
        #sf.setSpeed((mod+14)/14)
        #print(f"set speed to {sf.speed}")
'''


