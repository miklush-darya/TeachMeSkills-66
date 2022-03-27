
from abc import ABC, abstractmethod, abstractproperty

class Player(ABC):

    def __init__(self, name):
        self.name = name

    def setWeapon(self, weapon):
        self.weapon = weapon

    @abstractproperty
    def action(self):
        pass

    @abstractproperty
    def health(self):
        pass

    @abstractproperty
    def damage(self):
        pass


#шаги на поле
#################################
class Field(ABC):
    @abstractmethod
    def starting_position(self):
        pass

class MageField(Field):
    @property
    def starting_position(self): 
        return 'step: 1'

class ArcherField(Field):
    @property
    def starting_position(self):
        return 'step: 5'

class WarriorField(Field):
    @property
    def starting_position(self):
        return 'step: 10'


# оружие
##############################
class Weapon(ABC):    
    @abstractmethod
    def write(self, work):
        pass

class Club(Weapon):
    def write(self, work):
	    return "club", work

class BowArrows(Weapon):
    def write(self, work):
	    return 'bow and arrows', work

class MagicStaff(Weapon):
    def write(self, work):
	    return 'magic staff', work


#игроки
###########################
class Warrior(Player):

    weapon = Club()

    @property
    def action(self):
        return "action: Beat Enemies"

    def health(self):
        return "health: 100"

    def damage(self):
        return "damage: -10"

class Archer(Player):

    weapon = BowArrows()

    @property
    def action(self):
        return "action: Shoots Arrows"

    def health(self):
        return "health: 150"

    def damage(self):
        return "damage: -15"

class Mage(Player):

    weapon = MagicStaff()

    @property
    def action(self):
        return "action: Magic Strike"

    def health(self):
        return "health: 200"

    def damage(self):
        return "damage: -25"

x = Mage('mag')
print(x.health())