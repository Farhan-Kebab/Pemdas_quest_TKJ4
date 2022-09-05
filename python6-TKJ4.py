
list_kosong = []
list_buah = ['Pisang', 'Nanas', 'Melon', 'Durian']
list_nilai = [80, 70, 90, 60]
list_jawaban = [150, 33.33, 'Presiden Sukarno', False]
print(list_kosong, list_buah, list_nilai, list_jawaban)

print(list_buah[0])
print(list_buah[2])
print(list_buah[1])
print(list_buah[3])

print(list_buah[0:1])
print(list_buah[0:2])
print(list_buah[1:3])
print(list_buah[0:-1])
print(list_buah[-1:-3])
print(list_buah[-1:3])
print(list_buah[-3:-1])

print(list_buah[0:])
print(list_buah[1:])
print(list_buah[2:])
print(list_buah[3:])
print(list_buah[:0])
print(list_buah[:1])
print(list_buah[:2])
print(list_buah[:3])
print(list_buah[:4])

# ubah data pertama
list_buah[0] = 'Jeruk'

print(list_buah)

# ubah data terakhir
list_buah[-1] = 'Mangga'

print(list_buah)

# ubah data dalam range
list_buah[1:3] = ['Naga', 'Pepaya']

print(list_buah)

# tambah data di belakang list
list_buah.append('Sirsak')
print(list_buah)