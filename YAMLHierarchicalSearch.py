#!/usr/bin/python3
# YAML Hierarchical Search
# Nicholas Schmidt
# 29 Nov 2020

# Imports
from ruamel.yaml import YAML

# Object Definitions

# Class Definitions
# They're not here to stay, just passing through
class YAMLHierarchicalSearch:

    # Initial Variable Settings
    #
    yhs_data = ""
    yhs_filename = ""
    yhs_verbosity = ""
    yhs_yaml = YAML(typ='safe')

    # And construct with specific endpoint
    def __init__(self, init_data, init_verbosity):
        # Set variables from constructor
        self.yhs_verbosity = init_verbosity
        # Other classes don't have a good way to type data without calling the OS. Let's create a file handle, and use the exception to see if it's a file.
        try:
            self.yhs_data = self.yhs_yaml.load(open(init_data, 'r'))
        except FileNotFoundError:
            self.yhs_data = init_data
        except Exception as exc: 
            print('E9999: An unknown error has occurred!')
            print(exc)
        else:
            if self.yhs_verbosity:
                print(self.yhs_data)

    # Functions

    # Print All Class Objects
    def print_class(self):
        print(self.yhs_data)
        print(self.yhs_filename)
        print(self.yhs_verbosity)
        print(self.yhs_yaml)
