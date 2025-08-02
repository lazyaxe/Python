#Similar to List Comprehension
keys_or_names = ["Patrick", "Pro", "Itachi", "Aura"]
values_or_grades=["A", "S", "A+", "F"]
dictionary_or_dataset = {k:v for k,v in zip(keys_or_names, values_or_grades) if v.isalpha() and k.isalpha()}
print(dictionary_or_dataset)