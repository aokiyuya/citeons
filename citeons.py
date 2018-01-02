# coding: utf-8
###########################
# Author: Yuya Aoki
#
###########################
import random
from weapon import Unarmed
from keywords import *
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
        self.init_regists()
        self.weak = []

    def addvanced_status(self):
        self.stress = 0
        self.state = None
        self.equip(Unarmed())
        self.hp = self.max_hp()
        self.mp = self.max_mp()
        self.critical = False

    def init_skills(self):
        self.skills = { skill: 0.1 for skill in skill_list }

    def init_weapopn_skills(self):
        self.weapopn_skills = { shape: 0.1 for shape in weapon_shape_list }

    def init_regists(self):
        self.regist = { regist: 0.1 for regist in regist_list}

    def equip(self, weapon):
        self.weapon = weapon

    def max_hp(self):
        return (100 - self.stress) * (self.weight + self.taf)

    def max_mp(self):
        return (100 - self.stress) * (self.inter + self.taf)

    def atack(self, enemy, skill=None):
        if skill is not None:
            if skill.instance() == MAGIC:
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
        if kind != OMNI:
            self.regist[kind] += 0.001
        return self.taf + self.regist[kind]

    def magic_block(self, kind):
        if kind != OMNI:
            self.regist[kind] += 0.001
        return self.mag + self.taf + self.regist[kind]

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
        self.print_now_hp()

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
        self.print_now_hp()

    def magic_nockback(self, enemy_magic, per=None):
        if enemy_magic in self.weak:
            self.state = NOCKBACK
        if per is None:
            return None
        rand = random.randint(0, 100)
        if per > rand:
            self.state = NOCKBACK

    def accuracy(self):
        tmp = (self.agi + self.height + self.dex) / 10
        return tmp

    def aboidance(self):
        tmp = float(self.agi + self.dex) / (self.height + self.weight)
        return tmp

    def is_hit(self, enemy):
        hit_rate = self.accuracy() / enemy.aboidance()
        per = hit_rate + self.weapopn_skills[self.weapon.get_shape()] / 10
        self.dice = random.randint(0, 100)
        if self.dice == 0:
            print('critical')
            self.critical = True
            return True
        elif self.dice < per:
            print('Hit!')
            return True
        else:
            return False
    def print_now_hp(self):
        string = ' '.join([self.name , NOW_HP , str(self.hp)])
        print(string)




def main():
    pass


if __name__ == '__main__':
    # code
    main()
