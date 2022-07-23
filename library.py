from librarymodule import StringGeneratorForDictionaries

class Library(object):
  # index when book not in library
  NOT_IN_LIBRARY = 0

  # index when book added to library
  ADD = 1

  # index when book removed from library
  REMOVE = 2

  # index when patron not a member of library
  NOT_A_MEMBER = 3

  # index when patron becomes member of library
  JOIN = 4

  # index when patron ends membership in library
  LEAVE = 5

  # index when book information is accessed
  ACCESS = 6

  # index when patron information is accessed
  LOOK_UP = 7

  RETURN = 8

  # most reacent transaction with respect to either a book or a patron
  TRANS_STATUS = [" is not in library",
                  " has been added to the library",
                  " has been removed from the library ",
                  " is not a library member ",
                  " has been added as a library member",
                  " has been removed as a library member",
                  " has been accessed", 
                  " member files have been accessed",
                  " must return all books before ending membership"]

  def __init__(self, name):
    self.__name = name
    self.__patrons = {}
    self.__transaction_status = ''
    self.__books = {}

  def get_all_patrons(self):
    return self.__patrons
  
  def get_all_books(self):
    return self.__books
    
  def get_name(self):
    return self.__name   

  def get_transaction_status(self):
    return self.__transaction_status     

  def get_patron(self, name):
    member = None
    if self.is_member(name):
      member = self.__patrons[name]
      self.__set_transaction_status('',name,self.LOOK_UP)
    else:
      self.__set_transaction_status('',name,self.NOT_A_MEMBER)
    return member 

  def get_book(self, title):
    book = None
    if self.in_library(title):
      book = self.__books[title]
      self.__set_transaction_status(title,'',self.ACCESS)
    else:
      self.__set_transaction_status(title,'',self.NOT_IN_LIBRARY)
    return book

    for name in self.__patrons.keys():
      if patron_name == name:
        return True
    return False

  def has_members(self):
    return len(self.__patrons.keys()) > 0

  def in_library(self, title):
    for book in self.__books.keys():
      if title == book:
        return True
    return False

  def has_books(self): 
    return len(self.__books.keys()) > 0

  def add_patron(self, patron):
    name_patron = patron.get_name()
    self.__set_transaction_status('',name_patron,self.JOIN)
    self.__patrons[name_patron] = patron

  def remove_patron(self, name):
    if self.is_member(name):
      if self.get_patron(name).has_checked_out_books():
        self.__set_transaction_status('',name,self.RETURN)
      else:
        self.__patrons.pop(name)
        self.__set_transaction_status('',name,self.LEAVE)
    else:
      self.__set_transaction_status('',name,self.NOT_A_MEMBER)

  def __set_transaction_status(self, title, name, index):
    self.__transaction_status = title + name + self.TRANS_STATUS[index]


  def add_book(self, book):
    title = book.get_title()
    self.__set_transaction_status(title, '', self.ADD)
    self.__books[title] = book

  def remove_book(self, title):
    if self.in_library(title):
      if self.get_book(title).is_checked_out():
        patron = self.get_book(title).get_patron()
        patron.decrement()
      self.__set_transaction_status(title,'',self.REMOVE)
      self.__books.pop(title)
    else:
      self.__set_transaction_status(title,'',self.NOT_IN_LIBRARY)

  def __str__(self):
    patron_dict = StringGeneratorForDictionaries(self.__patrons,'Patrons')
    book_dict = StringGeneratorForDictionaries(self.__books,'Books')
    return "\n{}\n{}\n{}".format(str(self.get_name()),
    book_dict.get_dict_string() if self.has_books() else "There are no books in the library",
    patron_dict.get_dict_string() if self.has_members() else "There are no patrons in the library")