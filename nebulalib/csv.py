import os
class CSV:
    def __init__(self, file_path):
        self.file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'x') as file:
                pass
            print(f"[WARN] - [CSV-Worker] - File {file_path} created.")
        else:
            print(f"File {file_path} found.")
    def add_row(self, row):
        text = ','.join(row) + '\n'
        with open(self.file_path, 'a') as file:
            file.write(','.join(row) + '\n')