#def concat_string(str1, str2):
#    #return str1 + str2
#    return " ".join([str1,str2])

#print(concat_string("Hello","bawbag"))

#def mean(*args):
#    return sum(args) / len(args)
#
#print(mean(10, 20, 30, 40))

def str_sort(*args):
    new_args = [val.upper() for val in args]
    return sorted(new_args)

print(str_sort("snow","glacier","iceberg"))