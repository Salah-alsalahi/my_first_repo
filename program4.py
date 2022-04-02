from ast import NotIn
import csv
from msilib import Directory
from operator import truediv
import os
import datetime
from xmlrpc.client import boolean
import glob
from os import listdir

dEuration = []
each0_store = []
paths = []
es = "\\"
path = "courses\math101\L01"
extension = 'csv'

items = os.listdir(path)
for item in items:
    # print(item)
    if item == "classInfo.csv":
        with open(path + es + item) as clsInfo:
            duration = csv.reader(clsInfo)
            for lin in duration:
                dEuration = lin
        # declaration of this class menutes and sessions as tow variables
        this_class_deuration_menutes = int(dEuration[0])
        this_class_deuration_sessions = int(dEuration[1])
        print('#'*10)
        print("section info")
        print(f"menutes is " + str(this_class_deuration_menutes) +
              " and sessions is " + str(this_class_deuration_sessions))
        # print(f"sessions is " + str(this_class_deuration_sessions))
        print('#'*10)

    elif item == "classList.csv":
        classList_from_thisSheet0 = []
        clsList_abcens_list0 = []
        clsList_abcens_order = 0
        with open(path + es + item) as clasList:
            st_classList = csv.reader(clasList)
            for line2 in st_classList:
                classList_from_thisSheet0.append(line2[0])
                clsList_abcens_list0.append(0)
                # clsList_abcens_order += 1
            # print(clsList_abcens_list)#list by the same index of (classList_from_thisSheet) and contain zeros
        clsList_abcens_list = clsList_abcens_list0[1:]
        classList_from_thisSheet = classList_from_thisSheet0[1:]
        student_count = len(classList_from_thisSheet)
        print('as username count ')
        print(f"student in this section is " + str(len(clsList_abcens_list)))
        # print(clsList_abcens_list)
        print(f"student in this section is " + str(student_count))
        print('#'*10)
    else:
        long = []
        login = []
        logout = []
        userName1 = []
        with open(path + es + item) as lec:
            c_reader = csv.reader(lec)
            # lecFileName = []
            # lecFileName.append(str(lec))
            # print(type(lecFileName))
            # print(item)
            for line in c_reader:
                userName1.append(line[1])
                login.append(line[5])
                logout.append(line[4])
                long.append(line[6])
        userName = userName1[1:]
        userCount = len(userName)
        lecName = []
        lecName = item
        lecName1 = lecName[7:15]
        # print(len(lecName))
        abcentShoudBe = student_count-userCount
        print("on day"+lecName1 + str(userCount) +
              " abcens is "+str(abcentShoudBe))
        # print(f"abcent count is"+str(abcentShoudBe))
        # function that returne student abcens
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
        # length_of_username_list = len(userName)
        keys = classList_from_thisSheet
        values = total_menutes
        dictionary = {}
        for key, value in zip(keys, values):
            dictionary[key] = value
        # print(dictionary)
        # length_of_username_list = len(userName)
        keys = userName
        values = total_menutes
        dictionary = {}
        for key, value in zip(keys, values):
            dictionary[key] = value
        htm = 0
        abcentSt = []
        if len(classList_from_thisSheet) == len(userName):
            print("there is no abcens here")
        else:
            # print("some one is abcent and we are going to find him")
            for student in classList_from_thisSheet:
                if student in userName:
                    pass
                    # print(f"{student} is found")
                # now we catch an abcent student -so we should asign its index +1 in the(clsList_abcens_list)
                else:
                    # print(f"{student} is abcent")
                    abcentSt.append(student)
                    stIndex = classList_from_thisSheet.index(student)
                    # print(stIndex)
                    # print(clsList_abcens_list[stIndex])
                    # print(type(stIndex))
                    # print("student " + student +
                    #   " is abcent his index " + str(stIndex))
                    # #now we call list of abcens (clsList_abcens_list) and asign list[index]+=1
                    stIndex_stutus = clsList_abcens_list[stIndex]
                    # print(student+" whos index " + str(stIndex) +
                    #   "his abcens "+str(stIndex_stutus))
                    clsList_abcens_list[stIndex] += 1
                    stIndex_stutus = clsList_abcens_list[stIndex]
keys = classList_from_thisSheet
values = clsList_abcens_list
dictionary_f = {}
for key, value in zip(keys, values):
    dictionary_f[key] = value

print("{" + "\n".join("{!r}: {!r},".format(k, v)
      for k, v in dictionary_f.items()) + "}")

# print(dictionary_f)


#
#
#
# 3

# print(clsList_abcens_list)

#
#
##

# print(student+" whos index " + str(stIndex) +
#   "his abcens "+str(stIndex_stutus))

# stIndex_stutus = clsList_abcens_list[stIndex]
# print(student+" his abcens "+str(stIndex_stutus))
# clsList_abcens_list[stIndex] += 1


#
#
#
#
# print(f"abcent students are {abcentSt}")
# nameWith_abcens_time = classList_from_thisSheet
# valuesForAbce = []
# t = -1
# # print(type(len(nameWith_abcens_time)))
# while t <= len(nameWith_abcens_time):
#     t += 1
#     valuesForAbce.append(total_menutes[t])
# print(len(valuesForAbce))

# for t in nameWith_abcens_time:
#     valuesForAbce.append(total_menutes)
# keys = nameWith_abcens_time
# values = total_menutes
# dictionary1 = {}
# for key, value in zip(keys, values):
#     dictionary[key] = value
