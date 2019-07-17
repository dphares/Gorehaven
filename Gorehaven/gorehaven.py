import progtrack


def main():
    if progtrack.gameprog == 0:
        import introseq
        introseq.introduction()
    if progtrack.gameprog == 1:
        import arenaregister
        arenaregister.ledger()
    if progtrack.gameprog == 2:
        import hub
        hub.hub()


main()






