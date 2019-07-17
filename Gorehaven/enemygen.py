#Generates an enemy randomly within certain level range of the player. Base stats are dictated randomly in a range by
#the level the enemy spawns as.


def enemygenerator():
    import random
    import charsheet
    import namegen
    namegen.namegen()
    enemyname = namegen.enemyname
    if charsheet.level == 1:
        enemylevel = random.randrange(1,4)
    else:
        enemylevel = random.randrange(charsheet.level-1, charsheet.level+3)
    enemygold = random.randint(enemylevel*3,enemylevel*5)
    enemystr = random.randint(enemylevel*3,enemylevel*6)
    enemydex = random.randint(enemylevel*3,enemylevel*6)
    enemyint = random.randint(enemylevel*3,enemylevel*6)
    enemyhp = 100+(random.randint(enemylevel*2,enemylevel*5))
    enemymaxhp = enemyhp
    import currentenemy
    currentenemy.name = enemyname
    currentenemy.level = enemylevel
    currentenemy.gold = enemygold
    currentenemy.str = enemystr
    currentenemy.dex = enemydex
    currentenemy.int = enemyint
    currentenemy.hp = enemyhp
    currentenemy.maxhp = enemymaxhp

