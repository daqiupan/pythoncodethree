import csv
with open('D:/test.csv','rb')as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


# import csv
# list=['1','2','3']
# outfile='D:test.csv'
# out=open(outfile,'a')
# csv_writer=csv.writer(out)
# csv_writer.writerow(list)
# out=open(outfile,'w',nowline='')
# csv_writer=csv.writer(out)
# csv_writer.writerow(list)