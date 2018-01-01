#! !(which python)
# coding: utf-8
###########################
# Author: Yuya Aoki
#
###########################
import random
from weapon import Unarmed
# import weapon as wp
# import skill as sk

random.seed()


class Citeons(object):
    def __init__(self, read=False, name=None, height=180, weight=70, taf=50, mag=50, inter=50, agi=50, dex=50):
        if read:
            pass
        self.name = name
        self.height = height
        self.weight = weight
        self.taf = taf
        self.mag = mag
        self.inter = inter
        self.agi = agi
        self.dex = dex
        self.addvanced_status()
        self.init_skills()
        self.init_weapopn_skills()
        self.init_resists()
        self.weak = []

    def addvanced_status(self):
        self.stress = 0
        self.state = None
        self.equip(Unarmed())
        self.hp = self.max_hp()
        self.mp = self.max_mp()
        self.critical = False

    def init_skills(self):
        self.skills = {
                'slash': 0.1,
                'blow': 0.1,
                'thrust': 0.1,
                'flame': 0.1,
                'fleeze': 0.1,
                'electric': 0.1,
                'wind': 0.1,
                'bless': 0.1,
                'curse': 0.1,
                'omni': 0.1
                }

    def init_weapopn_skills(self):
        self.weapopn_skills = {
                'Halberd': 0.1,
                'Sword': 0.1,
                'Long sword': 0.1,
                'Bow': 0.1,
                'Fist': 0.1,
                'Gun': 0.1,
                'Spear': 0.1,
                'Blunt': 0.1,  # 鈍器
                'Cane': 0.1  # 杖
                }

    def init_resists(self):
        self.resist = {
                'slash': 0.1,
                'blow': 0.1,
                'thrust': 0.1,
                'flame': 0.1,
                'fleeze': 0.1,
                'electric': 0.1,
                'wind': 0.1,
                'bless': 0.1,
                'curse': 0.1
                }

    def equip(self, weapon):
        self.weapon = weapon

    def max_hp(self):
        return (100 - self.stress) * (self.weight + self.taf)

    def max_mp(self):
        return (100 - self.stress) * (self.inter + self.taf)

    def atack(self, enemy, skill=None):
        if skill is not None:
            if skill.instance() == 'Magic':
                self.magic_atack(enemy, skill)
            else:
                self.skill_atack(enemy, skill)
        else:
            self.weapon_atack(enemy)

    def skill_atack(self, enemy, skill):
        pass

    def weapon_atack(self, enemy):
        self.critical = False
        weapon_value = self.weapon.get_power() * self.skills[self.weapon.get_kind()]
        char_value = (self.height + self.weight) * self.speed() / 100
        if self.is_hit(enemy):
            if self.critical:
                enemy.damage((weapon_value + char_value) * 2, enemy.weapon)
                enemy.nockback(self.weight, per=50)
            else:
                enemy.damage((weapon_value + char_value) * self.dice / 100, enemy.weapon)
                enemy.nockback(self.weight)
        else:
            print("しかし攻撃はあたらなかった")
        self.skills[self.weapon.get_kind()] += 0.01

    def block(self, kind):
        if kind != 'omni':
            self.resist[kind] += 0.001
        return self.taf + self.resist[kind]

    def magic_block(self, kind):
        if kind != 'omni':
            self.resist[kind] += 0.001
        return self.mag + self.taf + self.resist[kind]

    def speed(self):
        return 100 - self.weight + self.agi

    def damage(self, point, weapon):
        block_value = self.block(weapon.get_kind())
        if self.critical:
            dm = point
        elif block_value > point:
            dm = 1
        else:
            dm = point - block_value
        self.hp = self.hp - dm
        print(self.name, '残りHP:', self.hp)

    def nockback(self, enemy_weight, per=None):
        if per is None:
            per = enemy_weight - self.weight + 10
        rand = random.randint(0, 100)
        if per > rand:
            self.state = 'nockback'

    def magic_atack(self, enemy, magic):
        self.critical = False
        char_value = self.mag + magic.get_power() + self.inter * self.skills[magic.get_kind()]
        if self.is_hit(enemy):
            if self.critical:
                enemy.magick_damage(char_value * 2, magic)
                enemy.nockback(magic, per=50)
            else:
                enemy.magick_damage(char_value * self.dice / 100, magic)
                enemy.magic_nockback(magic)
        else:
            print("しかし攻撃はあたらなかった")
        self.skills[self.weapon.get_kind()] += 0.01

    def magick_damage(self, point, magic):
        block_value = self.magic_block(magic.get_kind())
        if self.critical:
            dm = point
        elif block_value > point:
            dm = 1
        else:
            dm = point - block_value
        self.hp = self.hp - dm
        print(self.name, '残りHP:', self.hp)

    def magic_nockback(self, enemy_magic, per=None):
        if enemy_magic in self.weak:
            self.state = 'nockback'
        if per is None:
            return None
        rand = random.randint(0, 100)
        if per > rand:
            self.state = 'nockback'

    def accuracy(self):
        return (self.agi + self.height + self.dex) / 10

    def aboidance(self):
        return (self.agi + self.dex) / (self.height + self.weight)

    def is_hit(self, enemy):
        hit_rate = self.accuracy() / enemy.aboidance()
        per = hit_rate + self.weapopn_skills[self.weapon.get_shape()] / 10
        self.dice = random.randint(0, 100)
        # print(per, self.dice)
        if self.dice == 0:
            print('critical')
            self.critical = True
            return True
        elif self.dice < per:
            print('Hit!')
            return True
        else:
            return False



def main():
    pass


if __name__ == '__main__':
    # code
    main()
