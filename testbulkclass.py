import Bulkclass

d = int(raw_input("Number of dimensions of the problem? 2 or 3"))
if d==2 :
    x = int(raw_input("Number of elements on axis X?"))
    y = int(raw_input("Number of elements on axis Y?"))
    Bulkcard_to_be_write = Bulkclass.Bulklist2D(x,y).write_bulklist()
    with open("Nastran.bdf","a") as bdf:
        for card in Bulkcard_to_be_write:
            bdf.write(card)

elif d==3:
    x = int(raw_input("Number of elements on axis X?"))
    y = int(raw_input("Number of elements on axis Y?"))
    z = int(raw_input("Number of elements on axis Z?"))
    Bulkcard_to_be_write = Bulkclass.Bulklist3D(x, y,z).write_bulklist()
    with open("Nastran.bdf", "a") as bdf:
        for card in Bulkcard_to_be_write:
            bdf.write(card)
else:
    raise NotImplementedError

