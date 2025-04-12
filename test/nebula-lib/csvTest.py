import csv

csv = csv.CSV("test.csv")
csv.add_row(["Name", "Age"])

with open("test.csv", "a") as f:
    f.write("gyatt")

    f.write("\nJohn,30")