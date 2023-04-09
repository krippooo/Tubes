import csv

def login():
    uname = input("usr")
    pw = input("pw")
    with open(r"C:\Tubes daspro\csv tubes\user.csv", mode='r') as f:        #buat ngeakses si csv
        reader = csv.DictReader(f, delimiter=';')                           #ngeread csv
        for row in reader:                                                  
            if row['username'] == uname and row['password'] == pw :         #row[blabla] sesuai kolom
                print("Selamat Datang, "+uname+"!")
                print("Masukkan Command \"help\" untuk daftar command yang dapat kamu panggil.")
                break
        if row['username'] != uname :
            print("Username tidak terdaftar!")
        elif row['password'] != pw :
            print("Password salah!")
            
login()
