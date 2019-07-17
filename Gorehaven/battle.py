def battle():
    import charsheet
    import currentenemy
    import enemygen
    enemygen.enemygenerator()
    import battlecrier
    battlecrier.battlestart()
    input('Battle has been joined!')
    import hub
    hub.hub()