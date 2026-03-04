# # basic file write
# filename = input("Enter filename: ")
# content_ = "This is a test\n"
# try:
#     outfile = open(filename, "w")
#     try:
#         outfile.write(content_)
#     finally:
#         outfile.close()
# except FileNotFoundError:
#     print("File not Found")
# print('Continue with program')

# rearrange.py
##
#  This program reads data from a csv file that contains movie information,
#  filters out unwanted data, and produces a new csv file.
#

from csv import reader, writer

# Open the two csv files.
infile = open("movies.csv", encoding="UTF-8")
csvReader = reader(infile)

outfile = open("filtered2.csv", "w", encoding="UTF-8")
csvWriter = writer(outfile)

# Add the list of column headers to the csv file.
headers = ["Name", "Year", "Actors"]
csvWriter.writerow(headers)

# Skip the row of column headers in the reader.
next(csvReader)

# Filter the rows of data.
for row in csvReader:
    year = int(row[1])
    if year >= 1990 and year <= 1999:
        newRow = [row[0], row[1], row[4]]
        csvWriter.writerow(newRow)
infile.close()
outfile.close()