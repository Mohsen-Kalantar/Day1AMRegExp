import pickle

d={"Nyon":[2.3, 4.5, 8.7], "Lausanne":[2.1, 6.5, 8.5] , "Geneve":[3.1, 9.5, 10.5]}

with open("dict.ser", "wb") as fic: 
    pickle.dump(d,fic)
