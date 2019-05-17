import re

with open('access_log_Jul95', 'r') as file:
    step = 1
    for lines_of_file in file.readlines():
        pattern = r".+01/Jul/1995:00:[0-10]:[0-60].+NASA.+"
        if re.search(pattern, lines_of_file):
            step = step + 1
print("Amount of request : " + str(step-1))

