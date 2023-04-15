import matplotlib.pyplot as plt
import json
from datetime import datetime

def graph():
    dico = {'bandages': list(), 'temps': list()}
    plt.title('graph of the donnation of bandages over the days')
    plt.xlabel('time')
    plt.ylabel('Nb bandage')
    with open('data.json','r') as fichier:
        for ligne in fichier:
            fichierdico = json.loads(ligne[:-1])
            dico['bandages'].append(int(fichierdico['bandages']))
            dico['temps'].append(datetime.strptime(fichierdico['temps'], '%Y-%m-%d %H:%M:%S'))
            plt.xticks(rotation='vertical')
        plt.plot(dico['temps'], dico['bandages'], label='bandages', color=plt.get_cmap('jet_r')(10))
        plt.show()
graph()

