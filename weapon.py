#! !(which python)
# coding: utf-8
###########################
# Author: Yuya Aoki
#
###########################


class Weapon(object):
    def __init__(self):
        self.shape = 'Sword'
        self.kind = 'slash'
        self.power = 100

    def get_kind(self):
        return self.kind

    def get_power(self):
        return self.power

    def get_shape(self):
        return self.shape


class Unarmed(Weapon):
    def __init__(self):
        self.shape = 'Fist'
        self.kind = 'blow'
        self.power = 1
