cars ={"make":"Supra","color":"black","horse power":"382","top speed":"282mph"}

print (cars["color"])
print (cars["make"])
print (cars["top speed"])
print(cars["horse power"])

for key,value in cars.items():
    print(key)
    print("/n")
    print(value)