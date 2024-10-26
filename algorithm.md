### Algorithm Document
1. Function: Room Dimensions
    * Name: room_dimensions
    * Parameter: None
    * Return: square_feet
    * Algorithm
        1. ask user to input length, convert to float
        2. ask user to input width, convert to float
        3. while True;
            1. if length > 0 and width > 0
               * square_feet = length * width
               * output to user the square feet of the room
               * insert break
            2. otherwise
                * output to user they inputted an invalid value and to try again
                * ask user to input length, convert to float
                * ask user to input width, convert to float
                * square_feet = length * width
        4. return square feet

2. Function: Flooring Material
    * Name: material
    * Parameter: square_feet)
    * Return: cost
    * Algorithm
        1. display to the user their flooring options and the prices per square foot of each option
        2. ask user to input the material, convert to lower and get rid of whitespace at beginning or the end
        3. While True: 
           1. if material == 'hardwood'
              * cost = square_feet * 1.39
              * output the cost of the room
              * insert a break
           2. otherwise if material == 'carpet'
              * cost = square_feet * 3.99
              * output the cost of the room
              * insert a break
           3. otherwise if material == 'tiles'
              * cost = square_feet * 4.99
              * output the cost of the room
              * insert a break
           4. otherwise
              * output to the user they entered an invalid input and to try again
              * ask user to input the material, convert to lower and get rid of whitespace at beginning or the end
           5. return cost

3. Function: Main
    * Name: main
    * Parameters: None
    * Return: None
    * Algorithm
      1. initialize cost and total_cost to 0
      2. output to the user to purpose of the program
      3. while count < 5
         1. call room_dimensions by setting square_feet = room_dimensions()
         2. call material(square_feet) by setting room_cost = material(square_feet)
         3. add 1 to count
         4. add room_cost to total_cost
      4. output the total cost of flooring all the rooms to the user
4. Call main()