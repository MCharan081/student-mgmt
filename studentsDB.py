import json
FILENAME="students.json"
def load_students():
    try:
        with open(FILENAME,'r') as f:
            return json.load(f)
    except FileNotFoundError:
            return []
    except json.JSONDecodeError:
            return []

def add_student(students):
     sid=input("Enter student ID: ")
     name=input("Enter student name: ")
     age=int(input("Enter student age: "))
     marks=input("Enter student marks: ")
     students.append({
          "id":sid,"name":name,"age":age,"marks":marks
     })
     print("Student added successfully.")

def display_students(students):
    if not students:
        print("No students found.")
        return
    print("\n=== Student Records ===")
    for student in students:
        print(f"ID:{student['id']}, Name: {student['name']}, Age: {student['age']}, Marks: {student['marks']}")

def search_student(students):
    sid=input("Enter student ID:")
    for student in students:
        if student['id']==sid:
            print(f'Found -> {student}')
            return
    print("Student not found")

def update_student(students):
    sid=input("Enter student ID to update:")
    for student in students:
        if student['id']==sid:
            student['name']=input("Enter new name:")
            student['age']=input("Enter new age:")
            student['marks']=input("Enter new marks:")
            print("Student data updated successfully.")
            return
        print("Student not found.")

def delete_student(students):
    sid=input("Enter student ID to delete:")
    for student in students:
        if student['id']==sid:
            students.remove(student)
            print(f'student deleted successfully.')
            return
    print("Student not found.")

def save_students(students):
    with open(FILENAME, "w") as f:

        json.dump(students, f, indent=4)
def main():
    students = load_students()
    print("students:",students)
    while True:
        print("\n=== StudentDB Menu ===")
        print("1. Add student")
        print("2. Display students")  
        print("3. Search student")
        print("4. Update student")
        print("5. Delete student")
        print("6. Save & Exit")

        choice=input("Enter your choice: ")
        if choice=="1":
            add_student(students)
            save_students(students)
        elif choice=="2":
            display_students(students)
        elif choice=="3":
            search_student(students)
        elif choice=="4":
            update_student(students)
        elif choice=="5":
            delete_student(students)
        elif choice=="6":
            save_students(students)
            print("Data saved Exiting...")
            break
        else:
            print("Invalid choice.Please try again.")
main()