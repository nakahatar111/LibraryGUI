import pickle

DIVIDER = '\n' + ('-' * 70) + '\n'

class StringGeneratorForDictionaries(object):

  def __init__(self, dictionary, dictionary_label):

    self.__dictionary = dictionary
    self.__dictionary_label = dictionary_label
 
  def get_dict_string(self):
    d_list = list(self.__dictionary.values())
    d_list.sort()
    return '\n' + self.__dictionary_label + ':\n' + \
           ('\n'.join(map(str, d_list)))        

class LibraryRecords(object):

  def __init__(self, file_name):
    self.__file_name = file_name

  def load(self):
    library_file_obj = open(self.__file_name, 'rb')
    library = pickle.load(library_file_obj)
    library_file_obj.close()
    return library

  def save(self, library):
    library_file_obj = open(self.__file_name, 'wb')
    pickle.dump(library, library_file_obj)
    library_file_obj.close()
