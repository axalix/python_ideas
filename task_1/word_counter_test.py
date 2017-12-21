# -*- coding: utf-8 -*-

import unittest
from words_stats import WordsStats


class TestWordsStats(unittest.TestCase):
    def setUp(self):
        self.ws = WordsStats()

    def tearDown(self):
        del self.ws

    str_english = """ 
        Hey You! How are you,how have you been?
        How everything has gone?
        You should see that movie"""

    str_english_case_sensitivity = """ 
        apple Apple ApPle
        appLE ApPlE"""

    str_alphanumeric = """ 
        aaa,bbb?ccc,ddd!
        aaa bbb ccc           ddd,,,
        aaa@bbb#ccc$ddd%"""

    str_utf8 = u""" 
                   הוראה הוראה        
        ένα, δυο one! τρία τέσσερα!
        ΈΝΑ ΔΥΟ one  ΤΡΊΑ, ΤΈΣΣΕΡΑ
        one Montréal, MONTRÉAL!!!, MontrÉal?! MontRÉAL...
        הוראה        
        один-one-два
        Два+one-один הוראה
        """

    def test_text_no_inpit(self):
        self.assertEqual(self.ws.total_words(), 0)
        self.assertEqual(self.ws.top_words(100), [])

    def test_text_latin(self):
        self.ws.process_text(self.str_english)
        self.assertEqual(self.ws.total_words(), 18)
        self.assertEqual(dict(self.ws.top_words(2)), {'you': 4, 'how': 3})

    def test_text_blank_string(self):
        self.ws.process_text("\n\n\n\n\n\n\n\n\n\n")
        self.assertEqual(self.ws.total_words(), 0)
        self.assertEqual(self.ws.top_words(100), [])

    def test_text_blank_string_header(self):
        self.ws.process_text("\n\n\n\n\n\n\n\n\n\naaa aaa aaa")
        self.assertEqual(self.ws.total_words(), 3)
        self.assertEqual(dict(self.ws.top_words(1)), {'aaa': 3})

    def test_text_case_sensitivity(self):
        self.ws.process_text(self.str_english_case_sensitivity)
        self.assertEqual(self.ws.total_words(), 5)
        self.assertEqual(dict(self.ws.top_words(100)), {'apple': 5})

    def test_text_non_alphanumeric(self):
        self.ws.process_text(self.str_alphanumeric)
        self.assertEqual(self.ws.total_words(), 12)
        self.assertEqual(dict(self.ws.top_words(100)),
                         {
                             'aaa': 3,
                             'bbb': 3,
                             'ccc': 3,
                             'ddd': 3
                         })

    def test_text_utf8(self):
        self.ws.process_text(self.str_utf8)
        self.assertEqual(self.ws.total_words(), 25)
        self.assertEqual(dict(self.ws.top_words(100)),
                         {
                             u'one': 5,
                             u'montréal': 4,
                             u'הוראה': 4,
                             u'ένα': 2,
                             u'δυο': 2,
                             u'τρία': 2,
                             u'τέσσερα': 2,
                             u'один': 2,
                             u'два': 2
                         })

    def test_text_splitting(self):
        self.ws.process_text('ap!ple app?le')
        self.assertEqual(dict(self.ws.top_words(100)),
                         {
                             'ap': 1,
                             'ple': 1,
                             'app': 1,
                             'le': 1
                         })

    def test_text_top_words_boundary(self):
        self.ws.process_text(' '.join(map(str, range(159))))
        self.assertEqual(len(self.ws.top_words(94)), 94)

    def test_file_missing_handles_ErrorException(self):
        with self.assertRaises(IOError):
            self.ws.process_file('missing_file.txt')

    def test_file_utf8(self):
        self.ws.process_file('word_counter_test_input.txt')
        self.assertEqual(self.ws.total_words(), 17)
        self.assertEqual(dict(self.ws.top_words(100)),
                         {
                             u'one': 5,
                             u'ένα': 2,
                             u'δυο': 2,
                             u'τρία': 2,
                             u'τέσσερα': 2,
                             u'один': 2,
                             u'два': 2
                         })


if __name__ == '__main__':
    unittest.main()
