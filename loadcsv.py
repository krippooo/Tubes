def loadcandi():
    import bangun

    f=open("candi.csv",'r')

    candi=bangun.hitungcandi()+1
    arr_candi=[["" for j in range (5)]for i in range (candi)]

    for i in range (0, candi):
        r=f.readline().rstrip()

        c=0
        temp=""
        for j in range (len(r)):
            if r[j]!=";" :
                temp+=r[j]

            else:
                arr_candi[i][c]=temp
                c+=1
                temp=""

            if j==len(r)-1:
                arr_candi[i][4]=temp

    return(arr_candi)

    f.close()

def hitunguser():
    #fungsi ini menghitung banyaknya user yang terdaftar
    #read from csv
    f=open("user.csv",'r')
    user=-1
    baris=f.readline()
    while(baris):
        user+=1
        baris=f.readline()

    return(user)

def loaduser():
    f=open("user.csv",'r')
    banyak_user=hitunguser()+1

    arr_user=[["" for j in range (3)] for i in range (banyak_user)]
    for i in range (0, banyak_user):
        r=f.readline().rstrip()

        c=0
        temp=""
        for j in range (len(r)):
            if r[j]!=";" :
                temp+=r[j]

            else:
                arr_user[i][c]=temp
                c+=1
                temp=""

            if j==len(r)-1:
                arr_user[i][2]=temp
    f.close()

    return(arr_user)
