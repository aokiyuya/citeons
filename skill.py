#! !(which python)
# coding: utf-8
###########################
# Author: Yuya Aoki
#
###########################
from keywords import *


class Skill(object):
    def __init__(self):
        self.kind = SLASH
        self.power = 100

    def get_kind(self):
        return self.kind

    def get_power(self):
        return self.power

    def instance(self):
        return ATACK


class Magic(Skill):
    def __init__(self):
        self.kind = OMNI
        self.power = 100

    def instance(self):
        return MAGIC


class Flame_arrow(Magic):
    def __init__(self):
        self.kind = FLAME
        self.power = 500
