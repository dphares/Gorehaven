import charsheet
import currentenemy


def battlestart():
    print("Your opponent is",'\n',currentenemy.name,'\n','Of level',currentenemy.level,'\n','Health: ',currentenemy.hp,'/',currentenemy.maxhp,'\n','\n','Versus','\n')
    print(charsheet.player,'\n''Of level',charsheet.level,'\n','Health:',charsheet.currenthp,'/',charsheet.maxhp,'\n''Stamina:',charsheet.stam,'/',charsheet.maxstam,'\n')