''' 
Create a function that takes an attendance record (array of bools) and returns true if the student should be suspended. They should be suspended if:
- they missed 3 or more days in a row
- they missed 7 days total  
'''

def AttendanceRecord(record):
    # if sum(record) >= 7:
    #     return True
    missed = 0
    consec = 0
    for day in record:
        while record[day] == False: #does this work?
            consec += 1
        if consec >= 3:
            return True
        if record[day] == False:
            missed += 1
    if missed >= 7:
        return True
