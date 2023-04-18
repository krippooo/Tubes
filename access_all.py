#F01 #F02 #F15 #F16

#F01 Login
def login(users,role):
    if role=="-": #Cek apakah sudah ada pemain yang login
        #Minta masukan
        uname = input("Masukkan username: ")
    
        #Cek availability username
        registered=False
        found=0
        for i in range(110):
            if uname==users[i][0]:
                registered=True
                found=i
                break
        
        if not registered:
            print("Username tidak terdaftar!")
        else: #Jika username registered
            #Cek password
            pw = input("Masukkan password: ")
            if users[found][1]==pw:
                print(f"Selamat datang, {uname}!")
                print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
                role=users[found][2]
            else:
                print("Password salah!")

    else: #Jika sudah ada pemain yang login
        print("Login gagal!")
        print(f"Anda telah login dengan username {uname}, silahkan lakukan “logout” sebelum melakukan login kembali.")

    return(uname,role)


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

