from tkinter import *
import random
import time
import sqlite3

#MENU
Menu = Tk()
Menu.title("Menu")
Menu.geometry("480x600")
Menu.grab_set()

#MAP
global NextFloor
NextFloor = []
global CurrentFloor
CurrentFloor = []
global FloorEvents
FloorEvents=[]
global RevealedRooms
RevealedRooms = []
global FoundRooms
FoundRooms = -1

global item
#FUNCTIONS
#-Character-
global hp
hp = 0
global Dex
Dex = 0
global Int
Int = 0
global Wis
Wis = 0
global Cha
Cha = 0

global Armour
Armour = 0

global Attack
Attack = 0

global Gold
Gold = 0

#Inventories
global HelmetsInv
HelmetsInv = []
global ChestInv
ChestInv = []
global LegsInv
LegsInv = []
global BootsInv
BootsInv = []
global HandsInv
HandsInv = []
global WeaponsInv
WeaponsInv = []

#Equipped
global HelmetsEquip
HelmetsEquip = ""
global ChestEquip
ChestEquip = ""
global LegsEquip
LegsEquip = ""
global BootsEquip
BootsEquip = ""
global HandsEquip
HandsEquip = ""
global LHandEquip
LHandEquip = ""
global RHandEquip
RHandEquip = ""

#Equipped ID
global HelmetsEquipID
HelmetsEquiID = ""
global ChestEquipID
ChestEquipID = ""
global LegsEquipID
LegsEquipID = ""
global BootsEquipID
BootsEquipID = ""
global HandsEquipID
HandsEquipID = ""
global LHandEquipID
LHandEquipID = ""
global RHandEquipID
RHandEquipID = ""


#Enable
global Created
Created = 0

global PlayerX
global PlayerY
PlayerX = 0
PlayerY = 0
                    
#-Proficiency-
global ProfPoints
ProfPoints = IntVar()

#MENU
#-Functions-
def Start():
    CharacterCreation = Toplevel()
    CharacterCreation.title("CharacterCreation")
    CharacterCreation.geometry("680x800")
    CharacterCreation.grab_set()
#-Frames-
    #-Stats-
    StatsFrame = LabelFrame(CharacterCreation, text="Stats", width=280, height=450)
    StatsFrame.grid(row=0, column=0, padx=10, pady=10)
    StatsFrame.place(x=10,y=0)
    StatsFrame.grid_propagate(0)
    #-Race-
    RaceFrame = LabelFrame(CharacterCreation, text="Race", width=280, height=250)
    RaceFrame.grid(row=0, column=0, padx=10, pady=10)
    RaceFrame.place(x=390,y=0)
    RaceFrame.grid_propagate(0)
    #-Proficiencies-
    ProFrame = LabelFrame(CharacterCreation, text="Proficiencies", width=660, height=340)
    ProFrame.grid(row=1, column=1, padx=10, pady=10)
    ProFrame.place(x=10,y=450)
    ProFrame.grid_propagate(0)
    #-Name-
    ChrFrame = LabelFrame(CharacterCreation, text="Character", width=280, height=200)
    ChrFrame.grid(row=0, column=2, padx=10, pady=10)
    ChrFrame.place(x=390,y=249)
    ChrFrame.grid_propagate(0)

    ProfPointsLabel = Label(ProFrame, text="Proficiency Points: "+str(ProfPoints.get())).grid(row=0,column=0)

    global hp
    hp = 0
    global Dex
    Dex = 0
    global Int
    Int = 0
    global Wis
    Wis = 0
    global Cha
    Cha = 0

#-Labels-
    #-Roll-Stats-
#--HP--
    def RollStats():
        global hp
        for x in range (0,2):
            dice = random.randint(1,6)
            hp = hp + dice
        hp = hp + 15 #HP min 17 max 27
    #--Dex---
        global Dex
        dice = random.randint(1,6)
        Dex = Dex + dice
        Dex = Dex + 6 #Dex min 7 max 12
    #--Int---
        global Int
        dice = random.randint(1,6)
        Int = Int + dice
        Int = Int + 6 #Int min 7 max 12
    #--Wis---
        global Wis
        dice = random.randint(1,6)
        Wis = Wis + dice
        Wis = Wis + 6 #Wis min 7 max 12
    #--Cha---
        global Cha
        dice = random.randint(1,6)
        Cha = Cha + dice
        Cha = Cha + 6 #Cha min 7 max 12

        HPLabel = Label(StatsFrame, text="HP: "+str(hp)+"\n",anchor="w",width=15)
        HPLabel.grid(row=0)
        HPLabel.config(font=("Courier", 12))

        DexLabel = Label(StatsFrame, text="Dexterity: "+str(Dex)+"\n",anchor="w",width=15)
        DexLabel.grid(row=1)
        DexLabel.config(font=("Courier", 12))

        WisLabel = Label(StatsFrame, text="Wisdom: "+str(Wis)+"\n",anchor="w",width=15)
        WisLabel.grid(row=2)
        WisLabel.config(font=("Courier", 12))

        ChaLabel = Label(StatsFrame, text="Charisma: "+str(Cha)+"\n",anchor="w",width=15)
        ChaLabel.grid(row=3)
        ChaLabel.config(font=("Courier", 12))

    RollStats()



#Proficiency
    ProfBows = IntVar()
    ProfBowsTick = Checkbutton(ProFrame, text="Bows",variable=ProfBows,command=lambda: Check(ProfBows)).grid(row=1,sticky="w")

    ProfPolearms = IntVar()
    ProfPolearmsTick = Checkbutton(ProFrame, text="Polearms",variable=ProfPolearms, command=lambda: Check(ProfPolearms)).grid(sticky="w")

    ProfSwords = IntVar()
    ProfSwordsTick = Checkbutton(ProFrame, text="Swords",variable=ProfSwords, command=lambda: Check(ProfSwords)).grid(sticky="w")

    ProfStaves = IntVar()
    ProfStavesTick = Checkbutton(ProFrame, text="Staves",variable=ProfStaves, command=lambda: Check(ProfStaves)).grid(sticky="w")

    def Check(a):
        state = a.get()
        pp = ProfPoints.get()
        if pp == 0:
            if state == 1:
                a.set(0)
            if state == 0:
                ProfPoints.set(pp+1)
        else:
            if state == 1:
                ProfPoints.set(pp-1)
            if state == 0:
                ProfPoints.set(pp+1)
        ProfPointsLabel = Label(ProFrame, text="Proficiency Points: "+str(ProfPoints.get())).grid(row=0,column=0)

#Choose race
    Race = StringVar()
    Race.get()
    
    def RaceUpdate(value):
        RaceLabel = Label(ChrFrame, text="Race: "+value, width=12, anchor="w").grid(row=4,sticky="w")
        global hp
        hp = 0
        global Dex
        Dex = 0
        global Int
        Int = 0
        global Wis
        Wis = 0
        global Cha
        Cha = 0
        global Created
        if value == "Human":
            ProfPoints.set(4)
            Created = 1
        if value == "Elf":
            hp = -3
            Dex = 2
            Cha = 2
            ProfPoints.set(3)
            Created = 1
        if value == "Dwarf":
            hp = 5
            Dex = -2
            Int = -2
            ProfPoints.set(3)
            Created = 1
        ProfPointsLabel = Label(ProFrame, text="Proficiency Points: "+str(ProfPoints.get())).grid(row=0)
        RollStats()

    Radiobutton(RaceFrame, text="Human", variable=Race, value="Human",width=15, anchor="w",font=("Courier", 12)).grid()
    Radiobutton(RaceFrame, text="Elf", variable=Race, value="Elf",width=15, anchor="w",font=("Courier", 12)).grid()
    Radiobutton(RaceFrame, text="Dwarf", variable=Race, value="Dwarf",width=15, anchor="w",font=("Courier", 12)).grid()

    RaceConfirm = Button(RaceFrame, text="Confirm", command=lambda: RaceUpdate(Race.get()),width=12).grid(row=3,sticky="w")

#Name character
    NameInput = Entry(ChrFrame, width=25)
    NameInput.grid(padx=60,pady=0)
    NameInput.insert(0, "Enter your name: ")

    def NameUpdate():
        NameLabel = Label(ChrFrame, text="Name: "+NameInput.get(),anchor="w",width=25).grid(row=3,sticky="w")

    NameConfirm = Button(ChrFrame, text="Confirm", command=NameUpdate, width=15).grid()

#START ADVENTURE
    def AdventureStart():
        if Created == 1:
            MainWindow = Toplevel()
            MainWindow.title("MainWindow")
            MainWindow.geometry("960x800")

            EventFrame = LabelFrame(MainWindow, text="", width=400, height=400)
            EventFrame.grid(row=0, column=0, padx=10, pady=10)
            EventFrame.grid_propagate(0)

            TextFrame = LabelFrame(MainWindow, text="", width=650, height=370)
            TextFrame.grid(row=1, column=0, padx=10, pady=10)
            TextFrame.place(x=10, y=420)
            TextFrame.grid_propagate(0)

            #-Stats-
            StatsFrame = LabelFrame(MainWindow, text="Stats", width=250, height=408)
            StatsFrame.grid(row=0, column=2, padx=10, pady=10)
            StatsFrame.place(x=415,y=2)
            StatsFrame.grid_propagate(0)

            CharacterFrame = LabelFrame(MainWindow, text="Character", width=280, height=378)
            CharacterFrame.grid(row=1, column=3, padx=10, pady=10)
            CharacterFrame.place(x=670, y=412)
            CharacterFrame.grid_propagate(0)

            MapFrame = LabelFrame(MainWindow, text="Map", width=280, height=250)
            MapFrame.grid(row=0, column=3, padx=10, pady=10)
            MapFrame.place(x=670,y=2)
            MapFrame.grid_propagate(0)

            MapFrame2 = LabelFrame(MapFrame, text="", width=220, height=220)
            MapFrame2.grid(row=0, column=3, padx=10, pady=10)
            MapFrame2.place(x=50,y=0)
            MapFrame2.grid_propagate(0)

            CharacterCreation.destroy()

#MAINWINDOW
    #--Event--
        TextBox = Listbox(TextFrame, width=54, height=22, font=12)
        TextBox.grid()
        def Text(a):
            TextBox.insert(0, str(a))

    #--Stats--
        HPLabel = Label(StatsFrame, text="HP: "+str(hp)+"\n",anchor="w",width=15)
        HPLabel.grid(row=0)
        HPLabel.config(font=("Courier", 12))

        DexLabel = Label(StatsFrame, text="Dexterity: "+str(Dex)+"\n",anchor="w",width=15)
        DexLabel.grid(row=1)
        DexLabel.config(font=("Courier", 12))

        WisLabel = Label(StatsFrame, text="Wisdom: "+str(Wis)+"\n",anchor="w",width=15)
        WisLabel.grid(row=2)
        WisLabel.config(font=("Courier", 12))

        ChaLabel = Label(StatsFrame, text="Charisma: "+str(Cha)+"\n",anchor="w",width=15)
        ChaLabel.grid(row=3)
        ChaLabel.config(font=("Courier", 12))

        ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
        ArmourLabel.grid(row=4)
        ArmourLabel.config(font=("Courier", 12))

        AttackLabel = Label(StatsFrame, text="Attack: "+str(Attack)+"\n",anchor="w",width=15)
        AttackLabel.grid(row=5)
        AttackLabel.config(font=("Courier", 12))

    #--Character--
        def AddItem(t,r): #ERROR = just need to add all rarities for each item
            global itemADD
            if t == "Weapon":
                conn = sqlite3.connect('Weapons.db')
                c = conn.cursor()
                c.execute("SELECT * From Weapons WHERE Rarity =?", (r,))
                items = c.fetchall()
                itemADD = random.choice(items)
                WeaponsInv.append(itemADD)
            if t == "Helmet":
                conn = sqlite3.connect('Armour.db')
                c = conn.cursor()
                c.execute("SELECT * From Armours WHERE Rarity =? AND Type =?", (r,t,))
                items = c.fetchall()
                itemADD = random.choice(items)
                HelmetsInv.append(itemADD)
            if t == "Chest":
                conn = sqlite3.connect('Armour.db')
                c = conn.cursor()
                c.execute("SELECT * From Armours WHERE Rarity =? AND Type =?", (r,t,))
                items = c.fetchall()
                itemADD = random.choice(items)
                ChestInv.append(itemADD)
            if t == "Legs":
                conn = sqlite3.connect('Armour.db')
                c = conn.cursor()
                c.execute("SELECT * From Armours WHERE Rarity =? AND Type =?", (r,t,))
                items = c.fetchall()
                itemADD = random.choice(items)
                LegsInv.append(itemADD)
            if t == "Boots":
                conn = sqlite3.connect('Armour.db')
                c = conn.cursor()
                c.execute("SELECT * From Armours WHERE Rarity =? AND Type =?", (r,t,))
                items = c.fetchall()
                itemADD = random.choice(items)
                BootsInv.append(itemADD)
            if t == "Hands":
                conn = sqlite3.connect('Armour.db')
                c = conn.cursor()
                c.execute("SELECT * From Armours WHERE Rarity =? AND Type =?", (r,t,))
                items = c.fetchall()
                itemADD = random.choice(items)
                HandsInv.append(itemADD)
            if t == "Item":  #FIX INV
                x = random.randint(0,5)
                if x == 0:
                    conn = sqlite3.connect('Weapons.db')
                    c = conn.cursor()
                    c.execute("SELECT * From Weapons WHERE Rarity =?", (r,))
                    items = c.fetchall()
                    itemADD = random.choice(items)
                    WeaponsInv.append(itemADD)
                if x == 1:
                    conn = sqlite3.connect('Armour.db')
                    c = conn.cursor()
                    c.execute("SELECT * From Armours WHERE Rarity =?", (r,))
                    items = c.fetchall()
                    itemADD = random.choice(items)
                    HelmetsInv.append(itemADD)
                if x == 2:
                    conn = sqlite3.connect('Armour.db')
                    c = conn.cursor()
                    c.execute("SELECT * From Armours WHERE Rarity =?", (r,))
                    items = c.fetchall()
                    itemADD = random.choice(items)
                    ChestInv.append(itemADD)
                if x == 3:
                    conn = sqlite3.connect('Armour.db')
                    c = conn.cursor()
                    c.execute("SELECT * From Armours WHERE Rarity =?", (r,))
                    items = c.fetchall()
                    itemADD = random.choice(items)
                    LegsInv.append(itemADD)
                if x == 4:
                    conn = sqlite3.connect('Armour.db')
                    c = conn.cursor()
                    c.execute("SELECT * From Armours WHERE Rarity =?", (r,))
                    items = c.fetchall()
                    itemADD = random.choice(items)
                    BootsInv.append(itemADD)
                if x == 5:
                    conn = sqlite3.connect('Armour.db')
                    c = conn.cursor()
                    c.execute("SELECT * From Armours WHERE Rarity =?", (r,))
                    items = c.fetchall()
                    itemADD = random.choice(items)
                    HandsInv.append(itemADD)
            TextBox.insert(0,("Added: "+itemADD[0]))
            conn.commit()
            conn.close()

        def OpenInv(a):
            global item
            if a == "Helmet":
                Helmets = Toplevel()
                Helmets.title("Head")
                Helmets.geometry("400x400")
                Helmets.grab_set()
                
                HelmetsFrame = LabelFrame(Helmets,width=398,height=398)
                HelmetsFrame.grid(padx=2,pady=2)
                HelmetsFrame.grid_propagate(0)

                HelmetsList = Listbox(HelmetsFrame,width=43,height=20,font=12)
                HelmetsList.grid(padx=2,pady=2)

                for item in HelmetsInv:
                    HelmetsList.insert(END,item[0])

                def EquipHelmet():
                    global HelmetsEquip
                    global HelmetsEquipID
                    if HelmetsList.get(ANCHOR) != "":
                        if HelmetsEquip != "":
                            for item in HelmetsInv:
                                if HelmetsList.get(ANCHOR) == item[0]:
                                    #Unequip
                                    HelmetsList.insert(END,HelmetsEquip)
                                    HelmetsInv.append(HelmetsEquipID)
                                    print("Unequip: "+HelmetsEquip)

                                    global Armour
                                    Armour = Armour - HandsEquipID[3]
                                    ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                                    ArmourLabel.grid(row=4)
                                    ArmourLabel.config(font=("Courier", 12))

                                    #Equip
                                    HelmetsList.delete(ANCHOR)
                                    HelmetsEquip = item[0]
                                    HelmetsEquipID = item
                                    HelmetsInv.remove(item)
                                    print("Equip: "+HelmetsEquip)
                        else:
                            for item in HelmetsInv:
                                if HelmetsList.get(ANCHOR) == item[0]:
                                    print("Equip: "+item[0])
                                    HelmetsList.delete(ANCHOR)
                                    HelmetsEquip = item[0]
                                    HelmetsEquipID = item
                                    HelmetsInv.remove(item)
                        Armour = Armour + HelmetsEquipID[3]
                        ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                        ArmourLabel.grid(row=4)
                        ArmourLabel.config(font=("Courier", 12))
                                    
                EquipButton = Button(HelmetsFrame, text="Equip", command=EquipHelmet, font=12,width=10)
                EquipButton.grid()
                EquipButton.place(x=262,y=350)

            if a == "Chest":
                Chests = Toplevel()
                Chests.title("Chest")
                Chests.geometry("400x400")
                Chests.grab_set()

                ChestsFrame = LabelFrame(Chests,width=398,height=398)
                ChestsFrame.grid(padx=2,pady=2)
                ChestsFrame.grid_propagate(0)

                ChestsList = Listbox(ChestsFrame,width=43,height=20,font=12)
                ChestsList.grid(padx=2,pady=2)
                for item in ChestInv:
                    ChestsList.insert(END,item[0])
                    
                def EquipChest():
                    global ChestEquip
                    global ChestEquipID
                    if ChestsList.get(ANCHOR) != "":
                        if ChestEquip != "":
                            for item in ChestInv:
                                if ChestsList.get(ANCHOR) == item[0]:
                                    #Unequip
                                    print("Unequip: "+item[0])
                                    ChestsList.insert(END,ChestEquip)
                                    ChestInv.append(ChestEquipID)

                                    global Armour
                                    Armour = Armour - HandsEquipID[3]
                                    ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                                    ArmourLabel.grid(row=4)
                                    ArmourLabel.config(font=("Courier", 12))

                                    #Equip
                                    print("Equip: "+item[0])
                                    ChestsList.delete(ANCHOR)
                                    ChestEquip = item[0]
                                    ChestEquipID = item
                                    ChestInv.remove(item)
                        else:
                            for item in ChestInv:
                                if ChestsList.get(ANCHOR) == item[0]:
                                    print("Equip: "+item[0])
                                    ChestsList.delete(ANCHOR)
                                    ChestEquip = item[0]
                                    ChestEquipID = item
                                    ChestInv.remove(item)
                        Armour = Armour + ChestEquipID[3]
                        ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                        ArmourLabel.grid(row=4)
                        ArmourLabel.config(font=("Courier", 12))
                                    
                EquipButton = Button(ChestsFrame, text="Equip", command=EquipChest, font=12,width=10)
                EquipButton.grid()
                EquipButton.place(x=262,y=350)

            if a == "Legs":
                Legs = Toplevel()
                Legs.title("Legs")
                Legs.geometry("400x400")
                Legs.grab_set()

                LegsFrame = LabelFrame(Legs,width=398,height=398)
                LegsFrame.grid(padx=2,pady=2)
                LegsFrame.grid_propagate(0)

                LegsList = Listbox(LegsFrame,width=43,height=20,font=12)
                LegsList.grid(padx=2,pady=2)
                for item in LegsInv:
                    LegsList.insert(END,item[0])
                              
                def EquipLegs():
                    global LegsEquip
                    global LegsEquipID
                    if LegsList.get(ANCHOR) != "":
                        if LegsEquip != "":
                            for item in LegsInv:
                                if LegsList.get(ANCHOR) == item[0]:
                                    #Unequip
                                    print("Unequip: "+item[0])
                                    LegsList.insert(END,LegsEquip)
                                    LegsInv.append(LegsEquipID)
                                    
                                    global Armour
                                    Armour = Armour - HandsEquipID[3]
                                    ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                                    ArmourLabel.grid(row=4)
                                    ArmourLabel.config(font=("Courier", 12))

                                    #Equip
                                    print("Equip: "+item[0])
                                    LegsList.delete(ANCHOR)
                                    LegsEquip = item[0]
                                    LegsEquipID = item
                                    LegsInv.remove(item)
                        else:
                            for item in LegsInv:
                                if LegsList.get(ANCHOR) == item[0]:
                                    print("Equip: "+item[0])
                                    LegsList.delete(ANCHOR)
                                    LegsEquip = item[0]
                                    LegsEquipID = item
                                    LegsInv.remove(item)

                        Armour = Armour + LegsEquipID[3]
                        ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                        ArmourLabel.grid(row=4)
                        ArmourLabel.config(font=("Courier", 12))
                                    
                EquipButton = Button(LegsFrame, text="Equip", command=EquipLegs, font=12,width=10)
                EquipButton.grid()
                EquipButton.place(x=262,y=350)

            if a == "Boots":
                Boots = Toplevel()
                Boots.title("Feet")
                Boots.geometry("400x400")
                Boots.grab_set()

                BootsFrame = LabelFrame(Boots,width=398,height=398)
                BootsFrame.grid(padx=2,pady=2)
                BootsFrame.grid_propagate(0)

                BootsList = Listbox(BootsFrame,width=43,height=20,font=12)
                BootsList.grid(padx=2,pady=2)
                for item in BootsInv:
                    BootsList.insert(END,item[0])

                def EquipBoots():
                    global BootsEquip
                    global BootsEquipID
                    if BootsList.get(ANCHOR) != "":
                        if BootsEquip != "":
                            for item in BootsInv:
                                if BootsList.get(ANCHOR) == item[0]:
                                    #Unequip
                                    print("Unequip: "+item[0])
                                    BootsList.insert(END,BootsEquip)
                                    BootsInv.append(BootsEquipID)

                                    global Armour
                                    Armour = Armour - HandsEquipID[3]
                                    ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                                    ArmourLabel.grid(row=4)
                                    ArmourLabel.config(font=("Courier", 12))

                                    #Equip
                                    print("Equip: "+item[0])
                                    BootsList.delete(ANCHOR)
                                    BootsEquip = item[0]
                                    BootsEquipID = item
                                    BootsInv.remove(item)
                        else:
                            for item in BootsInv:
                                if BootsList.get(ANCHOR) == item[0]:
                                    print("Equip: "+item[0])
                                    BootsList.delete(ANCHOR)
                                    BootsEquip = item[0]
                                    BootsEquipID = item
                                    BootsInv.remove(item)

                        Armour = Armour + BootsEquipID[3]
                        ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                        ArmourLabel.grid(row=4)
                        ArmourLabel.config(font=("Courier", 12))

                EquipButton = Button(BootsFrame, text="Equip", command=EquipBoots, font=12,width=10)
                EquipButton.grid()
                EquipButton.place(x=262,y=350)

            if a == "Hands":
                Hands = Toplevel()
                Hands.title("Hands")
                Hands.geometry("400x400")
                Hands.grab_set()

                HandsFrame = LabelFrame(Hands,width=398,height=398)
                HandsFrame.grid(padx=2,pady=2)
                HandsFrame.grid_propagate(0)

                HandsList = Listbox(HandsFrame,width=43,height=20,font=12)
                HandsList.grid(padx=2,pady=2)
                for item in HandsInv:
                    HandsList.insert(END,item[0])

                def EquipHands():
                    global HandsEquip
                    global HandsEquipID
                    if HandsList.get(ANCHOR) != "":
                        if HandsEquip != "":
                            for item in HandsInv:
                                if HandsList.get(ANCHOR) == item[0]:
                                    #Unequip
                                    print("Unequip: "+item[0])
                                    HandsList.insert(END,HandsEquip)
                                    HandsInv.append(HandsEquipID)

                                    global Armour
                                    Armour = Armour - HandsEquipID[3]
                                    ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                                    ArmourLabel.grid(row=4)
                                    ArmourLabel.config(font=("Courier", 12))

                                    #Equip
                                    print("Equip: "+item[0])
                                    HandsList.delete(ANCHOR)
                                    HandsEquip = item[0]
                                    HandsEquipID = item
                                    HandsInv.remove(item)
                        else:
                            for item in HandsInv:
                                if HandsList.get(ANCHOR) == item[0]:
                                    print("Equip: "+item[0])
                                    HandsList.delete(ANCHOR)
                                    HandsEquip = item[0]
                                    HandsEquipID = item
                                    HandsInv.remove(item)
                        Armour = Armour + HandsEquipID[3]
                        ArmourLabel = Label(StatsFrame, text="Armour: "+str(Armour)+"\n",anchor="w",width=15)
                        ArmourLabel.grid(row=4)
                        ArmourLabel.config(font=("Courier", 12))

                EquipButton = Button(HandsFrame, text="Equip", command=EquipHands, font=12,width=10)
                EquipButton.grid()
                EquipButton.place(x=262,y=350)

            if a == "LHand":
                Weapons = Toplevel()
                Weapons.title("Hands")
                Weapons.geometry("400x400")
                Weapons.grab_set()

                WeaponsFrame = LabelFrame(Weapons,width=398,height=398)
                WeaponsFrame.grid(padx=2,pady=2)
                WeaponsFrame.grid_propagate(0)

                WeaponsList = Listbox(WeaponsFrame,width=43,height=20,font=12)
                WeaponsList.grid(padx=2,pady=2)
                for item in WeaponsInv:
                    WeaponsList.insert(END,item[0])

                def EquipLHand():
                    global LHandEquip
                    global LHandEquipID
                    if WeaponsList.get(ANCHOR) != "":
                        if LHandEquip != "":
                            for item in WeaponsInv:
                                if WeaponsList.get(ANCHOR) == item[0]:
                                    #Unequip
                                    print("Unequip: "+item[0])
                                    WeaponsList.insert(END,LHandEquip)
                                    WeaponsInv.append(LHandEquipID)
                                    
                                    global Attack
                                    Attack = Attack - LHandEquipID[3]
                                    AttackLabel = Label(StatsFrame, text="Attack: "+str(Attack)+"\n",anchor="w",width=15)
                                    AttackLabel.grid(row=5)
                                    AttackLabel.config(font=("Courier", 12))

                                    #Equip
                                    print("Equip: "+item[0])
                                    WeaponsList.delete(ANCHOR)
                                    LHandEquip = item[0]
                                    LHandEquipID = item
                                    WeaponsInv.remove(item)
                        else:
                            for item in WeaponsInv:
                                if WeaponsList.get(ANCHOR) == item[0]:
                                    print("Equip: "+item[0])
                                    WeaponsList.delete(ANCHOR)
                                    LHandEquip = item[0]
                                    LHandEquipID = item
                                    WeaponsInv.remove(item)

                        Attack = Attack + LHandEquipID[3]
                        AttackLabel = Label(StatsFrame, text="Attack: "+str(Attack)+"\n",anchor="w",width=15)
                        AttackLabel.grid(row=5)
                        AttackLabel.config(font=("Courier", 12))

                EquipButton = Button(WeaponsFrame, text="Equip", command=EquipLHand, font=12,width=10)
                EquipButton.grid()
                EquipButton.place(x=262,y=350)

            if a == "RHand":
                Weapons = Toplevel()
                Weapons.title("Hands")
                Weapons.geometry("400x400")
                Weapons.grab_set()

                WeaponsFrame = LabelFrame(Weapons,width=398,height=398)
                WeaponsFrame.grid(padx=2,pady=2)
                WeaponsFrame.grid_propagate(0)

                WeaponsList = Listbox(WeaponsFrame,width=43,height=20,font=12)
                WeaponsList.grid(padx=2,pady=2)
                for item in WeaponsInv:
                    WeaponsList.insert(END,item[0])

                def EquipRHand():
                    global RHandEquip
                    global RHandEquipID
                    if WeaponsList.get(ANCHOR) != "":
                        if RHandEquip != "":
                            for item in WeaponsInv:
                                if WeaponsList.get(ANCHOR) == item[0]:
                                    #Unequip
                                    print("Unequip: "+item[0])
                                    WeaponsList.insert(END,RHandEquip)
                                    WeaponsInv.append(RHandEquipID)

                                    global Attack
                                    Attack = Attack - RHandEquipID[3]
                                    AttackLabel = Label(StatsFrame, text="Attack: "+str(Attack)+"\n",anchor="w",width=15)
                                    AttackLabel.grid(row=5)
                                    AttackLabel.config(font=("Courier", 12))
                                    
                                    #Equip
                                    print("Equip: "+item[0])
                                    WeaponsList.delete(ANCHOR)
                                    RHandEquip = item[0]
                                    RHandEquipID = item
                                    WeaponsInv.remove(item)
                        else:
                            for item in WeaponsInv:
                                if WeaponsList.get(ANCHOR) == item[0]:
                                    print("Equip: "+item[0])
                                    WeaponsList.delete(ANCHOR)
                                    RHandEquip = item[0]
                                    RHandEquipID = item
                                    WeaponsInv.remove(item)

                        Attack = Attack + RHandEquipID[3]
                        AttackLabel = Label(StatsFrame, text="Attack: "+str(Attack)+"\n",anchor="w",width=15)
                        AttackLabel.grid(row=5)
                        AttackLabel.config(font=("Courier", 12))

                EquipButton = Button(WeaponsFrame, text="Equip", command=EquipRHand, font=12,width=10)
                EquipButton.grid()
                EquipButton.place(x=262,y=350)



        #-HEAD-
        HeadSlot = LabelFrame(CharacterFrame,width=50,height=50)
        HeadSlot.grid()
        HeadSlot.place(x=115,y=20)
        HeadSlot.grid_propagate(0)

        HeadSelect = Button(HeadSlot, text="Head", command=lambda: OpenInv("Helmet"), height=2, width=5)
        HeadSelect.grid(pady=2)
        
        #-CHEST-
        ChestSlot = LabelFrame(CharacterFrame,width=50,height=50)
        ChestSlot.grid()
        ChestSlot.place(x=115,y=100)
        ChestSlot.grid_propagate(0)

        ChestSelect = Button(ChestSlot, text="Chest", command=lambda: OpenInv("Chest"), height=2, width=5)
        ChestSelect.grid(pady=2)

        #-LEGS-
        LegsSlot = LabelFrame(CharacterFrame,width=50,height=50)
        LegsSlot.grid()
        LegsSlot.place(x=115,y=200)
        LegsSlot.grid_propagate(0)

        LegsSelect = Button(LegsSlot, text="Legs", command=lambda: OpenInv("Legs"), height=2, width=5)
        LegsSelect.grid(pady=2)

        #-FEET-
        FeetSlot = LabelFrame(CharacterFrame,width=50,height=50)
        FeetSlot.grid()
        FeetSlot.place(x=115,y=290)
        FeetSlot.grid_propagate(0)

        FeetSelect = Button(FeetSlot, text="Feet", command=lambda: OpenInv("Boots"), height=2, width=5)
        FeetSelect.grid(pady=2)

        #-HANDS-
        HandSlot = LabelFrame(CharacterFrame,width=50,height=50)
        HandSlot.grid()
        HandSlot.place(x=180,y=90)
        HandSlot.grid_propagate(0)
        

        HandSelect = Button(HandSlot, text="Hands", command=lambda: OpenInv("Hands"), height=2, width=5)
        HandSelect.grid(pady=2)

        #-LEFT-HAND-
        LHandSlot = LabelFrame(CharacterFrame,width=50,height=50)
        LHandSlot.grid()
        LHandSlot.place(x=50,y=155)

        LHandSelect = Button(LHandSlot, text="Left\n Hand", command=lambda: OpenInv("LHand"), height=2, width=5)
        LHandSelect.grid(pady=2)

        #-RIGHT-HAND-
        RHandSlot = LabelFrame(CharacterFrame,width=50,height=50)
        RHandSlot.grid()
        RHandSlot.place(x=180,y=155)

        RHandSelect = Button(RHandSlot, text="Right\n Hand", command=lambda: OpenInv("RHand"), height=2, width=5)
        RHandSelect.grid(pady=2)
        
        #MAP
        def MapShow():
            MapExpand = Toplevel()
            MapExpand.title("Map")
            MapExpand.geometry("1000x1000")
            MapExpand.grab_set()

            MapExpandFrame = LabelFrame(MapExpand,width=998,height=998)
            MapExpandFrame.grid(padx=2,pady=2)
            MapExpandFrame.grid_propagate(0)
            for c in range(0,len(CurrentFloor)):
                for r in range(0,len(CurrentFloor[c])):
                    RoomFrame = LabelFrame(MapExpandFrame, text="", width=50, height=50)
                    RoomFrame.grid(row=c, column=r)
                    RoomFrame.grid_propagate(0)
                    RoomLabel = Label(RoomFrame, text="", font=0.1)
                    RoomLabel.grid(padx=11,pady=9)
            for x in RevealedRooms:
                c = x[0]
                r = x[1]
                if (CurrentFloor[c][r]) == "x":
                    RoomFrame = LabelFrame(MapExpandFrame, text="", width=50, height=50)
                    RoomFrame.grid(row=c, column=r)
                    RoomFrame.grid_propagate(0)
                    RoomLabel = Label(RoomFrame, text="X", font=0.1)
                    RoomLabel.grid(padx=11,pady=9)
                if (CurrentFloor[c][r]) == "E":
                    RoomFrame = LabelFrame(MapExpandFrame, text="", width=50, height=50)
                    RoomFrame.grid(row=c, column=r)
                    RoomFrame.grid_propagate(0)
                    EndLabel = Label(RoomFrame, text="E", font=0.1)
                    EndLabel.grid(padx=11,pady=9)
                if (CurrentFloor[c][r]) == "S":
                    RoomFrame = LabelFrame(MapExpandFrame, text="", width=50, height=50)
                    RoomFrame.grid(row=0, column=r)
                    RoomFrame.grid_propagate(0)
                    StartLabel = Label(RoomFrame, text="S", font=0.1)
                    StartLabel.grid(padx=11,pady=9)

        MapBtn = Button(MapFrame, text="Expand", command=MapShow, height=2, width=5)
        MapBtn.grid()
        MapBtn.place(x=230,y=189)

        #-GenerateMap-
        def FloorReset(d):
        #-FIRST-
            global CurrentFloor
            CurrentFloor = []
            for x in range(1,d+1):
                CurrentFloor.append([])
            for x in range(1,d+1):
                for i in range(1,d+1):
                    CurrentFloor[x-1].append("_")
            CurrentFloor[0][random.randint(0,d-1)] = "E"
            
        def MapGenerate(d):
            Text("You enter the dungeon")
            FloorReset(d)
        #-NEXT-ROOM-
            x = 0
            for elm in (CurrentFloor[0]):
                x += 1
                if elm == "E":
                    current_row_pos = x-1
                    Startx = x-1
            current_column_pos = 0
        #-MOVEMENT-
            for x in range(0,d):
                #Create Room
                Break = False
                for c in range (0,d):#Column Element
                    if Break == True:
                        break
                    for r in range (0,d):#Row Element
                        if Break == True:
                            break
                        if CurrentFloor[c][r] == "E": #Check for end
                            actions = ["Back","Forward","Left","Right"]
                            for x in range(0,4):
                                movement = random.choice(actions) #Choose movement
                            #Back
                                if movement == "Back":
                                    if c != 0: #If column isnt first
                                        current_row_pos = r
                                        current_column_pos = c-1 #Previous Column
                                        if CurrentFloor[current_column_pos][current_row_pos] == "_":
                                            Break = True
                                            break
                                        else:
                                            actions.remove(str(movement))
                                    else:
                                        actions.remove(str(movement))
                            #Forward
                                if movement == "Forward":
                                    if c != d-1: #If column isnt last
                                        current_row_pos = r
                                        current_column_pos = c+1 #Next Column
                                        if CurrentFloor[current_column_pos][current_row_pos] == "_":
                                            Break = True
                                            break
                                        else:
                                            actions.remove(str(movement))
                                    else:
                                        actions.remove(str(movement))
                            #Left
                                if movement == "Left":
                                    if r != 0: #If row isnt first
                                        current_row_pos = r-1 #Previous row
                                        current_column_pos = c
                                        if CurrentFloor[current_column_pos][current_row_pos] == "_":
                                            Break = True
                                            break
                                        else:
                                            actions.remove(str(movement))
                                    else:
                                        actions.remove(str(movement))
                            #Right
                                if movement == "Right":
                                    if r != d-1:#If row isnt last
                                        current_row_pos = r+1 #Next row
                                        current_column_pos = c
                                        if CurrentFloor[current_column_pos][current_row_pos] == "_":
                                            Break = True
                                            break
                                        else:
                                            actions.remove(str(movement))
                                    else:
                                        actions.remove(str(movement))
                                        
                            CurrentFloor[c][r] = "x" #Set previous room to x
                            CurrentFloor[current_column_pos][current_row_pos] = "E" #Set current room to E
                CurrentFloor[0][Startx] = "S"


        #Adventure


        def LeaveDungeon():
            for x in RevealedRooms:
                c = x[0]
                r = x[1]
                if (CurrentFloor[c][r]) == "E":
                    Text("You leave the dungeon")
                    MapFrame.after(10, AdventureTrigger)
                    for x in range(0,len(RevealedRooms)):
                        RevealedRooms.remove(RevealedRooms[0])
                    for widget in MapFrame2.winfo_children():
                        widget.destroy()
        def AdventureTrigger():
            AdventureButton = Button(EventFrame, text="Adventure", width=55, height=5, command=lambda: AdventureFind())
            AdventureButton.grid()
            AdventureButton.place(x=0,y=310)
            def AdventureFind():
                AdventureButton.destroy()
                AdventureEvents = ["Dungeon"]
                c = random.choice(AdventureEvents)
                if c == "Dungeon":
                    EnterButton = Button(EventFrame, text="Enter", width=55, height=5, command=lambda: EnterDungeon(random.randint(5,20)))
                    EnterButton.grid()
                    EnterButton.place(x=0,y=310)
                    Text("You find a dungeon")         
                    def EnterDungeon(d):
                        EnterButton.destroy()
                        #Enter Dungeon
                        MapGenerate(d)
                        #Forwad
                        ForwardButton = Button(EventFrame, text="South", width=11, command=lambda: Move("Forward"))
                        ForwardButton.grid()
                        ForwardButton.place(x=155,y=369)
                        #Back
                        BackButton = Button(EventFrame, text="North", width=11, command=lambda: Move("Back"))
                        BackButton.grid()
                        BackButton.place(x=155,y=319)
                        #Left
                        LeftButton = Button(EventFrame, text="West", width=11, command=lambda: Move("Left"))
                        LeftButton.grid()
                        LeftButton.place(x=105,y=344)
                        #Right
                        RightButton = Button(EventFrame, text="East", width=11, command=lambda: Move("Right"))
                        RightButton.grid()
                        RightButton.place(x=205,y=344)

                        LeaveButton = Button(EventFrame, text="Leave", width=11, command=LeaveDungeon)
                        LeaveButton.grid()
                        LeaveButton.place(x=307,y=369)

                        Events = ["Treasure","Fight","Empty"]
                        for x in range(0,d):
                            c = random.choice(Events)
                            FloorEvents.append(c)
                        #Find Start
                        for c in range(0,len(CurrentFloor)):
                            for r in range(0,len(CurrentFloor[c])):
                                if CurrentFloor[c][r] == "S":
                                    global PlayerX
                                    global PlayerY
                                    PlayerX = r
                                    PlayerY = c
                                    XLabel = Label(MapFrame, text="x: "+str(PlayerX*10))
                                    XLabel.grid(row=0,sticky="w")
                                    YLabel = Label(MapFrame, text="y: "+str(PlayerY*10))
                                    YLabel.grid(row=1,sticky="w")
                                    RevealedRooms.append([PlayerY,PlayerX])

        def Move(m):
            global PlayerY
            global PlayerX
            global FoundRooms
            global Gold
            if m == "Forward":
                if CurrentFloor[PlayerY+1][PlayerX] != "_":
                    PlayerY = PlayerY + 1
                    Text("You go south")
            if m == "Back":
                if CurrentFloor[PlayerY-1][PlayerX] != "_":
                    PlayerY = PlayerY - 1
                    Text("You go north")
            if m == "Left":
                if CurrentFloor[PlayerY][PlayerX-1] != "_":
                    PlayerX = PlayerX - 1
                    Text("You go west")
            if m == "Right":
                if CurrentFloor[PlayerY][PlayerX+1] != "_":
                    PlayerX = PlayerX + 1
                    Text("You go east")
            x = ([PlayerY,PlayerX]) not in RevealedRooms
            print(x)
            if x == True:
                RevealedRooms.append([PlayerY,PlayerX])
                print(FloorEvents)
                FoundRooms += 1
                print(FoundRooms)
                print(FloorEvents[FoundRooms])
                if FloorEvents[FoundRooms] == "Treasure":
                    Text("You found treasure!")
                    Treasures = ["Gold","Item"]
                    b = random.randint(0,1)
                    c = Treasures[b]
                    print(c)
                    if c == "Gold":
                        x = random.randint(10,100)
                        Text("+"+str(x)+" Gold")
                        Gold = Gold + x
                    elif c == "Item":
                        r = random.randint(0,100)
                        if r < 1: #1%
                            AddItem("Item","Legendary")
                        elif r < 5: #4%
                            AddItem("Item","Epic")
                        elif r < 20:#15%
                            AddItem("Item","Rare")
                        elif r < 50:#30%
                            AddItem("Item","Uncommon")
                        elif r < 100:#50%
                            AddItem("Item","Common")
            #Mark on map
            for x in RevealedRooms:
                c = x[0]
                r = x[1]
                if (CurrentFloor[c][r]) == "x":
                    RoomFrame = LabelFrame(MapFrame2, text="", width=12, height=12)
                    RoomFrame.grid(row=c, column=r)
                    RoomFrame.grid_propagate(0)
                    RoomLabel = Label(RoomFrame, text="X", font=1)
                    RoomLabel.grid(padx=11,pady=9)
                if (CurrentFloor[c][r]) == "E":
                    RoomFrame = LabelFrame(MapFrame2, text="E", width=12, height=12)
                    RoomFrame.grid(row=c, column=r)
                    RoomFrame.grid_propagate(0)
                    EndLabel = Label(RoomFrame, text="E", font=1)
                    EndLabel.grid(padx=11,pady=9)
                if (CurrentFloor[c][r]) == "S":
                    RoomFrame = LabelFrame(MapFrame2, text="", width=12, height=12)
                    RoomFrame.grid(row=0, column=r)
                    RoomFrame.grid_propagate(0)
                    StartLabel = Label(RoomFrame, text="S", font=1)
                    StartLabel.grid(padx=11,pady=9)
            XLabel = Label(MapFrame, text="x: "+str(PlayerX*10))
            XLabel.grid(row=0,sticky="w")
            YLabel = Label(MapFrame, text="y: "+str(PlayerY*10))
            YLabel.grid(row=1,sticky="w")

        MapFrame.after(10, AdventureTrigger)

        #Starting Text and gear
        Text("Your adventure begins!")
        AddItem("Weapon","Common")
        AddItem("Helmet","Common")
        AddItem("Chest","Common")
        AddItem("Legs","Common")
        AddItem("Boots","Common")
        AddItem("Hands","Common")



    AdventureButton = Button(ProFrame, text="Start", command=AdventureStart, padx=50, pady=25).grid(column=10,padx=404,pady=120)

#-Buttons-
#--Menu--
StartButton = Button(Menu, text="Start", command=Start, padx=50, pady=25)
StartButton.place(x=175,y=10)







Menu.mainloop()

