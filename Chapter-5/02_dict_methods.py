d={} # Empty dictionary
marks= {
    "Aarav": 100,
    "Shubham": 56,
    "Rohan": 23
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())
# marks.update({"Aarav":99, "Renuka":100})
# print(marks)

print(marks.get("Aarav")) # Prints None when item doesn't match to the dictionary
print(marks["Aarav"]) # Prints an error when item doesn't match to the dictionary
