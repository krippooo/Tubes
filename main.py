import commands
import argparse
import loadsave
import sys
#MATRIKS
users=[]
candi=[]
bahan_bangunan=[]

role="-"
uname="-"

parser = argparse.ArgumentParser()
parser.add_argument('nama_folder',nargs='?', default='__no_value__')
args = parser.parse_args()

if args.nama_folder == '__no_value__':
    sys.exit("\nTidak ada nama folder yang diberikan!\n\nUsage: python main.py <nama_folder>.")
else:
    users,candi,bahan_bangunan = loadsave.load(args.nama_folder)
    print("Selamat datang di Program \"Manajerial Candi\"! ")
    print("masukkan menu login dan silahkan isi username anda.")

while True:
  masukan = input(">>> ")
  role,uname,users,candi,bahan_bangunan=commands.run(masukan,role,uname,users,candi,bahan_bangunan)
  
