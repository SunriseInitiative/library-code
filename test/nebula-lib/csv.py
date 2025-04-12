import os
class CSV:
    def __init__(self, file_path):
        self.file_path = file_path
        self.fileValid = False
        if not os.path.exists(file_path):
            with open(file_path, 'x') as file:
                pass
            if not os.path.exists(self.file_path):
                print(f"[WARN] - [CSV-Worker] - File {self.file_path} created.")
                self.fileValid = True
            else:
                print(f"[ERROR] - [CSV-Worker] - File {self.file_path} created, aborting now")
                self.fileValid = False
                raise NotADirectoryError
        else:
            print(f"File {file_path} found.")
    def add_row(self, row):
        text = ','.join(row) + '\n'
        with open(self.file_path, 'a') as file:
            file.write(','.join(row) + '\n')