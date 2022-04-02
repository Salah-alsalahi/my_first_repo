from ast import NotIn
import csv
from operator import truediv
import os
import datetime
from xmlrpc.client import boolean

deuratioN = []
path = 'courses/math101/L01'
with open(path + '\classInfo.csv') as filed:
    duration = csv.reader(filed)
    next(duration)
    for line in duration:
        deuratioN = line

# declaration of this class menutes and sessions as tow variables
this_class_deuration_menutes = int(deuratioN[0])
this_class_deuration_sessions = int(deuratioN[1])
# print(type(this_class_deuration_menutes))
# print(type(this_class_deuration_sessions))
# print values of deuration menutes and sessions
print(f"this class menutes is " + str(this_class_deuration_menutes))
print(f"this class sessions is " + str(this_class_deuration_sessions))

# userName from sheeet
classList_from_thisSheet0 = []
with open("courses\math101\L01\classList.csv") as filed:
    classList = csv.reader(filed)
    for line in classList:
        classList_from_thisSheet0.append(line[0])
classList_from_thisSheet = classList_from_thisSheet0[1:]
student_count = len(classList_from_thisSheet)
print(f"student count in this section is " + str(student_count))
# print(classList_from_thisSheet)


# lecture
# lists of user name is userName and time as long
long = []
login = []
logout = []
userName1 = []
with open(path + '/Lecture 8-16-21.csv') as file:  # open lecture csv
    c_reader = csv.reader(file)
    for line in c_reader:
        userName1.append(line[1])
        login.append(line[5])
        logout.append(line[4])
        long.append(line[6])
userName = userName1[1:]
userCount = len(userName)
print(f"student count in this lecture is " + str(userCount))
abcentShoudBe = student_count-userCount
print(f"abcent count is"+str(abcentShoudBe))
# function that returne student abcens
h = 1
aa = long[1:]  # store of hour column from csv
hour = []  # store of each student hour
while h < len(aa):  # collection the hours
    a = int(aa[h][0])*60
    hour.append(a)
    h += 1
# extraction menutes filed as list of integers " menutes "
m = 1
menute = []
while m < len(aa):  # collection the menutes
    a1 = int(aa[m][2])*10
    a2 = int(aa[m][3])
    if a2 != ":":
        a3 = a1+a2
        menute.append(a3)
    else:
        menute.append(a1)
    m += 1
# adding hours and menutes as on list containing total minutes for each student
hm = 0
total_menutes = []
while hm < len(hour):
    each_student_menutes = hour[hm] + menute[hm]
    total_menutes.append(each_student_menutes)
    hm += 1
length_of_username_list = len(userName)
keys = userName
values = total_menutes
dictionary = {}
for key, value in zip(keys, values):
    dictionary[key] = value
# print(dictionary)

htm = 0
abcentSt = []
if len(classList_from_thisSheet) == len(userName):
    print("there is no abcens here")
else:
    print("some one is abcent and we are going to find him")
    for student in classList_from_thisSheet:
        if student in userName:
            pass
            # print(f"{student} is found")
        else:
            # print(f"{student} is abcent")
            abcentSt.append(student)
print(f"abcent students are {abcentSt}")
