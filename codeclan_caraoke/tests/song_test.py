import unittest

from classes.song import Song

class TestSong(unittest.TestCase):

    def setUp(self):
        self.song = Song("Graffiti", "Chvrches")

    def test_song_has_title(self):
        self.assertEqual("Graffiti", self.song.title)

    def test_song_has_artist(self):
        self.assertEqual("Chvrches", self.song.artist)