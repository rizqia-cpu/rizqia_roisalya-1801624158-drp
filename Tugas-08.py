print("Halo, boleh aku tahu siapa namamu?")
user = input("Namaku... ")

print(f"\nHai, salam kenal {user}! 👋🤩")
print("Aku mau nunjukkin kamu sesuatu, nih:")
print(f"\n ♟️  1. Papan Catur milik {user} ♟️")

for baris in range(8):
    print("        ", end="")
    for kolom in range(8):
        if (baris + kolom) % 2 == 0:
            print("⬜", end="")
        else:
            print("⬛", end="")
    print()
    
print(f"\n 📋 2. Daftar Aktivitas {user} 📋")
print("       Di sini kamu bisa mencatat aktivitas yang ingin kamu lakukan!")

Daftar_aktivitas = []
Jumlah_aktivitas = int(input(f"       Berapa banyak aktivitas yang perlu kamu lakukan, {user}? "))

for i in range(Jumlah_aktivitas):
    print(f"\n       🐈 Aktivitas ke-{i+1} 🐈")

    Nama_aktivitas = input("          Aktivitas  : ")
    Tenggat_aktivitas = input("          Deadline   : ")
    Keterangan_aktivitas = input("          Keterangan : ")

    Aktivitas= {
        "Aktivitas": Nama_aktivitas,
        "Deadline": Tenggat_aktivitas,
        "Keterangan": Keterangan_aktivitas
    }
    Daftar_aktivitas.append(Aktivitas)
print()

print("------------------------------")
print(f"\n🪴  Daftar Aktivitas yang Tercatat: 🪴")
print()

for i in range(len(Daftar_aktivitas)):
    print(f"💠 Kegiatan {i + 1} 💠")
    print(f"   Aktivitas  : {Daftar_aktivitas[i]['Aktivitas']}")
    print(f"   Deadline   : {Daftar_aktivitas[i]['Deadline']}")
    print(f"   Keterangan : {Daftar_aktivitas[i]['Keterangan']}")
    print()

print("------------------------------")
print("Total aktivitas:", len(Daftar_aktivitas))
print(f"Nah, sudah tercatat. Jangan lupa dikerjakan yaa, {user}! 💫")
print()