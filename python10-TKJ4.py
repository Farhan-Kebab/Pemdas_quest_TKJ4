# Membuat Tipe Data List

koleksi_data_str = ["Pisang", "Pangga", "Jambu", "Semangka"]

koleksi_data_int = [200, 300, 400, 500]

koleksi_data_mix = ["Rizky Billar", 100, True, "Reza Arap"]

print("koleksi data string:", koleksi_data_str)

print("koleksi data integer:", koleksi_data_int)

print("koleksi data campuran:", koleksi_data_mix)

# buatlah 3 kumpulan data: Nama hewan, Nilai UTS, Nama teman sebangku kalian

list_nama_hewan = ["anjing", "babi", "elang"]

list_nilai_uts = [76, 50, 45,]

list_teman_sebangku = ["ilal aseli", "fajri roblox", "rifqi cepot", "angga sepuh kapal"]

print("list Nama Hewan:", list_nama_hewan)

print("List Nilai UTS:", list_nilai_uts)

print("List Nama Teman Sebangku:", list_teman_sebangku)

# data ke-2 nama hewan
print("data ke-2 nama hewan:", list_nama_hewan[1])

# data ke-3 nilai uts
print('data ke-3 nilai uts:', list_nilai_uts[2])

# data ke-1 nama teman sebangku
print('data ke-1 nama teman sebangku:', list_teman_sebangku[1])

# tambahkan 1 data disetiap data koleksi

list_nama_hewan.append('icikiwir')
list_nilai_uts.append('93')
list_teman_sebangku.append('bandar apran')

# ubahlah data ke-3 nama hewan

list_nama_hewan[2] = 'penguin'
print(list_nama_hewan)

