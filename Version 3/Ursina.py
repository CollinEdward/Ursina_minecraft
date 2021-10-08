from ursina import *
from ursina import texture 
import ursina.

class test_cube(Entity):
    def __init__(self):
        super().__init__(
            model = "cube",
            color = color.white,
            texture = "white_cube",
            rotation = Vec3(45,45,45)
        )

class button(Button):
    def __init__(self):
        super().__init__(
            # When creating a button you have to parent the button to the scene
            parent = scene,
            model = "cube",
            texture = "brick",
            # This color is the color that it is when nothing is happening 
            color = color.blue,
            # This is when you hover your mouse over the button
            highlight_color = color.orange,
            # And this is when pressed on
            pressed_color = color.white

        )

    def input(self, key):
        if self.hovered:
            if key == "left mouse down":
                print("nice")

def update():
    if held_keys["a"]:
        test_square.x -= 1 * time.dt

app = Ursina()

#        We use Entity function in python for almost anything that has to be rendered
                # Then the model is which shape
                                # Color is the color of the Entity
                                                        # Scale is on the x and y axis
test_square = Entity(model = "quad", color= color.orange, scale = (1,4), position = (5,1))

space_texture = load_texture("space.png")
rocket = Entity(model = "quad", texture = space_texture)

BUtton = button()


app.run()
