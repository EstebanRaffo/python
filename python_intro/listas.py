temperatures = [20, 30, 40, 50, 60]
temperatures1 = [20, 30, 40, 50]

print("Son iguales ?", temperatures == temperatures1)
print(f"temperatures tiene {len(temperatures)} valores")

for item in temperatures:
    print(item)

temperatures[3] = 60
print(temperatures)

techList = ["Apple", "Google", "Microsoft", "Dell"]
techList.append("Uala")
print(techList[1:3])
print(len(techList))

techList.remove("Dell")
print(techList)

techList.insert(2, "Tesla")
print(techList)
print("Apple" in techList)
techList.clear()
print(techList)