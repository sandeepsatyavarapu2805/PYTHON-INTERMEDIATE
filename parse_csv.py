import csv

# using normal reader and writer of CSV
with open('names.csv', 'r', newline='') as f, \
     open('names_new.csv', 'w', newline='') as nf:

    reader = csv.reader(f)
    print(reader) # we need to iterate it . its just an object which just points and does not open it benefits large files
    # next(data) # moves the pointer to next one , in here the next line

    writer = csv.writer(nf, delimiter='\t') # it constructs the object instance to write the data with a new delimiter '\t'

    '''for line in reader:
        writer.writerow(line)
    '''
    # the above loop is good but we can also do this which is better

    writer.writerows(reader)


# using dict reader and writer for CSV files
with open('names.csv','r', newline='') as f, \
     open('names_new.csv','w', newline='') as nf:
    
    reader_dict = csv.DictReader(f) # it formats the everything in the file into dictionary with keys as the file headers for every info

    # for line in reader_dict:
    #     print(line)
    headers = reader_dict.fieldnames
    writer_dict = csv.DictWriter(nf, fieldnames=headers, delimiter='-')
    
    writer_dict.writeheader()
    writer_dict.writerows(reader_dict)