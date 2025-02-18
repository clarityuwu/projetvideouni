import unittest
import os
import csv
from data import Point, save_csv

class TestSaveCSV(unittest.TestCase):
    def setUp(self):
        # Create Point objects
        self.points = [Point(1, 2, 3), Point(4, 5, 1), Point(7, 8, 2)]
        self.filename = "testfile"
        self.directory = os.path.expanduser("~/Documents/video1234")
        self.file_path = os.path.join(self.directory, f"{self.filename}_video1234.csv")
    
    def tearDown(self):
        # Remove the test file
        if os.path.exists(self.file_path):
            os.remove(self.file_path)
    
    def test_save_csv_creates_directory(self):
        # Remove the directory
        if os.path.exists(self.directory):
            os.rmdir(self.directory)
        
        save_csv(self.filename, self.points)
        
        # Check if directory
        self.assertTrue(os.path.exists(self.directory))
    
    def test_save_csv_creates_file(self):
        save_csv(self.filename, self.points)
        
        # Check if the file
        self.assertTrue(os.path.exists(self.file_path))
    
    def test_save_csv_writes_correct_data(self):
        save_csv(self.filename, self.points)
        
        # Check if the file contains the correct data
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(file)
            rows = list(reader)
        
        # Expected data
        expected_rows = [
            ['x', 'y', 'frame'],
            ['4', '5', '1'],
            ['7', '8', '2'],
            ['1', '2', '3']
        ]
        
        self.assertEqual(rows, expected_rows)

if __name__ == '__main__':
    unittest.main()