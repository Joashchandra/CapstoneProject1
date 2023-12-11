import os
import random
import string
from tabulate import tabulate
from operator import itemgetter
# Capstone Project Yellow Pages Joash Christian Chandra JCDS Jakarta
#initial data
pages = [
    {"ID" : 'l3NzGnb3aNTY', "No Telefon" : "08182637645", "Nama" : "Budi Bola", "Kelamin" : "Pria", "Kota" : "Jakarta", "Alamat" : "Jl. Kapuk Raya"},
    {"ID" : '2S1RTBFuXlVG', "No Telefon" : "08171744837", "Nama" : "Anton Bolang", "Kelamin" : "Pria", "Kota" : "Tangerang", "Alamat" : "Jl. Gading Serpong"},
    {"ID" : 'awH4E6nQiexR', "No Telefon" : "08185783246", "Nama" : "Wonder Woman", "Kelamin" : "Wanita", "Kota" : "Tangerang", "Alamat" : "Jl. Gading Serpong"},
    {"ID" : '4wfX8IloTN5n', "No Telefon" : "08137483261", "Nama" : "Suparman", "Kelamin" : "Pria", "Kota" : "Jakarta", "Alamat" : "Jl. Pantai Indah Kapuk"},
    {"ID" : 'Xy24JTMfHzrR', "No Telefon" : "08372817341", "Nama" : "Benjamin Franklin", "Kelamin" : "Pria", "Kota" : "Tangerang", "Alamat" : "Jl. Bsd"},
    {"ID" : 'ypWYO7XrvNNb', "No Telefon" : "08372817341", "Nama" : "Lyla Smith", "Kelamin" : "Wanita", "Kota" : "Tangerang", "Alamat" : "Jl. Gading Serpong"}
]

def cont() :
    input("Press enter to continue...")

#load data
def loadData() :
    headers = pages[0].keys()
    data = [i.values() for i in pages]
    return headers,data

#print semua
def showAll() :
    head,data = loadData()
    print(tabulate(data,head))
    print(f"\n{len(pages)} data ditampilkan")     

#print sesuai dengan value input dan index
def cari(val,index) :
    head, data = loadData()
    temp = []
    found = False
    for i in range(len(data)) :
        if list(data[i])[index].lower() == val.lower() :
            temp.append(list(data[i]))
            found = True
    if found == True :
        temp = sorted(temp, key=itemgetter(2))
        print(tabulate(temp,head))
        print(f"\n{len(temp)} data ditemukan")
        return found
    else :
        print("Data tidak ditemukan")
        return found
    
#untuk cek apakah id unique atau tidak
def isExist(val,key) :
    cek = False
    for i in range(len(pages)) :
        if pages[i][key] == val :
            cek = True
            break
    return cek

#fungsi untuk generate random id
def generateID() :
    while True :
        id = ''.join(random.choices(string.ascii_letters + string.digits, k=12))
        cek = isExist(id,'ID')
        if cek == False :
            print(f"ID : {id}")
            return id

#insert data satu per keys yang diminta
def inputData(dict) :
    data = {}
    cond = True
    while cond :
        data[dict] = input(f"Masukkan {dict} : ")
        if dict == "No Telefon" :
            if data[dict].isdigit() == False :
                print("Data harus Angka")
            else :
                cond = False
        elif dict == "Nama" or dict == "Kota" :
            cek = cekAlphabet(data[dict].split())
            if cek == False :
                print(f"{dict} hanya boleh Alfabet")
            else :
                data[dict] = capital(data[dict].lower().split())
                cond = False
        elif dict == "Kelamin" :
            if data[dict].lower() == "pria" or data[dict].lower() == "wanita" :
                data[dict] = capital(data[dict].lower().split())
                cond = False
            else :
                print("Hanya ada Pria dan Wanita (Tidak menerima LGBT)")
        elif dict == "Alamat" :
            data[dict] = capital(data[dict].lower().split())
            cond = False
        else :
            print("Tidak ada keys tersebut")     
    return data

#function update
def update(id):
    cond1 = True
    found = False
    for i in range(len(pages)):
        if pages[i]['ID'] == id :
            found = True
            while cond1 :
                while True :
                    os.system("cls")
                    cond3 = True
                    print("Pilihan data yang akan di update")
                    print ("Pilihan : No Telfon, Nama, Kelamin, Kota, Alamat\n")
                    n = input("Data yang ingin di update : ")
                    cek = cekAlphabet(n)
                    if cek == True :
                        n = capital(n.lower().split())
                        if n in pages[i].keys() and n.upper() != 'ID':
                            pages[i].update(inputData(n))
                            print("Data berhasil di update")
                            break
                        elif n.upper() == 'ID' :
                            print("Tidak bisa mengupdate ID")
                        else :
                            print("Keys tidak ditemukan")
                    else :
                        print("Input hanya boleh alfabet")
                    cont()
                while True :
                    n = input("Lanjut update? (Y/N) : ")
                    if n.lower() == "y" :
                        break
                    elif n.lower() == "n" :
                        cond1 = False
                        break
                    else :
                        print("Input Hanya boleh Y/N")
    if found == False :
        print("ID tidak ditemukan")

#fungsi hapus id
def deleteData(val,key) :
    for i in range(len(pages)) :
        if pages[i][key] == val :
            pages.pop(i)
            print("Data telah dihapus")
            break

#fungsi cek    
def cekAlphabet(string) :
    cek = ""
    for i in string :
        cek += i
    return cek.isalpha()

#fungsi capitalize
def capital(data) :
    cap = [i.capitalize() for i in data]
    cap = " ".join(cap)
    return cap

# Main Program
while True :
    os.system("cls")
    try :
        print("Welcome to Yellow Pages\n")
        print("1. Search Menu")
        print("2. Add Data")
        print("3. Update Menu")
        print("4. Delete Menu")
        print("5. Exit Program")
        n = int(input("Pilih Menu : "))
        if n == 1 :
            while True :
                try :
                    os.system("cls")
                    print("\tSearch Menu\n")
                    print("1. Tampilkan Semua")
                    print("2. Cari Nama")
                    print("3. Cari Kota")
                    print("4. Kembali ke Menu Utama")
                    n = int(input("Pilih Menu : "))
                    if n == 1 :
                        os.system("cls")
                        showAll()
                    elif n == 2 :
                        os.system("cls")
                        nama = input("Masukkan Nama yang dicari (Nama Lengkap) : ")
                        cek = cekAlphabet(nama.split())
                        if cek == True :
                            cari(nama,2)
                        else :
                            print("Input hanya boleh alfabet!")
                    elif n == 3 :
                        os.system('cls')
                        kota = input("Masukkan Kota yang dicari : ")
                        cek = cekAlphabet(kota)
                        if cek == True :
                            cari(kota,4)
                        else :
                            print("Input hanya boleh alfabet")
                    elif n == 4 :
                        break
                    else :
                        print("Hanya ada pilihan menu 1-4")
                    cont()
                except :
                    print("Input Hanya Angka")
                    cont()
        elif n == 2 :
            os.system('cls')
            data = {}
            print("Penambahan Data")
            data["ID"] = generateID()
            data.update(inputData('No Telefon'))
            data.update(inputData("Nama"))
            data.update(inputData("Kelamin"))
            data.update(inputData("Kota"))
            data.update(inputData("Alamat"))
            pages.append(data)
            print("Data berhasil dimasukkan!")      
        elif n == 3 :
            while True : 
                try:
                    os.system("cls")
                    print("Update Menu\n")
                    print("1. Input ID")
                    print("2. Cari Nama")
                    print("3. Cari No Telefon")
                    print("4. Kembali ke Menu Utama")
                    n = int(input("Pilih Menu : "))
                    if n == 1 :
                        id = input("Masukkan ID yang ingin di update : ")
                        update(id)
                    elif n == 2 :
                        while True :
                            nama = input("Masukkan nama yang ingin di cari : ")
                            cek = cekAlphabet(nama.split())
                            if cek == True :
                                found = cari(nama,2)
                                if found == True :
                                    id = input("\nMasukkan ID yang ingin di update : ")
                                    update(id)
                                    break
                            else :
                                print("Input hanya boleh alfabet")
                    elif n == 3 :
                        while True :
                            no = input("Masukkan no telefon yang ingin dicari : ")
                            cek = no.isdigit()
                            if cek == True :
                                found = cari(no,1)
                                if found == True :
                                    id = input("\nMasukkan ID yang ingin di update : ")
                                    update(id)
                                    break
                            else :
                                print("Input hanya boleh digit")
                    elif n == 4 :
                        break
                    else :
                        print("Hanya ada pilihan menu 1-4")
                    cont()
                except:
                    print("Input Hanya Angka")
                    cont()
        elif n == 4 :
            while True :
                try :
                    os.system("cls")
                    print("Delete Menu\n")
                    print("1. Cari Nama")
                    print("2. Hapus by ID")
                    print("3. Hapus Sesuai Nama")
                    print("4. Hapus Semua Data")
                    print("5. Kembali ke Menu Utama")
                    n = int(input("Pilih Menu : "))   
                    if n == 1 :
                        while True :
                            os.system('cls')
                            nama = input("Masukkan nama yang ingin di cari : ")
                            cek = cekAlphabet(nama.lower().split())
                            if cek == True:
                                found = cari(nama,2)
                                if found == True :
                                    while True :
                                        id = input("Masukkan ID yang ingin dihapus : ")
                                        cek = isExist(id,'ID')
                                        if cek == True :
                                            deleteData(id,'ID')
                                            break
                                break
                            else :
                                print("Input hanya boleh alphabet")

                    elif n == 2 :
                        os.system('cls')
                        id = input("Masukkan ID yang ingin dihapus : ")
                        exist = isExist(id,'ID')
                        if exist == True :
                            deleteData(id,'ID')
                        else :
                            print("ID tidak ditemukan")

                    elif n == 3:
                        os.system('cls')
                        nama = input("Masukkan nama : ")
                        cek = cekAlphabet(nama.split())
                        if cek == True :
                            exist =  isExist(nama,'Nama')
                            if exist == True :
                                deleteData(nama,'Nama')
                            else :
                                print("Nama tidak ditemukan")
                        else :
                            print("Input hanya boleh Alfabet")

                    elif n == 4 :
                        while True :
                            n = input("Apakah anda yakin? (y/n) : ")
                            if n.lower() == "y" :
                                pages.clear()
                                print("Semua Data Telah dihapus")
                                break
                            elif n.lower() == "n" :
                                break
                            else :
                                print("Input hanya y atau n")
                    elif n == 5 :
                        break
                    else :
                        print("Hanya ada pilihan menu 1-5")
                    cont()
                except :
                    print("Input Hanya Angka")
        elif n == 5 :
            break 
        else :
            print("Hanya ada pilihan menu 1-5")
        cont()
    except :
        print("Input Hanya Angka")
        cont()