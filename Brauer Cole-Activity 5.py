# rewrite the Lesson 5 area program to have  a seperate function for the area
# of a square, the area of a rectangle, and the area of a circle
#(3.14 * radius**2). this program should include a menu interface

def print_options():
    print("Options:")
    print(" 'p' print options")
    print(" 's' calculate area of a square")
    print(" 'r' calculate area of a rectangle")
    print(" 'c' calculate area of a circle")
    print(" 'd' display formulas")
    print(" 'q' quit the program")
print("This program will calculate the area of a square, rectangle or a circle.")

def square(L):
    return L * L

def rectangle(W, H):
    return W * H

def circle(R):
      return 3.14 * R ** 2

choice = "p"
while choice != "q":
    if choice == "s":
        L = float(input("Length of one side of the square: "))
        print("Area of the square:", square(L))
        choice = input("option: ")
    elif choice == "r":
        W = float(input("Width of rectangle: "))
        H = float(input("Length of rectangle: "))
        print("Area of rectangle: ", rectangle(W, H))
        choice = input("option: ")
    elif choice == "c":
        R = float(input("Radius of circle: "))
        print("Area of circle: ", circle(R))
        choice = input("option: ")
    elif choice == "d":
        print("Area of a square: Length x Length")
        print("Area of a rectangle: Length x Width")
        print("Area of a circle: 3.14 x Radius x Radius")
        choice = input("option:")
    elif choice == "p":
        print_options()
        choice = input("options: ")
    else:
        print("unrecognized option. Please enter 'p' to display options")
        choice = input("option: ")
    if choice == "q":
        print("You will now exit the program")
        import time
        time.sleep(2)

