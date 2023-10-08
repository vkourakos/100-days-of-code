def turn_right():
    turn_left()
    turn_left()
    turn_left()

                            
while not wall_in_front():
    move()
turn_left() 

while not at_goal():      
    if wall_on_right():
        if not wall_in_front():
            move()
        else:
            turn_left()
    else:
        turn_right()
        move()
   
    
    



