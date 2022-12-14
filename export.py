import dbconnect
import csv
import json


def tuples_to_dict(tuples_list):
    list_dict = []
    for item in tuples_list:
        ln = item[1]
        fn = item[2]
        ph = item[3]
        dscr = item[4]
        list_dict.append(dict(lastname=ln, firstname=fn, phone=ph, description=dscr))
    exit_dict = {"records": list_dict}
    return exit_dict


def json_export(file_name):
    dict_records = tuples_to_dict(dbconnect.view())
    json_out = json.dumps(dict_records, ensure_ascii=False)
    with open(file_name, 'w') as file:
        file.writelines(json_out)


json_export('out.json')

print(dbconnect.view())


def csv_export(file_name):
    data = dbconnect.view()
    with open(file_name, 'w', newline="") as file:
        csvwriter = csv.writer(file, delimiter = ';')
        csvwriter.writerow(['id','lastname','firstname','phone','description'])
        for item in data:
            csvwriter.writerow(item)

csv_export('out.csv')