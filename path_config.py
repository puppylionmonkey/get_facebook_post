import os
import getpass
import sys

os_system = sys.platform
your_name = getpass.getuser()
# print(getpass.getuser())

# project_path
current_directory = os.path.dirname(os.path.abspath(__file__))
# print(current_directory)
project_path = current_directory + '/'
