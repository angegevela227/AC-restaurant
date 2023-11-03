#creating a empty list 
course_subjects = []
#loop for the subject that user want to input
for subject in range(3):
    course= input('enter course code and subject title:  ')
    #the course code and subject title part will split
    code,subject = course.split(" ", 1)
    course_subject= f"{code }-{subject}"
    course_subjects.append(course_subject)
  
#display the result
print(course_subjects)
