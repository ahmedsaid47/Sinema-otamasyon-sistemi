import Rezervasyon as mod
import Dosyaokuma as dos
toplamCiro=0.0
while (True):

    #girdi = seçim için kullanıcıdan alınır
    girdi=input("lütfen birini seçin\n1-Rezervasyon\n2-Salonu Yazdır\n3-Yeni Etkinlik\n4-Toplam Ciro\n0-çıkış")
    if (girdi=="1"):
        #k=kategori
        k=int(input("lütfen kategorinizi seçin1/2/3/4"))
        #s=sayı(bilet sayısı)
        s=int(input("lütfen bilet sayınızı yazın"))
        if(s<=dos.maxbilet):
            if (mod.Bosyervarmi(k, s)):
                mod.Rezervasyon(k, s)
                print("Rezervasyon gerçekleşti")
                print("Fiyat: ",dos.fiyathesapla(k,s))
                print("İndirimli fiyat: ",dos.indirimlifiyat(k,s,dos.fiyathesapla(k,s)))
                toplamCiro=toplamCiro+dos.indirimlifiyat(k,s,dos.fiyathesapla(k,s))
            else:
                print("malasef yeteri kadar yer yok")
        else:
            print("Alacağınız bilet max sayısı ",dos.maxbilet," \nlütfen daha düşük bir değer girin")
    elif(girdi=="2"):
        mod.Salonyazdir()

    elif(girdi=="3"):
        mod.Salonolustur()
    elif(girdi=="4"):
        print("Toplam Ciro",toplamCiro)
    else:
        print("iyi günler")
        break







