import time
import requests
import re
import json
from datetime import datetime

dico = {'bandages': 0,'temps':''}
while True:
    try:
        x = requests.get('https://www.escapefromtarkov.com/bandage')
        nbbandage = re.findall(r'String\(([0-9]{1,8})', str(x.content))[0]
        temps = str(datetime.now())[:-7]
        dico['temps']= temps
        dico['bandages']= nbbandage
        print(f'{nbbandage} Bandages at {temps}')
        with open('data.json','a+') as fichier:
            fichier.write(json.dumps(dico)+'\n')
        time.sleep(60)
    except Exception as error:
        print(error)
        pass
    
