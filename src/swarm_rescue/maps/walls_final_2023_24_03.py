"""
This file was generated by the tool 'image_to_map.py' in the directory tools.
This tool permits to create this kind of file by providing it an image of the
map we want to create.
"""
import sys
from pathlib import Path

# Insert the parent directory of the current file's directory into sys.path.
# This allows Python to locate modules that are one level above the current
# script, in this case spg_overlay.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from spg_overlay.entities.normal_wall import NormalWall, NormalBox


# Dimension of the map : (1700, 1100)
# Dimension factor : 1.0
def add_boxes(playground):
    pass


def add_walls(playground):
    # vertical wall 0
    wall = NormalWall(pos_start=(-630, 546),
                      pos_end=(-630, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 1
    wall = NormalWall(pos_start=(-422, 546),
                      pos_end=(-422, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 2
    wall = NormalWall(pos_start=(-246, 546),
                      pos_end=(-246, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 3
    wall = NormalWall(pos_start=(-68, 546),
                      pos_end=(-68, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 4
    wall = NormalWall(pos_start=(132, 546),
                      pos_end=(132, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 5
    wall = NormalWall(pos_start=(321, 546),
                      pos_end=(321, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 6
    wall = NormalWall(pos_start=(494, 546),
                      pos_end=(494, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 7
    wall = NormalWall(pos_start=(677, 546),
                      pos_end=(677, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 8
    wall = NormalWall(pos_start=(-628, 544),
                      pos_end=(-628, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 9
    wall = NormalWall(pos_start=(-420, 544),
                      pos_end=(-420, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 10
    wall = NormalWall(pos_start=(-244, 544),
                      pos_end=(-244, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 11
    wall = NormalWall(pos_start=(-66, 544),
                      pos_end=(-66, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 12
    wall = NormalWall(pos_start=(134, 544),
                      pos_end=(134, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 13
    wall = NormalWall(pos_start=(323, 544),
                      pos_end=(323, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 14
    wall = NormalWall(pos_start=(496, 544),
                      pos_end=(496, 317))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 15
    wall = NormalWall(pos_start=(679, 544),
                      pos_end=(679, 317))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 16
    wall = NormalWall(pos_start=(-845, 318),
                      pos_end=(-788, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 17
    wall = NormalWall(pos_start=(-846, 320),
                      pos_end=(-788, 320))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 18
    wall = NormalWall(pos_start=(783, 318),
                      pos_end=(844, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 19
    wall = NormalWall(pos_start=(-696, 320),
                      pos_end=(-564, 320))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 20
    wall = NormalWall(pos_start=(-472, 320),
                      pos_end=(-351, 320))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 21
    wall = NormalWall(pos_start=(-136, 320),
                      pos_end=(-9, 320))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 22
    wall = NormalWall(pos_start=(83, 320),
                      pos_end=(177, 320))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 23
    wall = NormalWall(pos_start=(270, 320),
                      pos_end=(392, 320))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 24
    wall = NormalWall(pos_start=(599, 320),
                      pos_end=(676, 320))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 25
    wall = NormalWall(pos_start=(784, 320),
                      pos_end=(844, 320))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 26
    wall = NormalWall(pos_start=(-696, 318),
                      pos_end=(-566, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 27
    wall = NormalWall(pos_start=(-472, 318),
                      pos_end=(-353, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 28
    wall = NormalWall(pos_start=(-259, 318),
                      pos_end=(-230, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 29
    wall = NormalWall(pos_start=(-136, 318),
                      pos_end=(-11, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 30
    wall = NormalWall(pos_start=(83, 318),
                      pos_end=(176, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 31
    wall = NormalWall(pos_start=(270, 318),
                      pos_end=(390, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 32
    wall = NormalWall(pos_start=(484, 318),
                      pos_end=(506, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 33
    wall = NormalWall(pos_start=(599, 318),
                      pos_end=(690, 318))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 34
    wall = NormalWall(pos_start=(-845, 230),
                      pos_end=(-723, 230))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 35
    wall = NormalWall(pos_start=(-846, 232),
                      pos_end=(-723, 232))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 36
    wall = NormalWall(pos_start=(757, 230),
                      pos_end=(844, 230))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 37
    wall = NormalWall(pos_start=(-631, 232),
                      pos_end=(-352, 232))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 38
    wall = NormalWall(pos_start=(-260, 232),
                      pos_end=(-11, 232))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 39
    wall = NormalWall(pos_start=(81, 232),
                      pos_end=(299, 232))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 40
    wall = NormalWall(pos_start=(391, 232),
                      pos_end=(666, 232))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 41
    wall = NormalWall(pos_start=(758, 232),
                      pos_end=(844, 232))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 42
    wall = NormalWall(pos_start=(-631, 230),
                      pos_end=(-353, 230))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 43
    wall = NormalWall(pos_start=(-260, 230),
                      pos_end=(-12, 230))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 44
    wall = NormalWall(pos_start=(81, 230),
                      pos_end=(298, 230))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 45
    wall = NormalWall(pos_start=(391, 230),
                      pos_end=(665, 230))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 46
    wall = NormalWall(pos_start=(-121, 231),
                      pos_end=(-121, -16))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 47
    wall = NormalWall(pos_start=(220, 231),
                      pos_end=(220, -16))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 48
    wall = NormalWall(pos_start=(-119, 229),
                      pos_end=(-119, -16))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 49
    wall = NormalWall(pos_start=(222, 229),
                      pos_end=(222, -16))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 50
    wall = NormalWall(pos_start=(-670, 129),
                      pos_end=(-493, 129))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 51
    wall = NormalWall(pos_start=(-667, 131),
                      pos_end=(-667, 96))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 52
    wall = NormalWall(pos_start=(-284, 132),
                      pos_end=(-284, 92))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 53
    wall = NormalWall(pos_start=(-669, 135),
                      pos_end=(-669, 97))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 54
    wall = NormalWall(pos_start=(-672, 131),
                      pos_end=(-281, 131))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 55
    wall = NormalWall(pos_start=(-491, 229),
                      pos_end=(-491, -16))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 56
    wall = NormalWall(pos_start=(-490, 129),
                      pos_end=(-284, 129))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 57
    wall = NormalWall(pos_start=(-286, 131),
                      pos_end=(-286, 93))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 58
    wall = NormalWall(pos_start=(-493, 231),
                      pos_end=(-493, -16))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 59
    wall = NormalWall(pos_start=(348, 122),
                      pos_end=(529, 122))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 60
    wall = NormalWall(pos_start=(351, 123),
                      pos_end=(351, 84))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 61
    wall = NormalWall(pos_start=(693, 126),
                      pos_end=(693, 83))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 62
    wall = NormalWall(pos_start=(349, 126),
                      pos_end=(349, 86))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 63
    wall = NormalWall(pos_start=(349, 124),
                      pos_end=(696, 124))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 64
    wall = NormalWall(pos_start=(531, 229),
                      pos_end=(531, -16))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 65
    wall = NormalWall(pos_start=(532, 122),
                      pos_end=(693, 122))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 66
    wall = NormalWall(pos_start=(691, 124),
                      pos_end=(691, 84))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 67
    wall = NormalWall(pos_start=(529, 231),
                      pos_end=(529, -15))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 68
    wall = NormalWall(pos_start=(-845, -15),
                      pos_end=(-67, -15))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 69
    wall = NormalWall(pos_start=(-846, -13),
                      pos_end=(-66, -13))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 70
    wall = NormalWall(pos_start=(29, -13),
                      pos_end=(55, -13))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 71
    wall = NormalWall(pos_start=(147, -13),
                      pos_end=(844, -13))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 72
    wall = NormalWall(pos_start=(29, -15),
                      pos_end=(54, -15))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 73
    wall = NormalWall(pos_start=(147, -15),
                      pos_end=(845, -15))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 74
    wall = NormalWall(pos_start=(-456, -150),
                      pos_end=(-456, -547))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 75
    wall = NormalWall(pos_start=(-456, -152),
                      pos_end=(-120, -152))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 76
    wall = NormalWall(pos_start=(-123, -150),
                      pos_end=(-123, -407))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 77
    wall = NormalWall(pos_start=(-453, -154),
                      pos_end=(-123, -154))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 78
    wall = NormalWall(pos_start=(-454, -151),
                      pos_end=(-454, -547))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 79
    wall = NormalWall(pos_start=(-299, -153),
                      pos_end=(-299, -173))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 80
    wall = NormalWall(pos_start=(-297, -155),
                      pos_end=(-297, -173))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 81
    wall = NormalWall(pos_start=(802, -166),
                      pos_end=(844, -166))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 82
    wall = NormalWall(pos_start=(441, -162),
                      pos_end=(441, -209))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 83
    wall = NormalWall(pos_start=(441, -164),
                      pos_end=(711, -164))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 84
    wall = NormalWall(pos_start=(803, -164),
                      pos_end=(844, -164))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 85
    wall = NormalWall(pos_start=(140, -163),
                      pos_end=(140, -182))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 86
    wall = NormalWall(pos_start=(141, -166),
                      pos_end=(159, -166))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 87
    wall = NormalWall(pos_start=(155, -165),
                      pos_end=(155, -185))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 88
    wall = NormalWall(pos_start=(444, -166),
                      pos_end=(710, -166))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 89
    wall = NormalWall(pos_start=(844, 548),
                      pos_end=(844, -547))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 90
    wall = NormalWall(pos_start=(443, -163),
                      pos_end=(443, -209))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 91
    wall = NormalWall(pos_start=(657, -165),
                      pos_end=(657, -461))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 92
    wall = NormalWall(pos_start=(659, -167),
                      pos_end=(659, -461))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 93
    wall = NormalWall(pos_start=(138, -181),
                      pos_end=(158, -181))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 94
    wall = NormalWall(pos_start=(-299, -264),
                      pos_end=(-299, -547))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 95
    wall = NormalWall(pos_start=(137, -266),
                      pos_end=(137, -285))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 96
    wall = NormalWall(pos_start=(138, -269),
                      pos_end=(156, -269))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 97
    wall = NormalWall(pos_start=(152, -268),
                      pos_end=(152, -288))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 98
    wall = NormalWall(pos_start=(135, -284),
                      pos_end=(155, -284))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 99
    wall = NormalWall(pos_start=(-298, -353),
                      pos_end=(-232, -353))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 100
    wall = NormalWall(pos_start=(-297, -264),
                      pos_end=(-297, -547))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 101
    wall = NormalWall(pos_start=(-296, -355),
                      pos_end=(-233, -355))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 102
    wall = NormalWall(pos_start=(-125, -152),
                      pos_end=(-125, -407))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 103
    wall = NormalWall(pos_start=(137, -373),
                      pos_end=(137, -392))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 104
    wall = NormalWall(pos_start=(138, -376),
                      pos_end=(156, -376))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 105
    wall = NormalWall(pos_start=(152, -375),
                      pos_end=(152, -395))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 106
    wall = NormalWall(pos_start=(135, -391),
                      pos_end=(155, -391))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 107
    wall = NormalWall(pos_start=(134, -476),
                      pos_end=(134, -495))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 108
    wall = NormalWall(pos_start=(135, -479),
                      pos_end=(153, -479))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 109
    wall = NormalWall(pos_start=(149, -478),
                      pos_end=(149, -498))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 110
    wall = NormalWall(pos_start=(132, -494),
                      pos_end=(152, -494))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 111
    wall = NormalWall(pos_start=(-125, -498),
                      pos_end=(-125, -547))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 112
    wall = NormalWall(pos_start=(-123, -498),
                      pos_end=(-123, -547))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 113
    wall = NormalWall(pos_start=(441, -500),
                      pos_end=(441, -546))
    playground.add(wall, wall.wall_coordinates)

    # vertical wall 114
    wall = NormalWall(pos_start=(443, -500),
                      pos_end=(443, -547))
    playground.add(wall, wall.wall_coordinates)

    # horizontal wall 115
    wall = NormalWall(pos_start=(-845, -544),
                      pos_end=(846, -544))
    playground.add(wall, wall.wall_coordinates)

    # AJOUT MANUEL du mur en pointillé, car ne peut pas être généré automatiquement.
    for y in range(-502, -211, 20):
        wall = NormalWall(pos_start=(442, y),
                          pos_end=(442, y - 10))
        playground.add(wall, wall.wall_coordinates)
