
import sys

from constants import NON_WALKABLE, SYMBOL_DICT
from draw_utils import draw_tile

class Array(object):
    """Array is the map"""

    def __init__(self, tile_list:list):
        # tile_list == [[coordinate, tile_type] ... ]
        self.tile_inst_dict = {}
        for tile in tile_list:
            pos = tile[0]
            tile_type = tile[1]
            self.tile_inst_dict[pos] = Tile(tile_type)

    def is_walkable(self, new_position):

        if not new_position in self.tile_inst_dict:
            return False

        tile_type = self.tile_inst_dict[new_position].tile_type
        print("tile type:", tile_type)

        if tile_type in NON_WALKABLE:
            return False

        # TODO: if guard or other cases
        return True

    def draw(self):
        for key, tile in self.tile_inst_dict.items():
            draw_tile(key, tile.tile_type)

class Tile(object):
    """Tile is a tile on the map"""

    def __init__(self, tile_type) -> None:
        self.tile_type = tile_type

    def draw():
        pass

def convert_file_to_array_list(file, symbol_dict):
    """prepare data for array"""
    opened_file = file.open()
    line_list = opened_file.readlines()
    array_list = []
    y_value = 1
    for line in line_list:
        for x_value in range(len(line) - 1):
            array_list.append([(x_value,y_value), symbol_dict[line[x_value - 1]]])
    return array_list

def convert_text_to_array_list(text):
    """prepare data for array"""
    array_list = []
    line_list = text.split("\n")
    y_value = 1
    for line in line_list:
        for x_value in range(1,len(line) + 1):
            array_list.append([(x_value, y_value), SYMBOL_DICT[line[x_value - 1]]])
        y_value += 1
    return array_list

def print_array(array_inst:Array, x_range:int, y_range:int):
    """print all static object of an array"""
    for y_value in range(1,y_range + 1):
        row = ""
        for x_value in range(1,x_range + 1):
            row += array_inst.tile_inst_dict[(x_value, y_value)].static_obj + " "
        print(row)