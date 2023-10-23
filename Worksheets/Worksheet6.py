# Question 1
dict1 = {'sc0011': 'Ali Bin Ahmad', 'sc0012': 'Wong Fei Hung', 'sc0013': 'James Purple', 'sc0014': 'Salimah Wahid'}
dict2 = {'it1011': 'Abdus Salam', 'it1012': 'Alex Chung', 'it1013': 'Anastasia Zeus', 'it1014': 'Vihaan Arjun'}
dict3 = {'ai2011': 'Charles Lewin', 'ai2012': 'Apollo Leto', 'ai2013': 'Ciarra Vega', 'ai2014': 'Lara Gould'}
dict4 = {}

for i in dict1, dict2, dict3:
    dict4.update(i)
    
print(dict4)


# Question 2
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d3 = {}

for i, j in d2.items():
    for p, q in d1.items():
        if i == p:
            d3.update({i: j+q})

print(d3)

a
# Question 3
dict_num = {'even': [], 'odd': []}

for i in range(1, 51):
    if i % 2 == 0:
        dict_num["even"].append(i)
    else:
        dict_num["odd"].append(i)

print(dict_num)


# Question 4
my_dict = {'a': 500, 'b': 200, 'c': 1500, 'd': 20, 'x': 1550, 'v': 260}

min_value = min(my_dict.values())
max_value = max(my_dict.values())

print("Min value is:", min_value)
print("Max value is:", max_value)