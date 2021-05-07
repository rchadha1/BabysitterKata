

hours_dict = {5:[15,12, 24], 6:[15,12, 24], 7:[15,12, 24], 8:[15,12, 24], 9:[15,12, 15], 10:[15,8, 15], 11:[20,8, 15], 12:[20,16, 15], 1:[20,16, 15], 2:[20,16, 15], 3:[20, 16, 15]}
hours = [5,6,7,8,9,10,11, 12, 1,2,3]

hours_index = {}
for i in range(0, len(hours)):
    hours_index[hours[i]] = i

def get_family():
    while(True):
        family = input("Enter Family Name [A, B or C]: ")
        if family.rstrip() not in ["a", "A", "b", "B", "c", "C"]:
            print("You must choose a valid family")
            continue
        

        return family.upper()

def get_start_time():
    while(True):
        start_time = input("Enter Start Time[HH:MM AM/PM]: ")
        time , am_pm = start_time.split(" ")
        hours, minutes = [int(i) for i in time.split(":")]
        if am_pm == "AM" and hours not in [12, 1, 2, 3]:
            print("Must choose a time between 5:00 PM and 4:00 AM")
            continue
        if am_pm == "PM" and hours not in list(range(5,12)):
            print("Must choose a time between 5:00 PM and 4:00 AM")
            continue        

        if minutes > 59 or minutes < 0:
            print("Must chooser a valid time")
            continue

        return str(hours) + ":" + str(minutes)


def get_end_time(start_time):
    #start_Time != end_time
    while(True):
        end_time = input("Enter End Time[HH:MM AM/PM]: ")
        time , am_pm = end_time.split(" ")
        hours, minutes = [int(i) for i in time.split(":")]
        if am_pm == "AM" and hours not in [12, 1, 2, 3, 4]:
            print("Must choose a time between 5:00 PM and 4:00 AM")
            continue
        if am_pm == "PM" and hours not in list(range(5,12)):
            print("Must choose a time between 5:00 PM and 4:00 AM")
            continue
        if hours == 4 and minutes != 0:
            print("Must choose a time between 5:00 PM and 4:00 AM")
            continue

        if minutes > 59 or minutes < 0:
            print("Must choose a valid time")
            continue

        #end_time > start_time
        st_hours, st_min = [int(i) for i in start_time.split(":")]
        if hours == 4:
            pass

        elif hours_index[hours] < hours_index[st_hours]:
            print("End Time cannot be before start_time")
            continue

        elif hours_index[hours] == hours_index[st_hours]:
            if st_min > minutes:
                print("End Time cannot be before start_time")
                continue

            if st_min == minutes:
                print("End Time cannot be equal to start_time")
                continue

        return str(hours) + ":" + str(minutes)


def compute_salary(family, start_time, end_time):
    #hours = compute_number_of_hours(start_time, end_time)
    
    #index represents which value in dictionary we care about
    index = -1

    if family == "A":
        index = 0

    elif family == "B":
        index = 1
    else:
        index = 2

    salary = 0

    start_index = hours_index[int(start_time.split(":")[0])]
    

    end_hour, end_minutes = [int(i) for i in end_time.split(":")]
    if end_minutes > 0:
        end_hour += 1
        end_minues = 0
    

    end_index = hours_index[end_hour -1]


    for i in range(start_index, end_index +1):
        salary += hours_dict[hours[i]][index]

    print(salary)


if __name__ == "__main__":
    family = get_family()
    start_time = get_start_time()
    end_time = get_end_time(start_time)

    print(family, start_time, end_time)

    compute_salary(family, start_time, end_time)

    ## get index of start_time
    ## get index of end time
    ## iterate through start index, end Index
    ## and get salary from dict



##compute_salary("A", "6:45", "6:50")
