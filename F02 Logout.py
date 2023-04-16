def logout():
    #I.S. username defined, akses defined, username had login
    #F.S. akses - (dikosongkan) 

    if akses!="-":
        akses="-"
        username="-"
        print("Logour berhasil!")

    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
