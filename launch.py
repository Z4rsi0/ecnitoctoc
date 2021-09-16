#!/usr/bin/env python3

import os
from time import sleep

print("Lancement du bot")
os.system('echo 1 > /home/twitter/ecnitoctoc/launch.status')
os.system('python3 /home/twitter/ecnitoctoc/favretweet.py')   #commande qui lance le programe
os.system('echo 0 > /home/twitter/ecnitoctoc/launch.status')
print('Restart en cours')
sleep(1)
exit()
