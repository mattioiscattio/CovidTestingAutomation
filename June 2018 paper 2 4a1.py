title = input("enter the title of the book in the library.")
year = str(input("enter the year that the book was released."))
def librarycode(title, year):
    return(title[0:3]+year[0:2]+"\n")
file = open("Paper2June20184a1.txt", "a+")
file.write(librarycode(title,year))
file.close()