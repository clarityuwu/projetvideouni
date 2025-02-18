import os
import csv

class Point:
    def __init__(self, x, y, frame):
        self.x = x
        self.y = y
        self.frame = frame
        
def save_csv(filename, points, directory=None):
    try:
        # Sort points by frame
        points.sort(key=lambda point: point.frame)
        
        # Default directory path
        if directory is None:
            directory = os.path.expanduser("~/Documents/video1234")
        
        # Create the directory if it doesn't exist
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        # Define the full file path
        file_path = os.path.join(directory, f"{filename}_video1234.csv")
        
        # Write the points to the CSV file
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['x', 'y', 'frame'])
            for point in points:
                writer.writerow([point.x, point.y, point.frame])
    except PermissionError:
        raise PermissionError("You do not have the rights to write to this directory.")
    except Exception as e:
        raise RuntimeError(f"An error occurred while saving the CSV file: {e}")