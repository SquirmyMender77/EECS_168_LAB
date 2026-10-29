from circle import Circle
def create_user_circle():
    print("Enter information for Circle:")
    r = float(input("Radius: "))
    x = float(input("X Position: "))
    y = float(input("Y Position: "))
    return Circle(x, y, r)
def print_circle_info(circ, name="Circle"):
    print(f"Information for {name}:")
    print(f"location: ({circ.x},{circ.y})")
    print(f"diameter: {circ.diameter()}")
    print(f"area: {circ.area()}")
    print(f"circumference {circ.circumference()}")
    print(f"distance from the origin: {circ.dist_to_origin()}")
def main():
    circle1=create_user_circle()
    circle2=create_user_circle()
    print_circle_info(circle1, "Circle 1")
    print_circle_info(circle2, "Circle 2")
    print("Do the circles overlap?", circle1.is_overlap(circle2))
    print("Is circle 1 inside circle 2?", circle1.is_inside(circle2))
if __name__ == "__main__":
    main()
