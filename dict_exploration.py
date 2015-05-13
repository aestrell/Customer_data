monthNumbers = {'Jan':1, 'Feb':2, 'Mar':3, 'Apr':4, 'May':5}
print monthNumbers
print monthNumbers['Jan']
print monthNumbers.keys()

keys = []
values = []
for month in monthNumbers:
    print month
    keys.append(month)
    values.append(monthNumbers[month])

print keys
print values

a = ['Jan', 'Feb', 3]
for i in a:
    print i

if 'Jan' in monthNumbers:
    monthNumbers['Jan'] = monthNumbers['Jan'] +1
    print 'Value of Jan increased by 1'

else:
    monthNumbers['Jan'] = 1
    print'key Jan created in the Dictionary'
