from os import name
        
def validasi_login(uname,passw):
    u = []
    p = []
    validasi = False 
    data = open("C:\Tubes daspro\Login\datalogin.txt", "r")
    for i in data:
        a,b = i.split(",")
        b = b.strip()
        u.append(a)
        p.append(b)
        if (a==uname and b == passw):
            validasi = True
            break
    if (uname not in u) :
        print("Username tidak terdaftar!")
    elif (passw not in p) :
        print("Password salah!")
    data.close()
    if validasi :
        print("Selamat datang, " + uname + "!", end='\n')
        print("Masukkan command \"help\" untuk daftar command yang dapat kamu panggil")

def access(uname,passw) :
    if uname == "Bandung":
        akses = 1 #indikasi kalo tiap command aksesnya tergantung role
    elif uname == "Roro":
        akses = 2
    elif uname == "Jin" and passw == "Pengumpul":
        akses = 3
    elif uname == "Jin" and passw == "Pembangun":
        akses = 4
    return akses

def ubahjin(nama_jin):
    u = []
    p = []
    data = open("C:\Tubes daspro\Login\id_jin,pekerjaan.txt", "r")
    for i in data:
        a,b = i.split(",")
        b = b.strip()
        u.append(a)
        p.append(b)
        if a == nama_jin:
            if b == "Pengumpul":
                print("Jin ini bertipe \" Pengumpul \". Yakin ingin mengubah ke tipe \" Pembangun \" (Y/N)?", end=" ") 
                ubah = input()
                if ubah == "Y" or ubah == "y":
                    data.replace("Pengumpul", "Pembangun")
                    print("\n")
                    print("Jin telah berhasil diubah")
                elif ubah == "N" or ubah == "n":
                    print("Jin tidak diubah")
                else :  
                    print("Harap meng-inputkan karakter Y atau N")     
            elif b == "Pembangun":
                print("Jin ini bertipe \" Pembangun \". Yakin ingin mengubah ke tipe \" Pengumpul \" (Y/N)?", end=" ") 
                ubah = input()
                if ubah == "Y" or ubah == "y":
                    data.replace("Pembangun", "Pengumpul")
                    print("\n")
                    print("Jin telah berhasil diubah")
                elif ubah == "N" or ubah == "n":
                    print("Jin tidak diubah")
                else :  
                    print("Harap meng-inputkan karakter Y atau N")
    if (a not in u) :
        print("\n","Tidak ada jin dengan nama seperti itu")
    if (a in u) :
        if p == "Pengumpul":
            ubah = input("Jin ini bertipe \" Pengumpul \". Yakin ingin mengubah ke tipe \" Pembangun \" (Y/N)?", end=" ") 
            if ubah == "Y" or ubah == "y":
                data.replace("Pengumpul", "Pembangun")
                print("\n")
                print("Jin telah berhasil diubah")
            elif ubah == "N" or ubah == "n":
                print("Jin tidak diubah")
            else :  
                print("Harap meng-inputkan karakter Y atau N")     
        elif p == "Pembangun":
            ubah = input("Jin ini bertipe \" Pembangun \". Yakin ingin mengubah ke tipe \" Pengumpul \" (Y/N)?", end=" ") 
            if ubah == "Y" or ubah == "y":
                data.replace("Pembangun", "Pengumpul")
                print("\n")
                print("Jin telah berhasil diubah")
            elif ubah == "N" or ubah == "n":
                print("Jin tidak diubah")
            else :  
                print("Harap meng-inputkan karakter Y atau N")
    data.close()
def akses(uname):
    if uname == "Bandung":
        command = input()
        if command == "ubahjin":
            nama_jin = input("Masukkan Username Jin : ")  
            ubahjin(nama_jin)
            akses(uname)

def mulai():
    command = input(">>> ")
    if command == "login":
        name = input ("Masukkan username: ")
        password = input("Masukkan password: ")
        validasi_login(name,password)
        akses(name)
mulai()