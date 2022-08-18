name = input('Enter name: ')
name_list = name.split()

initials = ''

for name in name_list:
    initials += (name[0].upper() + '.')

print([initials])
