gradeDict = {'Kelly': 89, 'David': 65, 'Jack': 95, 'Samantha': 78}

print(gradeDict)

print(gradeDict['David'])

gradeDict['David'] = 56

print(gradeDict)

gradeDict['Jessy'] = 92

print(gradeDict)

del gradeDict['David']

print(gradeDict)

gradeDict = {'Kelly': [89, 88],
    'Jack': [95, 87],
    'Sam': [78, 89],
    'Jimmy': [90, 88]}

print(gradeDict)

print(gradeDict['Jack'])