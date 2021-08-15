
import openpyxl
import pandas
from getNames import getNamesFromExcelFiles

student_names = getNamesFromExcelFiles()

students_grades_dic = {}

for student in student_names:
    grades = []
    print(f'enter <Arabic> grade for "{student}" = ')
    grades.append(int(input()))
    print(f'enter <Math> grade for "{student}" = ')
    grades.append(int(input()))
    print(f'enter <English> grade for "{student}" = ')
    grades.append(int(input()))
    students_grades_dic[student] = grades
    print("----------------------------------")


dataframe = pandas.DataFrame.from_dict(students_grades_dic, orient="index",columns=["Arabic", "Math", "English"])
dataframe["AVG"] = dataframe.mean(axis=1)

max_avg = dataframe["AVG"].max()
x = dataframe[dataframe.AVG == max_avg].index
index = ""
for i in x:
    index = i
dataframe.to_excel("classgrades.xlsx")

wb = openpyxl.load_workbook(filename = 'classgrades.xlsx')
active_sheet = wb.active
active_sheet["A1"] = "Names"
active_sheet["G5"] = "Top of class= "
active_sheet["H5"] = index
wb.save("classgrades.xlsx")