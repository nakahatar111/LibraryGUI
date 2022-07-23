from tkinter import *
from tkinter import messagebox
from tkinter import simpledialog
from patron import *
from book import *
from library import *
from librarymodule import StringGeneratorForDictionaries

WIDTH = 50

ROW_0 = 0
ROW_1 = 1
ROW_2 = 2
ROW_3 = 3
ROW_4 = 4
ROW_5 = 5
ROW_6 = 6
ROW_7 = 7
ROW_8 = 8
ROW_9 = 9
ROW_10 = 10
ROW_11 = 11
ROW_12 = 12
ROW_13 = 13
ROW_14 = 14
ROW_15 = 15
ROW_16 = 16
ROW_17 = 17
ROW_18 = 18
ROW_19 = 19
ROW_20 = 20

COL_0 = 0
COL_1 = 1
COL_2 = 2
COL_3 = 3
COL_4 = 4

class LibraryGUI:
  def __init__(self):

    self.win = Tk()

    self.win.withdraw()
    self.Ask_Library_Name = simpledialog.askstring(title="Library Name", prompt="Enter Library Name:")
    self.win.deiconify()
    
    if self.Ask_Library_Name == None or self.Ask_Library_Name == '':
      self.Ask_Library_Name = 'Library'
    
    self.__library = Library(self.Ask_Library_Name)
    
    self.__Transaction_History = list()

    self.win.title(self.__library.get_name())
    
    self.Library_Title = StringVar()
    self.CheckB_Status_Value = StringVar()
    self.ReturnB_Status_Value = StringVar()
    self.Book_Status_Value = StringVar()
    self.Patron_Status_Value = StringVar()
    self.Join_Status_Value = StringVar()
    self.Leave_Status_Value = StringVar()
    self.AddB_Status_Value = StringVar()
    self.RemoveB_Status_Value = StringVar()

    self.__set_transcation = False
    self.__Clear_Transaction_Status()

    self.Library_Title.set(self.__library.get_name())

    #Library Title
    self.Library_Title_Label = Label(self.win, textvariable = self.Library_Title)

    #Checkout Book
    self.CheckB_Label = Label(self.win, text = "Checkout Books")
    self.CheckB_Title_Label = Label(self.win, text = "Title")
    self.CheckB_Patron_Label = Label(self.win, text = "Patron")
    self.CheckB_Status_Label = Label(self.win, text = "Status")
    self.CheckB_Title_Entry = Entry(self.win, width = WIDTH)
    self.CheckB_Patron_Entry = Entry(self.win, width = WIDTH)
    self.CheckB_Button = Button(self.win, text = "Checkout Book", command = self.__CheckOutBook)
    self.CheckB_Status = Label(self.win, textvariable = self.CheckB_Status_Value)

    #Return Book
    self.ReturnB_Label = Label(self.win, text = "Return Books")
    self.ReturnB_Title_Label = Label(self.win, text = "Title")
    self.ReturnB_Patron_Label = Label(self.win, text = "Patron")
    self.ReturnB_Status_Label = Label(self.win, text = "Status")
    self.ReturnB_Title_Entry = Entry(self.win, width = WIDTH)
    self.ReturnB_Button = Button(self.win, text = "Return Book", command = self.__ReturnBook)
    self.ReturnB_Status = Label(self.win, textvariable = self.ReturnB_Status_Value)

    #Seach
    self.Search_Label = Label(self.win, text = "SEARCH")

    #Book
    self.Book_Label = Label(self.win, text = "Book")
    self.Book_Title_Label = Label(self.win, text = "Title")
    self.Book_Status_Label = Label(self.win, text = "Status")
    self.Book_Title_Entry = Entry(self.win, width = WIDTH)
    self.Book_Status = Label(self.win, textvariable = self.Book_Status_Value)

    #Patron
    self.Patron_Label = Label(self.win, text = "Patron")
    self.Patron_Name_Label = Label(self.win, text = "Name")
    self.Patron_Status_Label = Label(self.win, text = "Status")
    self.Patron_Name_Entry = Entry(self.win, width = WIDTH)
    self.Patron_Status = Label(self.win, textvariable = self.Patron_Status_Value)

    #Membership
    self.Membership_Label = Label(self.win, text = "MEMBERSHIP")

    #Join
    self.Join_Label = Label(self.win, text = "Join")
    self.Join_Name_Label = Label(self.win, text = "Name")
    self.Join_Status_Label = Label(self.win, text = "Status")
    self.Join_Name_Entry = Entry(self.win, width = WIDTH)
    self.Join_Status = Label(self.win, textvariable = self.Join_Status_Value)

    #Leave
    self.Leave_Label = Label(self.win, text = "Leave")
    self.Leave_Name_Label = Label(self.win, text = "Name")
    self.Leave_Status_Label = Label(self.win, text = "Status")
    self.Leave_Name_Entry = Entry(self.win, width = WIDTH)
    self.Leave_Status = Label(self.win, textvariable = self.Leave_Status_Value)
    
    #Book Collection
    self.BookC_Label = Label(self.win, text = "BOOK COLLECTION")

    #Add Book
    self.AddB_Label = Label(self.win, text = "Add Book")
    self.AddB_Title_Label = Label(self.win, text = "Title")
    self.AddB_Author_Label = Label(self.win, text = "Author")
    self.AddB_Status_Label = Label(self.win, text = "Status")
    self.AddB_Title_Entry = Entry(self.win, width = WIDTH)
    self.AddB_Author_Entry = Entry(self.win, width = WIDTH)
    self.AddB_Button = Button(self.win, text = "Add Book", command = self.__AddBook)
    self.AddB_Status = Label(self.win, textvariable = self.AddB_Status_Value)

    #Remove Book
    self.RemoveB_Label = Label(self.win, text = "Remove Book")
    self.RemoveB_Title_Label = Label(self.win, text = "Title")
    self.RemoveB_Author_Label = Label(self.win, text = "Author")
    self.RemoveB_Status_Label = Label(self.win, text = "Status")
    self.RemoveB_Title_Entry = Entry(self.win, width = WIDTH)
    self.RemoveB_Button = Button(self.win, text = "Remove Book", command = self.__RemoveBook)
    self.RemoveB_Status = Label(self.win, textvariable = self.RemoveB_Status_Value)

    #Binding
    self.Book_Title_Entry.bind("<Return>", self.__SearchBook)
    self.Patron_Name_Entry.bind("<Return>", self.__SearchPatron)
    self.Join_Name_Entry.bind("<Return>", self.__Join)
    self.Leave_Name_Entry.bind("<Return>", self.__Leave)

    #CheckBox
    self.Check_Patron = Checkbutton(self.win, text = 'List of Patron', command = self.__Open_Patron_list)
    self.Check_Book = Checkbutton(self.win, text = 'List of Book', command = self.__Open_Book_list)
    self.Check_History = Checkbutton(self.win, text = 'Transaction History', command = self.__Open_Transaction_History)


    #Grid
    self.Library_Title_Label.grid(row = ROW_0, column = COL_2)

    self.CheckB_Label.grid(row = ROW_1, column = COL_1)
    self.CheckB_Title_Label.grid(row = ROW_2, column =COL_0)
    self.CheckB_Patron_Label.grid(row = ROW_3, column =COL_0)
    self.CheckB_Status_Label.grid(row = ROW_5, column = COL_0)
    self.CheckB_Title_Entry.grid(row = ROW_2, column = COL_1)
    self.CheckB_Patron_Entry.grid(row = ROW_3, column = COL_1)
    self.CheckB_Button.grid(row = ROW_4, column = COL_1)
    self.CheckB_Status.grid(row = ROW_5, column = COL_1)
    
    self.ReturnB_Label.grid(row = ROW_1, column = COL_4)
    self.ReturnB_Title_Label.grid(row = ROW_2, column = COL_3)
    self.ReturnB_Patron_Label.grid(row = ROW_3, column = COL_3)
    self.ReturnB_Status_Label.grid(row = ROW_5, column = COL_3)
    self.ReturnB_Title_Entry.grid(row = ROW_2, column = COL_4)
    self.ReturnB_Button.grid(row = ROW_4, column = COL_4)
    self.ReturnB_Status.grid(row = ROW_5, column = COL_4)

    self.Search_Label.grid(row = ROW_6, column = COL_2)

    self.Book_Label.grid(row = ROW_7, column = COL_1)
    self.Book_Title_Label.grid(row = ROW_8, column = COL_0)
    self.Book_Status_Label.grid(row = ROW_9, column = COL_0)
    self.Book_Title_Entry.grid(row = ROW_8, column = COL_1)
    self.Book_Status.grid(row = ROW_9, column = COL_1)

    self.Patron_Label.grid(row = ROW_7, column = COL_4)
    self.Patron_Name_Label.grid(row = ROW_8, column = COL_3)
    self.Patron_Status_Label.grid(row = ROW_9, column = COL_3)
    self.Patron_Name_Entry.grid(row = ROW_8, column = COL_4)
    self.Patron_Status.grid(row = ROW_9, column = COL_4)
    
    self.Membership_Label.grid(row = ROW_10, column = COL_2)

    self.Join_Label.grid(row = ROW_11, column = COL_1)
    self.Join_Name_Label.grid(row = ROW_12, column = COL_0)
    self.Join_Status_Label.grid(row = ROW_13, column = COL_0)
    self.Join_Name_Entry.grid(row = ROW_12, column = COL_1)
    self.Join_Status.grid(row = ROW_13, column = COL_1)

    self.Leave_Label.grid(row = ROW_11, column = COL_4)
    self.Leave_Name_Label.grid(row = ROW_12, column = COL_3)
    self.Leave_Status_Label.grid(row = ROW_13, column = COL_3)
    self.Leave_Name_Entry.grid(row = ROW_12, column = COL_4)
    self.Leave_Status.grid(row = ROW_13, column = COL_4)
    
    self.BookC_Label.grid(row = ROW_14, column = COL_2)

    self.AddB_Label.grid(row = ROW_15, column = COL_1)
    self.AddB_Title_Label.grid(row = ROW_16, column = COL_0)
    self.AddB_Author_Label.grid(row = ROW_17, column = COL_0)
    self.AddB_Status_Label.grid(row = ROW_19, column = COL_0)
    self.AddB_Title_Entry.grid(row = ROW_16, column = COL_1)
    self.AddB_Author_Entry.grid(row = ROW_17, column = COL_1)
    self.AddB_Button.grid(row = ROW_18, column = COL_1)
    self.AddB_Status.grid(row = ROW_19, column = COL_1)

    self.RemoveB_Label.grid(row = ROW_15, column = COL_4)
    self.RemoveB_Title_Label.grid(row = ROW_16, column = COL_3)
    self.RemoveB_Author_Label.grid(row = ROW_17, column = COL_3)
    self.RemoveB_Status_Label.grid(row = ROW_19, column = COL_3)
    self.RemoveB_Title_Entry.grid(row = ROW_16, column = COL_4)
    self.RemoveB_Button.grid(row = ROW_18, column = COL_4)
    self.RemoveB_Status.grid(row = ROW_19, column = COL_4)

    self.Check_Patron.grid(row = ROW_20, column = COL_2)
    self.Check_Book.grid(row = ROW_20, column = COL_1)
    self.Check_History.grid(row = ROW_20, column =COL_0)
    

    mainloop()

  def __CheckOutBook(self):
    status = ''
    title = self.CheckB_Title_Entry.get()
    name = self.CheckB_Patron_Entry.get()
    if title and name:
      self.__Clear_Transaction_Status()
      member = self.__library.get_patron(name)
      book = self.__library.get_book(title)
      if book and member:
        book.borrow_me(member)
        status = book.get_transaction_status()
        self.CheckB_Status_Value.set(status)
      else:
        status = self.__library.get_transaction_status()
        self.CheckB_Status_Value.set(status)
      self.__Transaction_History.append(status)

  def __ReturnBook(self):
    status = ''
    title = self.ReturnB_Title_Entry.get()
    if title:
      self.__Clear_Transaction_Status()
      book = self.__library.get_book(title)
      status = self.__library.get_transaction_status()
      self.ReturnB_Status_Value.set(status)
      if book:
        book.return_me()
        status = book.get_transaction_status()
        self.ReturnB_Status_Value.set(status)
      self.__Transaction_History.append(status)

  def __SearchBook(self,event):
    status = ''
    title = self.Book_Title_Entry.get()
    if title:
      self.__Clear_Transaction_Status()
      book = self.__library.get_book(title)
      status = self.__library.get_transaction_status()
      if book:
        status += '\n'+str(book)
      self.Book_Status_Value.set(status)
      self.__Transaction_History.append(status)

  def __SearchPatron(self,event):
    status = ''
    name = self.Patron_Name_Entry.get()
    if name:
      self.__Clear_Transaction_Status()
      patron = self.__library.get_patron(name)
      status = self.__library.get_transaction_status()
      if patron:
        status += '\n'+str(patron)
      self.Patron_Status_Value.set(status)
      self.__Transaction_History.append(status)

  def __Join(self,event):
    status = ''
    name = self.Join_Name_Entry.get()
    if name:
      self.__Clear_Transaction_Status()
      if self.__library.is_member(name):
        status = str(name)+" is already a member"
        self.Join_Status_Value.set(status)
      else:
        newPatron = Patron(name)
        self.__library.add_patron(newPatron)
        status = self.__library.get_transaction_status()
        self.Join_Status_Value.set(status)
      self.__Transaction_History.append(status)

  def __Leave(self,event): 
    status = ''
    name = self.Leave_Name_Entry.get()
    if name:
      self.__Clear_Transaction_Status()
      self.__library.remove_patron(name)
      status = self.__library.get_transaction_status()
      self.Leave_Status_Value.set(status)
      self.__Transaction_History.append(status)
    
  def __AddBook(self):
    status = ''
    title = self.AddB_Title_Entry.get()
    author = self.AddB_Author_Entry.get()
    if title and author:
      self.__Clear_Transaction_Status()
      newBook = Book(title,author)
      self.__library.add_book(newBook)
      status = self.__library.get_transaction_status()
      self.AddB_Status_Value.set(status)
      self.__Transaction_History.append(status)
      

  def __RemoveBook(self): 
    status = ''
    title = self.RemoveB_Title_Entry.get()
    if title:
      self.__Clear_Transaction_Status()
      self.__library.remove_book(title)
      status = self.__library.get_transaction_status()
      self.RemoveB_Status_Value.set(status)
      self.__Transaction_History.append(status)


      #Additional Enhancements
  
  def __Clear_Transaction_Status(self):
    self.CheckB_Status_Value.set('No Transaction')
    self.ReturnB_Status_Value.set('No Transaction')
    self.Book_Status_Value.set('No Transaction')
    self.Patron_Status_Value.set('No Transaction')
    self.Join_Status_Value.set('No Transaction')
    self.Leave_Status_Value.set('No Transaction')
    self.AddB_Status_Value.set('No Transaction')
    self.RemoveB_Status_Value.set('No Transaction')
    if self.__set_transcation:
      self.__Clear_Entry()
    self.__set_transcation = True

  def __Clear_Entry(self): 
    self.CheckB_Title_Entry.delete(0, 'end')
    self.CheckB_Patron_Entry.delete(0, 'end')
    self.ReturnB_Title_Entry.delete(0, 'end')
    self.Book_Title_Entry.delete(0, 'end')
    self.Patron_Name_Entry.delete(0, 'end')
    self.Join_Name_Entry.delete(0, 'end')
    self.Leave_Name_Entry.delete(0, 'end')
    self.AddB_Title_Entry.delete(0, 'end')
    self.AddB_Author_Entry.delete(0, 'end')
    self.RemoveB_Title_Entry.delete(0, 'end')
    

  def __Open_Patron_list(self):
    patron_dict = StringGeneratorForDictionaries(self.__library.get_all_patrons(),'Patrons')
    messagebox.showinfo('List Of Patron',
    patron_dict.get_dict_string() if self.__library.has_members() else "There are no patrons in the library")
    self.Check_Patron.deselect()
  
  def __Open_Book_list(self):
    book_dict = StringGeneratorForDictionaries(self.__library.get_all_books(),'Books')
    messagebox.showinfo('List Of Book',
    book_dict.get_dict_string() if self.__library.has_books() else "There are no books in the library")
    self.Check_Book.deselect()

  def __get_transaction_str(self):
    transaction_str = ''
    for transaction in self.__Transaction_History:
      transaction_str += str(transaction) + '\n\n'
    return transaction_str
  
  def __Open_Transaction_History(self):
    messagebox.showinfo('Transaction History', 
    self.__get_transaction_str() if len(self.__Transaction_History) > 0 else "No Transaction History")
    self.Check_History.deselect()


LibraryGUI()