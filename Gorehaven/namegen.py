import random
#Name generator for hostile NPCs encountered in The Arena, and potentially elsewhere.
#Potentially influence NPC stats depending on randomly assigned title?
namepre = ['Kor', 'Al', 'Gor', 'Zar', 'El', 'Tak', 'Hex']
namesuf = ['ioth', 'agarn', "'toth", 'ius']
title = ['The Great', 'The Brave', 'The Cunning', 'The Strong', 'The Conqueror', 'The Reckless']

def namegen():
    first = random.choice(namepre)
    second = random.choice(namesuf)
    last = random.choice(title)
    global enemyname
    enemyname = first + second + ' ' + last