all_data = [['John', 'Emily', 'Michael', 'Mary','Steven'],
            ['Maria', 'Juan', 'Javier', 'Natalia','Pilar']]
names_of_interest = []
for names in all_data:
    enough_es = [name for name in names if name.count('e') >= 2]
    names_of_interest.append(enough_es)
print(names_of_interest)
