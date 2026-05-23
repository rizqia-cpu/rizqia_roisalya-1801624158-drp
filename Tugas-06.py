from datetime import datetime

print("hai, selamat pagi!")
print("kamu lagi mau melakukan aktivitas apa nih pagi hari ini?")
print("mau sarapan")
print("mau pergi kerja")

aktivitas = input ("masukkan aktivitas yang ingin kamu lakukan sekarang:")

if aktivitas.lower() == "mau sarapan":
    print("okei siap, mau sarapan apa hari ini? berikut pilihan menunya!")
    print("telur")
    print("ikan")
    print("nugget")

    menu = input ("ketik menu sarapan yang kamu mau:")

    if menu.lower() == "telur" or menu.lower () == "ikan" or menu.lower() == "nugget":
        print (f"wow, pilihan bagus, {menu} tersedia. silakan dimasak terlebih dahulu, ya!")
    else:
     print(f"noo, pilihan kamu ngga tersedia. kamu harus beli bahannya dulu nih!")

elif aktivitas.lower()== "mau pergi kerja":
   waktu = datetime.now()
   print("wow, okei! wait, lemme check the time!")
   print(f"hm... sekarang sudah pukul {waktu}")

   if waktu.hour < 08.00:
    print("nah, masih ada waktu nih, ayo semangat siap-siapnya!")
   elif waktu.hour == 08.00:
    print("ehh, sudah jam 08.00 tau, besok-besok lebih awal ya!")
   else:
    print("waduh, ini mah udah telat, gimana sih kamu?! lain kali lebih serius dong!")
    