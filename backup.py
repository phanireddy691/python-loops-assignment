def clean_names(data):
    backup = data
    backup.append('Cleaned')
    return backup


names = [' Alice', 'Bob ']
new_names = clean_names(names)
print(new_names)
