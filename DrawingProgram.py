from DrawingProgramlterator import DrawingProgramIterator
from Shape import Shape


class DrawingProgram:
    """
    This class has a list of shapes. It provides method to add, get, replace,
    sort, remove, print and iterate the shapes in the list.
    """

    def __init__(self, shapes=None):
        self.__collection_of_shapes = []
        if shapes:
            for shape in shapes:
                self.add_shape(shape)

    def add_shape(self, shape):
        """
        Add the shape to the shape_list.
        :param shape: Shape object to add to the list
        :return: None
        :exception: TypeError is raised if the parameter passed is not a shape object.
        """
        if isinstance(shape, Shape):
            self.__collection_of_shapes.append(shape)
        else:
            raise TypeError("Invalid Data type. Input needs to be an instance of a subclass of Shape class.")

    def remove_shape(self, shape):
        """
        Removes all data(Shape) if present in the list.
        :param shape: Shape to remove.
        :return: The number of elements removed.
        """
        count = 0
        while shape in self.__collection_of_shapes:
            count += 1
            self.__collection_of_shapes.remove(shape)
        print("count: " + str(count))
        return count

    def print_shape(self, shape):
        """
        prints all shapes that match the type of the shape passed in
        :param shape: type of the shape to print
        :return: None
        """
        shape_string_list = []
        for item in self.__collection_of_shapes:
            if isinstance(item, shape.__class__):
                shape_string_list.append(shape.__str__())
        print("\n".join(shape_string_list))

    def sort_shapes(self):
        """
        Sorts the list of shapes--runs in O(nlogn).
        Shapes will be sorted first by name,
        then by area if names are same.
        :return: None
        """
        self.__collection_of_shapes = self.quick_sort(self.__collection_of_shapes)

    def __str__(self):
        """
        Returns a string representation of each of the shapes--
        each shape will be separated from others by a newline(\n)
        :return: the string representation of the shapes
        """
        shape_string_list = []
        for shape in self.__collection_of_shapes:
            shape_string_list.append(shape.__str__())
        if len(shape_string_list) != 0:
            return "\n".join(shape_string_list)+"\n"
        else:
            return " "

    def get_shape(self, index):
        """
        returns the shape at the specified index
        :param index: index of the list to retrieve the shape.
        :exception:TypeError is raised if the index is not an integer.
        :exception:ValueError is raised if the index is out of range.
        :return: Shape
        """
        if not isinstance(index, int):
            raise TypeError("Invalid data type. Index must be an integer.")
        if index >= len(self.__collection_of_shapes):
            raise ValueError("Invalid data. Index is out of range.")
        return self.__collection_of_shapes[index]

    def set_shape(self, index, shape):
        """
        set the shape at the specified index
        :param shape: Shape
        :param index: index of the list to set the shape.
        """
        self.__collection_of_shapes[index] = shape

    def quick_sort(self, list_to_sort):
        """
        Sort the list using quick sort algorithm.
        :param list_to_sort: list
        :return: Sorted list
        """
        # left = []
        # equal = []
        # right = []
        # if len(list_to_sort) > 1:
        #     pivot = list_to_sort[0]
        #     for x in list_to_sort:
        #         if x < pivot:
        #             left.append(x)
        #         elif x == pivot:
        #             equal.append(x)
        #         elif x > pivot:
        #             right.append(x)
        #     return self.quick_sort(left) + equal + self.quick_sort(right)
        # else:
        #     return list_to_sort

        def quick_sort_impl(left, right):
            if left >= right:
                return
            pivot = list_to_sort[left]
            j = left
            i = j + 1
            while i <= right:
                if pivot > list_to_sort[i]:
                    j += 1
                    list_to_sort[j], list_to_sort[i] = list_to_sort[i], list_to_sort[j]
                i += 1
            list_to_sort[left], list_to_sort[j] = list_to_sort[j] , list_to_sort[left]
            mid = j

            quick_sort_impl(left, mid-1)
            quick_sort_impl(mid+1, right)

        quick_sort_impl(0, len(list_to_sort)-1)
        return list_to_sort

    def __iter__(self):
        """
        Creates an iterator to iterate across the collection of shapes.
        :return: Iterator
        """
        return DrawingProgramIterator(self.__collection_of_shapes)