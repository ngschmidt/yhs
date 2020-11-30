#!/usr/bin/python3
# YAML Hierarchical Search
# Nicholas Schmidt
# 29 Nov 2020

# Imports
from ruamel.yaml import YAML
from ruamel.yaml import scanner

# Object Definitions

# Class Definitions
# They're not here to stay, just passing through
class YAMLHierarchicalSearch:

    # Initial Variable Settings
    #
    yhs_data = ""
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
            if (self.yhs_verbosity > 0):
                print('I2000: Not found as file, trying as a string...')
            self.yhs_data = init_data
        except scanner.ScannerError as exc:
            print('E1001: YAML Parsing error!')
            if (self.yhs_verbosity > 0):
                print(exc)
        except Exception as exc:
            print('E9999: An unknown error has occurred!')
            if (self.yhs_verbosity > 0):
                print(exc)
                print(type(exc))
                print(exc.args)
        else:
            if self.yhs_verbosity > 0:
                print(self.yhs_data)
        finally:
            if self.yhs_verbosity > 0:
                self.print_class()

    # Functions

    # Print All Class Objects
    def print_class(self):
        if self.yhs_data == "":
            print('No Valid YAML Data found!')
            return False
        else:
            print('YAML Data: ' + str(self.yhs_data))
            print(type(self.yhs_data))
            print('Parsing Verbosity: ' + str(self.yhs_verbosity))
            print('RUAMEL Dump: ' + str(self.yhs_yaml))
            return True
