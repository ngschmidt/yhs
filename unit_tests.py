#!/usr/bin/python3
# Execution for YAML Hierarchical Search
# Nicholas Schmidt
# 29 Nov 2020

# OS Iteration for Unit Testing
from os import scandir

# Import YAMLHierarchicalSearch
from YAMLHierarchicalSearch import YAMLHierarchicalSearch

# Unit Test Counters
fail_count = 0
pass_count = 0
total_count = 0

# Iter through tests directory, and run test
for test_case in scandir('unit_tests/'):
    test_unit = YAMLHierarchicalSearch(test_case.path, 0)
    test_unit_result = test_unit.print_class()
    if (test_case.path.startswith('unit_tests/pass')):
        print('SHOULD PASS Case ' + test_case.path + " Result: " + str(test_unit_result))
        if (test_unit_result == True):
            pass_count +=1
        else:
            fail_count +=1
        total_count +=1
    if (test_case.path.startswith('unit_tests/fail')):
        print('SHOULD FAIL Case ' + test_case.path + " Result: " + str(test_unit_result))
        if (test_unit_result == False):
            pass_count +=1
        else:
            fail_count +=1
        total_count +=1

print('Fail Count: ' + str(fail_count))
print('Pass Count: ' + str(pass_count))

# Tryblock to fix the div/0 issue for now
try:
    print("{:.0%}".format(pass_count/total_count) + ' Pass Rate!' )
    print("{:.0%}".format(fail_count/total_count) + ' Fail Rate!' )
except:
    pass
