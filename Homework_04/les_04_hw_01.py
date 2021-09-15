from sys import argv

script_name, output, rate, bonus = argv

print()
print('script name: ', script_name)
print('output in hours: ', output)
print('rate per hour: ', rate)
print('bonus: ', bonus)
print(f'\nwages = {(int(output) * int(rate)) + int(bonus)}')
