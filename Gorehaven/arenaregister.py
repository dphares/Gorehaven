import charsheet
import progtrack


def ledger():
    charsheet.player = input('What is your name, Warrior? ')
    confirm = input('You wish to be called {}?     (Y/N) '.format(charsheet.player))
    if confirm.lower() != 'y' and confirm.lower() != 'n':
        confirm2 = input('Please verify your name, Warrior. Are you {}?   Input (Y)es or (N)o '.format(charsheet.player))
        if confirm2.lower() == 'y':
            charsheet.player = charsheet.player
            print('Very well, {}, best of luck in your adventure.'.format(charsheet.player))
            progtrack.gameprog = progtrack.gameprog + 1
            import gorehaven
            gorehaven.main()
        else:
            print('Well then...')
            ledger()
    if confirm.lower() == 'y':
        charsheet.player = charsheet.player
        print('Very well, {}, best of luck in your adventure.'.format(charsheet.player))
        progtrack.gameprog = progtrack.gameprog + 1
        import gorehaven
        gorehaven.main()
    else:
        print('Well then...')
        ledger()