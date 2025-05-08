# collection of {key:value}pairs orders , no duplicate

capitals = {"USA": "WASHINTOON",
            "INDIA":"DELHI"}

            
(dir(capitals))
print(capitals.get("USA"))


if capitals.get("JAPAN"):
    print("The capital exist")
 
else:
    print("It do not exist")


capitals.update({"GERMANY": "BERLIN"})
capitals.update({"USA":"DETROIT"})

keys = capitals.keys()
print(keys)

values = capitals.values()
print(values)

items = capitals.items() 
print(items)


for key, value in capitals.items():
    print(f"{keys}: {values}")