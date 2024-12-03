inputText = open('input.txt')
reports = []

lines = inputText.read().splitlines()

for line in lines:
    levels = line.split(' ')
    reports.append(levels)

#A report is valid if each of the entries is in ascending or descending order, and
#they only increase/decrease by 1-3
def checkReport(report):
    current = int(report[0])
    second = int(report[1])
    increasing=False
    if second > current:
        increasing=True
    else:
        increasing=False
    counter = 1
    while counter < len(report):
        #First ensure that we have 1-3 more:
        difference = abs(int(report[counter]) - current)
        if (difference < 1) or (difference > 3):
            break
        if increasing:
            if int(report[counter]) < current:
                break
        else:
            if int(report[counter]) > current:
                break
        current = int(report[counter])
        counter+=1
    if counter == len(report):
        return True
    else:
        return False

safe = 0
for report in reports:
    if (checkReport(report)):
        safe+=1
    else:
        #Try all combinations of attempting to make it safe. (For part 2)
        counter = 0
        while counter < len(report):
            currentReport = report.copy()
            currentReport.pop(counter)
            if (checkReport(currentReport)):
                safe+=1
                break
            counter+=1

print(safe)