

class DrawingProgramIterator:
    """
    The DrawingProgramIterator class provides the ability to
    iterate across the collection of shapes in DrawingProgram using a for loop
    """
    def __init__(self, collection_of_shapes):
        self.__list = collection_of_shapes
        self.__index = 0

    def __next__(self):
        """
        return the next value of the shape list or raise a StopIteration.
        :return: shape
        """
        if self.__index == len(self.__list):
            raise StopIteration
        shape_in_list = self.__list[self.__index]
        self.__index += 1
        return shape_in_list
