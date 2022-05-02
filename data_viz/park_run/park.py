import csv

filename = 'python/data_viz/park_run/park_run.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)