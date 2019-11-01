import csv

def update(name, vol, price):
    with open('users.csv', 'w') as csvfile:
        row = [name, vol, price]
        obj = csv.writer(csvfile)
        obj.writerow(row)
    csvfile.close()
    
    
def search_data(name_s):
    with open('users.csv','r') as csvfile:
        obj = csv.reader(csvfile)
        for name, vol, price in obj:
            if(name_s==name):
                return (vol, price)
    csvfile.close()
        
