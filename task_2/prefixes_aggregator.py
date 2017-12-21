import re
import codecs


def _shared_prefix_words(str1, str2):
    space_idx = 0
    s1 = min(str1, str2)
    s2 = max(str1, str2)

    for i, c in enumerate(s1):
        if c.isspace():
            space_idx = i
        if c != s2[i]:
            return s1[:space_idx].rstrip()

    if s1 == s2 or s2[len(s1)].isspace():
        return s1.rstrip()
    else:
        return s1[:space_idx].rstrip()


def aggregator(gen):
    pattern = ''
    prev_line = ''

    for prev_line in gen:
        prev_line = prev_line.strip()
        if prev_line:
            break

    for line in gen:
        line = line.strip()
        if not line:
            continue

        if not _shared_prefix_words(pattern, line):
            if pattern:
                yield pattern
            pattern = _shared_prefix_words(prev_line, line)
        prev_line = line

    if pattern:
        yield _shared_prefix_words(pattern, prev_line)


def process_file(file_name):
    r = []
    with codecs.open(file_name, encoding='utf-8') as f:
        for prefix in aggregator(f):
            r.append(prefix)
    return r


def process_text(text):
    r = []
    for prefix in aggregator(iter(text.splitlines())):
        r.append(prefix)
    return r
