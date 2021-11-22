

class DrawingProgramIterator:
    def __init__(self, collection_of_shapes):
        self.list = collection_of_shapes
        self.index = 0

    def __next__(self):
        if self.index == len(self.list):
            raise StopIteration
        shape_in_list = self.list[self.index]
        self.index += 1
        return shape_in_list
