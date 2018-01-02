#! !(which python)
# coding: utf-8
###########################
# Author: Yuya Aoki
#
###########################
from keywords import *


class Weapon(object):
    def __init__(self):
        self.shape = SWORD
        self.kind = SLASH
        self.power = 100

    def get_kind(self):
        return self.kind

    def get_power(self):
        return self.power

    def get_shape(self):
        return self.shape


class Unarmed(Weapon):
    def __init__(self):
        self.shape = FIST
        self.kind = BLOW
        self.power = 100
