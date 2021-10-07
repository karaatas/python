def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(":")
    ogrenciAdi = liste[0]
    notlar = liste[1].split(",")
    not1 = int(notlar[0])
    not2 = int(notlar[1])
    not3 = int(notlar[2])
    ortalama = (not1+not2+not3)/3

    if ortalama > 90 and ortalama<=100:
        harf = "AA"
    elif ortalama>80 and ortalama<=90:
        harf = "AB"
    elif ortalama>60 and ortalama<=80:
        harf = " BB"
    elif ortalama>40 and ortalama<=60:
        harf = "BC"
    else:
        harf = "CC"
    return ogrenciAdi + ":" + harf + "\n"
    
def ortalamalari_oku():
    with open("sinav_notlari.txt") as file:
        # result= file.read()
        # print(result)
        for satir in file:
            print(not_hesapla(satir))

def not_gir():
    ad = input("ad:")
    soyad = input("soyad:")
    not1 = input("not 1:")
    not2 = input("not 2:")
    not3 = input("not 3:")
    with open("sinav_notlari.txt","a", encoding="utf-8") as file:
        file.write(ad+" "+ soyad+ ":"+not1+","+not2+","+not3+"\n")

def not_kayit():
    with open("sinav_notlari.txt", "r") as file:
       liste = []
       for i in file:
           liste.append(not_hesapla(i))
    with open("sonuclar.txt", "w", encoding="utf-8") as file2:
            for i in liste:
                file2.write(i)

while True:
    islem = input("1-Notları oku\n2-Not gir\n3-not kayıt et\n4-çıkış\n")

    if islem == "1":
        ortalamalari_oku()
    elif islem == "2":
        not_gir()
    elif islem == "3":
        not_kayit()
    else:
        break