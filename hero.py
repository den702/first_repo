class Hero():
    """"class to create hero for our game"""
    def __init__(self, name,level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100
    def show_hero(self):
        """print all parameters of this hero"""
        discription = (self.name + " level is " + str(self.level) + " race is " + self.race + "health is " + str(self.health)).title()
        print(discription)
    def levvel_up(self):
        """upgrade level of hero"""
        self.level = self.level + 1
    def move(self):
        """start moving hero"""
        print("Hero " + self.name + " start moving...")
    def set_health(self, new_health):
        self.health = new_health


class SuperHero(Hero):
    """"class to create superhero"""
    def __init__(self, name, level, race, magiclevel):
        """initiate our super hero"""
        super().__init__(name, level, race)
        self.magiclevel = magiclevel
        self.magic = 100
    def makemagic(self):
        """use magic"""
        self.magic -= 10
    def show_hero(self):
        discription = (self.name + " level is " + str(self.level) + " race is " + self.race + "health is " + str(self.health) +
                       "magic is: " + str(self.magic)).title()
        print(discription)