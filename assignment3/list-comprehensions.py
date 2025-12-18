import csv

#Task3

def get_employee_fullname ():
    try:
        with open('..\\csv\\employees.csv', 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            names = [(a[1] + " " + a[2]) for a in reader]  
            return names                    
                
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

def get_employees_with_e(names):
    e_employees = [a for a in names if 'e' in a or 'E' in a]
    return e_employees
    
print('==')
print(get_employee_fullname())
print('==')
print(get_employees_with_e(get_employee_fullname()))