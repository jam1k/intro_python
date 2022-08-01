# Write your solution here
import math
student_number = float (input ("How many students on the course? "))
group_size = float (input ("Desired group size? "))
result = math.ceil(student_number / group_size)
print (f"Number of groups formed: {result}")