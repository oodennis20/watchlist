import unittest
from models import movie
Movie = movie.Movie

class MovieTest(unittest.TestCase):
    '''
    to test behaviour of the Movie class
    '''
    
    def setUp(self):
        self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://image.tmdb.org/t/p/w500/khsjha27hbs',8.5,129993)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_movie,Movie))
    
if __name__ == '__main__':
    unittest.main()