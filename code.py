def bound_to_180(angle):
    
    if angle>=0:
        return(angle%180)
    if angle <0:
        return(angle%-180)
    
    return 0


def is_angle_between(first_angle, middle_angle, second_angle):
    if middle_angle <  second_angle and  middle_angle >  first_angle:
        
        return True
    else:
        return False
        
        
print(bound_to_180(-183))
print(is_angle_between(2, 122, 21))
