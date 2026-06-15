def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="John", age=20, course="Python")