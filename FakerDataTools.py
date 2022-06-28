#!/usr/bin/env python3


def Faker_Data_Tools(created_by="Ruben Leonardo Sigalingging."):
	import faker
	from faker import Faker
	from os import system
	system("clear")
	from sys import version_info
	from faker.providers import internet
	from pyfiglet import figlet_format
	tema=figlet_format("Faker",font="slant")
	print(tema)
	print("[!] Dibuat Oleh: Ruben Leonardo Sigalingging.")
	print("[!] Dibuat Pada: Selasa, 28 Juni 2022, Pukul 8:55 PM.")
	print("[!] Menggunakan: Python Versi 3.8.10\n")


	fake=Faker()
	# print(fake)
	# BUAT PERULANGAN UNTUK MENAMPILKAN NAMA DENGAN BANYAKKK :)
	# GASSS EAAAA
	pilih_lokasi_negara=str(input("\033[91m[\033[94m+\033[91m] \033[94mPilih Lokasi Negara\n\n\033[91m[\033[94m+\033[91m] \033[94m'Italia' -> \033[91m'it_IT'\n\033[91m[\033[94m+\033[91m] \033[94m'Indonesia' -> \033[91m'id_ID'\n\033[91m[\033[94m+\033[91m] \033[94m'Amerika' -> \033[91m'en-US'\n\033[91m[\033[94m+\033[91m] \033[94m'Jepang' -> \033[91m'jp_JP'\n\n\n\033[91m[\033[94m+\033[91m] \033[94mPilih Disini: \033[91m"))
	pembuat_nama_palsu=Faker(pilih_lokasi_negara)
	print("\n")
	jumlah_nama_palsu=int(input("\033[91m[\033[94m+\033[91m] \033[94mMau Buat \033[91mBerapa Nama: \n\033[91m[\033[94m+\033[91m] \033[94m1-50: \033[91m"))
	print("\n")
	for nama_palsu in range(jumlah_nama_palsu):
		print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Name: \033[91m{pembuat_nama_palsu.name()}")
	print("\n")
	print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Address: \033[91m{fake.address()}")
	print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Email: \033[91m{fake.email()}")
	print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Text: \033[91m{fake.text()}")
	print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Latitude: \033[91m{fake.latitude()}")
	print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Longitude: \033[91m{fake.longitude()}")
	print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Private IP Address: \033[91m{fake.ipv4_private()}")
	print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Public IP Address: \033[91m{fake.ipv4_public()}")
	# print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Medical Profession: \033[91m{fake.medical_profession()}")
	# print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Foo: \033[91m{fake.foo()}")
	# print(f"\033[91m[\033[94m+\033[91m] \033[94mFake Random: \033[91m{fake.random()}")

Faker_Data_Tools()