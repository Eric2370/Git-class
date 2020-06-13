"""
ICS 31 Lab 9  Problem 1
Driver:  UCI_ID: 52601026  Name: Qiren Feng
"""
class Pet:
    Name = ""
    Age = 0
    Type = ""

def make_pet(name: str, pet_type: str, age: int) -> Pet:
    c = Pet()
    c.Name = name
    c.Age = age
    c.Type = pet_type
    return c

def add_pet(name: str, pet_type: str, age: int, pets: dict):
    c = make_pet(name, pet_type, age)
    pets[name] = c

def load_pets(file_name: str) -> dict:
    f = open(file_name,"r")
    d = {}
    for i in f:
        line = i.split()
        add_pet(line[0], line[1], int(line[2]), d)
    f.close()
    return d

def save_sorted_pets(file_name: str, pets: dict):
    f = open(file_name,"w")
    keys = list(pets.keys())
    keys.sort()
    for i in keys:
        f.write(pets[i].Name + '\t' + pets[i].Type + '\t' + pets[i].Age + '\n')
    f.close()

def main():
    d = load_pets("pets.txt")
    save_sorted_pets("sorted_pets.txt",d)

if __name__ == "__main__":
    main()
        
