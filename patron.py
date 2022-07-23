class Patron:
  # Maximum number of books Patron can take out (int)
  MAX_BOOKS_OUT = 3

  STATUS = [" can borrow up to 3 books", " can borrow two more books", \
            " can borrow one more book", " must return book(s)"]

  def __init__(self, name):
    self.__name = name
    self.__num_books_out = 0
    self.__status = self.STATUS[0]

  def can_check_out_books(self):
    return self.__num_books_out < self.MAX_BOOKS_OUT

  def has_checked_out_books(self):
     return self.__num_books_out > 0

  def get_name(self):
    return self.__name

  def get_status(self):
    return self.__name + self.__status

  def get_num_books_out(self):
    return self.__num_books_out

  def __update_status(self):
    self.__status = self.STATUS[self.__num_books_out]

  def increment(self):
    self.__num_books_out +=1
    self.__update_status()

  def decrement(self):
    if self.__num_books_out >= 1:
      self.__num_books_out -=1
      self.__update_status()

  def __lt__(self, other):
    return (not self is other) and (type(self) == type(other)) and \
           self.__name < other.__name

  def __eq__(self, other):
    return self is other or \
           (type(self) == type(other) and \
            self.__name == other.__name and \
            self.__status == other.__status and \
            self.__num_books_out == other.__num_books_out)

  def __str__(self):
    return "{} can borrow up to {} books, {} book(s) out".format(self.__name, self.MAX_BOOKS_OUT - self.__num_books_out, self.__num_books_out)