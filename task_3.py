# with open('text_2.txt') as file:
#     employ_list = file.readlines()
#     employees = {}
#     salary_sum = 0
#     for strings in employ_list:
#         emp_data = strings.split()
#         employees.update({emp_data[0]: float(emp_data[1])})
#         salary_sum += float(emp_data[1])
# mean_salary = salary_sum / len(employees)
# print(f'Средний оклад {mean_salary}')
#
# for key, value in employees.items():
#     if value < 20000:
#         print(f'Работник {key} имеет оклад менее 20000')
