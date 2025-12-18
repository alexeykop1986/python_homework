# Task1
def hello():
    return 'Hello!'

# Task2
def greet(name):
    return "Hello, " + name + "!"

# Task3
def calc (a,b,operation="multiply"):
    try:
        if operation == "add":
            return a+b
        elif operation == "subtract":
            return a-b
        elif operation=="multiply":
            return a*b
        elif operation=="divide":
            return a/b
        elif operation=="modulo":
            return a%b
        elif operation=="int_divide":
            return a//b
        elif operation=="power":
            return a**b
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't " + operation +" those values!"
    except Exception as e:
        return "Opps, something is wrong"
    
# Task4
def data_type_conversion(a, operation):
    try:
        if operation=="float":
            return float(a)
        elif operation=="str":
            return str(a)
        elif operation=="int":
            return int(a)
    except Exception as e:
        return "You can't convert " + a + " into a " + operation + "."
    
# Task5
def grade(*args):
    try:
        av=sum(args)/len(args)
        if av >= 90:
            return "A"
        elif av >= 80:
            return "B"
        elif av >= 70:
            return "C"
        elif av >= 60:
            return "D"
        elif av < 60:
            return "F"
    except TypeError:
        return "Invalid data was provided."
    
# Task6
def repeat(a,t):
    b=""
    for i in range(t):
        b=b+a
    return b

# Task7
def student_scores(typeOfScore,**kwargs):
    if typeOfScore == "best":
        bestScore = 0
        name=""
        for key, value in kwargs.items():
            if value > bestScore:
                bestScore = value
                name=key
        return name
    elif typeOfScore == "mean":
        sum = 0
        for key, value in kwargs.items():
            sum=sum+value
        return sum/len(kwargs)
    else:
        return ""

# Task8
def titleize(s):
    words=s.split()
    result =""
    for i, word in enumerate(words):
        if i == 0:
            result=result+word.capitalize()+ " "
        elif i == len(words)-1:
            result=result+word.capitalize()
        elif word not in ("a", "on", "an", "the", "of", "and", "is", "in"):
            result=result+word.capitalize()+ " "
        else:
            result=result+word+ " "
    return result

#Task9
def hangman(secret,guess):
    result =""
    for ch in secret:
        if ch in guess:
            result = result + ch
        else:
            result = result + "_"
    return result

# Task10
def pig_latin(s):
    result=""
    words=s.split()
    for word in words:
        newWord = word
        if word[0] in "aeiou":
            newWord = newWord + "ay" 
        else:
            for ch in word:
                if ch not in "aeio":
                    newWord = newWord[1:] + ch
                else:
                    newWord = newWord + "ay"
                    break
        result=result+newWord+" "
    return result.strip()