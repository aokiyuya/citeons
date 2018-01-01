#! !(which python)
# coding: utf-8
###########################
# Author: Yuya Aoki
#
###########################


class Skill(object):
    def __init__(self):
        self.kind = 'slash'
        self.power = 100

    def get_kind(self):
        return self.kind

    def get_power(self):
        return self.power

    def instance(self):
        return 'Atack'


class Magic(Skill):
    def __init__(self):
        self.kind = 'omni'
        self.power = 100

    def instance(self):
        return 'Magic'


class Flame_arrow(Magic):
    def __init__(self):
        self.kind = 'flame'
        self.power = 400
