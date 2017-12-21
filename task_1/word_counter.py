# Create a simple application that takes a UTF-8 plain-text file as input and outputs:
#
# Total number of words in text file
# Ten most common words and number of occurrences for each
#
# Requirements:
# Python 2.7+
# You can use any of Python's standard libraries: https://docs.python.org/2/library/index.html
# Read the data from a text file
# You application should be run from the command line using a single command. For example:
# python ./word_counter.py input.txt

import sys
from words_stats import WordsStats


TOP_WORDS_NUMBER = 10

try:
    file_name_arg = str(sys.argv[1])
except:
    print "You are missing a file name as input \n"\
          'Example: python ./word_counter.py input.txt'
    sys.exit(1)

ws = WordsStats()
try:
    ws.process_file(file_name_arg)
except IOError:
    print 'File not found, please use this format python ./word_counter.py input.txt'
    exit(1)

#------ Output

print str(ws.total_words()) + ' words found (in total, including duplicates)'

print 'Most common ones:'
top_words_number_arg = int(sys.argv[2] if len(sys.argv) > 2 else TOP_WORDS_NUMBER)
for el in ws.top_words(top_words_number_arg):
    print el[0] + ' => ' + str(el[1])
