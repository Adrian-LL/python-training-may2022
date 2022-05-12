# 1. Given the following dictionary:
d = {
  'times': 100,
  'name': 'George',
  'hobbies': ['fishing', 'hiking'],
}
# add key 'friends' to d with ['Andrei', 'Mihai', 'Alina'] as value
d['friends'] = ['Andrei', 'Mihai', 'Alina']
print('Dictionary after adding "friends":', d)

# sort value for key 'friends'
d['friends'].sort()
print('Dictionary after sorting "friends":', d)

# remove 'hiking' from hobbies list
d['hobbies'].remove('hiking')
print('Dictionary after removing hobby:', d)

# remove 'times' key from d
del d['times']
print('Dictionary after removing "times" key:', d)


# 2. Create a dictionary of dictionaries to store the following data
# ({<id>: {"interface": <interface>, "ip": <ip>, ...}, ...}):

d = {
    1: {
        "interface": "Ethernet0",
        "ip": "1.1.1.1",
        "status": "up",
    },
    2: {
        "interface": "Ethernet1",
        "ip": "2.2.2.2",
        "status": "down",
    },
    3: {
        "interface": "Serial0",
        "ip": "3.3.3.3",
        "status": "up",
    },
    4: {
        "interface": "Serial1",
        "ip": "4.4.4.4",
        "status": "up",
    },
}

# Write a python program to find the status of a given id
interface_id = int(input("ID: "))
print(f"Status for interface {interface_id}: {d[interface_id]['status']}")


# Write a python program to find interface and IP of all interfaces which are up
print('The following interfaces are up:')
for val in d.values():
    if val['status'] == 'up':
        print(val["ip"], val["interface"])

# Write a python program to count how many ethernet interfaces there are
count = 0
for val in d.values():
    # if 'ethernet' in val['interface'].lower():
    if val['interface'].startswith('Ethernet'):
        count += 1
print(f'Found {count} Ethernet interfaces.')

# Write a python program to add a new entry to the dictionary
# (auto-increment the id)
new_interface = {
    "interface": "Serial11",
    "ip": "4.4.5.6",
    "status": "down",
}
new_key = max(d.keys()) + 1
d[new_key] = new_interface

print(d)


# 3. Given a list of strings build a dictionary that has each unique string as a
# key and the number of appearances as a value
words = ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']
# Version 1
occurrences = {}
for word in set(words):
    occurrences[word] = words.count(word)
print(occurrences)

# Version 2
occurrences = {}
for word in words:
    if word in occurrences:
        occurrences[word] += 1
    else:
        occurrences[word] = 1
print(occurrences)

# Version 3
occurrences = {}
for word in words:
    occurrences[word] = occurrences.get(word, 0) + 1
print(occurrences)
