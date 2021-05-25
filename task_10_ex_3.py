import csv


def get_top_performers(file_path, number_of_top_students=5):
    with open(file_path) as file:
        fcsv = csv.reader(file)
        db = sorted(list(fcsv)[1:], key=lambda x: float(x[2]), reverse=True)
    return [x[0] for x in db][:number_of_top_students]


def write_students_age_desc(file_path, output_file):
    with open(file_path) as file:
        fcsv = csv.reader(file)
        first = next(fcsv)
        db = sorted(list(fcsv), key=lambda x: x[1], reverse=True)
    with open(output_file, 'w', newline="") as file:
        fcsv2 = csv.writer(file)
        fcsv2.writerow(first)
        fcsv2.writerows(db)
