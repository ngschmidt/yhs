#!/usr/bin/python3
# YAML Hierarchical Search
# Nicholas Schmidt
# 29 Nov 2020

# Imports

# Object Definitions

# Class Definitions
# They're not here to stay, just passing through
class YAMLHierarchicalSearch:

    # Initial Variable Settings
    #
    yhs_data = ""
    yhs_filename = ""

    # And construct with specific endpoint
    def __init__(self, init_data):
        # Set variables from constructor
        self.yhs_data = init_data
        print(self.yhs_data)
    
    @classmethod
    def from_file_name (cls, init_filename):
        "Initialize YAML data from a file"
        try:
            init_data = open(init_filename).readlines()
        except FileNotFoundError:
            print('E1000: File not found!')
        except:
            print('E9999: Unknown Error opening file!')
        else:
            return cls(init_data)
    
    # Functions

    # Print All Class Objects
    def print_class(self):
        print(self.yhs_data)
        print(self.yhs_filename)
