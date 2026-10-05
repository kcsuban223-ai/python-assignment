print("===========================================")
print("STUDENT RESULT MANAGEMENT SYSTEM")
print("===========================================")
print("1. Enter Student Details")
print("2. Calculate Result")
print("3. Display Result")
print("4. Exit")

print("===========================================")
print("STUDENT RESULT MANAGEMENT SYSTEM")
print("===========================================")
name=input("Enter your name: ")
roll_number=int(input("Enter your roll number: "))
print("Student Name :", name)
print("Roll number:", roll_number)
py=int(input("Enter your marks in python"))
math=int(input("Enter your marks in Mathematics"))
english=int(input("Enter your marks in English"))
db=int(input("Enter your marks in Database"))
com=int(input("Enter your marks in Computer"))
def calculate_total(a,b,c,d,e):
    total=a+b+c+d+e
    return total
total=calculate_total(py,math,english,db,com)
def calculate_percentage(total):
    per=total/5
    return per
percentage=calculate_percentage(total)
def calculate_grade(percentage):
    if(percentage<50):
        return ("F")
    elif(percentage<60):
        return("D")
    elif(percentage<70):
        return("C")
    elif(percentage<80):
        return("B")
    elif(percentage<101):
        return("A")
def check_result(a,b,c,d,e):
    if(a>40 and b>40 and c>40 and d>40 and e>40):
        return ("Pass")
    elif(a<40 or b<40 or c<40 or d<40 or e<40):
        return("Fail")
print("Student Name: ",name)
print("Roll No. ",roll_number)
print("Python: ",py)
print("Mathematics: ",math)
print("English: ",english)
print("Database: ", db)
print("Computer:", com)
print("Total: ",total)
print("Percentage:", percentage)
print("Grade: ",calculate_grade(percentage))
print("Result:", check_result(py,math,english,db,com))


