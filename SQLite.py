import sqlite3
conn=sqlite3.connect("CPUs.sqlite")

def create_cpu():
    with conn:
        conn.execute("CREATE TABLE CPUs(Name TEXT PRIMARY KEY, Cores INT, Threads INT, Speed DECIMAL)")

def add_cpus():
    with conn:
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1200',4,4,3.1)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1300X',4,4,3.4)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1400',4,8,3.2)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1500X',4,8,3.5)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1600',6,12,3.2)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1600X',6,12,3.6)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1700',8,16,3.0)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1700X',8,16,3.4)")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed) VALUES('1800X',8,16,3.6)")

def print_cpu():
    with conn:
        cur=conn.execute("SELECT Name, Cores, Threads, Speed from CPUs")
        for row in cur:
            print("")
            print("Name: ",row[0])
            print("Cores: ",row[1])
            print("Threads: ",row[2])
            print("Speed: ",row[3],"Ghz")
        print ("The End")


def print_row():
    with conn:
        PrintCPU=input("CPU SKU: ")
        cur=conn.execute("SELECT Name, Cores, Threads, Speed FROM CPUs WHERE Name = ?",(PrintCPU,))
        row=cur.fetchone()
        print("Name: ",row[0],"Cores: ",row[1],"Threads: ",row[2],"Speed: ",row[3],"Ghz")

def search_cores():
    MinCores=input("How many cores do you want?: ")
    with conn:
        cur=conn.execute("SELECT Cores, Name FROM CPUs WHERE Cores>=? ORDER BY Cores", (MinCores,))
        for row in cur:
            print(row[0],"Cores",row[1])

def add_cpu():
    with conn:
        NewName=input("CPU SKU: ")
        NewCores=input("Core Count: ")
        NewThreads=input("Threads: ")
        NewSpeed=input("Frequency: ")
        conn.execute("INSERT INTO CPUs(Name,Cores,Threads,Speed)VALUES(?,?,?,?)",(NewName,NewCores,NewThreads,NewSpeed))

def del_cpu():
    with conn:
        DelCPU=input("CPU SKU to delete: ")
        cur=conn.execute("SELECT Name, Cores, Threads, Speed FROM CPUs WHERE Name = ?",(DelCPU,))
        row=cur.fetchone()
        print("Name: ",row[0],"Cores: ",row[1],"Threads: ",row[2],"Speed: ",row[3],"Ghz")
        confirm=input("Are you sure you want to delete this SKU? y/n ")
        if confirm == "y":
            conn.execute("DELETE FROM CPUs WHERE Name = ?",(DelCPU,))

def update_cpu():
    with conn:
        UpdateCPU=input("CPU SKU to update: ")
        cur=conn.execute("SELECT Name, Cores, Threads, Speed FROM CPUs WHERE Name = ?",(UpdateCPU,))
        row = cur.fetchone()
        print("CPU SKU: ",row[0],"Cores: ",row[1],"Threads: ",row[2],"Frequency: ",row[3],"Ghz")
        CPUSpeed=input("New Frequency: ")
        conn.execute("UPDATE CPUs SET Speed=? WHERE Name=?",(CPUSpeed,UpdateCPU))
        cur=conn.execute("SELECT Name, Cores, Threads, Speed FROM CPUs WHERE Name = ?",(UpdateCPU,))
        row = cur.fetchone()
        print("CPU SKU: ",row[0],"Cores: ",row[1],"Threads: ",row[2],"Frequency: ",row[3],"Ghz")

'''
Commands:
create_cpu()
- makes database, use only once
add_cpus()
- adds some cpus to the database, use only once
print_cpu()
- shows whole database
print_row()
- shows specs of a single cpu
search_cores()
- shows cpus with more than a certain core count
add_cpu()
- add cpu to database
del_cpu()
- delete cpu from database
update_cpu()
- update specs of a cpu
'''

# Main menu, exception handling not fully implemented yet

loop = True
while loop==True:
    choice=int(input('''
--------------------------------------
This is the menu, Choose a number:
1. Create Table
2. Add existing values
3. Print the whole table
4. Print a specific row
5. Search based on core count
6. Add a new record
7. Delete a record
8. Update a record
9. Quit

: '''))
    if choice == 1:
        try:
            create_cpu()
        except sqlite3.OperationalError:
            print("The table already exists.")
    elif choice == 2:
        try:
            add_cpus()
        except sqlite3.IntegrityError:
            print("Values already in table.")
    elif choice == 3:
        print_cpu()
    elif choice == 4:
        try:
            print_row()
        except TypeError:
            print("That is an invalid SKU.")
    elif choice == 5:
        search_cores()
    elif choice == 6:
        add_cpu()
    elif choice == 7:
        del_cpu()
    elif choice == 8:
        update_cpu()


