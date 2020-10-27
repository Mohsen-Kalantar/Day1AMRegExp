import pickle

with open("dict.ser", "rb") as fic: 
    d=pickle.load(fic)

print(d)
print(d["Nyon"])