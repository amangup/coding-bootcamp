import pprint

def get_records(filename, seperator="\t"):
    records = []
    with open(filename) as data_file:
        for line in data_file:
            row = line.split(seperator)
            records.append(tuple(row))

    headers = {}
    for i, item in enumerate(records[0]):
        headers[item] = i
    return headers, records[1:]

def main():
    staff_headers, staff_records = get_records("ca_staff_data_2016.csv")
    student_headers, student_records = get_records("ca_student_data_2016.csv")

    num_teachers = 0
    num_male_teachers = 0
    num_female_teachers = 0
    county_ages = {}
    for record in staff_records:
        is_teacher = float(record[staff_headers["FTE Teaching"]]) > 0
        gender = record[staff_headers["GenderCode"]]
        if is_teacher:
            num_teachers += 1

            if gender == "M":
                num_male_teachers += 1
            elif gender == "F":
                num_female_teachers += 1

            county = record[staff_headers["CountyName"]].strip()
            age = int(record[staff_headers["Age"]])

            ages_list = county_ages.get(county, [])
            ages_list.append(age)
            county_ages[county] = ages_list

    print (county_ages['ALPINE'])

    county_age_stats = {}
    for key, value in county_ages.items():
        value.sort()
        county_age_stats[key] = (value[0], value[int(len(value) / 2)],
                                 value[-1], len(value))

    num_students = 0
    for record in student_records:
        num_students += int(record[student_headers["ENR_TOTAL"]])

    print("Number of teachers: %s" % num_teachers)
    print("Number of students: %s" % num_students)
    print("California has %.2f percent female teachers" %
          ((num_female_teachers / num_teachers) * 100))
    print("Teacher age statistics in every county (min, median, max):")
    pprint.pprint(county_age_stats)


if __name__ == "__main__":
    main()
