# author @ DAMILOLA OKAFOR
# This file is used to perform unit tests specifically
# on the dataset namely media and news files

import unittest
import jsonParser


class MyTestCase(unittest.TestCase):
    # Test the news file name is correct for the news.csv
    def test_newfilename(self):
        result = jsonParser.Data_file.name
        self.assertEqual(result, 'news.csv')

    # Test the media file name is correct for the media.csv
    def test_mediafilename(self):
        result = jsonParser.Media_file.name
        self.assertEqual(result, 'media.csv')

    # Checking the byline for the first item in the news array dataset
    def test_newsfilebyline(self):
        result = jsonParser.News_data[0]['byline']
        self.assertEqual(result, 'By Dani Blum')

    # Checking the title for the 19th item in the news array dataset
    def test_newsfiletitle(self):
        result = jsonParser.News_data[19]['title']
        self.assertEqual(result, 'George Booth, New Yorker Cartoonist of Sublime Zaniness, Dies at 96')

    # Checking the copyright for the first item in the media array dataset
    def test_mediafilecopyright(self):
        result = jsonParser.Media_data[0]['copyright']
        self.assertEqual(result, 'Kathy Willens/Associated Press')

    # Checking the url for the 10th item in the news array dataset
    def test_tenthItemInNewsData(self):
        result = jsonParser.News_data[10]['url']
        self.assertEqual(result, "https://www.nytimes.com/article/crowd-crush-safety.html")
