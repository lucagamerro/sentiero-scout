from tkinter import *

def gettone():
    global nome, squadriglia, specialita, primo, secondo, terzo
    nomefileprimitivo = nomefilep.get()
    nomefile = nomefileprimitivo + ".csv"
    nome = nomep.get()
    squadriglia = squadrigliap.get()
    specialita = specialitap.get()
    primo = primop.get()
    secondo = secondop.get()
    terzo = terzop.get()
    out_file = open(nomefile, "a")
    out_file.write(nome)
    out_file.write("; ")
    out_file.write(squadriglia)
    out_file.write("; ")
    out_file.write(specialita)
    out_file.write("; ")
    out_file.write(primo)
    out_file.write("; ")
    out_file.write(secondo)
    out_file.write("; ")
    out_file.write(terzo)
    out_file.write("\n")
    out_file.close()



ro = Tk()
ro.geometry("900x1000")
ro.title("IMPEGNI DEL SENTIERO")
a = Label(ro, text="IMPEGNI DEL SENTIERO")
a.pack()
b = Label(ro, text="Nome file:")
b.pack()
nomefilep = Entry(ro, text="")
nomefilep.pack()
c = Label(ro, text="Nome:")
c.pack()
nomep = Entry(ro)
nomep.pack()
d = Label(ro, text="Squadriglia:")
d.pack()
squadrigliap = Entry(ro)
squadrigliap.pack()
e = Label(ro, text="Specialita':")
e.pack()
specialitap = Entry(ro,)
specialitap.pack()
f = Label(ro, text="Impegno per me stesso")
f.pack()
primop = Entry(ro)
primop.pack()
g = Label(ro, text="Impegno per la squadriglia")
g.pack()
secondop = Entry(ro)
secondop.pack()
h = Label(ro, text="Impegno per il reparto")
h.pack()
terzop = Entry(ro)
terzop.pack()
salva = Button(ro, text=" SALVA ", command=gettone)
salva.pack()
ro.mainloop()

