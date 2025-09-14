Tiket_vip = ["1","2","3","4","5","6","7","8","9","10",
"11","12","13","14","15","16","17","18","19","20"]

Tiket_reguler = ["21","22","23","24","25","26","27","28","29","30",
"31","32","33","34","35","36","37","38","39","40",
"41","42","43","44","45","46","47","48","49","50",
"51","52","53","54","55","56","57","58","59","60",
"61","62","63","64","65","66","67","68","69","70",
"71","72","73","74","75","76","77","78","79","80",
"81","82","83","84","85","86","87","88","89","90",
"91","92","93","94","95","96","97","98","99","100"]

Data_pusat = []

while True : 
    print("--------------------------------------------")
    print("Menu")
    print("--------------------------------------------")
    print("1. Mengecek VIP Atau Reguler")
    print("2. Pengecekan Kursi VIP dan Reguler")
    print("3. Memasukkan Tiket Ke Data Pusat ")
    print("4. Menghapus Tiket Dari Data List Tiket ")
    print("5. Logout")
    print("--------------------------------------------")

    Menu = int(input ("Pilih Menu Apa: "))

    # Cara pengecekan tiket VIP atau Reguler
    if Menu == 1:
        Pengecekan_tiket1 = input("Sebutkan No Tiket Untuk Mengecek Jenis Tiket: ")
        if Pengecekan_tiket1 in Tiket_vip :
            print ("Tiket Ini Adalah Vip")
        else :
            print ("Tiket Ini Adalah Reguler")

    # Untuk Mengecek Kursi

    if Menu == 2:
        Pengecekan_tiket2 = input("Sebutkan No Tiket Untuk Mengecek Kursi: ")
        if Pengecekan_tiket2 == Tiket_vip[0]:
            print("Kursi Anda adalah A1")
        elif Pengecekan_tiket2 == Tiket_vip[1]:
            print("Kursi Anda adalah A2")
        elif Pengecekan_tiket2 == Tiket_vip[2]:
            print("Kursi Anda adalah A3")
        elif Pengecekan_tiket2 == Tiket_vip[3]:
            print("Kursi Anda adalah A4")
        elif Pengecekan_tiket2 == Tiket_vip[4]:
            print("Kursi Anda adalah A5")
        elif Pengecekan_tiket2 == Tiket_vip[5]:
            print("Kursi Anda adalah A6")
        elif Pengecekan_tiket2 == Tiket_vip[6]:
            print("Kursi Anda adalah A7")
        elif Pengecekan_tiket2 == Tiket_vip[7]:
            print("Kursi Anda adalah A8")
        elif Pengecekan_tiket2 == Tiket_vip[8]:
            print("Kursi Anda adalah A9")
        elif Pengecekan_tiket2 == Tiket_vip[9]:
            print("Kursi Anda adalah A10")
        elif Pengecekan_tiket2 == Tiket_vip[10]:
            print("Kursi Anda adalah B1")
        elif Pengecekan_tiket2 == Tiket_vip[11]:
            print("Kursi Anda adalah B2")
        elif Pengecekan_tiket2 == Tiket_vip[12]:
            print("Kursi Anda adalah B3")
        elif Pengecekan_tiket2 == Tiket_vip[13]:
            print("Kursi Anda adalah B4")
        elif Pengecekan_tiket2 == Tiket_vip[14]:
            print("Kursi Anda adalah B5")
        elif Pengecekan_tiket2 == Tiket_vip[15]:
            print("Kursi Anda adalah B6")
        elif Pengecekan_tiket2 == Tiket_vip[16]:
            print("Kursi Anda adalah B7")
        elif Pengecekan_tiket2 == Tiket_vip[17]:
            print("Kursi Anda adalah B8")
        elif Pengecekan_tiket2 == Tiket_vip[18]:
            print("Kursi Anda adalah B9")
        elif Pengecekan_tiket2 == Tiket_vip[19]:
            print("Kursi Anda adalah B10")
        else :
            print ("Penonton Tidak Memiliki Kursi Khusus dan Bisa Menonton Dengan Berdiri") 

    # Untuk Menambahkan tiket ke data pusat

    if Menu == 3 :
        Pengecekan_tiket3 = input("Sebutkan No Tiket Untuk Dimasukkan Ke Data Pusat: ")
        Data_pusat.append(Pengecekan_tiket3)
        print(f"{Pengecekan_tiket3} Sudah Di Masukkan")
        print(Data_pusat)

    if Menu == 4:
            Pengecekan_tiket4 = input("Sebutkan No Tiket Untuk Di Hapus: ")
            if Pengecekan_tiket4 in Tiket_vip:
                Tiket_vip.remove(Pengecekan_tiket4)
                print (f"{Pengecekan_tiket4} Sudah Terhapus")
            else:
                Tiket_reguler.remove(Pengecekan_tiket4)
                print (f"{Pengecekan_tiket4} Sudah Terhapus")
            print (Tiket_vip)
            print (Tiket_reguler)

    if Menu == 5:
        print ("Anda Sudah Keluar")
        break
