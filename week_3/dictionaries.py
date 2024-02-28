laptop ={"make":"Dell","color":"black","weight":"1.2kg","windows":"11 pro"}

print (laptop["color"])
print (laptop["make"])
print (laptop["weight"])

for key,value in laptop.items():
    print(key)
    print("/n")
    print(value)
laptop["size"] = "1200mm x 600mm"
print(laptop)