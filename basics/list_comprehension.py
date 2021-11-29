#temps = [221,234,312,299,-9999,286]
#new_temp = [temp / 10 for temp in temps if temp != -9999]
#print(new_temp)

def gen_int_list(in_list):
    my_int_list = [num for num in in_list if num != 'no data']
    return my_int_list

my_list = [1,9,"no data",7,"no data",3]
print(gen_int_list(my_list))

def gen_pos_list(in_list):
    my_pos_list = [num for num in in_list if num > 0]
    return my_pos_list

my_list = [5,2,-8,-3,0,-6,7,4]
print(gen_pos_list(my_list))

def gen_int_list(in_list):
    my_int_list = [num if num != 'no data' else 0 for num in in_list ]
    return my_int_list

my_list = [1,9,"no data",7,"no data",3]
print(gen_int_list(my_list))

def gen_sum_dec_list(in_list):
    my_dec_list = [float(num) if num != 'no data' else 0 for num in in_list ]
    return sum(my_dec_list)

my_list = ['0.7','0.9','0.5','-0.2','0.6','0.4','-0.6','0.3','-0.5']
print(gen_sum_dec_list(my_list))