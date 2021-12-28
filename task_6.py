# with open('text_4.txt') as file:
#     subj_list = file.readlines()
#     final_dict = {}
#     for subs in subj_list:
#         subjects = subs.split()
#         total_hours = 0
#         for i in subjects[1:]:
#             if i != '-':
#                 nums = '0'
#                 for el in i:
#                     if el.isdigit():
#                         nums += el
#                     else:
#                         break
#                 total_hours += int(nums)
#         final_dict.update({subjects[0]: total_hours})
# print(final_dict)
