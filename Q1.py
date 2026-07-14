class BookStore:
    NoOfBooks=0

    def __init__(self,Name,Author):
        self.Name=Name
        self.Author=Author
        BookStore.NoOfBooks+=1

    def Display(self):
        print("Book name is",self.Name  ,"By author",self.Author  ,"NO of books is",BookStore.NoOfBooks)

obj1=BookStore("nothing","Sakshi")
obj1.Display()

obj2=BookStore("Linux System Programming","Robert Love")
obj2.Display()

