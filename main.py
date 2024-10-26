# Programmers: Cody and Krishon
# Course: CS151, Professor Zee
# Due Date: October 30th, 2024
# Lab Assignment: Lab 07
# Problem Statement: Find cost of flooring 5 rooms given length, width, and floor type
# Data In: length, width, material
# Data Out: cost (room cost), total_cost (overall cost), square_feet (area of room)
# Credits: none other than class notes


# Purpose:  [find the room dimensions and calculate square feet]
# Parameters: [None]
# Return: [square feet, float, area of room]
def room_dimensions():
    #find and verify dimensions of room
    length = float(input("Enter room length: "))
    width = float(input("Enter room width: "))
    while True:
        if length > 0 and width > 0:
            square_feet = length * width
            print('The square footage of the room is', square_feet)
            break
        else:
            print('Either length or width is an invalid input, try again')
            length = float(input("Enter room length: "))
            width = float(input("Enter room width: "))
            square_feet = length * width
    return square_feet

# Purpose:  [find the material type and calculate cost of one room]
# Parameters: [square_feet]
# Return: [cost, float with 2 decimal places, cost of one room ]
def material(square_feet):
    print('*' * 200)
    #caputre the type of material the user wants tthe floor to be
    print('Cost of flooring type:\nHardwood: $1.39 per square foot\nCarpet: $3.99 per square foot\nTiles: $4.99 per square foot')
    material = str(input('\nEnter the material of the room, hardwood, carpet, or tiles: '))
    material = material.lower().strip()
    #find and output the cost of the room given the flooring type
    while True:
        if material == 'hardwood':
            cost = square_feet * 1.39
            print(f'\nThe cost for the room is ${cost:.2f}')
            print('*' * 200)
            break
        elif material == 'carpet':
            cost = square_feet * 3.99
            print(f'\nThe cost for the room is ${cost:.2f}')
            print('*' * 200)
            break
        elif material == 'tiles':
            cost = square_feet * 4.99
            print(f'\nThe cost for the room is ${cost:.2f}')
            print('*' * 200)
            break
        else:
            print('Invalid input, please try again.')
            print('*' * 200)
            material = input('\nEnter the material of the room, hardwood, carpet, or tiles: ')
            material = material.lower().strip()
    return cost

# Purpose:  [make the main function to make sure user can enter exactly 5 rooms, calculate the total cost]
# Parameters: [None]
# Return: [No return value]
def main():
    #initialize variables
    count = 0
    total_cost = 0
    #output the purpose
    print('This program calculates the cost of flooring 5 different rooms.')
    print('*' * 200)
    #make so user gets exactly 5 rooms
    while count < 5:
        square_feet = room_dimensions()
        room_cost = material(square_feet)
        count +=1
        total_cost += room_cost
    #output total cost of all the rooms
    print(f'The total cost for flooring all of the rooms is ${total_cost:.2f}')

#call the main function
main()









