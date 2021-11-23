

class DrawingProgramIterator:
    """
    The DrawingProgramIterator class provides the ability to
    iterate across the collection of shapes in DrawingProgram using a for loop
    """
    def __init__(self, collection_of_shapes):
        self.list = collection_of_shapes
        self.index = 0

    def __next__(self):
        """
        return the next value of the shape list or raise a StopIteration.
        :return: shape
        """
        if self.index == len(self.list):
            raise StopIteration
        shape_in_list = self.list[self.index]
        self.index += 1
        return shape_in_list
