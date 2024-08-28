import os
from dotenv import load_dotenv
load_dotenv()

"""
UNIT: CONTANTS
~~~~~~~~~~~~~~
    In this block of code we are stored all users nickname and their a work group type.
    Also, bellow the are stored the Template of Bot Messege 
"""
GROUP_ALL = list(map(os.getenv, ["KPOLYA_POLYA", "COSMOS", "SUN", 
                                 "HANYI", "MARAD", "TEN", "YARE", "SKI", 
                                 "LISHY", "ALPHABET", "NAS", "BOM", "ANYAN"]))
GROUP_DESIGNER = list(map(os.getenv, ["SUN", "COSMOS", "HANYI", 
                                      "ALPHABET", "NAS", "BOM", "STREPIS"]))
GROUP_PHOTORATHER = list(map(os.getenv, ["SKI","COSMOS", "POLI", "ALIAS", "TEN"]))
GROUP_COPYRIGTHER = list(map(os.getenv, ["SKI","KPOLYA_POLYA","YARE", "ANYAN", "NIKI"]))
GROUP_ME = list(map(os.getenv, ['NIKI']))


GROUPS = {
    'ALL': GROUP_ALL,
    'DESIGNER': GROUP_DESIGNER,
    'PHOTORATHER': GROUP_PHOTORATHER,
    'COPYRIGTHER': GROUP_COPYRIGTHER,
    "ME": GROUP_ME
}

MSG_GROUP_NOT_EXIST = 'Группа {group_name} не существует'
MSG_USER_ADDED = '{user} добавлен в группу {group_name}'
MSG_NO_ACCESS = 'У вас нет доступа к этому боту'


"""
UNIt: LOGGER
~~~~~~~~~~~~
"""

METHODS_LOGGER_NAME, METHODS_LOGGER_FILE = 'METHODS', 'methods.log'
