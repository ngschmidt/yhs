#!/usr/bin/python3
# YAML Hierarchical Search
# Nicholas Schmidt
# 29 Nov 2020

# Imports
from ruamel.yaml import YAML
from ruamel.yaml import scanner
import yaml

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
        if isinstance(self.yhs_data, dict):
            print('YAML Data: ' + str(self.yhs_data))
            print(type(self.yhs_data))
            print('Parsing Verbosity: ' + str(self.yhs_verbosity))
            print('RUAMEL Dump: ' + str(self.yhs_yaml))
            return True            
        else:
            print('No Valid YAML Data found! type is ' + str(type(self.yhs_data)))
            return False


    # Find Elements hat match names provided
    def find_element_by_string(self, search_string, search_obj=None):
        if not search_obj:
            search_obj = self.yhs_data
        if isinstance(search_obj, (dict)):
            for i in search_obj:
                if search_string in str(search_obj[i]):
                    print(yaml.dump(search_obj[i]))
                if isinstance(search_obj[i], (dict, list)):
                    self.find_element_by_string(search_string, search_obj[i])
                if self.yhs_verbosity:
                    print('Found a ' + str(type(search_obj[i])))
                else:
                    pass
        elif isinstance(search_obj, (list)):
            for i in search_obj:
                if search_string in str(i):
                    print(yaml.dump(i))
                if isinstance(i, (dict, list)):
                    self.find_element_by_string(search_string, i)   
                if self.yhs_verbosity:
                    print('Found a ' + str(type(i)))
        else:
            pass
