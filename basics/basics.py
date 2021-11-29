from typing import Tuple


def mean(my_values):
    if isinstance(my_values,dict):
        the_mean = sum(my_values.values()) / len(my_values)
    elif isinstance(my_values,Tuple):
        the_mean = sum(my_values.values()) / len(my_values)
    else:
        the_mean = sum(my_values) / len(my_values)
    
    return the_mean

student_dict = {"Dave": 81.2, "Bob": 78.3, "Susan": 90.1, "Eric": 85.5}
student_list = [81.2, 78.3, 90.1, 85.5]


print(mean(student_dict))
print(mean(student_list))