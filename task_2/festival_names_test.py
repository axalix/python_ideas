# -*- coding: utf-8 -*-

import unittest

import prefixes_aggregator as unique_prefixes


class TestFestivalNames(unittest.TestCase):

    test_str_original = """
Lady Gaga
Lollapalooza 4 Day Pass with Chance The Rapper, The Killers, Muse, Arcade Fire, The xx, Lorde, Blink 182, DJ Snake, Justice and more Tickets (August 3-6)
Lollapalooza Friday Only with The Killers, Blink-182, DJ Snake, Run The Jewels, Ryan Adams, Phantogram, Gramatik and more
Lollapalooza Sunday Only with Arcade Fire, Justice, Big Sean, The Shins, Zeds Dead, Tove Lo, Grouplove, Lil Yachty, Milky Chance and more
Newport Jazz Friday Evening Concert with Trombone Shorty and Rhiannon Giddens
Oakland Athletics at Toronto Blue Jays
Osheaga Music and Arts Festival 3 Day Pass with The Weeknd, Muse, Lorde, Major Lazer, Alabama Shakes and more Tickets (August 4-6)
Osheaga Music and Arts Festival Saturday Only with Muse, Major Lazer, Arkells, Dawes, Father John Misty and more
Osheaga Music and Arts Festival Sunday Only with The Weeknd, Alabama Shakes, Vance Joy, Crystal Castles, Russ, Die Antwoord and more
OVO Fest 2017 - Machel Montano with Bunji Garlin & more
The Meadows Music and Arts Festival 3 Day Pass featuring Jay Z, Red Hot Chili Peppers, Gorillaz, Future, Nas, Bassnectar, Weezer and more Tickets (September 15-17)
The Meadows Music and Arts Festival Friday Only with Jay Z, Run the Jewels, Migos and more
Toronto Blue Jays at Tampa Bay Rays
WayHome Music Festival 3 Day Pass with Imagine Dragons, Frank Ocean, Flume, Justice, Solange and more Tickets (July 28-30)
WayHome Music Festival Friday Only with Flume, Cage the Elephant, Justice and more
WayHome Music Festival Saturday Only with Imagine Dragons, Vance Joy, Solange and more'
"""

    # Lollapalooza
    # Osheaga Music and Arts Festival
    # The Meadows Music and Arts Festival
    # WayHome Music Festival

    def test_text_no_inpit(self):
        self.assertEqual(unique_prefixes.process_text(''), [])

    def test_text_one_line(self):
        self.assertEqual(unique_prefixes.process_text('Christmas Festival'), [])

    def test_text_two_same_line(self):
        line = 'Christmas'
        self.assertEqual(unique_prefixes.process_text(line + "\n" + line), [line])

    def test_text_original(self):
        self.assertEqual(unique_prefixes.process_text(self.test_str_original),
             [
                'Lollapalooza',
                'Osheaga Music and Arts Festival',
                'The Meadows Music and Arts Festival',
                'WayHome Music Festival'
              ])

    def test_text_new_lines_gaps(self):
        test_str = """


Osheaga Music and Arts Festival Saturday AAA


Osheaga Music and Arts Festival Saturday BBB

Osheaga Music and Arts Festival Saturday CCC

Osheaga Music and Arts Festival Sunday AAA

Osheaga Music and Arts Festival Sunday BBB

Osheaga Music and Arts Festival Sunday CCC

            
        """
        print(unique_prefixes.process_text(test_str))
        self.assertEqual(unique_prefixes.process_text(test_str), ['Osheaga Music and Arts Festival'])

    def test_text_increasing_line(self):
        test_str = """
a
a b
a b c
a b c d
a b c d e
"""
        self.assertEqual(unique_prefixes.process_text(test_str), ['a'])

    def test_text_decreasing_line(self):
        test_str = """
a b c d e
a b c d
a b c
a b
a
    """
        self.assertEqual(unique_prefixes.process_text(test_str), ['a'])

    def test_file_missing_handles_ErrorException(self):
        with self.assertRaises(IOError):
            unique_prefixes.process_file('missing_file.txt')

    def test_file(self):
        self.assertEqual(unique_prefixes.process_file('festival_names_test_input.txt'), [
            'Lollapalooza',
            'Osheaga Music and Arts Festival',
            'The Meadows Music and Arts Festival',
            'WayHome Music Festival'
        ])


if __name__ == '__main__':
    unittest.main()
