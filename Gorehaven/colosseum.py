def colosseum():
    fight = input('Do you seek battle?  (Y/N) ')
    while fight.lower() != 'y' and fight.lower() != 'n':
        fight = input('Do you seek battle?  Input (Y)es or (N)o ')
    if fight.lower() == 'n':
        print('Live to fight another day.')
        import hub
        hub.hub()
    if fight.lower() == 'y':
        import battle
        battle.battle()
