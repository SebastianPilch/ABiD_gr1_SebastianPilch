import pandas

data = {'name': ['Sebastian', 'Tomasz', 'Jan', 'Aleksandra', 'Wiktoria'], 'surname': ['Pilch', 'Nowak', 'Kowalski', 'Wójcik', "Wiśniewski"], 'age': [23, 20, 15, 33, 50], 'sex':['F', 'M', 'M', 'F', 'M']}
df = pandas.DataFrame(data=data)

print('\n\nFunkcja info:\n')
df.info()
print('\n\nFunkcja describe:\n')
print(df.describe())
print('\n\nFunkcja head(3 pierwsze rekordy):\n')
print(df.head(3))
