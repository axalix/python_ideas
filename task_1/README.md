Task #1
-----------------------------

Create a simple application that takes a UTF-8 plain-text file as input and outputs:

- Total number of words in text file
- Ten most common words and number of occurrences for each
  

Requirements
-----------------------------
- Python 2.7+
- You can use any of Python's standard libraries: https://docs.python.org/2/library/index.html
- Read the data from a text file
- You application should be run from the command line using a single command. For example:

        python ./word_counter.py input.txt
    
- Please include a test suite demonstrating the correctness of your solution and a README file clearly explaining how to build, run and test your application.
    

Files in a "task_1" directory
-----------------------------
- README.md - this file
- words_stats.py - `WordsStats class` that holds core logic for a task
- word_counter.py - console command implementation 
- word_counter_test.py - unit test for a task
- word_counter_test_input.txt - an example of a text file that can be tried in a console



How to build
-----------------------------

- Be sure you have Python 2.7+ installed
- `cd /path/to/task_1`
- `python ./word_counter.py input.txt`
    
*Note:*  Be sure `python` command is pointing to python2. Alternatively try `puthon2`.


Running the tests
-----------------------------
- `python ./word_counter_test.py`
    

