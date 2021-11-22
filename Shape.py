import abc


class Shape(metaclass=abc.ABCMeta):

    def __init__(self, name_of_shape):
        self.name_of_shape = name_of_shape

    def get_name_of_shape(self):
        return self.name_of_shape

    def area(self):
        pass

    def perimeter(self):
        pass

    def __str__(self):
        return str(self.name_of_shape)+"area:"+str(self.area())+", perimeter:"+str(self.perimeter())

    def draw(self):
        print(self.__str__())

    def __gt__(self, other):
        if isinstance(other, Shape):
            if other.get_name_of_shape() == self.get_name_of_shape():
                if self.area()>other.area():
                    return True
                return False
            elif self.get_name_of_shape()> other.get_name_of_shape():
                return True
            return False
        raise Exception("Other is not a shape")

    def __eq__(self, other):
        if isinstance(other, Shape):
            return other.get_name_of_shape() == self.get_name_of_shape() and self.area()==other.area()
        raise Exception("Other is not a shape")

    def __lt__(self, other):
        return (not self.__gt__(other)) and (not self.__eq__(other))