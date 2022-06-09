import csv

csv_filepath ="data.csv"
aseet  = '1099738898474'

def find_IILP(id):
	with open(csv_filepath, 'r') as reader:
	   	
    		for row in reader.readlines()[1:]:
    			
    			columns = row.strip().split(",")
    			if id in columns[0]:
    				starting_price = (columns[4])
    				print(starting_price)
    				
    				
find_IILP(aseet)