
#Global variabel
#mested list data barang untuk reseller
item_reseller = [
    ["S001",'360 Crystal Massager Lifting Eye Cream Eye Gel Serum', 'eye cream',279000,0.05, 200],
    ["S002",'5X Ceramide Barrier Series Moisturize Gel Moisturizer Cream', 'moisturizer', 249000,0.05, 273],
    ["S003",'Glowing Moisturizer Day & Night Cream Moisture Gel', 'moisturizer', 169000,0.05, 170],
    ["S004",'5X Ceramide Low pH Cleanser Facial Wash Gentle Cleanser', 'face wash',149000,0.5, 299],
    ["S005",'Tranexamic Acid 3% Advanced Bright Serum', 'serum',329000,0.10, 100],
    ["S006",'All Day Light Sunscreen Spray SPF50 PA++++ Sunscreen Mist', 'sunscreen',12900,0.10, 330],
]
list_title = ['kode', 'item', 'category', 'harga jual','diskon reseller', ' sisa stok']

#nested list data penjualan untuk admin
penjualan = [
    ["S001",'360 Crystal Massager Lifting Eye Cream Eye Gel Serum', 'eye cream',50000,279000, 100],
    ["S002",'5X Ceramide Barrier Series Moisturize Gel Moisturizer Cream', 'moisturizer',45000, 249000,227],
    ["S003",'Glowing Moisturizer Day & Night Cream Moisture Gel', 'moisturizer',40000, 169000, 330],
    ["S004",'5X Ceramide Low pH Cleanser Facial Wash Gentle Cleanser', 'face wash',25000, 149000, 201],
    ["S005",'Tranexamic Acid 3% Advanced Bright Serum', 'serum',50000, 329000, 400],
    ["S006",'All Day Light Sunscreen Spray SPF50 PA++++ Sunscreen Mist', 'sunscreen',32000,129000,670],
]
kolom_penjualan = ['kode', 'item', 'category', 'modal', 'harga','terjual']
#=========================================================================================================================================================

#=========================================================================================================================================================

#fitur filter pencarian data penjualan admin berdasarkan category
def data_key_category():
    #input kategori
    key_inputan = input('Masukan Category Item untuk mencari Item: ')

    #iniliasisasi nilai index  0
    idx = 0
    #total_index berisi panjang dari len penjualan -1 karena pakai index
    total_idx = len(penjualan) -1 

    for item in penjualan:
        # list category ada di index 2
        category = item[2]
        #key inputan di lower supaya nilai = category
        #memasukan kemungkinan dengan mencari 1-1
        if key_inputan.lower() == category:
            print('Deskripsi Data Penjualan Untuk Item yang Anda Cari, Sebagai Berikut:')
            print(kolom_penjualan[0], '\t\t:', item[0])
            print(kolom_penjualan[1], '\t\t:', item[1])
            print(kolom_penjualan[2], '\t:', category)
            print(kolom_penjualan[3], '\t\t:', item[3])
            print(kolom_penjualan[4], '\t\t:', item[4])
            print(kolom_penjualan[5], '\t:', item[5])
            baca_data_penjualan()
            break

        if key_inputan != category:
            #kodisi jika data yang dimasukan 
            if total_idx == idx:
                print('Data Tidak Tersedia Silahkan Input Kode Item Yang Tersedia')
                #data minta diinput lagi yang benar jadi panggil fungsi
                data_key_category()
                break
        #menemukan item terakhir
        idx = idx +1 

#fitur filter pencarian data penjualan admin berdasarkan kode
def data_key_kode():
    key_inputan = input('Masukan Kode Item untuk mecari Item: ')

    idx = 0
    total_idx = len(penjualan) -1 

    for item in penjualan:
        code = item[0]
        if key_inputan == code:
            print('berikut deskripsi data penjualan sktinfic untuk barang:')
            print(kolom_penjualan[0], '\t\t:', code)
            print(kolom_penjualan[1], '\t\t:', item[1])
            print(kolom_penjualan[2], '\t:', item[2])
            print(kolom_penjualan[3], '\t\t:', item[3])
            print(kolom_penjualan[4], '\t\t:', item[4])
            print(kolom_penjualan[5], '\t:', item[5])
            baca_data_penjualan()
            break

        if key_inputan != code:
            if total_idx == idx:
                    print('data tidak tersedia silahkan input kode item yang tersedia')
                    data_key_kode()
                    break
        idx = idx +1

#tabel data penjualan admin
def data_penjualan():
    print(43*(' '),'Daftar Data Penjualan Skintific',43*(' '))
    print(120 *'=')
    print('|',kolom_penjualan[0], 5*' ','|', kolom_penjualan[1], 53*' ','|', kolom_penjualan[2],' ','|', kolom_penjualan[3],'|', kolom_penjualan[4], 4*' ','|',kolom_penjualan[5],1*'','|')
    print(120 *'=')
  
    for i in penjualan:
        kolom_1 = i[0]
        kolom_2 = i[1] 
        kolom_3 = i[2]
        kolom_4 = i[3]
        kolom_5 = i[4]
        kolom_6 = i[5]

        #pembatas + index kolom +(panjang len kolom - total len kolom) maka dari itu nilainya beda2
        print('| '+ kolom_1 +(11-len(kolom_1))*" "
            +'| '+ kolom_2 +(59-len(kolom_2))*" "
            +'| '+ kolom_3 +(11-len(kolom_3))*" "
            + '| ' + str(kolom_4) + (6- len(str(kolom_4))) * " "
            + '| ' + str(kolom_5) + (11- len(str(kolom_5))) * " "
            + '| ' + str(kolom_6) + (7 - len(str(kolom_6))) * " "
            + '  |')
    print(120*"=")
    baca_data_penjualan()

#menu read data penjualan admin
def baca_data_penjualan():
    print('Pilih Tampilan Data Penjualan yang Diinginkan')
    daftar_menu = ['Tabel Data Penjulan', 'Berdarkan Kode', 'Berdasarkan Category','Kembali ke Menu Admin']
   
   #fungsi menu supaya ga nulis 1-1 nilai angka
   #inisialisasi idx = 1 supaya yang muncul angka 1 dulu
    idx = 1
    for i in daftar_menu:
        #fungsi str di idx in case masukan inputan dalam bentuk string,  tipe data ga bisa di campur
        print('klik',str(idx),'untuk menu', i)
        idx = idx +1
    
    nama_menu = input ('pilih menu: ')

    if nama_menu == '1':
        data_penjualan()
    elif nama_menu == '2':
        data_key_kode()
    elif nama_menu == '3':
        data_key_category()
    elif nama_menu == '4':
        menu_admin()
    else:
        print('Data tidak Tersedia, Silahkan Input Kembali')
        baca_data_penjualan()

#create data penjualan admin
def tambah_data_penjualan():
    print('Silahkan tambahkan item baru kedalam tabel data penjualan skintific')
    kode = input('masukan kode barang: ')
    item = input('masukan nama barang: ')
    category = input ('masukan kategori barang: ')
    modal = input ('masukan nominal modal: ')
    harga = input ('masukan harga jual: ')
    terjual = 0
    
    #karena modal dan harga str di ubah ke int
    try: 
        nilai_modal = int(modal)
    except ValueError : #value error nampung isi pesan yang bermasalah 
        nilai_modal = 0

    try:
        nilai_harga = int(harga)
    except ValueError:
        nilai_harga = 0

    #data disamakan dengan yang ada di tabel EYD
    edit_data= [kode.upper(), item.capitalize(), category.lower(),nilai_modal, nilai_harga, terjual]
    #print(produk_inputan)

    for item in penjualan:
        code = item[0]
        if code == kode.upper(): 
            print('Kode sudah terdaftar')
            tambah_data_penjualan()
            break
    
    penjualan.append(edit_data)
    print('item sudah ditambahkan silahkan cek pada tabel data penjualan')
    baca_data_penjualan()

#update data penjualan admin
def update_data_penjualan():
    print('Silahkan update item baru kedalam tabel data penjualan skintific')
    kode = input('masukan kode barang: ')
    
    idx = 0
    for item in penjualan:
        code = item[0]
        if kode == code: 
            break  
        idx = idx +1
    
    if idx > len(penjualan)-1:
        print('kode tidak ditemukan')
        update_data_penjualan()
    else:
        data_penjualan = penjualan[idx]
        item = input('masukan nama barang: ')
        category = input ('masukan kategori barang: ')
        modal = input ('masukan nominal modal: ')
        harga = input ('masukan harga jual: ')
        terjual = data_penjualan[5]

        try: 
            nilai_modal = int(modal)
        except ValueError:
            nilai_modal = 0

        try:
            nilai_harga = int(harga)
        except ValueError:
            nilai_harga = 0

        produk_inputan= [kode.upper(), item.capitalize(), category.lower(),nilai_modal, nilai_harga, terjual]
        penjualan[idx] = produk_inputan
        print('item sudah di update')
        baca_data_penjualan()

#delete data penjualan admin
def delete_list_penjualan():
    print.upper(25*(' '),'Hapus Data Barang penjualan skintific!',25*(' '))
    hapus_barang = input('Silahkan masukan kode barang yang ingin dihapus: ')

    idx = 0 
    for barang in penjualan:
        code = barang[0]
        if hapus_barang == code:
            break
        idx = idx+1  


    if idx > len(penjualan)-1:
        print('Data Tidak Ditemukan!\nSilahkan Masukan Kemabali Kode Barang')
        delete_list_penjualan()

    penjualan.pop(idx)
    print(25*(' '), 'item', idx ,'Skintific Telah di Hapus Dari Tabel Penjualan',25*(' '))
    baca_data_penjualan()

#menu utama admin
def menu_admin():
    print(25*('+'),'Welcome admin skintific',25*('+'))
    print(25*(' '),'Daftar Informasi laporan Penjualan',25*(' '))
    menu = ['Baca Data Penjualan', 'Tambah Data Penjualan','Update Data Penjualan', 'hapus List Penjualan', 'exit' ]
   
    idx = 1
    for i in menu:
        print('klik',str(idx),'untuk menu', i)
        idx = idx +1
    
    nama_menu = input ('silahkan pilih menu: ')
    
    if nama_menu == '1':
        baca_data_penjualan()
    elif nama_menu == '2':
        tambah_data_penjualan()
    elif nama_menu == '3':
        update_data_penjualan()
    elif nama_menu == '4':
        delete_list_penjualan()
    elif nama_menu == '5':
        print('exit')
    else:
        print(25*('+'),'Silahkan Masukan Data yang Ada Pada Daftar Menu',25*('+'))
        menu_admin()

#login admin max 3x
def login_admin():
    username = ['admin1','admin2']
    password = ['pass1','pass2']
    percobaan = 0
    sisa_percobaan = 3
    print(25*('+'),'Welcome Admin Skintific',25*('+'))
    while percobaan <3:
        if(percobaan >= 3):
            print(25*('+'),'Anda Sudan Mencapai Batas Percobaan Login',25*('+'))
            break
        else:
            ID = input('username: ')
            pswd = input('password: ')

            try :
                index_username = username.index(ID) 
                index_password = password.index(pswd)
                
                if index_username == index_password:
                    menu_admin()
                    break
                else:
                    percobaan +=1
                    sisa_percobaan -=1
                    print(25*(' '),'Sisa Percobaan Login Sebanyak', sisa_percobaan, 'Kali',25*(' '))
                    print(25*('+'),'Username atau Password Salah Silahkan Masukan Data Yang Benar',25*('+'))

            except ValueError :
                percobaan +=1
                sisa_percobaan -=1
                if percobaan >= 3:
                    print(' Anda Sudah Mencapai Batas Percobaan Login \n Silahkan hubungi CS Skintific Pada link Instagram Offical Kami @skintific.official')
                    break
                else:
                    print(25*(' '),'Sisa Percobaan Login Sebanyak', sisa_percobaan, 'Kali',25*(' '))
                    print(25*(' '),'username & password tidak terdaftar',25*(' '))    

#=========================================================================================================================================================
#inputan reseller cek harga disc
def harga_reseller():
    print(50*(' '),'Daftar harga reseller Skintific',65*(' '))
    print(132 *'=')
    print('|',list_title[0], 5*' ','|', list_title[1], 53*' ','|', list_title[2],' ','|', list_title[3],'|', list_title[4],'|',list_title[5],'|')
    print(132 *'=')
  
    for i in item_reseller:
        kolom_1 = i[0]
        kolom_2 = i[1] 
        kolom_3 = i[2]
        kolom_4 = i[3]
        kolom_5 = i[4]
        kolom_6 = i[5]
        print('| '+ kolom_1 +(11-len(kolom_1))*" "
            +'| '+ kolom_2 +(59-len(kolom_2))*" "
            +'| '+ kolom_3 +(11-len(kolom_3))*" "
            + '| ' + str(kolom_4) + (11- len(str(kolom_4))) * " "
            + '| ' + str(kolom_5) + (16- len(str(kolom_5))) * " "
            + '| ' + str(kolom_6) + (9 - len(str(kolom_6))) * " "
            + '  |')
    print(132*"=")

# #menu utama reseller
# def menu_reseller():
#     print(25*('+'),'Daftar Informasi reseller skintific',25*('+'))
#     menu = ['Cek Stok Barang','Hitung Harga Reseller', 'Exit' ]
   
#     idx = 1
#     for i in menu:
#         print('klik',str(idx),'untuk menu', i)
#         idx = idx +1
    
#     nama_menu = input ('silahkan pilih menu: ')
    
#     if nama_menu == '1':
#         harga_reseller()
#         menu_reseller()
#     elif nama_menu == '2':
#         cek_harga_seller()
#     elif nama_menu == '3':
#         print(25*('+'),'Sampai Jumpa Sahabat Reseller Skintific!',25*('+'))
#     else:
#         print('Pilihan Tidak Ada di Daftar Menu Silahkan Input Kembali')
#         menu_reseller()


# def cek_harga_seller():
#     key_inputan = input('Masukan Kode Item Untuk Tahu Harga Diskon: ')

#     while True:
#         jumlah_beli = input('Masukan Jumlah Item Untuk Tahu Harga Diskon: ')
#         if jumlah_beli.isdigit():
#             jumlah_beli = int(jumlah_beli)
#             break
#         else:
#             print('Silahkan Masukan Data Sesuai Permintaan')

#     for item in item_reseller:
#         code = item[0]
#         if key_inputan == code: 
#             found = True
#             stok_barang = item
#             print(list_title[0], '\t\t\t\t:', stok_barang[0])
#             print(list_title[1], '\t\t\t\t:', stok_barang[1])
#             print(list_title[2], '\t\t\t:', stok_barang[2])
#             print(list_title[3], '\t\t\t:', stok_barang[3])
#             print(list_title[4], '\t\t:', stok_barang[4])
#             print(list_title[5], '\t\t\t:', stok_barang[5])
            

#             harga_jual = stok_barang[3]
            
#             jumlah_barang = stok_barang[4]

#             harga_diskon = harga_jual * stok_barang[4]

#             total_harga= (harga_jual - harga_diskon)* jumlah_beli


#             print(f'Harga Reseller Resmi Untuk Pembelian {jumlah_beli} Item Adalah {round(total_harga)} Rupiah')
#             menu_reseller()
#             break
    
#     if not found:
#         print('Silahkan Masukan Kembali Data Dengan Benar')

cek_harga_seller()
#tabel harga reseller

#login reseller max 3x
def login_reseller():

    username = ['reseller1','reseller2']
    password = ['seller1', 'seller2']
    percobaan = 0
    sisa_percobaan = 3
    print(25*('+'),'Welcome Sahabat Reseller Skintific',25*('+'),'\n',25*(' '),'Silahkan Masukan ID dan Password',25*(' '))
    while percobaan <3:
        if(percobaan >= 3):
            print('gagal login sudah 3x')
            break
        else:
            ID = input('Username: ')
            pswd = input('Password: ')

            try :
                index_username = username.index(ID) 
                index_password = password.index(pswd)
                
                if index_username == index_password:
                    menu_reseller()
                    break
                else:
                    percobaan +=1
                    sisa_percobaan -=1
                    print('Silahkan Masukan Kembali Password dan Username yang Benar')
                    print('Sisa Percobaan Anda Sebanyak', sisa_percobaan, 'Kali')
                    

            except ValueError :
                percobaan +=1
                sisa_percobaan -=1
                if percobaan >= 3:
                    print(' Anda Sudah Mencapai Batas Percobaan Login \n Silahkan hubungi CS Skintific pada link instagram offical kami @skintific.official')
                    break
                else:
                    print('Username dan Password Tidak Terdaftar, Mohon Cek kembali password')   
                    print('Sisa Percobaan Anda Sebanyak', sisa_percobaan, 'Kali') 

#menu login admin/reseller/keluar
def menu():
    print(25*('+'),'Welcome to Skintific!', 25*('+'))
    menu = ['admin','reseller','exit']
    idx = 1
    for i in menu:
        print('klik',idx,'untuk login sebagai', i)
        idx = idx +1
    
    nama_menu = input ('pilih menu: ')

    if nama_menu == '1':
        login_admin()
    elif nama_menu == '2':
        login_reseller()
    elif nama_menu == '3':
        ('log out')
    else:
        print('Pilihan Tidak Terdaftar Dalam Kolom Menu, Silahkan Input Kembali')
        menu()

menu()