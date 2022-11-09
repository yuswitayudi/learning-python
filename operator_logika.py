nama = input("Please input your name: ")
bypass = "admin"
if len(nama) > 8 or bypass == nama:
    print("oke masuk", nama)
else:
    print("Nama anda terlalu pendek maseh")