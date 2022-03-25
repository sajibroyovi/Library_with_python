
class Library:
    def __init__(self,book_list):
        self.books=book_list

    def diplay_all_book(self):
        print("Books available in the library are: ")
        for book in self.books:
            print("\t $ " +book )

    def borrow(self,book_name):
        if book_name in self.books:
            print(f"The book name:{book_name} has been issued to you. Please keep it safe and return it within one week")
            self.books.remove(book_name)
            return True
        else:
            print("The book that you are trying to borrow is not available on the library. Please try after sometime latter")
            return False

    def return_book(self,book_name):
        self.books.append(book_name)
        print("Thank you for returning the book. Hope you are enjoyed it.")

class Student:

    def request_book(self):
        self.book_name=input("Enter the book you want to borrow :")
        return self.book_name

    def ruturn_book(self):
        self.book_name=input("Enter the book name that you want to return :")
        return self.book_name

if __name__== "__main__":

    main_library=Library(['python','c++','c','django','flutter','dbms','os'])
    student=Student()
    print("------ Welcome To The World Book Library ------")
    print("\t ****Knowledge is Devine****")

    while(True):
        
        print('''
            1. See the available books in the library
            2. Borrow the book
            3. Return the book
            4. Exit
        
        ''')
        n=int(input("Please enter your choice: "))

        if n==1:
            main_library.diplay_all_book()
        elif n==2:
            main_library.borrow(student.request_book())

        elif n==3:
            main_library.return_book(student.ruturn_book())

        elif n==4:
            exit()
        else:
            print("Wrong input..😑😑 Please enter a valid input🙏🙏")
        

