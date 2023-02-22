metin=open("Metin.txt","r")
fiyat={1:0,2:0,3:0,4:0}
katalog=[]
x=[]
x=metin.readline()
y=x.split("-")
maxbilet= int(y[1])
for i in range(1,5):
    x = metin.readline()
    y = x.split("-")
    fiyat[i] = y[1]
k=0
s=0
f=0
def fiyathesapla(k,s):
    q=int(fiyat[k]) * s
    return q


for i in range(1,13):
    indirim = {"Kategori": 0, "Min": 0, "Max": 0, "Oran": 0}
    x = metin.readline()
    y=x.split("-")
    indirim["Kategori"]=int(y[0])
    indirim["Min"] = int(y[1])
    indirim["Max"] = int(y[2])
    indirim["Oran"] = int(y[3])
    katalog.append(indirim)
yenif=0
toplam=0
def indirimlifiyat(k, s, f):
    for i in range(12):
        if(katalog[i]["Kategori"]==k and katalog[i]["Min"]<=s and katalog[i]["Max"]>=s):
            (f-f*(katalog[i]["Oran"]/100))
            #toplam +=yenif
            return(f-f*(katalog[i]["Oran"]/100))
        else:
            fiyathesapla(k,s)