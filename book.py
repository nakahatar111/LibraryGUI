class Book:
  # index when book is first created (int)
  NONE = 0
  
  # index when book is loaned successfully (int)
  SUCCESSFUL = 1
  
  # index when patron is put on waiting list (int) 
  WAIT = 2
  
  # index when request for loan is unsuccessful (int)
  UNSUCCESSFUL = 3
  
  # index when book is returned (int)
  RETURNED = 4
  
  # index when request for loan is invalid (int)
  INVALID = 5
  
  TRANS_STATUS = [" No transactions yet",
                  " successfully checked out ",
                  " has been put on waiting list for ",
                  " must return books before taking out ",
                  " has returned ",
                  " has recorded an invalid transaction re:  "]


  def __init__(self, title, author):
    self.__title = title
    self.__author = author
    self.__transaction_status = self.TRANS_STATUS[self.NONE]
    self.__patron = None
    self.__waitlist = list()

  def is_checked_out(self):
    return bool(self.__patron)

  def is_reserved(self):
    return len(self.__waitlist) > 0

  def has_book(self, patron):
    return self.__patron == patron
 
  def is_in_waitlist(self, patron):
    return patron in self.__waitlist

  def __needs_two_part_status(self):
    return "returned" in self.__transaction_status and not "\n" in self.__transaction_status


  def get_title(self):
    return self.__title  

  def get_author(self):
    return self.__author

  def get_patron(self):  
    return self.__patron

  def get_waitlist_str(self):
    waitlist_str = ''
    for name in self.__waitlist:
      waitlist_str += str(name) + '\n'
    return waitlist_str

  def get_transaction_status(self):
   return self.__transaction_status


  def borrow_me(self, patron, previous=""):
    if self.is_checked_out():
      if self.has_book(patron):
        self.__set_transaction_status(patron.get_name(), self.INVALID)
      else:
        if self.is_in_waitlist(patron):
          self.__set_transaction_status(patron.get_name(), self.INVALID)
        else:
          self.__set_transaction_status(patron.get_name(), self.WAIT)
          self.__put_in_wait_list(patron)
    else:
      if patron.can_check_out_books():
        self.__set_transaction_status(patron.get_name(), self.SUCCESSFUL)
        self.__patron = patron
        self.__lend_book(patron)
      else:
        self.__set_transaction_status(patron.get_name(), self.UNSUCCESSFUL)

  def return_me(self): 
    if self.is_checked_out():
      self.__reset_patron()
      self.__set_transaction_status(self.__patron.get_name(),self.RETURNED)
    else:
      self.__set_transaction_status('Unknown',self.INVALID)
    self.__patron = None
    if self.is_reserved():
      self.__lend_to_next_patron()

  def __lend_book(self, patron): 
    patron.increment()

  def __reset_patron(self):                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
    self.__patron.decrement()

  def __lend_to_next_patron(self):
    if not self.is_checked_out():
      if self.is_reserved():
        next_person = self.__waitlist.pop(0)
        self.borrow_me(next_person,self.get_transaction_status()+'\n')

  def __put_in_wait_list(self, patron):
    self.__waitlist.append(patron)

  def __set_transaction_status(self, name, index, previous=''):# trans_status mutator
    if self.__needs_two_part_status() and name != 'Unknown':
      self.__transaction_status += '\n'
    else:
      self.__transaction_status =''
    self.__transaction_status += name + self.TRANS_STATUS[index] + self.__title


  def __lt__(self, other):
    return (not self is other) and (type(self) == type(other)) and \
           self.__title < other.__title

  def __eq__(self, other):
    return self is other or \
           (type(self) == type(other) and self.__title == other.__title)

  def __str__(self):
    if self.is_checked_out():
      patron = "Patron: "+ str(self.__patron) +"\n"
    else:
      patron = "Not checked out\n"
    return "Title: %s \nAuthor: %s \n%sWait list: %s\n" %(self.__title,self.__author,patron, self.get_waitlist_str())