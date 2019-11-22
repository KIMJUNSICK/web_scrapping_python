import csv


def save_to_file(jobs):
    # open the file
    # write something in file you opened
    file = open("jobs.csv", mode="w")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])
    for job in jobs:
        writer.writerow(list(job.values()))  # list ftn transform dict_values to list
    return

