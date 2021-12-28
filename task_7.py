# import json
#
# firms = {}
# profit_sum = 0
# firm_sum = 0
# with open('text_5.txt') as file:
#     firm_data = file.readlines()
#     for i in firm_data:
#         data = i.split()
#         total_profit = int(data[2]) - int(data[3])
#         firms.update({data[0]: total_profit})
#         if total_profit > 0:
#             profit_sum += total_profit
#             firm_sum += 1
# mean_profit = profit_sum / firm_sum
# total = [firms, {'Mean profit': mean_profit}]
#
# with open('total.json', 'w') as file:
#     json.dump(total, file)
#