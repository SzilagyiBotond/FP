from dataclasses import dataclass


@dataclass
class Pieces:
    __x_coordinate: int
    __y_coordinate: int
    __property: str

    @property
    def x_coordinate(self):
        return self.__x_coordinate

    @x_coordinate.setter
    def x_coordinate(self, new_x_coordinate):
        self.__x_coordinate = new_x_coordinate

    @property
    def y_coordinate(self):
        return self.__y_coordinate

    @y_coordinate.setter
    def y_coordinate(self, new_y_coordinate):
        self.__y_coordinate = new_y_coordinate

    @property
    def property(self):
        return self.__property

    @property.setter
    def property(self, new_property):
        self.__property = new_property
