#F01 #F02 #F15 #F16

#F01 Login
def login(uname,users,role):
    if role=="-": #Cek apakah sudah ada pemain yang login
        #Minta masukan
        uname = input("Masukkan username: ")
    
        #Cek availability username
        registered=False
        found=0
        for i in range(110):
            if uname==users[i][0] and uname!="":
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
def help(role):
    if role == "-" :
        print("=========== HELP ===========")
        print("1. login")
        print("Untuk masuk menggunakan akun")
        print("2. exit")
        print("Untuk keluar dari program dan kembali ke terminal")
    elif role == "bandung_bondowoso":
        print("=========== HELP ===========")
        print("1. logout")
        print("Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("Untuk memanggil jin")
        print("3. hapusjin")
        print("Untuk menghapus jin")
        print('4. ubahjin')
        print('Untuk mengubah role jin')
        print('5. batchkumpul')
        print('Untuk menyuruh para jin pengumpul mengumpulkan bahan')
        print('6. batchbangun')
        print('Untuk menyuruh para jin pembangun untuk membangun candi')
        print('7. laporanjin')
        print('Untuk melihat kinerja para jin dan informasi mengenai bahan bangunan')
        print('8. laporancandi')
        print('Untuk mengetahui progress pembangunan candi')
    elif role == "roro_jonggrang":
        print("=========== HELP ===========")
        print("1. logout")
        print("Untuk keluar dari akun yang digunakan sekarang")
        print("2. hancurkancandi")
        print("Untuk menghancurkan candi dan menggagalkan usaha Bandung Bondowoso")
        print("3. ayamberkokok")
        print("Untuk menyelesaikan permainan")
    elif role == "jin_pembangun":
        print("=========== HELP ===========")
        print("1. logout")
        print("Untuk keluar dari akun yang digunakan sekarang")
        print('2. bangun')
        print('Untuk membangun candi')
    elif role == 'jin_pengumpul':
        print("=========== HELP ===========")
        print("1. logout")
        print("Untuk keluar dari akun yang digunakan sekarang")
        print("2. kumpul")
        print('Untuk mengumpulkan bahan bangunan')

#F16 Exit
def exit():
    asdf

