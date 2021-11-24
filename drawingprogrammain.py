from ShapeFactory import ShapeFactory
from DrawingProgram import DrawingProgram

ORDERED_LIST = [
    ShapeFactory.create_circle(4),
    ShapeFactory.create_circle(1),
    ShapeFactory.create_circle(10),
    ShapeFactory.create_circle(5),
    ShapeFactory.create_rectangle(3, 4),
    ShapeFactory.create_rectangle(4, 5),
    ShapeFactory.create_rectangle(5, 6),
    ShapeFactory.create_square(4),
    ShapeFactory.create_square(5),
    ShapeFactory.create_square(10),
    ShapeFactory.create_square(100),
    ShapeFactory.create_triangle(4, 4, 4),
    ShapeFactory.create_triangle(5, 5, 5),
    ShapeFactory.create_triangle(2, 2, 2),
]
drawing = DrawingProgram()
print(f"Print empty DrawingProgram:\n\n{drawing}")
for shape in reversed(ORDERED_LIST):
    drawing.add_shape(shape)
print(f"Print DrawingProgram after add shapes:\n\n{drawing}")

drawing.sort_shapes()
print(f"Print DrawingProgram after sort shapes:\n\n{drawing}")
for shape in ORDERED_LIST:
    drawing.add_shape(shape)
print(f"Print DrawingProgram after second add shapes:\n\n{drawing}")
drawing.set_shape(6, ORDERED_LIST[10])
drawing.set_shape(11, ORDERED_LIST[4])
drawing.set_shape(8, ORDERED_LIST[1])
print(f"Print DrawingProgram after replace shapes:\n\n{drawing}")
drawing.sort_shapes()
print(f"Print DrawingProgram after second sort shapes:\n\n{drawing}")
