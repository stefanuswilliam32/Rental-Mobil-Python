from tabulate import tabulate

passwordAdmin = "Admin123"


def menuAwal(mobil, customer):
    print("------------------ Willy Rental ------------------\n")
            
    print("Halo Selamat Datang\n\n")

    while True:
        login = input("Tolong masukkan no telpon anda dengan format (08xxxxxxxxxx) : ")

        if login == passwordAdmin:
            menuAdmin(mobil, customer)

        elif login.isnumeric() and login[0] == '0' and login[1] == '8' and 9 < len(login) < 14:
            loginCustomer(login)

        else:
            print("Maaf input no. telpon anda salah\n")


def menuAdmin(mobil, customer):
    
    while True:
        print("\n\n------------------ Admin ------------------\n\n")
        print("[1] Data Mobil\n[2] Data Customer\n[3] Logout")
        i = input("Input index menu : ")

        if i == "1":
            menuDataMobilAdmin(mobil)

        elif i == "2":
            menuDataCustomerAdmin(customer)

        elif i == "3":
            menuAwal(mobil, customer)

        else:
            print("Input salah.\n")


def menuDataMobilAdmin(mobil):
    while True:
        print("\n----------- Menu Data Mobil ---------------\n\n")
        print("[1] Menampilkan Data\n[2] Menambah Mobil\n[3] Mengubah Data\n[4] Menghapus Data\n[5] Kembali")
        i = input("Input Index Menu : ")

        if i == "1":
            menuMenampilkanDataMobilAdmin()

        elif i == "2":
            menuMenambahMobilAdmin(mobil)

        elif i == "3":
            menuMengubahDataMobilAdmin(mobil)

        elif i == "4":
            menuMenghapusMobilAdmin(mobil)
            

        elif i == "5":
            break
        else:
            print("Input salah.\n")


def menuMenampilkanDataMobilAdmin():
    while True:
        print("\n--------- Menampilkan Data Mobil ----------\n\n")
        print("[1] Tampilkan Semua Data\n[2] Tampilkan Data Mobil Sesuai Plat Mobil\n[3] Kembali")
        i = input("Input Index Menu : ")

        if i == "1":
            printDataMobil()

        elif i == "2":
            printDataMobilPlat()
        
        elif i == "3":
            break

        else:
            print("Input salah.\n")


def printDataMobil():
    if len(mobil) != 0:
        values = []
        for i, j in mobil.items():
            innerValues = []
            innerValues.append(i)
            innerValues.append(j["mobil"])
            innerValues.append(j["harga"])
            innerValues.append(j["transmisi"])
            innerValues.append(j["bahanBakar"])
            innerValues.append(j["warna"])
            if j["statusPinjam"]:
                innerValues.append("Sedang di Pinjam")

            else:
                innerValues.append("Tidak di Pinjam")

            innerValues.append(j["lamaHari"])
            values.append(innerValues)
        
        print(tabulate(values, headers=["Plat Mobil", "Mobil", "Harga", "Transmisi", "Bahan Bakar", "Warna", "Status", "Lama Hari"], tablefmt="grid"))
    
    else: 
        print("\nData Mobil Tidak Ada.\n")


def printDataMobilPlat():
    if len(mobil) != 0:
        
        plat = input("\nMasukkan plat mobil : ").upper()
        if plat not in mobil:
            print("\nPlat mobil tidak ada.")
            return

        if mobil[plat]["statusPinjam"]:
            status = "Sedang di Pinjam"

        else:
            status = "Tidak di Pinjam"

        print(f"\n\n-Plat Mobil : {plat}\n-Mobil : {mobil[plat]["mobil"]}\n-Harga : {mobil[plat]["harga"]}\n-Transmisi : {mobil[plat]["transmisi"]}\n-Bahan Bakar : {mobil[plat]["bahanBakar"]}\n-Warna : {mobil[plat]["warna"]}\n-Status : {status}\n-Lama Hari : {mobil[plat]["lamaHari"]}\n")
    
    else:
        print("\nData Mobil Tidak Ada.\n")


def menuMenambahMobilAdmin(mobil):
    while True:
        print("\n------------- Menambah Mobil --------------\n\n")
        printDataMobil()
        print("[1] Menambah Data Mobil\n[2] Kembali")
        i = input("Input Index Menu : ")

        if i == "1":
            menambahMobil(mobil)

        elif i == "2":
            break

        else:
            print("Input salah.\n")


def menambahMobil(mobil):
    plat = input("\nMasukkan plat mobil : ").upper()
    
    if plat in mobil.keys():
        print("\nPlat mobil sudah ada.\n")
        return

    jenisMobil = input("Masukkan jenis mobil : ")
    
    while True:
        harga = input("Masukkan harga sewa : ")
        if harga.isnumeric():
            break
        print("\nInput harga salah")

        while True:
            j = input("Melanjutkan penambahan mobil (ya/tidak) : ")

            if j.lower() == "ya":
                break

            elif j.lower() == "tidak":
                return

            else:
                print("Input Salah.")

    transmisi = input("Masukkan transmisi (AT/MT): ")
    bahanBakar = input("Masukkan bahan bakar : ")
    warna = input("Masukkan warna : ")

    print(f"\n\n-Plat Mobil : {plat}\n-Mobil : {jenisMobil}\n-Harga : {harga}\n-Transmisi : {transmisi}\n-Bahan Bakar : {bahanBakar}\n-Warna : {warna}\n")
    i = input("Mobil jadi ditambahkan (ya/tidak) : ")

    if i == "ya":
        mobil[plat.upper()] = {"mobil" : jenisMobil.capitalize(),
        "transmisi" : transmisi.upper(),
        "warna" : warna.capitalize(), 
        "bahanBakar" : bahanBakar.capitalize(),
        "harga" : int(harga),
        "statusPinjam" : False,
        "lamaHari" : 0}

        sortingMobilHarga(mobil)
        print("\nData Mobil Berhasil ditambahkan.\n")
 

def sortingMobilHarga(mobil):
    temp = dict(sorted(mobil.items(), key=lambda item: item[1]["harga"]))
    mobil.clear()
    mobil.update(temp)


def menuMengubahDataMobilAdmin(mobil):
    while True:
        print("\n---------- Mengubah Data Mobil -----------\n\n")
        printDataMobil()
        
        if len(mobil) != 0:
            print("[1] Mengubah Data Mobil\n[2] Kembali")
            i = input("Input Index Menu : ")

            if i == "1":
                mengubahDataMobil(mobil)

            elif i == "2":
                break

            else:
                print("Input salah.\n")

        else:
            print("\nData Mobil Tidak Ada.\n")
            return


def mengubahDataMobil(mobil):
    plat = input("\nMasukkan plat mobil : ").upper()
        
    if plat not in mobil:
        print("\nPlat mobil tidak ada.")
        return
    
    else:
        while True:
            print(f"\nData Mobil\n\n- Plat : {plat}\n- Mobil : {mobil[plat]["mobil"]}\n- Harga : {mobil[plat]["harga"]}\n- Transmisi : {mobil[plat]["transmisi"]}\n- Warna : {mobil[plat]["warna"]}\n- Bahan Bakar : {mobil[plat]["bahanBakar"]}\n")
            j = input("Data Jadi Diganti (ya/tidak): ").lower()
            
            if j == "ya":
                while True:
                    i = input("\nData yang ingin diubah : ").lower()

                    if i == "plat":
                        platGanti = input(f"Plat {plat} akan diganti dengan : ").upper()
                        
                        if platGanti not in mobil.keys():
                            while True:
                                j = input("Data Jadi Diganti (ya/tidak): ").lower()

                                if j == "ya":
                                    mobil[platGanti] = mobil.pop(plat)
                                    print("\nPlat Mobil Berhasil Diganti.\n")
                                    sortingMobilHarga(mobil)
                                    return
                                
                                elif j == "tidak":
                                    return
                                
                                else:
                                    print("Input Salah.\n")
                            

                        else: 
                            print(f"Plat {platGanti} Sudah Terdaftar.\n")
                            return

                    elif i == "mobil":
                        jenisMobil = input("Masukkan jenis mobil : ")
                        
                        while True:
                            j = input("Data Jadi Diganti (ya/tidak): ").lower()

                            if j == "ya":
                                mobil[plat]["mobil"] = jenisMobil.capitalize()
                                print("\nData Mobil Berhasil Diubah.\n")
                                return
                            
                            elif j == "tidak":
                                return
                            
                            else:
                                print("Input Salah.\n")


                    elif i == "harga":
                        while True:
                            harga = input("Masukkan harga sewa : ")
                            if harga.isnumeric():
                                break

                            print("\nInput harga salah\n")
                            
                            while True:
                                j = input("Melanjutkan perubahan harga mobil (ya/tidak) : ").lower()

                                if j == "ya":
                                    break

                                elif j == "tidak":
                                    return

                                else:
                                    print("Input Salah.\n")

                        while True:
                            j = input("Data Jadi Diganti (ya/tidak): ").lower()
                            if j == "ya":
                                mobil[plat]["harga"] = int(harga)
                                print("\nData Mobil Berhasil Diubah.\n")
                                sortingMobilHarga(mobil)
                                return
                            
                            elif j == "tidak":
                                return
                            
                            else:
                                print("Input Salah.\n")
                        
                    elif i == "transmisi":
                        transmisi = input("Masukkan transmisi (AT/MT): ").upper()
                        
                        while True:    
                            j = input("Data Jadi Diganti (ya/tidak): ").lower()

                            if j == "ya":
                                mobil[plat]["transmisi"] = transmisi.capitalize()
                                print("\nData Mobil Berhasil Diubah.\n")
                                return
                            
                            elif j == "tidak":
                                return
                            
                            else:
                                print("Input Salah.\n")

                    elif i == "warna":
                        warna = input("Masukkan warna : ")
                        j = input("Data Jadi Diganti (ya/tidak): ").lower()

                        while True:
                            if j == "ya":
                                mobil[plat.upper()]["warna"] = warna.capitalize()
                                print("\nData Mobil Berhasil Diubah.\n")
                                return
                            
                            elif j == "tidak":
                                return
                            
                            else:
                                print("Input Salah.\n")

                    elif i == "bahanbakar" or i == "bahan bakar":
                        bahanBakar = input("Masukkan bahan bakar : ")
                        j = input("Data Jadi Diganti (ya/tidak): ").lower()
                        
                        while True:
                            if j == "ya":
                                mobil[plat.upper()]["bahanBakar"] = bahanBakar.capitalize()    
                                print("\nData Mobil Berhasil Diubah.\n")
                                return
                            
                            elif j == "tidak":
                                return
                            
                            else:
                                print("Input Salah.\n")

                    else:
                        print("Input Salah.\n")
                    
            elif j == "tidak":
                return
            
            else:
                print("Input Salah.\n")


def menuMenghapusMobilAdmin(mobil):
    while True:
        print("\n------------- Menghapus Mobil --------------\n\n")
        printDataMobil()
        
        if len(mobil) != 0:
            print("[1] Menghapus Mobil\n[2] Kembali")
            i = input("Input Index Menu : ")

            if i == "1":
                menghapusMobil(mobil)

            elif i == "2":
                break

            else:
                print("Input salah.\n")
        
        else:
            print("\nData Mobil Tidak Ada.\n")
            return


def menghapusMobil(mobil):

    plat = input("\nPlat yang akan dihapus : ").upper()
    if plat in mobil:
        print(f"\nData Mobil\n\n- Plat : {plat}\n- Mobil : {mobil[plat]["mobil"]}\n- Harga : {mobil[plat]["harga"]}\n- Transmisi : {mobil[plat]["transmisi"]}\n- Warna : {mobil[plat]["warna"]}\n- Bahan Bakar : {mobil[plat]["bahanBakar"]}\n")
    
        while True:
            j = input("Data Jadi Dihapus (ya/tidak): ").lower()
            
            if j == "ya":
                if mobil[plat]["statusPinjam"] == False:
                    mobil.pop(plat)
                    print("Mobil Berhasil Dihapus.\n")
                    return
                else:
                    print("Mobil Sedang Dipinjam!\n")
                    return
                
            elif j == "tidak":
                break

            else:
                print("Input salah.\n")

    else:
        print(f"Plat {plat} tidak ada.\n")


def menuDataCustomerAdmin(customer):
    while True:
        print("\n--------- Menu Data Customer -------------\n\n")
        
        print("[1] Menampilkan Data\n[2] Mengubah Data\n[3] Menghapus Data\n[4] Kembali")
        i = input("Input Index Menu : ")

        if i == "1":
            menuMenampilkanDataCustomerAdmin()

        elif i == "2":
            menuMengubahDataCustomerAdmin(customer)

        elif i == "3":
            menuMenghapusDataCustomerAdmin(customer)

        elif i == "4":
            break

        else:
            print("Input salah.\n")


def menuMenampilkanDataCustomerAdmin():
    while True:
        print("\n-------- Menampilkan Data Customer ---------\n\n")
        print("[1] Tampilkan Semua Data\n[2] Tampilkan Data Customer Sesuai No. Telpon\n[3] Kembali")
        i = input("Input Index Menu : ")

        if i == "1":
            printDataCustomer()

        elif i == "2":
            printDataCustomerTelpon()
        
        elif i == "3":
            break

        else:
            print("Input salah.\n")


def printDataCustomer():
    if len(customer) != 0:
        values = []
        for i, j in customer.items():
            innerValues = []
            innerValues.append(i)
            innerValues.append(j["nama"])
            innerValues.append(j["alamat"])
            
            mobilPinjam = ""

            if len(j["mobil"]) != 0:
                for i in range(len(j["mobil"])):
                    mobilPinjam += j["mobil"][i]
                    
                    if i!= len(j["mobil"]) - 1: 
                        mobilPinjam += ", "
            else:
                mobilPinjam += "-"

            innerValues.append(mobilPinjam)

            values.append(innerValues)

        print(tabulate(values, headers=["No. Telpon", "Nama", "Alamat", "Mobil"], tablefmt="grid"))
        
    else:
        print("\nData Customer Tidak Ada.\n")


def printDataCustomerTelpon():
    if len(customer) != 0:
        
        noTelpon = input("\nMasukkan No. Telpon Customer : ")
        if noTelpon not in customer:
            print("\nNo telpon tidak ada.")
            return

        mobilPinjam = ""

        if len(customer[noTelpon]["mobil"]) != 0:
            for i in range(len(customer[noTelpon]["mobil"])):
                mobilPinjam += customer[noTelpon]["mobil"][i]
                
                if i!= len(customer[noTelpon]["mobil"]) - 1: 
                    mobilPinjam += ", "
        else:
            mobilPinjam += "-"

        print(f"\n\n-No Telpon : {noTelpon}\n-Nama : {customer[noTelpon]["nama"]}\n-Alamat : {customer[noTelpon]["alamat"]}\n-Mobil di Pinjam : {mobilPinjam}")
    
    else:
        print("\nData Customer Tidak Ada.\n")


def menuMengubahDataCustomerAdmin(customer):
    while True:
        print("\n--------- Mengubah Data Customer ----------\n\n")
        printDataCustomer()
        
        if len(customer) != 0:
            print("[1] Mengubah Data Customer\n[2] Kembali")
            i = input("Input Index Menu : ")

            if i == "1":
                mengubahDataCustomerAdmin(customer)

            elif i == "2":
                break

            else:
                print("Input salah.\n")

        else:
            print("\nData Customer Tidak Ada.\n")
            return


def mengubahDataCustomerAdmin(customer):
    noTelpon = input("\nMasukkan no. telpon customer : ")
        
    if noTelpon not in customer:
        print("\nNo. telpon customer tidak ada.")
        return

    else:
        while True:
            print(f"\n\n-No Telpon : {noTelpon}\n-Nama : {customer[noTelpon]["nama"]}\n-Alamat : {customer[noTelpon]["alamat"]}")
            j = input("\nData Jadi Diganti (ya/tidak): ").lower()
                
            if j == "ya":
                while True:
                        i = input("\nData yang ingin diubah : ").lower()

                        if i == "no telpon" or i == "notelpon" or i == "telpon":
                            noTelponBaru = input(f"No. Telpon {noTelpon} akan diganti dengan : ")
                            
                            while True:
                                if noTelponBaru.isnumeric() and noTelponBaru[0] == '0' and noTelponBaru[1] == '8' and 9 < len(noTelponBaru) < 14:
                                    if noTelponBaru not in customer:
                                        while True:
                                            j = input("Data Jadi Diganti (ya/tidak): ").lower()

                                            if j == "ya":
                                                customer[noTelponBaru] = customer.pop(noTelpon)
                                                print("\nNo. Telpon Berhasil Diganti.\n")
                                                return
                                            
                                            elif j == "tidak":
                                                return
                                            
                                            else:
                                                print("Input Salah.\n")

                                    else: 
                                        print(f"\nNo. Telpon {noTelponBaru} Sudah Terdaftar.\n")
                                        return
                                
                                else:
                                    print("Maaf input no. telpon anda salah\n")
                        
                        elif i == "nama":
                            nama = input("Masukkan nama : ")
                            
                            while True:
                                j = input("Data Jadi Diganti (ya/tidak): ").lower()

                                if j == "ya":
                                    customer[noTelpon]["nama"] = nama.capitalize()
                                    print("\nData Customer Berhasil Diubah.\n")
                                    return
                                
                                elif j == "tidak":
                                    return
                                
                                else:
                                    print("Input Salah.\n")
                        
                        elif i == "alamat":
                            alamat = input("Masukkan alamat : ")
                            
                            while True:
                                j = input("Data Jadi Diganti (ya/tidak): ").lower()

                                if j == "ya":
                                    customer[noTelpon]["alamat"] = alamat.capitalize()
                                    print("\nData Customer Berhasil Diubah.\n")
                                    return
                                
                                elif j == "tidak":
                                    return
                                
                                else:
                                    print("Input Salah.\n")

                        else:
                            print("Input Salah.\n")
                        
            elif j == "tidak":
                return
            
            else:
                print("Input Salah.\n")
                        

def menuCostumer(login):
    print("\n\n------------------ Customer ------------------")

    print("Hallo", customer[login]["nama"])


def loginCustomer(login):
    while True:
        if login in customer:
            password = input("Masukkan password anda : ")
            
            if password == customer[login]["password"]:
                menuCostumer(login)
            
            else:
                print("Maaf password anda salah !!!\n")
                i = input("Masukkan password lagi? (ya/tidak) ")

                if i.lower() != "ya":
                    break
        else:
            buatAkun = input("Nomor telpon anda belum terdaftar, ingin membuat akun (ya/tidak) : ")

            if buatAkun.lower() == "ya":
                password = input("Masukkan password anda :\n")
                nama = input("\nMasukkan nama anda :\n")
                alamat = input("\nMasukkan alamat anda :\n")

                customer[login] = {"password" : password, "nama" : nama.capitalize(), "alamat" : alamat, "mobil" : []}

                print("Akun anda berhasil dibuat\n\n")

                menuCostumer(login)

            elif buatAkun.lower() == "tidak":
                print("Terima kasih")
                break
            
            else:
                print("Maaf input anda salah.")
                break


mobil = {"D 1234 X" : {"mobil" : "Ayla", "transmisi" : "AT", "warna" : "Hitam", "bahanBakar" : "Pertalite", "harga" : 325000, "statusPinjam" : True, "lamaHari" : 7}, 
         "D 2345 B" : {"mobil" : "Ayla", "transmisi" : "MT", "warna" : "Putih", "bahanBakar" : "Pertalite", "harga" : 325000, "statusPinjam" : True, "lamaHari" : 2}, 
         "D 3456 F" : {"mobil" : "Brio Satya", "transmisi" : "AT", "warna" : "Abu", "bahanBakar" : "Pertalite", "harga" : 375000, "statusPinjam" : False, "lamaHari" : 0}, 
         "D 5678 H" : {"mobil" : "All New Avanza 2022", "transmisi" : "MT", "warna" : "Coklat", "bahanBakar" : "Pertamax", "harga" : 425000, "statusPinjam" : True, "lamaHari" : 4},
         "D 4214 T" : {"mobil" : "New HRV 2022", "transmisi" : "AT", "warna" : "Silver", "bahanBakar" : "Pertamax", "harga" : 650000, "statusPinjam" : False, "lamaHari" : 0},  
         "D 4321 C" : {"mobil" : "New Fortuner 4x2", "transmisi" : "MT", "warna" : "Hitam", "bahanBakar" : "Dexlite", "harga" : 950000, "statusPinjam" : True, "lamaHari" : 1}, 
         "D 4332 L" : {"mobil" : "Alphard", "transmisi" : "AT", "warna" : "Hitam", "bahanBakar" : "Pertamax", "harga" : 3250000, "statusPinjam" : False, "lamaHari" : 0}}



customer = {"082121025700" : {"password" : "12345678", "nama" : "Willy", "alamat" : "Jl. Permana", "mobil" : ["D 4321 C"]},
            "08123456789" : {"password" : "23456789", "nama" : "Stefanus", "alamat" : "Jl. Abc", "mobil" : []},
            "0832132121" : {"password" : "34567890", "nama" : "Wina", "alamat" : "Jl. Def", "mobil" : ["D 2345 B", "D 1234 X"]}}


menuAwal(mobil, customer)