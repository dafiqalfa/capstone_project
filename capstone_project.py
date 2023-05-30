import sys
import pyinputplus as pypi
import csv
import tabulate
import os

def show(dataBarang, title="\nDaftar Barang\n"):
    """_summary_

    Args:
        Dict (dictionary): dict yang akan ditampilkan
        printFormat (string): format tampilan di prompt
        title (str, optional): judul tampilan. Defaults to "\nDaftar Barang\n".
    """
    # menggambil baris dari index 1 dari database
    data = list(dataBarang.values())[1:]
    # variabel sementara untuk menyimpan perubahan
    data1 = []
    # menggambil columns dari index 0 sampai 5
    columns1 = headingsDataBarang[:6]
    # looping untuk menampilkan setiap data index i
    for i, values in enumerate(data): #[0]
        data2 = list(dataBarang.values())[1:][i][:5]
        data1.append(data2)

    while True:
        choice = ['Tampilkan data barang', 'Tampilkan detail barang','Kembali ke menu utama']
        inputSub = pypi.inputMenu(choices=choice, numbered=True)
        if inputSub == 'Tampilkan data barang':
            print(title)
            if data1 == []:
                # only display columns without any data
                print(tabulate.tabulate(data1, headers=columns1, tablefmt="github"))
                print("\nData doesn't exist!")
            else:
                # print database in tabular format
                print(tabulate.tabulate(data1, headers=columns1, tablefmt="github"))
                print('\n')

        elif inputSub == 'Tampilkan detail barang':
            idBarang = pypi.inputStr(prompt='Masukkan id barang: ', applyFunc=lambda x: x.upper(), blockRegexes=[r'[!@#$%^&*:;,.?]'])
            for i, value in enumerate(data):
                if idBarang in value:
                    datadetail = [['ID barang', data[i][0]],
                                 ['Nama Barang', data[i][1]],
                                 ['Tanggal', data[i][2]],
                                 ['Harga Jual', data[i][3]],
                                 ['Jumlah', data[i][4]],
                                 ['Sales', data[i][5]],
                                 ['Harga Beli', data[i][6]]]
                    print(tabulate.tabulate(datadetail, headers=['Data','Detail'], tablefmt="github"))
                    break
                elif i == len(data)-1:
                    print('ID barang tidak ada!')
        else :
            main()

def add():    
    choice = ['Tambahkan barang','Kembali ke menu utama']
    inputSub = pypi.inputMenu(choices=choice, numbered=True)
    if inputSub == 'Tambahkan barang':
        idBarang = pypi.inputStr(prompt='Masukkan id barang: ', applyFunc=lambda x: x.upper(), blockRegexes=[r'[!@#$%^&*:;,.?]'])
        for i, value in enumerate(dataBarang.copy().values()):
            if idBarang in value:
                print('ID barang sudah ada')
                add()
            elif i == len(dataBarang)-1:
                inputSub2 = pypi.inputYesNo(prompt='ID barang belum ada. Lengkapi detail barang (yes/no): ')
                if inputSub2 == 'yes':
                    inputIdBarang = pypi.inputStr(prompt='Masukkan id barang: ', applyFunc=lambda x: x.upper(), blockRegexes=[r'[!@#$%^&*:;,.?]'])
                    inputNamaBarang = pypi.inputStr(prompt='Masukkan nama barang: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|!@#$%^&*:;,.?]'])
                    inputSales = pypi.inputStr(prompt='Masukkan sales: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[!@#$%^&*:;,.?]'])
                    inputTanggal = str(pypi.inputDate(prompt='Masukkan tanggal (format YYYY/MM/DD): '))
                    inputHrgBeli = pypi.inputInt(prompt='Masukkan harga beli: ')
                    inputHrgJual = pypi.inputInt(prompt='Masukkan harga jual: ')
                    inputJmlBarang = pypi.inputInt(prompt='Masukkan jumlah barang: ')
                    keys1 = len(dataBarang)
                    inputSub3 = pypi.inputYesNo(prompt='Pastikan data yang anda masukkan sudah benar, apakah akan menyimpan data tersebut? (yes/no): ')
                    if inputSub3 == 'yes':
                        print('Data berhasil ditambahkan')
                        dataBarang.update({f'barang-{keys1}': [inputIdBarang, inputNamaBarang, inputTanggal, inputHrgJual, inputJmlBarang, inputSales, inputHrgBeli, ]})
                    else:
                        add()
                else:
                    add()
    else :
        main()

def delete():
    choice = ['Hapus barang','Kembali ke menu utama']
    inputSub = pypi.inputMenu(choices=choice, numbered=True)
    if inputSub == 'Hapus barang':
        delBarang = input(f'Masukkan ID Barang: ').upper()
        j = 0
        for i, value in dataBarang.copy().items():
            if delBarang in value:
                datadetail = [['ID barang', value[0]],
                                 ['Nama Barang', value[1]],
                                 ['Tanggal', value[2]],
                                 ['Harga Jual', value[3]],
                                 ['Jumlah', value[4]],
                                 ['Sales', value[5]],
                                 ['Harga Beli', value[6]]]
                print(tabulate.tabulate(datadetail, headers=['Data','Detail'], tablefmt="github"))
                inputSub1 = pypi.inputYesNo(prompt='ID barang ada. Yakin tetap menghapus? (yes/no): ')
                if inputSub1 == 'yes':
                    print('Data barang terhapus')
                    del dataBarang[i]
                    break
                else :
                    delete()
            
            elif j == len(dataBarang) -1:
                print('ID barang tidak ada')
                delete()
            j += 1
        delete()
    else :
        main()
    return dataBarang

def update():
    choice = ['Rubah data barang','Kembali ke menu utama']
    inputSub = pypi.inputMenu(choices=choice, numbered=True)
    if inputSub == 'Rubah data barang':
        idBarang = input(f'Masukkan ID barang: ').upper()
        x = 0
        for key, value in dataBarang.copy().items():
            if idBarang in value:
                datadetail = [['ID barang', value[0]],
                                 ['Nama Barang', value[1]],
                                 ['Tanggal', value[2]],
                                 ['Harga Jual', value[3]],
                                 ['Jumlah', value[4]],
                                 ['Sales', value[5]],
                                 ['Harga Beli', value[6]]]
                print(tabulate.tabulate(datadetail, headers=['Data','Detail'], tablefmt="github"))
                inputSub1 = pypi.inputYesNo(prompt='Apa anda akan merubah data barang tersebut? (yes/no): ')
                if inputSub1 == 'yes':
                    prompt = "Pilih data yang ingin dirubah\n"
                    choice = ['Nama barang','Tanggal','Harga jual','Jumlah','Sales','Harga beli',]
                    inputSub3 = pypi.inputMenu(prompt = prompt, choices=choice, numbered=True)
                    for j, value in enumerate(dataBarang.copy().values()):
                        k = key
                        if inputSub3 == 'Nama barang':
                            inputNamaBarang = pypi.inputStr(prompt='Masukkan nama barang terbaru: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|!@#$%^&*:;,.?]'])
                            inputSub4 = pypi.inputYesNo(prompt='Pastikan nama barang yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            if inputSub4 == 'yes':
                                dataBarang[key][1] = inputNamaBarang
                                print(f'Nama barang berhasil dirubah')
                                update()
                                break
                            else :
                                update()
                        elif inputSub3 == 'Tanggal':
                            inputTanggal = str(pypi.inputDate(prompt='Masukkan tanggal (format YYYY/MM/DD): '))
                            inputSub4 = pypi.inputYesNo(prompt='Pastikan tanggal yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            if inputSub4 == 'yes':
                                dataBarang[key][2] = inputTanggal
                                print(f'Tanggal berhasil dirubah')
                                update()
                                break
                            else :
                                update()
                        elif inputSub3 == 'Harga jual':
                            inputHrgJual = pypi.inputInt(prompt='Masukkan harga jual barang terbaru: ')
                            inputSub4 = pypi.inputYesNo(prompt='Pastikan harga jual yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            if inputSub4 == 'yes':
                                dataBarang[key][3] = inputHrgJual
                                print(f'Harga jual berhasil dirubah')
                                update()
                                break
                            else :
                                update()
                        elif inputSub3 == 'Jumlah':
                            inputJml = pypi.inputInt(prompt='Masukkan jumlah barang terbaru: ')
                            inputSub4 = pypi.inputYesNo(prompt='Pastikan jumlah barang yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            if inputSub4 == 'yes':
                                dataBarang[key][4] = inputJml
                                print(f'Jumlah barang berhasil dirubah')
                                update()
                                break
                            else :
                                update()
                        elif inputSub3 == 'Sales':
                            inputNamaBarang = pypi.inputStr(prompt='Masukkan sales barang terbaru: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9|!@#$%^&*:;,.?]'])
                            inputSub4 = pypi.inputYesNo(prompt='Pastikan sales barang yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            if inputSub4 == 'yes':
                                dataBarang[key][5] = inputNamaBarang
                                print(f'Sales berhasil dirubah')
                                update()
                                break
                            else :
                                update()
                        elif inputSub3 == 'Harga beli':
                            inputHrgBeli = pypi.inputInt(prompt='Masukkan harga beli barang terbaru: ')
                            inputSub4 = pypi.inputYesNo(prompt='Pastikan harga beli yang anda masukan benar, apakah tetap akan menyimpan? (yes/no): ')
                            if inputSub4 == 'yes':
                                dataBarang[key][6] = inputHrgBeli
                                print(f'Harga beli berhasil dirubah')
                                update()
                                break
                            else :
                                update()          
                        break
                update()
            elif x == len(dataBarang) -1:
                print('Id barang tidak tersedia')
                update()
            x += 1
        update()
    else:
        main()

def laba():
    choice = ['Cek laba', 'Kembali ke menu utama']
    inputSub = pypi.inputMenu(choices=choice, numbered=True)
    if inputSub == 'Cek laba':
        # column laba
        columnsLaba = [headingsDataBarang[0], headingsDataBarang[3], headingsDataBarang[6], headingsDataBarang[4], 'Laba']

        # 2D data list 
        data = list(dataBarang.values())[1:]

        labaBarang1 = []
        for i in data:
            labaBarang1.append([i[0],i[3],i[6],i[4],(i[3]-i[6])*i[4]])

        # total laba
        totalLaba = []
        for i in labaBarang1:
            totalLaba.append(i[4])

        # show laba table
        print(tabulate.tabulate(labaBarang1, headers=columnsLaba, tablefmt='github'))
        print(f'\nTotal Keuntungan sebesar {sum(totalLaba)} rupiah\n')
        laba()
    else:
        main()
    

def main():
    while True:
        # Menampilkan tampilan utama program
        print(
            """
Laporan Penjualan Barang

    Pilih:

    1. Menampilkan daftar barang
    2. Menambah barang
    3. Menghapus barang
    4. Update barang
    5. Cek laba
    6. Exit
"""
        )
        # Input fitur yang akan dijalankan
        menuNumber = pypi.inputInt(prompt="Masukkan angka yang ingin dijalankan: ", lessThan=7, greaterThan=0)
        # Fitur menampilkan daftar barang
        if menuNumber == 1:
            show(dataBarang)
        # Fitur menambahkan barang
        elif menuNumber == 2:
            add()
        # Fitur menghapus barang
        elif menuNumber == 3:
            delete()
        # Fitur membeli barang
        elif menuNumber == 4:
            update()
        # Fitur cek laba
        elif menuNumber == 5:
            laba()
        # Fitur exit program
        else:
            #Export data ke csv
            fileDataBarang = open(pathBarang, 'w', newline='')
            writerDataBarang = csv.writer(fileDataBarang, delimiter=';')
            writerDataBarang.writerows(dataBarang.values())
            fileDataBarang.close()
            sys.exit()

if __name__ == "__main__":
    #Import dataBarang dari file csv
    pathBarang = 'D:\purwadhika\capstone_project_modul1\dataBarang.csv'

    fileDataBarang = open(pathBarang)
    readerDataBarang = csv.reader(fileDataBarang, delimiter= ';')
    headingsDataBarang = next(readerDataBarang) #list yg berisi kolom

    dataBarang = {'colums': headingsDataBarang}
    for row in readerDataBarang:
        dataBarang.update(
            {
                str(f'{row[0]}'):
                [str(row[0]),
                 str(row[1]),
                 str(row[2]),
                 int(row[3]),
                 int(row[4]),
                 str(row[5]),
                 int(row[6])
                 ]
            }
        )
    main()
