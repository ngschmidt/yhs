#!/usr/bin/python3
# Execution for YAML Hierarchical Search
# Nicholas Schmidt
# 29 Nov 2020

# Command line parsing imports
import argparse

# Import YAMLHierarchicalSearch
from YAMLHierarchicalSearch import YAMLHierarchicalSearch

# Arguments Parsing
parser = argparse.ArgumentParser(description='Process YAML Inputs')
parser.add_argument('-v', '--verbosity', action='count', default=0, help='Output Verbosity')
parser.add_argument('input', help='Data input')
args = parser.parse_args()

yaml_input = YAMLHierarchicalSearch(args.input, args.verbosity)
