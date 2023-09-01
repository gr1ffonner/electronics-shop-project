import csv


with open(
    "/home/danya/code/profi/kate/electronics-shop-project/src/items.csv", "r"
) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(type(row))
