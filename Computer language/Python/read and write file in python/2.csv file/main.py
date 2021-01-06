import time
import csv
from datetime import datetime
# read with basics
'''
path = r"F:\Desktop\`\web scraping\read and write file in python\2.csv file\data.csv"
with open(path,'r') as rf:
    # row = street,city,zip,state,beds,baths,sq__ft,type,sale_date,price,latitude,longitude
    for line in rf:
        print(line)
'''

# read csv file nomaly (without csv module)
'''
path = r"F:\Desktop\`\web scraping\read and write file in python\2.csv file\data.csv"


lines = [line for line in open(path)]
header = lines[0].strip().split(',')  # here strip() remove last '\n'
print(header)


dataset = [line.strip().split(',') for line in open(path)]
start = time.perf_counter()
j = 1
for i in dataset:
    if j < 6:
        print(i)
    else :
        break
    j += 1
end = time.perf_counter()
print(f'time : {end-start}')
'''

# but what if you data contain's ','
# that's why we should use csv module

# with csv module
'''
path = r"F:\Desktop\`\web scraping\read and write file in python\2.csv file\data.csv"
with open(path,'r',newline='') as file:  # In some oprating system line ends with '\n' while others ';' 
                                     # wtih this newline keyword it will run across the all platform
    
    reader = csv.reader(file)
    header = next(reader)
    # data = [row for row in reader]
    # print(header)
    # print(data[0])

     
    #ot = 
    #['street', 'city', 'zip', 'state', 'beds', 'baths', 'sq__ft', 'type', 'sale_date', 'price', 'latitude', 'longitude']
    #['3526 HIGH ST', 'SACRAMENTO', '95838', 'CA', '2', '1', '836', 'Residential', 'Wed May 21 00:00:00 EDT 2008', '59222', '38.631913', '-121.434879']
    

    # but problem is that we didn't converted data type
    # all are string right now

    data = []
    for row in reader :
        street = row[0]
        city = row[1]
        zip_code = int(row[2])
        state = row[3]
        bed = int(row[4])
        baths = int(row[5])
        sq_ft = int(row[6])
        typ = row[7]
        date = row[8]
        price = int(row[9])
        a = float(row[10])
        b = float(row[11])

        data.append([street,city,zip_code,state,bed,baths,sq_ft,typ,date,price,a,b])

    # print(header)
    # for i in range(5):
    #     print(data[i])

    with open('result.csv','w') as wf:
        writer = csv.writer(wf,delimiter='|')   # delimiter's default value ','  but delimiter = seperator
        writer.writerow(["Date","Return"])      # if you set delimiter in writer then in reader defalut value ',' 
                                                # you have to set '|'

        for i in range(len(data) -1):
            todays_row = data[i]
            todays_date = todays_row[8]
            todays_price = todays_row[9]
            yesters_row = data[i+1]
            yesters_price = yesters_row[9]

            daily_return = (todays_price - yesters_price) / yesters_price
            writer.writerow([todays_date,daily_return])

        with open('result.csv','r') as rf:
            for line in rf:
                print(line)
'''

# with csv module but with onther function
with open('data.csv','r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    header = next(csv_reader)
    # data = []
    # for line in csv_reader:
    #     city = line['city']
    #     state = line['state']
    #     street = line['street']
    #     beds = line['beds']
    #     baths = line['baths']
    #     type_apt = line['type']
    #     price = line['price']

    #     data.append(dict(city = city,state = state,street = street,beds = beds,baths = baths, type = type_apt,price = price))


    j = 1
    for line in csv_reader:
        if j < 500:
            pass
            # print(line)
            # DictReader easy to use
            # ex. if you want to print or get street
            # print(line['street'])

            # but in reader 
            # print(line[0])

            # how ever read performance is way more better than dictread
            # bench mark

            # 100 rows
            # d_read : 3.5943301
            # read : 0.9628639

            # 500 rows
            # d_read : 11.242356899999999
            # read : 1.9256910999999999

            # solution:
            # use read but make comment like
            # street = 0
            # address = 1
            # baths = 2
        else :
            break
        j += 1

    '''
    with open('result2.csv','w') as write_file:
        fildname = [ 'city', 'state', 'street','beds', 'baths',  'type',  'price']
        csv_writer = csv.DictWriter(write_file,fildname)

        csv_writer.writeheader()

        for line in csv_reader:
            del line['zip']
            del line['sq__ft']
            del line['sale_date']
            del line['latitude']
            del line['longitude']

            csv_writer.writerow(line)
    '''


    # we have to create data and than pass in to csv_writer
    # another way is delete values with key

    '''
    with open('result2','w') as write_file:
        fildname = [ 'city', 'state', 'street','beds', 'baths',  'type',  'price']
        csv_writer = csv.DictWriter(write_file,fildname)

        csv_writer.writeheader()

        ['', '', '', '', '', '', '', '', '', '', '', '']
        for line in csv_reader:
            del line['zip']
            del line['sq__ft']
            del line['sale_date']
            del line['latitude']
            del line['longitude']

            csv_writer.writerow(line)
    '''






    

