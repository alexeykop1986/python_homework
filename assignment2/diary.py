#Task1
import traceback
def write_to_diary():
    try:
        with open('diary.txt', 'a') as file:
            first_iteration = True
            s=""
            while s!="done for now":
                if first_iteration:
                    s = input("What happened today? ")
                    file.write(s+"\n")
                    first_iteration=False
                else:
                    s = input("What else? ")
                    file.write(s+"\n")
                
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
