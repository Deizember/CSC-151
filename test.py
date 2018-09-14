class student:
    def __init__(self,firstName,lastName,age,idnumber,course,gender):
        self.age = age
        self.idnumber = idnumber
        self.firstName = firstName
        self.lastName = lastName
        self.course = course
        self.gender = gender
        
def checker (idnumber):
    f = open ('info.csv','r')
    counter = 0
    for line in f:
        currentline = line.split (",")
        if (currentline [0] == idnumber):
            counter = 1
    f.close ()
    if(counter == 1):
        return True
    else:
        return False        
        
def add (firstName, lastName, idnumber, age, gender, course):
    f = open ('info.csv','a')
    
    f.write(idnumber + ",")
    f.write (firstName + ",")
    f.write (lastName + ",")
    f.write (age + ",")
    f.write (gender + ",")
    f.write (course + "\n")
    f.close ()
    
def search (idnumber):
    if (checker (idnumber) == False):
        print ("\nERROR: Id number does not exist")
        pass        
    else:
        f = open ('info.csv','r')
        for line in f:
            currentline = line.split (",")
            if (currentline [0] == idnumber):
                print ('ID number:'+currentline[0])
                print ('Firstname: '+currentline [1])
                print('Lastname: '+currentline [2])
                print('Age: '+currentline [3])
                print ('Gender: '+currentline [4])
                print ('Course: '+currentline [5])
        f.close ()
    
def update(idnumber):
    if (checker (idnumber) == False):
        print ("\nERROR: Id number does not exist")
        pass
    else:
        storage  = []
        f = open ('info.csv','r')
        choice = input ('what  you want to update?\n(idnumber/firstname/lastname/age/gender/course): ')
        for line in f:       
            currentline = line.split(",")
            if(currentline [0] == idnumber):
                    if (choice == 'idnumber'):
                        newID= input ('Enter the new ID number: ')
                        storage.append(newID+ ","+currentline[1]+","+currentline [2]+","+currentline [3]+","+currentline [4]+","+currentline [5])
                    elif (choice == 'firstname'):
                        newfirstname = input ('Enter the new firstname: ')
                        storage.append(currentline [0]+ ","+newfirstname+","+currentline [2]+","+currentline [3]+","+currentline [4]+","+currentline [5])
                    elif(choice == 'lastname'):
                        newlastname = input ('Enter the new lastname: ')
                        storage.append(currentline [0]+ ","+currentline[1]+","+newlastname+","+currentline [3]+","+currentline [4]+","+currentline [5])
                    elif(choice == 'age'):
                        newage = input ('Enter the new age: ')
                        storage.append(currentline [0]+ ","+currentline[1]+","+currentline [2]+","+newage+","+currentline [4]+","+currentline [5])
                    elif (choice == 'gender'):
                        newgender = input ('Enter the new gender: ')
                        storage.append(currentline[0]+ ","+currentline[1]+","+currentline [2]+","+currentline [3]+","+newgender+","+currentline [5]) 
                    elif (choice == 'course'):
                        newcourse = input('Enter the new course: ')
                        storage.append(currentline[0]+ ","+currentline[1]+","+currentline [2]+","+currentline [3]+","+currentline [4]+","+newcourse+"\n")
            else:
                storage.append (line)       
        f.close ()
        f = open("info.csv","w")
        for l in storage:
            f.write(l)
        f.close()
    
def delete(idnumber):
    if (checker (idnumber) == False):
        print ("\nERROR: Id number does not exist")
        pass
    else:
        storage = []
        f = open("info.csv","r")
        for line in f:
            currentline = line.split (",")
            if (currentline[0] != idnumber):
                storage.append (line)
        f.close ()
        f = open ("info.csv","w")
        for l in storage:
            f.write (l)
        f.close ()

def oper():
    print ("Operations:\nadd\nupdate\nsearch\ndelete\n")
    	
    
print("\nBasic Student Database\n")

while (True):
    oper()
    operations = input('select an Operations: ')
    
    if (operations == 'add'):
        firstname = input('enter firstname: ')
        lastname = input('enter lastname: ')
        idnumber = input('enter id number: ')
        gender = input('enter gender: ')
        age = input('enter age: ')
        course = input('enter course: ')
        
        stud = student (firstname,lastname,age,idnumber,course,gender)
        add (stud.firstName,stud.lastName,stud.idnumber,stud.age,stud.gender,stud.course)

    elif (operations == 'search'):
        searchid = input ('enter the id no.: ')
        search (searchid)  
        
    elif (operations == 'update'):
        searchid = input ('enter the id number: ')
        update(searchid)
    elif (operations == 'delete'):
        searchid = input ('enter the id no.: ')
        delete(searchid)     
 
    choice = input("\nWant to try again? yes or no: ")
    if (choice == "no"):
            break