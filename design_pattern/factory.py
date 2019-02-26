"""
factory method vs abstract factory
"""
class Snowboard:
    def __init__(self, name):
        self.name = name

    def action(self):
        print("{} riding snowboard".format(self.name))

    # overriding for better memory usage
    def __eq__(self, other):
        return self.name == other.name

class Ski:
    def __init__(self, name):
        self.name = name

    def action(self):
        print("{} skiing".format(self.name))

    def __eq__(self, other):
        return self.name == other.name


class SnowWorld:
    def __init__(self, name):
        self.player_name = name
        self.sport = None

    def __str__(self):
        return "\n\n\t----------- SnowWorld -----------"

    # one factory method
    def choose_type(self, t):
        if t == "snowboard":
            # memory optimization
            if not self.sport:
                self.sport = Snowboard(self.player_name)
            else:
                if self.player_name != self.sport.name:
                    self.sport = Snowboard(self.player_name)
        elif t == "ski":
            if not self.sport:
                self.sport = Ski(self.player_name)
            else:
                if self.player_name != self.sport.name:
                    self.sport = Ski(self.player_name)
        else:
            raise ValueError("Only snowboard and ski are supported")

    def play(self):
        if not self.sport:
            raise ValueError("Sport type have not chosen yet!")
        self.sport.action()


class Surfing:
    def __init__(self, name):
        self.name = name

    def action(self):
        print("{} surfing on the wave!".format(self.name))

    def __eq__(self, other):
        return self.name == other.name


class Diving:
    def __init__(self, name):
        self.name = name

    def action(self):
        print("{} diving into the ocean!".format(self.name))

    def __eq__(self, other):
        return self.name == other.name


class OceanWorld:
    def __init__(self, name):
        self.player_name = name
        self.sport = None

    # another factory method
    def choose_type(self, t):
        if t == "diving":
            if not self.sport:
                self.sport = Diving(self.player_name)
            else:
                if self.player_name != self.sport.name:
                    self.sport = Diving(self.player_name)
        elif t == "surfing":
            if not self.sport:
                self.sport = Surfing(self.player_name)
            else:
                if self.player_name != self.sport.name:
                    self.sport = Surfing(self.player_name)
        else:
            raise ValueError("Only suring and diving are supported")

    def play(self):
        if not self.sport:
            raise ValueError("Sport type not chosen yet!")
        self.sport.action()


class GameEnv:
    def __init__(self, factory, t):
        self.world = factory
        self.type = t

    def play(self):
        self.world.choose_type(self.type)
        self.world.play()


if __name__ == "__main__":
    name = input("what is your name?")
    valid_input = False
    while not valid_input:
        world = input("ocean/snow?")
        if world == "ocean" or world == "snow":
            valid_input = True
    valid_input = False
    while not valid_input:
        if world == "snow":
            t = input("choose a type to play?(ski/snowboard)")
            if t == "snowboard" or t == "ski":
                valid_input = True
        if world == "ocean":
            t = input("choose a type to play?(surfing/diving)")
            if t == "surfing" or t == "diving":
                valid_input = True

    # abstract factory: same as interface or abstract class in JAVA
    game = OceanWorld if world == 'ocean' else SnowWorld
    env = GameEnv(game(name), t)
    env.play()
