def hub():
    destination = input('A bustling city both ripe with adventure and laden with disappointment in its most mortal form.'
          '\nWhere would you like to go?'
          '\n1) Arena'
          '\n2) Blacksmith'
          '\n3) General Goods Store'
          '\n')
    if destination == '1':
        import colosseum
        colosseum.colosseum()

