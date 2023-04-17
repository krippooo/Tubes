def loaduser():
    """memasukkan nilai-nilai di user.csv ke dalam matriks"""
    arr=[['' for j in range(3)] for i in range (110)]

    f=open("user.csv",'r')
    for i in range (0, 110):
        r=f.readline().rstrip()
        c=0
        temp=""
        for j in range (len(r)):
            if r[j]!=";" :
                temp+=r[j]

            else:
                arr[i][c]=temp
                c+=1
                temp=""

            if j==len(r)-1:
                arr[i][2]=temp
    f.close()

    return(arr)


def loadcandi():
    """memasukkan nilai-nilai di candi.csv ke dalam matriks"""

    arr=[['' for j in range(5)] for i in range (110)]

    f=open("candi.csv",'r')
    for i in range (0, 110):
        r=f.readline().rstrip()
        c=0
        temp=""
        for j in range (len(r)):
            if r[j]!=";" :
                temp+=r[j]

            else:
                arr[i][c]=temp
                c+=1
                temp=""

            if j==len(r)-1:
                arr[i][4]=temp
    f.close()

    return(arr)

def loadbahan():
    """memasukkan nilai-nilai di bahan_bangunan.csv ke dalam matriks"""

    arr=[['' for j in range(3)] for i in range (4)]

    f=open("bahan_bangunan.csv",'r')
    for i in range (4):
        r=f.readline().rstrip()
        c=0
        temp=""
        for j in range (len(r)):
            if r[j]!=";" :
                temp+=r[j]

            else:
                arr[i][c]=temp
                c+=1
                temp=""

            if j==len(r)-1:
                arr[i][2]=temp
    f.close()

    return(arr)
