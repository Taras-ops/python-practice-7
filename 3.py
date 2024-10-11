names = ["John Doe", "Jane Smith", "Emily Johnson", "Michael Brown"]

initials = [f'{name.split(' ')[0][0]}. {name.split(' ')[1][0]}.' for name in names]
print(initials)
