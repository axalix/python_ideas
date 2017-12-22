import re
import codecs
from collections import Counter


class WordsStats:

    def __init__(self):
        self.counter = Counter()
        self.words_number = 0

    def process_file(self, file_name):
        with codecs.open(file_name, encoding='utf-8') as f:
            for line in f:
                self.process_line(line)

    def process_text(self, text):
        for line in text.splitlines():
            self.process_line(line)

    def process_line(self, line):
        if not line:
            return
        for word in re.sub(r'[^\s\w]', ' ', line.lower(), flags=re.UNICODE).split():
            self.counter[word] += 1
            self.words_number += 1

    def total_words(self):
        return self.words_number

    def top_words(self, top_words_number):
        return self.counter.most_common(top_words_number)
