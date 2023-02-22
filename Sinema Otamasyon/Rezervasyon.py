#Salon sıfırlamak için kullanılır
def Salonolustur():
    w, h = 20, 20
    koltuk = [['-' for x in range(w)] for y in range(h)]


#her türlü durumda çalışması için salon oluşturma kodunu dışarıda da tanımladı.
w, h = 20, 20
koltuk= [['-' for x in range(w)] for y in range(h)]

#yer seçme kısmı burdan yapılır
def Rezervasyon(k,s):
    liste=[]                #biletlerin yer numaralarını bu listeye atarız.
    satıldı = 1                #Satılan bilet sayısının takibi için.
    if (k == 1):
        satıldı = 1
        for i in range(10):
            for j in range(5, 15):
                if (koltuk[i][j] == '-' and satıldı <= s):
                    koltuk[i][j] = 'X'
                    liste.append(str(i)+"-"+str(j))
                    satıldı += 1
    elif (k == 2):
        satıldı = 1
        for i in range(10):
            for j in range(4, -1, -1):
                if (koltuk[i][j] == '-' and satıldı <= s):
                    koltuk[i][j] = 'X'
                    satıldı += 1
                    liste.append(str(i) + "-" + str(j))
            for z in range(15, 20):
                if (koltuk[i][z] == '-' and satıldı <= s):
                    koltuk[i][z] = 'X'
                    satıldı += 1
                    liste.append(str(i) + "-" + str(j))
    elif (k == 3):
        satıldı = 1
        for i in range(10, 20):
            for j in range(5, 15):
                if (koltuk[i][j] == '-' and satıldı <= s):
                    koltuk[i][j] = 'X'
                    satıldı += 1
                    liste.append(str(i) + "-" + str(j))
    elif (k == 4):
        satıldı = 1
        for i in range(10, 20):
            for j in range(4, -1, -1):
                if (koltuk[i][j] == '-' and satıldı <= s):
                    koltuk[i][j] = 'X'
                    satıldı += 1
            for z in range(15, 20):
                if (koltuk[i][z] == '-' and satıldı <= s):
                    koltuk[i][z] = 'X'
                    satıldı += 1
                    liste.append(str(i) + "-" + str(j))
    print("alınan biletler",liste)



def Bosyervarmi(k, s):
    bosyer = 0
    if (k == 1):
        bosyer = 0
        for i in range(10):
            for j in range(5, 15):
                if (koltuk[i][j] == '-'):
                    bosyer += 1
    elif (k == 2):
        bosyer = 0
        for i in range(10):
            for j in range(4, -1, -1):
                if (koltuk[i][j] == '-'):
                    bosyer += 1
            for z in range(15, 20):
                if (koltuk[i][z] == '-'):
                    bosyer += 1
    elif (k == 3):
        bosyer = 0
        for i in range(10, 20):
            for j in range(5, 15):
                if (koltuk[i][j] == '-'):
                    bosyer += 1
    elif (k == 4):
        bosyer = 0
        for i in range(10, 20):
            for j in range(4, -1, -1):
                if (koltuk[i][j] == '-'):
                    bosyer += 1
            for z in range(15, 20):
                if (koltuk[i][z] == '-'):
                    bosyer += 1
    if ((bosyer) < s):
        return False
    else:
        return True

def Salonyazdir():
    for i in range(20):
        for j in range(20):
            print(koltuk[i][j], end="")
        print("")






