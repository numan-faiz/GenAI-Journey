# looping over data structures ------ dictionaries
student={"name":"numan","age":20,"grade":"A"}
for key in student:
    print(key)
#
# student={"name":"arsal","age":22,"course":"gen AI"}
# for key in student:
#     print(student[key])

# student={"name":"khan","age":24,"grade":"b"}
# for key in student:
#     print(key, ":",student[key])

student_list={"name":"khan","age":24,"grade":"b"},{"name":"zoya","age":29,"grade":"+"},
for student in student_list:
    print(f"name:{student.get('name','')} | grade:{student.get('grade','')} | age:{student.get('age','')}")
