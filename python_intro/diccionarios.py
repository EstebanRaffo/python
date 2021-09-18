fruits = {
    'banana': 0.49,
    'orange': 1.5,
    'apple': 1.09
}
for fruit in fruits:
    print(f"{fruit}: {fruits[fruit]}")

print(fruits)
fruits['banana'] = 2.60
print(fruits)
print(fruits['apple'])
fruits['melon'] = 3
print(fruits)

for fruit in fruits:
    print(f"{fruit}: {fruits[fruit]}")

fruits.pop('banana')
print(fruits)

for clave, valor in fruits.items():
    print(clave, valor)

del(fruits['apple'])

print(fruits)

