#Dmitrii Gusev

import tkinter as tk
from tkinter import messagebox
import math


class Shape:
    def __init__(self):
        self.x = 0.0
        self.y = 0.0

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y


class Circle(Shape):
    def __init__(self):
        Shape.__init__(self)

    def area(self):
        return math.pi * self.x ** 2


class Rectangle(Shape):
    def __init__(self):
        Shape.__init__(self)

    def area(self):
        return self.y * self.x


class Triangle(Shape):
    def __init__(self):
        Shape.__init__(self)

    def area(self):
        return self.y * self.x * 0.5


class Trapezoid(Shape):
    def __init__(self):
        Shape.__init__(self)
        self.z = 0.0

    def set_z(self, z):
        self.z = z

    def area(self):
        return self.z * (self.x + self.y) * 0.5



class ShapeCalculatorApp:
    def __init__(self, master):
        self.result_label = None
        self.calculate_button = None
        self.input_entry2 = None
        self.input_entry3 = None
        self.input_label3 = None
        self.result_value = None
        self.input_label2 = None
        self.input_entry1 = None
        self.input_label1 = None
        self.shape_option_menu = None
        self.shape_label = None
        self.master = master
        master.title("Shape Calculator")

        self.shape_var = tk.StringVar()
        self.shape_var.set("Circle")  # Default shape

        self.create_widgets()

    def create_widgets(self):
        self.shape_label = tk.Label(self.master, text="Select Shape:")
        self.shape_label.grid(row=0, column=0, sticky="w")

        self.shape_option_menu = tk.OptionMenu(self.master, self.shape_var, "Circle", "Rectangle", "Triangle",
                                               "Trapezoid", command=self.update_input_fields)
        self.shape_option_menu.grid(row=0, column=1)

        self.input_label1 = tk.Label(self.master, text="Input 1:")
        self.input_label1.grid(row=1, column=0, sticky="w")

        self.input_entry1 = tk.Entry(self.master)
        self.input_entry1.grid(row=1, column=1)

        self.input_label2 = tk.Label(self.master, text="Input 2:")
        self.input_label2.grid(row=2, column=0, sticky="w")

        self.input_entry2 = tk.Entry(self.master)
        self.input_entry2.grid(row=2, column=1)

        self.input_label3 = tk.Label(self.master, text="Input 3:")
        self.input_label3.grid(row=3, column=0, sticky="w")

        self.input_entry3 = tk.Entry(self.master)
        self.input_entry3.grid(row=3, column=1)

        self.calculate_button = tk.Button(self.master, text="Calculate", command=self.calculate_area)
        self.calculate_button.grid(row=4, columnspan=2)

        self.result_label = tk.Label(self.master, text="Result:")
        self.result_label.grid(row=5, column=0, sticky="w")

        self.result_value = tk.Label(self.master, text="")
        self.result_value.grid(row=5, column=1, sticky="w")

    def update_input_fields(self, shape):
        #clear result value when updating shape
        self.result_value.config(text="")

        if shape == "Circle":
            self.input_label1.config(text="Radius:")
            self.input_label2.grid_remove()
            self.input_entry2.grid_remove()
            self.input_label3.grid_remove()
            self.input_entry3.grid_remove()
        elif shape == "Rectangle":
            self.input_label1.config(text="Length:")
            self.input_label2.config(text="Width:")
            self.input_label2.grid()
            self.input_entry2.grid()
            self.input_label3.grid_remove()
            self.input_entry3.grid_remove()
        elif shape == "Triangle":
            self.input_label1.config(text="Base:")
            self.input_label2.config(text="Height:")
            self.input_label2.grid()
            self.input_entry2.grid()
            self.input_label3.grid_remove()
            self.input_entry3.grid_remove()
        elif shape == "Trapezoid":
            self.input_label1.config(text="Base 1:")
            self.input_label2.config(text="Base 2:")
            self.input_label3.config(text="Height:")
            self.input_label2.grid()
            self.input_entry2.grid()
            self.input_label3.grid()
            self.input_entry3.grid()

    def calculate_area(self):
        shape_type = self.shape_var.get()
        try:
            if shape_type == "Circle":
                radius = float(self.input_entry1.get())
                circle = Circle()
                circle.set_x(radius)
                area = circle.area()
            elif shape_type == "Rectangle":
                length = float(self.input_entry1.get())
                width = float(self.input_entry2.get())
                rectangle = Rectangle()
                rectangle.set_x(length)
                rectangle.set_y(width)
                area = rectangle.area()
            elif shape_type == "Triangle":
                base = float(self.input_entry1.get())
                height = float(self.input_entry2.get())
                triangle = Triangle()
                triangle.set_x(base)
                triangle.set_y(height)
                area = triangle.area()
            elif shape_type == "Trapezoid":
                base1 = float(self.input_entry1.get())
                base2 = float(self.input_entry2.get())
                height = float(self.input_entry3.get())
                trapezoid = Trapezoid()
                trapezoid.set_x(base1)
                trapezoid.set_y(base2)
                trapezoid.set_z(height)
                area = trapezoid.area()
            self.result_value.config(text=str(area))
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numeric values.")


def main():
    root = tk.Tk()
    app = ShapeCalculatorApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
