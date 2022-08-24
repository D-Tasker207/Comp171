#Lab 4 - Duncan Tasker 9/8/2021

def rectangle_area(length, width):
    '''
    :return: the area of the rectangle with the given length and width
    '''
    area = length * width
    return area


def test_rectangle_area():
    print("test_rectangle_area") 
    result = rectangle_area(3, 4)
    print("Result 1 should be 12:", result)
    result = rectangle_area(4, 3)
    print("Result 2 should be 12:", result)
    result = rectangle_area(3, 4.5)
    print("Result 3 should be 13.5:", result)
    result = rectangle_area(182.5, 64.375)
    print("Result 4 should be 11748.4375:", result)


def triangle_area(base, height):
    '''
    :return: the area of the triangle with the given base and height
    '''
    area = (base * height) / 2
    return area


def test_triangle_area():
    print("test_triangle_area") 
    result = triangle_area(3, 4)
    print("Result 1 should be 6:", result)
    result = triangle_area(4, 3)
    print("Result 2 should be 6:", result)
    result = triangle_area(3, 4.5)
    print("Result 3 should be 6.75:", result)
    result = triangle_area(182.5, 64.375)
    print("Result 4 should be 5874.21875:", result)


def house_surface_area(length, width, height, gable_height):
    '''
    :param gable_height: the height from the top of the wall to the peak of the gable
                         gable is always over the width of the house
    :return: the surface area of the exterior walls of the house including gables
    '''
    wall_area = (2 * rectangle_area(length, height)) + (2 * rectangle_area(width, height))
    gable_area = 2 * triangle_area(width, gable_height)
    total_house_area = wall_area + gable_area
    
    return total_house_area


def test_house_surface_area():
    print("test_house_surface_area") 
    result = house_surface_area(10, 5, 10, 5)
    print("Result 1 should be 325:", result)
    result = house_surface_area(20.5, 10.5, 11.5, 8.5)
    print("Result 2 should be 802.25:", result)
    result = house_surface_area(5, 10, 10, 5)
    print("Result 3 should be 350:", result)
    result = house_surface_area(10, 5, 10, 0)
    print("Result 4 should be 300:", result)
 
def userinputs():
    entering = "y"
    all_house_area = 0.0
    
    while entering == "y":
        try:
            house_length = float(input("\nEnter the length of the house :: "))
            house_width = float(input("Enter the width of the house :: "))
            house_height = float(input("Enter the height of the house :: "))
            gable_height = float(input("Enter the height of the gable :: "))
        except ValueError:
            print("Please input numbers only")
            userinputs()
        
        if house_length < 0 or house_width < 0 or house_height < 0 or gable_height < 0:
            print("Inputs cannot be negative")
            userinputs()
        
        house_area = house_surface_area(house_length, house_width, house_height, gable_height)
        print("\nThe area of the house is: ", house_area, " square feet", sep="")
        all_house_area += house_area
        
        entering = input("\nWould you like to enter another house? (y/n) :: ")
    
    print("\nThe total area of all houses is: ", all_house_area, " square feet", sep="")
    return null
 
def main():
    test_rectangle_area()
    test_triangle_area()
    test_house_surface_area()
    print("end of tests \n")
    
    userinputs()
main()