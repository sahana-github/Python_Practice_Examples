myDict = {
    "fast": "In a quick manner",
    "sahana": "coder",
    "marks": [1, 2, 3, 4],
    "anotherDict": {'sahana': 'player'},
    1: 2
}
print(myDict.keys())
print(type(myDict.keys()))
print(list(myDict.keys()))
print(myDict.values())
print(myDict.items())
print(myDict)
updateDict = {"Lovish": "friend"

              }
myDict.update(updateDict)
print(myDict)
print(myDict.get("sahana1"))
# print(myDict["sahana"])
