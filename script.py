import csv

outfile = open("output.csv", 'w')
outfile_header = "user_id, first_name, last_name, birthts, img_path\n"
outfile.write(outfile_header)
for i in range(99):
    user_id = 1000 + i
    with open("02-src-data/" + str(user_id) + ".csv", "r") as infile:
        reader = csv.reader(infile, delimiter = ',')
        header = next(reader)
        for row in reader:
            first_name = row[0]
            last_name = row[1]
            birth_date = row[2]
            img_path = "02-src-data/" + str(user_id) + ".png"
            line = "{}, {}, {}, {}, {}\n".format(str(user_id), first_name, last_name, birth_date, img_path)
            outfile.write(line)

outfile.close()