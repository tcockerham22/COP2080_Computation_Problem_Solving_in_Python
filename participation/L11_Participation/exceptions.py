# try:
#     filename = input("Enter filename: ")
#     infile = open(filename, "r")
#     line = infile.readline()
#     value = int(line)
# except IOError :
#    print("Error: file not found.")
  
# except ValueError as exception :
#    print("Error:", str(exception))

filename = input("Enter filename: ")
outfile = open(filename, "w")
content_ = "This is a test\n"
try:
    outfile.write(content_)
except:
    print("You messed up")
finally:
    outfile.close() 