temperatures = [20, 30, 40, 50]
for item in temperatures:
    print(item)


techList = ["Apple", "Google", "Microsoft", "Dell"]
print(techList[1:3])
print(len(techList))

techList.remove("Dell")
print(techList)

techList.insert(2, "Tesla")
print(techList)
print("Apple" in techList)
techList.clear()
print(techList)