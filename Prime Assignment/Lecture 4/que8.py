# Q8. Create a class Player with:

#  -> a class variable player_count
#  -> instance variables name and level

#  Track how many players were created.

class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level

        Player.player_count += 1

P1 = Player("Amit", 10)
P2 = Player("Raj", 5)

print(Player.player_count)