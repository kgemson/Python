import pandas as pd

column = ["John","Paul","George","Ringo"]

titled_columns = {"fname": column,
                    "sname": ["Lennon","McCartney","Harrison","Starr"],
                    "instrument": ["Guitar","Bass","Guitar","Drums"]}

my_data = pd.DataFrame(titled_columns)

# select values
my_column = my_data["fname"] # select entire column with that header. Can get specific fields by using [x] afterwards
my_row = my_data.iloc[1] # select entire row with index '1'
my_field = my_data["fname"].iloc[1] # select row with index '1' from column "fname". Or...
my_field2 = my_data.iloc[1]["fname"]

# manipulate data
initial_list=[]

for i in range(len(my_data)):
    inits = (str(my_data["fname"][i])[0:1].upper() + '.' + str(my_data["sname"][i])[0:1].upper() + '.')
    initial_list.append(inits)

my_data["initials"] = initial_list
#print(my_data)

# save to a (tab delimited) file
#my_data.to_csv("pandas_test2.txt",sep="\t")