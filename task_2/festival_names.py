# Given the following list of event names, find the unique festival names from the list.
# A festival is identified as the longest number of matching characters between consecutive lines where the numbers of lines is greater than one.
# For example, the expected output of the provided data is:

import sys
import prefixes_aggregator as unique_prefixes


try:
    file_name_arg = str(sys.argv[1])
except:
    print "You are missing a file name as input \n" \
          'Example: python ./festival_names.py input.txt'
    sys.exit(1)


try:
    unique_names = unique_prefixes.process_file(file_name_arg)
except IOError:
    print 'File not found, please use this format python ./word_counter.py input.txt'
    exit(1)

#------ Output

print 'Unique festival names:'
for name in unique_names:
     print name
