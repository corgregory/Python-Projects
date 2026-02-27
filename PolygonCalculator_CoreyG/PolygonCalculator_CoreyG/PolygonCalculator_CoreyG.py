"""
Build a Polygon Area Calculator
In this project, you will use object-oriented programming to create a Rectangle class and a Square class. The Square class should be a subclass of Rectangle and inherit its methods and attributes.

Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

User Stories:

You should create a Rectangle class.

When a Rectangle object is created, it should be initialized with width and height attributes. The class should also contain the following methods:

set_width: Sets the width of the rectangle.
set_height: Sets the height of the rectangle.
get_area: Returns area ( width×height
 ).
get_perimeter: Returns perimeter  2(width+height)
 .
get_diagonal: Returns diagonal  width2+height2−−−−−−−−−−−−−−√
 .
get_picture: Returns a string that represents the shape using lines of *. The number of lines should be equal to the height and the number of * in each line should be equal to the width. There should be a new line (\n) at the end of each line. If the width or height is larger than 50, this should return the string: Too big for picture..
get_amount_inside: Takes another shape (square or rectangle) as an argument. Returns the number of times the passed in shape could fit inside the shape (with no rotations). For instance, a rectangle with a width of 4 and a height of 8 could fit in two squares with sides of 4.
If an instance of a Rectangle is represented as a string, it should look like: Rectangle(width=5, height=10).

You should create a Square class that subclasses Rectangle.

When a Square object is created, it should be initialized with a single side length. The __init__ method should store the side length in both the width and height attributes from the Rectangle class.

The Square class should contain the following methods:

set_width: Overrides the set_width method from the Rectangle class. It should set the width and height to the side length.
set_height: Overrides the set_height method from the Rectangle class. It should set the width and height to the side length.
set_side: Sets the height and width of the square equal to the side length.
The Square class should be able to access the Rectangle class methods.

If an instance of a Square is represented as a string, it should look like: Square(side=9).

"""


class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width) -> None:
        self.width = width
    
    def set_height(self, height) -> None:
        self.height = height

     # here I a calculating the area of a rectangle A = L * W
    def get_area(self) -> float:
        area = self.width * self.height
        return area
    # Perimeter = 2 * (L + W)
    def get_perimeter(self) -> float:
        perimeter = 2 * (self.width + self.height)
        return perimeter
    # Diagonal = sqrt((W^2 + L^2)) * I could have imported the math module
    # but I decided not to over complicate the project 
    def get_diagonal(self) -> float:
        diagonal = (self.width **2 + self.height **2) **0.5
        return diagonal
    # get_picture gives a visual representation(*) of the rectangle
    # of N width and N height
    def get_picture(self) -> str:
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for stars in range(self.height):
            picture +=  "*" * self.width + "\n"
        return picture
    # this function will return how many times a shape can fit inside the other
    def get_amount_inside(self, other):
        return (self.width // other.width) * (self.height // other.height)

    # Visual Str format representation of a rectangle
    def __str__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    #square class inherits from rectangle so I used the super() to call
    #rectangle's constructor
    def __init__(self, side):
        super().__init__(side, side)
    # for the set width ansd height methods I created a set_ side method
    # that makes them equal to ensure it is indeed a square.
    def set_width(self,width):
        self.set_side(width)

    def set_height(self, height):
        self.set_side(height)

    def set_side(self, side):
        self.width = side
        self.height = side
    #string representation for a square of side N
    def __str__(self) -> str:
        return f"Square(side={self.width})"

    # my test calls are inside a main function as I am trying to get use to 
    # using this convention on all projects
def main():
    rect = Rectangle(10, 5)
    print(rect.get_area())
    rect.set_height(3)
    print(rect.get_perimeter())
    print(rect)
    print(rect.get_picture())

    sq = Square(9)
    print(sq.get_area())
    sq.set_side(4)
    print(sq.get_diagonal())
    print(sq)
    print(sq.get_picture())

    rect.set_height(8)
    rect.set_width(16)
    print(rect.get_amount_inside(sq))

if __name__ == "__main__":
    main() 