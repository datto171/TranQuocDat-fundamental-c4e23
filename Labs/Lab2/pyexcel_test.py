import pyexcel
from collections import OrderedDict



#prepare data
a_list_of_dictionaries = [
    OrderedDict({
        "title": "alo1",
        "number": 11,
    }),
    OrderedDict({
        "title": "alo1",
        "number": 11,
    }),
    OrderedDict({
        "title": "alo1",
        "number": 11,
    }),
]

#List_comprehension

pyexcel.save_as(records=a_list_of_dictionaries, dest_file_name="your_file.xls")
#save file using save_as()