def hapusjin():
    from summonjin import summon
    ji = summon()
    print(ji)
    jinh = input('Masukkan username jin : ')
    def isvalid(a):
        val = False
        for i in range(len(ji)):
            if ji[i]==(a,1) or ji[i]==(a,2):
                val = True
        return val
    def ismember(a):
        for i in range(len(ji)):
            if ji[i]==(a,1) or ji[i]==(a,2):
                jind = ji[i]
                return jind
    while isvalid(jinh)==False:
        if isvalid(jinh)==False:
            print('Tidak ada jin dengan username tersebut.')
            jinh = input('Masukkan username jin : ')
        else:
            jind = ismember(jinh)
            Hapus = input(f'Apakah anda yakin ingin menghapus jin dengan username {jinh} (Y/N)? ')
            if Hapus == 'Y' :
                ji.remove(jind)
                print('Jin telah berhasil dihapus dari alam gaib')
                print(ji)
    if isvalid(jinh)==True:
        jind = ismember(jinh)
        Hapus = input(f'Apakah anda yakin ingin menghapus jin dengan username {jinh} (Y/N)? ')
        if Hapus == 'Y' :
            ji.remove(jind)
            print('Jin telah berhasil dihapus dari alam gaib')
            print(ji)

if __name__=='__main__':   
    hapusjin()
