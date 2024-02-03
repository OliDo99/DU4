import re

list = []
ide = True
placeHolder = "PlAcEHoLdEr"
class Person:
    __hiddenBecauseWhyNot = "JustWhy"
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
    def iHaveToDoThis(self):
        self.__hiddenBecauseWhyNot += "?"
class Player(Person):
    def __init__(self,name,surname,number,POS):
        super().__init__(name,surname)
        self.number = number
        self.POS = POS
    def create_list(self):
        return [self.name,self.surname,self.number,self.POS]

    @classmethod
    def define_player(cls,name,surname,number,POS):
        return cls(name,surname,number,POS)

def vypis(number_player,name,surname,number):
    print("##############")
    print(f"PLAYER {number_player}")
    print(f"Name: {name}")
    print(f"Surname: {surname}")
    print(f"Number: {number}")
def input_new():
    print("Daj n ak chces nechecs pridat noveho usera")
    name= input("Zadaj meno: ")
    if name =='n':
        print("Ukoncujem")
        return False

    surname= input("Zadaj priezvisko: ")
    if surname =='n':
        print("Ukoncujem")
        return False

    while True: 
        number= input("Zadaj cislo: ")
        check = number.isnumeric()
        if check == True:
            break
        else:
            print("Len cisla")

    player_model = Player.define_player(name,surname,number,len(list) + 1)
    list.append(player_model.create_list())
    player_model.iHaveToDoThis()
    return True
def writeToFile():
    PLAYER_TEXT_FILE = open("players.txt","w") 
    for value in list:
        if value[0]==placeHolder:
            PLAYER_TEXT_FILE.write(f"-------------{value[1]}-------------\n")
            print("OOOOOK")
        else:
            print(value)
            vypis(value[3],value[0],value[1],value[2])
            PLAYER_TEXT_FILE.write("##############\n")
            PLAYER_TEXT_FILE.write(f"PLAYER {value[3]}\n")
            PLAYER_TEXT_FILE.write(f"Name: {value[0]}\n")
            PLAYER_TEXT_FILE.write(f"Surname: {value[1]}\n")
            PLAYER_TEXT_FILE.write(f"Number: {value[2]}\n")
    PLAYER_TEXT_FILE.close()
def readFiles(num):
    list_of_files = ["ca.txt", "cz.txt", "fi.txt", "se.txt", "sk.txt"]
    
    for value in num:
        new_text_file = open(list_of_files[value],"r+")
        player_model = Player.define_player(placeHolder,list_of_files[value].strip(".txt").upper(),0,0)
        list.append(player_model.create_list())
        player_model.iHaveToDoThis()
        for key in new_text_file:
            if re.search(r'PLAYER +[0-9]',key):   
                POS = key.replace("PLAYER ","").strip()
            if re.search(r'Name: +[a-zA-Z]',key):   
                name = key.replace("Name: ","").strip()
            if re.search(r'Surname: +[a-zA-Z]',key):
                surname = key.replace("Surname: ","").strip()
            if re.search(r'Number: +[0-9]',key):
                number = key.replace("Number: ","").strip()
                player_model = Player.define_player(name,surname,number,POS)
                list.append(player_model.create_list())
                player_model.iHaveToDoThis()
        new_text_file.close()
def workWithFiles():
    file_val = input("Aky file chces spracovat? (v,sk,cz,ca,fi,se)")
    match file_val:
        case "v":
            readFiles([0,1,2,3,4])
        case "sk":
            readFiles([4])
        case "cz":
            readFiles([1])
        case "ca":
            readFiles([0])
        case "fi":
            readFiles([2])
        case "se":
            readFiles([3])
def workWithChange(num,find_val):
    for value in list:
        if value[num] == find_val:
            print(f"Pred zmenou\n {value}")
            val_val = input(f"Po zmene {value[num]} --> ")
            value[num] = val_val
            print(value)
def changeData():
    want_val = input("Chces nieco zmenit? (a/n): ")
    if want_val=='a':
        co_val = input("Meno/Priezvisko/Cislo chces menit? (m/p/c): ")
        find_val = input("Co chces zmenit: ")

        match co_val:
            case 'm':
                workWithChange(0,find_val)
            case 'p':
                workWithChange(1,find_val)
            case 'c':
                workWithChange(2,find_val)

while ide == True:
    ide = input_new()
workWithFiles()
changeData()
writeToFile()