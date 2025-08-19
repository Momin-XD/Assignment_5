# Task 1
# Checking student's marks using simple dict functions

dict={"Rahul":78,"Mohit":80,"Chutki":90,"Nobita":36}
name=input("Enter Student's name: ")
val=dict.get(name)
if val is not None:
    print(f"{name}'s marks: {val}")
else:
    print("Student not found")