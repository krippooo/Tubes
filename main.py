import loadcsv
import commands

#MATRIKS
users=[]
candi=[]
bahan_bangunan=[]
users = loadcsv.loaduser() # Matriks data user
candi = loadcsv.loadcandi() # Matriks data candi
bahan_bangunan = loadcsv.loadbahan() # Data bahan bangunan

role="abc"
uname="abc"

while True:
  masukan = input(">>> ")
  role,uname,users,candi,bahan_bangunan=commands.run(masukan,role,uname,users,candi,bahan_bangunan)
  
