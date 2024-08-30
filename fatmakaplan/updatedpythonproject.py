import random
def tas_kagit_makas_FATMA_KAPLAN():
    print("TAŞ KAĞIT MAKAS ATEŞ OYUNU")
    print("Oyunun kuralları aşağıdaki gibidir:")
    print("1) Taş makası yener.")
    print("2) Kağıt taşı yener.")
    print("3) Makas kağıdı yener.")
    print("4) Ateş kağıdı yener.")
    print("5) Taş ateşi yener")
    print("6) Makas ateşi yener.")

    while True:
        player_wins=0
        pc_wins=0

        while pc_wins<2 and player_wins<2:
            print("Yeni Tur Başlıyor...")
            print("Taş,Kağıt,Makas veya Ateş 'i seçiniz. ")
            player_choose=input("Taş,Kağıt,Makas veya Ateş: ").lower()

            while player_choose not in ["taş","kağıt","makas","ateş"]:
                print("Geçersiz hamle seçimi yaptınız,lütfen dört seçenekten birini seçin.")
                player_choose=input("Taş,Kağıt,Makas,Ateş").lower()

            pc_choose= random.choice(["taş","kağıt","makas","ateş"])
            print(f"Bilgisayarın seçimi:{pc_choose}")

            if pc_choose==player_choose:
                print("Berabere")

            elif (player_choose=="taş" and pc_choose=="makas")or\
                 (player_choose=="taş" and pc_choose=="ateş")or\
                 (player_choose=="ateş" and pc_choose=="kağıt")or\
                 (player_choose=="kağıt" and pc_choose=="taş") or\
                 (player_choose=="makas"and pc_choose=="kağıt"):
                 print("Siz kazandınız!")
                 player_wins+=1

            else:
                print("Bilgisayar kazandı!")
                pc_wins+=1

            print(f"Skor Tablosu:"
                  f"Siz:{player_wins} - Bilgisayar:{pc_wins}")

        if player_wins==2:
            print("Tebrikler,siz kazandınız!")

        else:
            print("Maalesef kaybettiniz,bilgisayar kazandı!")

        while True:
            continue_ = input("Bir kez daha oynamak ister misiniz (Evet/Hayır): ").lower()
            pc_continue = random.choice(["evet", "hayır"])

            if continue_ == "evet" and pc_continue == "evet":
                print("Yeni oyun talebi karşılıklı onaylandı.")
                break
            elif continue_ == "hayır" or pc_continue == "hayır":
                print("Bilgisayar yeni oyun talebini reddetti. Oyun bitti.")
                return
            else:
                print("Geçersiz yanıt. Lütfen 'Evet' veya 'Hayır' yazın.")


if __name__=="__main__":
    tas_kagit_makas_FATMA_KAPLAN()
