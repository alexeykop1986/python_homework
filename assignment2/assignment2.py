import csv
import traceback
import os
import custom_module
import datetime
from datetime import datetime

#Task2
def read_employees ():
    try:
        with open('..\\csv\\employees.csv', 'r') as file:
            reader = csv.reader(file)
            rows=[]
            dict_for_return={}
            first=True
            
            for row in reader:
                if first:
                    dict_for_return["fields"]=row
                    first=False
                else:
                    rows.append(row)
            dict_for_return["rows"]=rows
            
            return dict_for_return                    
                
    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees=read_employees()

#Task3
def column_index (s):
    return employees["fields"].index(s)

employee_id_column=column_index("employee_id")

#Task4
def first_name (row_number):
    first_name_column = column_index("first_name")
    return employees["rows"][row_number][first_name_column] 
    # this works, but I am not sure that this approach is easy for 
    # understanding when reading the code 
    # maybe it is better to split it to 3 steps?
    # rows = employees["rows"]
    # row = rows[row_number]
    # return row[first_name_column]

#Task5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))

    return matches

#Task6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

#Task7
def sort_by_last_name():
   last_name_column=column_index("last_name")
   employees["rows"].sort(key=lambda row : row[last_name_column])
   return employees["rows"]

#Task8
def employee_dict(s):
    dict={}
    for item in employees["fields"]:
        if item != "employee_id":
            dict[item]=s[column_index(item)]        
    return dict

test_list = sort_by_last_name()
print(test_list[1])
print (employee_dict(test_list[1]))

#Task9
def all_employees_dict():
    dict={}
    for employee in employees["rows"]:
        dict[employee[employee_id_column]] = employee_dict(employee)
    return dict

print (all_employees_dict())

#Task10
def get_this_value():
    return os.getenv("THISVALUE")

#Task11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

print (custom_module.secret)
set_that_secret ("newSecret")
print (custom_module.secret)

#Task12
def read_minutes():
    minutes1 = {}
    minutes2 = {}

    def read_file(file_path):
        try:
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                rows=[]
                dict_for_return={}
                first=True
                
                for row in reader:
                    if first:
                        dict_for_return["fields"]=row
                        first=False
                    else:
                        rows.append(tuple(row))
                dict_for_return["rows"]=rows
                
                return dict_for_return                    
                    
        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
    minutes1 = read_file('..\\csv\\minutes1.csv')
    minutes2 = read_file('..\\csv\\minutes2.csv')

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()

#Task13
def create_minutes_set():
    set1=set(minutes1["rows"])
    set2=set(minutes2["rows"])
    union_set = set1.union(set2)
    return union_set

minutes_set=create_minutes_set()

#Task14
def create_minutes_list():
    minutes_list=list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))
    return minutes_list

minutes_list=create_minutes_list()

#Task15
def write_sorted_list():
    minutes_list = create_minutes_list()
    minutes_list.sort(key = lambda row : row[1], reverse=False) #even though asc is going by default I use reverse=False for training purpose
    minutes_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))

    def write_to_minutes_csv():
        try:
            with open('minutes.csv', 'a') as file:
                file.write(minutes1["fields"])
                file.write("\n")
                for item in minutes_list:
                    file.write(item)
                    file.write("\n")
                    
        except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")
    
    write_to_minutes_csv()
    return minutes_list