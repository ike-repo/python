# Write a Python program to sort a list of tuples using Lambda.
subject_marks = [('English', 88), ('Science', 90), ('Maths', 57), ('Social sciences', 85)]
subject_marks.sort(key = lambda x: x[1], reverse = True)
print(subject_marks)