

hours_dict = {5:[15,12, 24], 6:[15,12, 24], 7:[15,12, 24], 8:[15,12, 24], 9:[15,12, 15], 10:[15,8, 15], 11:[20,8, 15], 12:[20,16, 15], 1:[20,16, 15], 2:[20,16, 15], 3:[20, 16, 15]}
hours = [5,6,7,8,9,10,11, 12, 1,2,3]

hours_index = {}
for i in range(0, len(hours)):
    hours_index[hours[i]] = i

def compute_salary(family, start_time, end_time):
    #hours = compute_number_of_hours(start_time, end_time)
    
    #index represents which value in dictionary we care about
    index = -1

    if family == "A" or "a":
        index = 0

    elif family == "B" or "b":
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


    ## get index of start_time
    ## get index of end time
    ## iterate through start index, end Index
    ## and get salary from dict



compute_salary("A", "6:45", "2:30")
