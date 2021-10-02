import csv

# Read data
# write data


# Read csv data
movies_file_path = r"C:\Users\91901\Desktop\stock_feeds\files_data\all_movies.csv"

# open
file_obj = open(movies_file_path, 'r')

reader = csv.reader(file_obj)
print(reader)
headers = None

movies_1023_list = []
# find out movies realed on 2013
filter_year = 2017
for index, row in enumerate(reader):
    if index == 0:
        headers = row
    else:
        year = int(row[1])
        if year < filter_year:
            movies_1023_list.append(row)

print(headers)
print(movies_1023_list)

# Writing content to csv file
filtered_movies_file_path = r"C:\Users\91901\Desktop\stock_feeds\files_data\filtered_movies.csv"
file_obj_out = open(filtered_movies_file_path, 'w')
writer = csv.writer(file_obj_out)

writer.writerow(headers)
# content
for row in movies_1023_list:
    writer.writerow(row)


# using dictreader
movies_file_path = r"C:\Users\91901\Desktop\stock_feeds\files_data\all_movies.csv"
file_object = open(movies_file_path, 'r')
dict_reader = csv.DictReader(file_object, fieldnames=('Tle','', 'Director'))
print(dict_reader)
print(dir(dict_reader))
#print(next(dict_reader))
#print(next(dict_reader))
for data in dict_reader:
    print(data)
    # if int(data['Release year']) <= 2017:
    #     print(data)

# csv  dict writer



