#F01 #F02 #F15 #F16

#F01 Login
def login():
    uname = input("usr")
    pw = input("pw")
    role = "-"
    with open(r"C:\Tubes daspro\csv tubes\user.csv", mode='r') as f:        #buat ngeakses si csv
        reader = csv.DictReader(f, delimiter=';')                           #ngeread csv
        for row in reader:                                                  
            if row['username'] == uname and row['password'] == pw :         #row[blabla] sesuai kolom
                print("Selamat Datang, "+uname+"!")
                print("Masukkan Command \"help\" untuk daftar command yang dapat kamu panggil.")
                role = row['role']
                return (role)        
        if row['username'] != uname :
            print("Username tidak terdaftar!")
        elif row['password'] != pw :
            print("Password salah!")

#F02 Logout
def logout(akses,uname):
    if akses!="-":
        role="-"
        uname="-"
        print("Logout berhasil!")
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")

    return (role, uname)

#Untuk Checker
def tempstate(role, uname,users,candi,bahan_bangunan):
    print(role)
    print(uname)
    print(users)
    print(candi)
    print(bahan_bangunan)



#F15 Help
def help():
    asdf

#F16 Exit
def exit():
    asdf

