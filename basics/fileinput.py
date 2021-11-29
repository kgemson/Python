#myfile = open("fruits.txt")

#print(myfile.read())

    #with open("bear.txt") as myfile:
    #    content = myfile.read()
    #
    #print(content[:90])

#def foo(char, fpath):
#    with open(fpath) as myfile:
#        content = myfile.read()
#    
#    return(content.count(char))
#
#print(foo('t','bear.txt'))


#with open("snail.txt",'w') as myfile:
#    myfile.write("Snail")


#with open("bear.txt") as myfile:
#    content = myfile.read()
#
#with open("file.txt",'w') as outfile:
#    outfile.write(content[:90])


#with open("bear.txt") as infile:
#    content = infile.read()
#
#with open("bear2.txt",'a') as outfile:
#        outfile.write("\n" + content)


with open("data.txt",'a+') as myfile:
    myfile.seek(0)
    content = myfile.read()
    myfile.seek(0)
    myfile.write(content)