# This is a simple scenario based game

class Players(object):
    def player(invalue):
        newvalue = int(invalue)
        print(newvalue)
        if newvalue == 1:
            print("Hi")
            playerpoint = 10
            print(f"Goku is the player with points {playerpoint}")
            Fight.gokufight()

        elif newvalue == 2:
            playerpoint = 8
            print(f"Vegeta is the player")
            Fight.vegetafight()

        else :
            playerpoint = 7
            print(f"Gohan is the player with points {playerpoint}")
            Fight.gohanfight()



class Fight(object):
    def gokufight():
        value = input(" Goku your fight is against Freeza , Enter 1 to Dodge or 2 to Kamehame")
        value = int(value)
        if value == 1:
            print("You dodged and sent KamaHame to Freeza. You Win!!")
        else:
            Death.deathscene()
    def vegetafight():
        value = input(" Vegeta your fight is against Freeza , Enter 1 to Dodge or 2 to Kamehame")
        value = int(value)
        if value == 1:
            print("You dodged and sent freeze to Freeza. You Win!!")
        else:
            Death.deathscene()
    def gohanfight():
        value = input(" Gohan your fight is against Freeza , Enter 1 to Dodge or 2 to Kamehame")
        value = int(value)
        if value == 1:
            print("You dodged and sent Dubuks to Freeza. You Win!!")
        else:
            Death.deathscene()

class Death(object):
    def deathscene():
        print("You lost it. Dead!!")




inplayer = input("1 for Goku , 2 for Vegeta , 3 for Gohan")
Players.player(inplayer)
