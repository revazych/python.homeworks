# translation = {
#     'one': 'один',
#     'two': 'два',
#     'three': 'три',
#     'four': 'четыре'
# }
# with open('text_3.txt') as file, open('translated_text.txt', 'w') as new_text:
#     numerals = file.readlines()
#     for lines in numerals:
#         nums = lines.split()
#         rus_nums = translation.get(nums[0])
#         new_text.write(f'{lines.replace(nums[0], rus_nums)}')
