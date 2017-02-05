# Jose Capestany
# CS126L
# 4/29/2016
# Lab 11: Role-Playing Game

import random


class DiceRoller:
    # A utility class for dice rolling.

    def roll(self, times, sides):
        # Rolls times number of sides-sided dice; returns the total
        total = 0
        for i in range(times):
            roll = random.randint(1, sides)
            total += roll
        return total

r = DiceRoller()


class Attack:
    # Encapsulates the concept of an attack.

    def __init__(self, name, number_of_die, sides_of_die, damage_type):
        """Creates an attack with private attributes.

        Adds _name, _sides, _number, and _type
        to self, with values provided by arguments.

        """
        # TODO
        self._name = name
        self._sides = sides_of_die
        self._number = number_of_die
        self._type = damage_type

    def get_attack_type(self):
        """Returns the type of attack, as a string."""
        return self._type

    # TODO
    def set_attack_type(self, damage_type):
        self._type = damage_type

    def get_damage(self):
        damage = DiceRoller()
        return damage.roll(self._number, self._sides)

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_number_of_die(self):
        return self._number

    def set_number_of_die(self, number_of_die):
        self._number = number_of_die

    def get_sides_of_die(self):
        return self._sides

    def set_sides_of_die(self, sides_of_die):
        self._sides = sides_of_die


class Adventurer:

    # TODO
    def __init__(self, name, hit_points, armor, magic_resistance, initiative):
        self._name = name
        self._hp = hit_points
        self._armor = armor
        self._res = magic_resistance
        self._init = initiative

    # As long as you're not dead you're alive
    def is_alive(self):
        if self._hp > 0:
            return True
        else:
            return False

    # Roll between 0 and initiative
    def roll_intiative(self):
        return random.randint(0, self._init)

    # Lowers HP when you take damage
    # Armor reduces physical attacks
    # Resistance reduces magical attacks
    # If any number is lower than 0 set to 0
    # (no negative damage or HP)
    def take_damage(self, amount, damage_type):
        if damage_type == 'physical':
            amount -= self._armor
            if amount < 0:
                amount = 0
            self._hp -= amount
            if self._hp < 0:
                self._hp = 0
            print('%s takes %d damage after %d armor. %d HP remaining!' %
                  (self._name, amount, self._armor, self._hp))
        if damage_type == 'magic':
            amount -= self._res
            if amount < 0:
                amount = 0
            self._hp -= amount
            if self._hp < 0:
                self._hp = 0
            print('%s takes %d damage after %d resistance. %d HP remaining!' %
                  (self._name, amount, self._res, self._hp))

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    def get_hit_points(self):
        return self._hp

    def set_hit_pints(self, hit_points):
        self._hp = hit_points

    def get_armor(self):
        return self._armor

    def set_armor(self, armor):
        self._armor = armor

    def get_magic_resistance(self):
        return self._res

    def set_magic_resistance(self, magic_resistance):
        self._res = magic_resistance

    def get_initiative(self):
        return self._init

    def set_initiative(self, initiative):
        self._init = initiative


class Fighter(Adventurer):

    _HP = 40
    _ARMOR = 10
    _MR = 4

    def __init__(self, name, initiative):
        super().__init__(name, Fighter._HP, Fighter._ARMOR,
                         Fighter._MR, initiative)
        self._melee = Attack('Slash', 1, 8, 'physical')

    # TODO
    # Returns how much a strike does and what type it is and prints how much
    def strike(self):
        strike = (self._melee.get_damage(), self._melee.get_attack_type())
        print('%s attacks with %s for %d %s damage!' %
              (self._name, self._melee.get_name(), strike[0], strike[1]))
        return strike

    # Returns the character with their charecteristics
    def __str__(self):
        return '%s with %d HP and a %s attack (%dd%d).' %\
              (self._name, self._hp, self._melee.get_name(),
               self._melee.get_number_of_die(),
               self._melee.get_sides_of_die())


class Wizard(Adventurer):

    # TODO
    _HP = 20
    _ARMOR = 4
    _MR = 10

    def __init__(self, name, initiative):
        super().__init__(name, Wizard._HP, Wizard._ARMOR,
                         Wizard._MR, initiative)
        self._spell = Attack('Fireball', 3, 6, 'magic')

    # Same as strike but now called cast
    def cast(self):
        cast = (self._spell.get_damage(), self._spell.get_attack_type())
        print('%s attacks with %s for %d %s damage!' %
              (self._name, self._spell.get_name(), cast[0], cast[1]))
        return cast

    # Returns the character with their charecteristics
    def __str__(self):
        return '%s with %d HP and a %s attack (%dd%d).' %\
              (self._name, self._hp, self._spell.get_name(),
               self._spell.get_number_of_die(),
               self._spell.get_sides_of_die())


if __name__ == '__main__':
    # Create and announce fighters
    a = Fighter('Aragorn', 20)
    b = Wizard('Gandalf', 15)
    print('Created:', a, '\nCreated:', b)
    round = 0

    while a.is_alive() and b.is_alive():
        # Keeps track of rounds and announces it
        round += 1
        print('\n** ROUND %d!' % (round))
        a_init = 0
        b_init = 0
        # If their initiatives are tied
        while a_init == b_init:
            a_init = a.roll_intiative()
            b_init = b.roll_intiative()
        # If a wins initiative a deals damage to b
        if a_init > b_init:
            print(a.get_name(), 'wins initiative!')
            attack = a.strike()
            b.take_damage(attack[0], attack[1])
        # If b wins initiative b deals damage to a
        else:
            print(b.get_name(), 'wins initiative!')
            attack = b.cast()
            a.take_damage(attack[0], attack[1])
    # Anounces the winner
    if a.is_alive() is False:
        print('\n%s has won with %d HP left!' %\
              (b.get_name(), b.get_hit_points()))
    else:
        print('\n%s has won with %d HP left!' %\
              (a.get_name(), a.get_hit_points()))
