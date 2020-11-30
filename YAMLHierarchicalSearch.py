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
    def __init__(self, init_data):
        # Set variables from constructor
        self.yhs_data = init_data
        print(self.yhs_data)
        print(self.yhs_yaml.load(init_data))

    # Functions

    # Print All Class Objects
    def print_class(self):
        print(self.yhs_data)
        print(self.yhs_filename)
        print(self.yhs_verbosity)
        print(self.yhs_yaml)
