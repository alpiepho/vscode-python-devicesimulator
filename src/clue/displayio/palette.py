from .color_type import ColorType
from . import constants as CONSTANTS


class Palette:
    def __init__(self, color_count):
        self.color_count = color_count
        self.__contents = []

        for i in range(self.color_count):
            self.__contents.append(ColorType((0, 0, 0)))

    def __getitem__(self, index):
        if index >= self.color_count:
            raise IndexError(CONSTANTS.PALETTE_OUT_OF_RANGE)

        return self.__contents[index].rgb888

    def __setitem__(self, index, value):
        if index >= self.color_count:
            raise IndexError(CONSTANTS.PALETTE_OUT_OF_RANGE)

        self.__contents[index].rgb888 = value

    def make_transparent(self, index):
        self.__toggle_transparency(index, True)

    def make_opaque(self, index):
        self.__toggle_transparency(index, False)

    def __toggle_transparency(self, index, transparency):
        if self.__contents[index]:
            self.__contents[index].transparent = transparency