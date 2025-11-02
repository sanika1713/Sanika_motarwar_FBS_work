
from book import Book

ch = 0
while(ch != 5):
    b1 = Book()
    print('''Choose from below:
        1.Add Book
        2.Delete book by id
        3.Display all book
        4.Search book by id
        5.Exit''')
    ch = input('Enter your choice:')

    if(ch == '1'):
        b1.Addbook()
    elif(ch == '2'):
        b1.Delbook()
    elif(ch == '3'):
        b1.showall()
    elif(ch == '4'):
        b1.search()
    elif(ch == '5'):
        print('Exiting....')
    else:
        print('Invalid choice....')
