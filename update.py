import csv

def update(name, vol, price, company):
    row = [name, vol, price, company]
    with open('users.csv', 'a') as csv_file:
        obj = csv.writer(csv_file)
        obj.writerow(row)
    csv_file.close()
    
    
def search_data(name_s):
    with open('users.csv','r') as csvfile:
        obj = csv.reader(csvfile)
        for row in obj:
            if(row[0]==name_s):
                print(row)
    csvfile.close()

def print_data():
    with open('users.csv', 'r') as csv_file:
        obj = csv.reader(csv_file)
        for data in obj:
            print(data)
    csv_file.close()
    
