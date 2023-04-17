import loadcsv
import commands

#MATRIKS
users = loadcsv.loaduser() # Matriks data user
candi = loadcsv.loadcandi() # Matriks data candi
bahan_bangunan = loadcsv.loadbahan() # Data bahan bangunan

role="-"
uname="-"

while True:
  masukan = input(">>> ")
  commands.run(masukan,role)
