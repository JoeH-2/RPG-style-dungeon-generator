from tkinter import *
import sqlite3

root = Tk()
root.title("Item Creation")
root.geometry("400x400")

conn = sqlite3.connect('Weapons.db')
c = conn.cursor()

#c.execute("""CREATE TABLE Weapons (
#        Name text,
#        Rarity text,
#        Type text,
#        Attack integer
#        )""")

conn.commit()
conn.close()

#TABLE
conn = sqlite3.connect('Weapons.db')
c = conn.cursor()

c.execute("DELETE from Weapons WHERE Name = ''")
c.execute("DELETE from Weapons WHERE Rarity = ''")
c.execute("DELETE from Weapons WHERE Type = ''")
c.execute("DELETE from Weapons WHERE Attack = ''")

c.execute("SELECT * FROM Weapons")
items = c.fetchall()

for item in items:
    print(item)

conn.commit()
conn.close()

#ADD INTO WEAPONS
def submit(Name,Rarity,Type,Attack):
    conn = sqlite3.connect('Weapons.db')
    c = conn.cursor()

    c.execute("INSERT INTO Weapons VALUES (?,?,?,?)",(Name,Rarity,Type,Attack))
    
    conn.commit()
    conn.close()

    NameInput.delete(0, END)
    RarityInput.delete(0, END)
    TypeInput.delete(0, END)
    AttackInput.delete(0, END)

def delete(Name,Rarity,Type,Attack):
    conn = sqlite3.connect('Weapons.db')
    c = conn.cursor()
    c.execute("DELETE from Weapons WHERE Name=? AND Rarity=? AND Type=? AND Attack=?", (Name,Rarity,Type,Attack))
    c.execute("SELECT * FROM Weapons")
    items = c.fetchall()
    print('''''')
    for item in items:
        print(item)
    conn.commit()
    conn.close()

    NameInput.delete(0, END)
    RarityInput.delete(0, END)
    TypeInput.delete(0, END)
    AttackInput.delete(0, END)



#FIELDS
NameInput = Entry(root, width=30)
NameInput.grid(row=0, column=1, padx=20)

RarityInput = Entry(root, width=30)
RarityInput.grid(row=1, column=1, padx=20)

TypeInput = Entry(root, width=30)
TypeInput.grid(row=2, column=1, padx=20)

AttackInput = Entry(root, width=30)
AttackInput.grid(row=3, column=1, padx=20)

#LABELS
Name_Label = Label(root, text="Name")
Name_Label.grid(row=0, column=0)

Rarity_Label = Label(root, text="Rarity")
Rarity_Label.grid(row=1, column=0)

Type_Label = Label(root, text="Type")
Type_Label.grid(row=2, column=0)

Attack_Label = Label(root, text="Attack")
Attack_Label.grid(row=3, column=0)

#BUTTON
submit.btn = Button(root, text="Confirm", command=lambda: submit(NameInput.get(),RarityInput.get(),TypeInput.get(),AttackInput.get()))
submit.btn.grid(row=4, column=0, columnspan=1, pady=0, padx=0, ipadx=20)

delete.btn = Button(root, text="Delete", command=lambda: delete(NameInput.get(),RarityInput.get(),TypeInput.get(),AttackInput.get()))
delete.btn.grid(row=4, column=0, columnspan=2, pady=10, padx=100, ipadx=20)








root.mainloop()
