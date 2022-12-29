import csv
with open('diabetes.csv', 'r') as infile, open('output.csv', 'w') as outfile:
    
    rows = list(csv.reader(infile))
    null_count = 0
    for row in rows:
        for cell in row:
            
            if cell == '':
                null_count += 1
        csv.writer(outfile).writerow(row)
print(f'Total number of lines: {len(rows)}')
print(f'Total number of null values: {null_count}')
