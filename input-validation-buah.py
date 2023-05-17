# Type your answere here

import sys
import pyinputplus as pypi

def show(Dict, printFormat, title="\nDaftar Buah yang Tersedia\n"):
    """_summary_

    Args:
        Dict (dictionary): dict yang akan ditampilkan
        printFormat (string): format tampilan di prompt
        title (str, optional): judul tampilan. Defaults to "\nDaftar Buah yang Tersedia\n".
    """
    # Menampilkan judul
    print(title)
    # Loop item di dalam listFruit
    for value in Dict.values():
        # Menampilkan item berdasarkan format
        print(printFormat.format("", *value))


def add():
    # Meminta input buah, jumlah, dan harga
    nameFruit = pypi.inputStr("Masukkan nama buah: ", applyFunc=lambda x: x.capitalize(), blockRegexes=[r'[0-9]'])
    countFruit = pypi.inputInt(prompt="Masukkan stock buah: ")
    priceFruit = pypi.inputInt(prompt="Masukkan harga buah: ")
    # Loop item di dalam listFruit
    for key, value in listFruit.items():
        # Apabila buah sudah ada di dalam daftar
        if nameFruit in value:
            listFruit[key][2] += countFruit
            listFruit[key][3] = priceFruit
            break
    # Apabila buah tidak ada di dalam daftar
    else:
        index = len(listFruit) - 1
        listFruit.update({
            f'buah-{index}': [
                index, 
                nameFruit,
                countFruit,
                priceFruit
            ]
            }
        )
    # Menampilkan daftar buah terbaru
    show(listFruit, printFormat)


def delete():
    # Input indeks buah yang akan dihapus
    index = pypi.inputInt(prompt="Masukkan indeks buah yang ingin dihapus: ", lessThan=len(listFruit)-1)
    # Menghapus buah berdasarkan indeks
    del listFruit[f'buah-{index}']
    # Update indeks buah yang tersisa
    for key, value in listFruit.items():
        if key != 'column' and value[0] > index:
            del listFruit[key]
            listFruit.update({
                f'buah-{value[0] - 1}': [
                    value[0]-1, 
                    value[1], 
                    value[2], 
                    value[3]]
                }
            )
    # Menampilkan daftar buah terbaru
    show(listFruit, printFormat)


def buy():
    # Deklarasi variabel 'listChart'
    listChart = {
        'column': ["nama", "qty", "harga"],
    }
    while True:
        # Menampilkan data buah terbaru
        show(listFruit, printFormat)
        # Input indeks dan jumlah buah yang akan dibeli
        index = pypi.inputInt(prompt="\nMasukkan index buah yang ingin dibeli: ", lessThan=len(listFruit)-1)
        nameFruit = listFruit[f'buah-{index}']
        countFruit = pypi.inputInt(prompt="Masukkan jumlah yang ingin dibeli: ", )
        # Jika jumlah pesanan tidak terpenuhi, tampilkan pesan stock kurang
        if countFruit > nameFruit[2]:
            print(f"Stock tidak cukup, stock {nameFruit[1]} tinggal {nameFruit[2]}")
        # Selain itu, tambahkan ke 'listChart'
        else:
            index = len(listChart) - 1
            listChart.update({
                f'buah-{index}': [
                    nameFruit[1],
                    countFruit,
                    nameFruit[3]
                    ]
                }
            )
            # Kurangi persedian stock buah yang dipesan
            nameFruit[2] -= countFruit
            # Tampilkan isi keranjang belanjaan
            chartFormat = "{:<4}" + "{:<10}" * (len(listChart['column']))
            show(listChart, chartFormat, title="\nIsi Keranjang Anda\n")
            # Konfirmasi user apakah akan re-order
            reorder = pypi.inputYesNo(prompt="\nIngin beli yang lain? (Yes/No) ")
            if reorder.lower() == "no":
                break

    # Proses kalkulasi total harga
    for key, value in listChart.items():
        if key == 'column':
            value.append('total harga')
            listChart[key] = value
        else:
            # Kalkulasi Qty x Harga
            value.append(value[1] * value[2])
            listChart[key] = value

    # Proses pembayaran
    while True:
        # Menampilkan daftar belanja
        show(listChart, printFormat, title="\nDaftar Belanjaan Anda\n")
        # Hitung total harga yang harus dibayar
        price = 0
        for value in listChart.values():
            if value[-1] != 'total harga':
                price += value[-1]
        print(f"\nTotal yang harus dibayar: {price}")
        # Input jumlah uang pembayaran
        pay = pypi.inputInt(prompt="Masukkan jumlah uang: ")
        # Jika uang kurang, tampilkan pesan uang kurang
        # Minta user input ulang jumlah uang pembayaran
        if pay - price < 0:
            print(f"Uang anda kurang sebesar {abs(pay - price)}")
        # Sebaliknya, tampilkan kembalian dan terima kasih
        else:
            print(f"Uang kembalian anda {pay - price}, terima kasih.")
            break
    # Clear keranjang belanja
    del listChart


def main():
    while True:
        # Menampilkan tampilan utama program
        print(
            """
Selamat datang di pasar buah

    List menu:

    1. Menampilkan daftar buah
    2. Menambah buah
    3. Menghapus buah
    4. Membeli buah
    5. Exit
"""
        )
        # Input fitur yang akan dijalankan
        menuNumber = pypi.inputInt(prompt="Masukkan angka menu yang ingin dijalankan: ", lessThan=6, greaterThan=0)
        # Fitur menampilkan daftar buah
        if menuNumber == 1:
            show(listFruit, printFormat)
        # Fitur menambahkan buah
        elif menuNumber == 2:
            add()
        # Fitur menghapus buah
        elif menuNumber == 3:
            delete()
        # Fitur membeli buah
        elif menuNumber == 4:
            buy()
        # Fitur exit program
        else:
            sys.exit()


if __name__ == "__main__":
    # Deklrasi variabel 'listFruit'
    listFruit = {
        'column': ["index", "nama", "stock", "harga"],
        'buah-0': [0, "Apel", 20, 10000],
        'buah-1': [1, "Anggur", 25, 20000],
        'buah-2': [2, "Jeruk", 15, 15000],
    }
    # Deklarasi format tampilan di prompt
    printFormat = "{:<4}" + "{:<10}" * (len(listFruit['column']))
    # Menjalankan fungsi utama main()
    main()