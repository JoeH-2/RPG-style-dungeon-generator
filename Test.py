import random
from tkinter import *

Map = Tk()
Map.title("Map")
Map.geometry("1000x1000")
Map.grab_set()

MapFrame = LabelFrame(Map, text="Map", width=998, height=998)
MapFrame.grid(padx=1)
MapFrame.grid_propagate(0)


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
    FloorReset(d)
    for i in CurrentFloor:
        print(i)
#-NEXT-ROOM-
    x = 0
    for elm in (CurrentFloor[0]):
        x += 1
        if elm == "E":
            current_row_pos = x-1
            Startx = x-1
    current_column_pos = 0
#-MOVEMENT-FIX WHATEVER THE FUCK IS WRONG HERE!
    for x in range(0,d):
        print("Room: "+str(x+1))
        #Create Room
        Break = False
        for c in range (0,d):#Column Element
            if Break == True:
                break
            for r in range (0,d):#Row Element
                if Break == True:
                    break
                if CurrentFloor[c][r] == "E": #Check for end
                    print("Column: "+str(c))
                    print("Row: "+str(r))
                    actions = ["Back","Forward","Left","Right"]
                    for x in range(0,4):
                        movement = random.choice(actions) #Choose movement
                        print("TestMovement: "+movement)
                    #Back
                        if movement == "Back":
                            if c != 0: #If column isnt first
                                current_row_pos = r
                                current_column_pos = c-1 #Previous Column
                                if CurrentFloor[current_column_pos][current_row_pos] == "_":
                                    print("Accept")
                                    Break = True
                                    break
                                else:
                                    actions.remove(str(movement))
                                    print("Retry: Overlap")
                            else:
                                actions.remove(str(movement))
                                print("Retry: Wall")
                    #Forward
                        if movement == "Forward":
                            if c != d-1: #If column isnt last
                                current_row_pos = r
                                current_column_pos = c+1 #Next Column
                                if CurrentFloor[current_column_pos][current_row_pos] == "_":
                                    print("Accept")
                                    Break = True
                                    break
                                else:
                                    actions.remove(str(movement))
                                    print("Retry: Overlap")
                            else:
                                actions.remove(str(movement))
                                print("Retry: Wall")
                    #Left
                        if movement == "Left":
                            if r != 0: #If row isnt first
                                current_row_pos = r-1 #Previous row
                                current_column_pos = c
                                if CurrentFloor[current_column_pos][current_row_pos] == "_":
                                    print("Accept")
                                    Break = True
                                    break
                                else:
                                    actions.remove(str(movement))
                                    print("Retry: Overlap")
                            else:
                                actions.remove(str(movement))
                                print("Retry: Wall")
                    #Right
                        if movement == "Right":
                            if r != d-1:#If row isnt last
                                current_row_pos = r+1 #Next row
                                current_column_pos = c
                                if CurrentFloor[current_column_pos][current_row_pos] == "_":
                                    print("Accept")
                                    Break = True
                                    break
                                else:
                                    actions.remove(str(movement))
                                    print("Retry: Overlap")
                            else:
                                actions.remove(str(movement))
                                print("Retry: Wall")
                                
                    CurrentFloor[c][r] = "x" #Set previous room to x
                    CurrentFloor[current_column_pos][current_row_pos] = "E" #Set current room to E
                    RoomFrame = LabelFrame(MapFrame, text="", width=100, height=100)
                    RoomFrame.grid(row=c, column=r)
                    RoomFrame.grid_propagate(0)
                    RoomLabel = Label(RoomFrame, text="R", font=12)
                    RoomLabel.grid()
                    RoomFrame = LabelFrame(MapFrame, text="", width=100, height=100)
                    RoomFrame.grid(row=current_column_pos, column=current_row_pos)
                    RoomFrame.grid_propagate(0)
                    EndLabel = Label(RoomFrame, text="E", font=12)
                    EndLabel.grid()

    print('''''')
    CurrentFloor[0][Startx] = "S"
    RoomFrame = LabelFrame(MapFrame, text="", width=100, height=100)
    RoomFrame.grid(row=0, column=Startx)
    RoomFrame.grid_propagate(0)
    StartLabel = Label(RoomFrame, text="S", font=12)
    StartLabel.grid()
    for i in CurrentFloor:
        print(i)

    

MapGenerate(5)
