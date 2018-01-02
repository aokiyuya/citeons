#! !(which python)
# coding: utf-8
###########################
# Author: Yuya Aoki
#
###########################
import citeons
import skill as sk


def main():
    dongri = citeons.Citeons(name='dongri', height=160, weight=40, taf=10, mag=100, inter=30, agi=70, dex=40)
    tottori = citeons.Citeons(name='tottori', height=160, weight=40, taf=10, mag=100, inter=30, agi=70, dex=40)
    [tottori.atack(dongri) for i in range(100)]
    [dongri.atack(tottori, sk.Flame_arrow()) for i in range(100)]
    tottori.print_now_hp()
    dongri.print_now_hp()


if __name__ == '__main__':
    # code
    main()

