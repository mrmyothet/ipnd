# A list of students who can't graduate has been set
# User enters student names
# Return students who are eligible to graduate now
black_list = ["Susan", "John", "Michael","Robert"]

num_students = int(input("Enter number of students: "))
student_list = []
white_list = []

for student in range(num_students):
    prompt = input("Input a name: ")
    while prompt == '':
        prompt = input("Input a non_empty name: ")
    student_list.append(prompt)

for student in student_list:
    if student not in black_list:
        white_list.append(student)
print("These " + str(len(white_list)) + " students are allowed to graduate.")
print(sorted(white_list), sep='\n')
