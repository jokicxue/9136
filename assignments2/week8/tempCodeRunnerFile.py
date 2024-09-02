choose = int(input("Choose a table index (to display):\n"))
table = [
    (['Grade Code', 'Grade', 'Family Grade', 'Lower Mark', 'Upper Mark'], [['HD', 'High Distinction', 'Hardly Decent', '80', '100'], ['D', 'Distinction', 'Disappointing', '70', '79'], ['C', 'Credit', 'Catastrophic', '60', '69'], ['P', 'Pass', 'Permanent failure', '50', '59'], ['N', 'Fail', 'Never show your face again', '0', '49']]),
    (['Student ID', 'First Name', 'Last Name', 'Grade Code'], [['798154', 'Brynhildr', 'Blakeley', 'N'], ['134789', 'Felix', 'Li', 'N'], ['798951', 'Paityn', 'Summers', 'P'], ['465120', 'Turnus', 'Elliot', 'C'], ['963245', 'Alysia', 'Jervis', 'D'], ['469120', 'Muhammad', 'Saad', 'HD']]), 
    (['First Name', 'Joining year', 'Rabbit'], [['Brynhildr', '2022', 'Rabbit_1'], ['Turnus', '2023', 'Rabbit_2'], ['Jamaluddin', '2022', 'Rabbit_5']]),
    (['Rabbit', 'Birth year', 'Favorite treat'], [['Rabbit_1', '2022', 'Carrots'], ['Rabbit_2', '2023', 'Celery'], ['Rabbit_3', '2023', 'Broccoli'], ['Rabbit_4', '2024', 'Cabbage'], ['Rabbit_5', '2022', 'Lettuce']])]


if choose in range(len(table)):
    print(table[choose][1])

else:
    print("Incorrect table index. Try again.")

print(range(len(table)))