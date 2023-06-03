import random

class bcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Person:
    def __init__(self, hp, mp, atk, df, magic):
        self.maxHp = hp
        self.hp = hp
        self.maxMp = mp
        self.mp = mp
        self.atkl = atk - 10
        self.atkh = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic"]

    def generate_damage(self):
        return random.randrange(self.atkl, self.atkh)

    def generatge_spell_dmg(self, index):
        mgl = self.magic[index]["dmg"] - 5
        mgh = self.magic[index]["dmg"] + 5
        return random.randrange(mgl, mgh)

    def take_dmg(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0

        return self.hp

    def get_hp(self):
        return self.hp

    def get_maxHp(self):
        return self.maxHp

    def get_mp(self):
        return self.mp

    def get_maxMP(self):
        return self.maxMp

    def reduce_mp(self, cost):
        self.mp -= cost

    def get_spell_name(self, index):
        return self.magic[index]["name"]

    def get_spell_cost(self, index):
        return self.magic[index]["cost"]

    def choose_action(self):
        i = 1
        print("Actions: ")

        for itm in self.actions:
            print(str(i) + ": ", itm)
            i += 1

    def choost_spell(self):
        i = 1
        print("Magics: ")

        for spell in self.magic:
            print(str(i) + ": ", spell["name"], " (cost: ", str(spell["cost"]), ")")
            i += 1