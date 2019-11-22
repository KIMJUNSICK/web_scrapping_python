import csv


def save_to_file():
    file = open("jobs.csv", mode="w")
    # mode="w" is meant that only can write something in file, not read
    # when re-open the file, existing contents disappear
    print(file)
    return

