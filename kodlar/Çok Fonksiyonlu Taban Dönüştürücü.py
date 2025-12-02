def binary_sayıya_dönüştürücü(sayı):               #sayıyı 10'luk tabandan 2'lik tabana dönüştüren fonksiyon string toplama yöntemiyle
    if sayı == 0:                                  #sayı 0 olduğunda zaman kaybetmemek için direkt 0 diyoruz
        return "Sayının 2.tabandaki karşılığı 0"   #sayının karşılığının 0 olduğunu bildirip fonksiyonu kapatıyoruz

    sonuc = ""                                     #string toplama için önce boş bir string oluşturuyoruz
    isaret = 1                                     #varsayılan olarak işaretimizi + olarak atıyoruz

    if sayı < 0:                                   #girilen değerin işaretini kontrol ediyoruz
        sayı = -sayı                               #işaret negatifse kolaylık olsun diye onu pozitife dönüştürüyoruz
        isaret = -1                                #işaretimizi - olarak değiştiriyoruz

    while sayı > 0:                                #sayıyı binary'e çevirmek için döngü
        sonuc = str(sayı % 2) + sonuc              #sayıyı binary'e çevirmek için mod alıp string toplama
        sayı //= 2                                 #sayının 2'ye bölümünü sayıya atama

    if isaret == -1:                               #işaret + ise kodu buraya yönlendirme
        return "-" + sonuc                         #işaret - olduğunda sonucu - göstermek için string toplaması
    if isaret == +1:                               #işaret + ise kodu buraya yönlendirme
        return sonuc                               #işaret + olduğunda sonucu değiştirmeden dış dünyaya gönderme

def hex_sayıya_dönüştürücü(sayı):                 #sayıyı 10'luk tabandan 16'lık tabana dönüştüren fonksiyon string toplama yöntemiyle
    if sayı == 0:                                 #sayı 0 olduğunda zaman kaybetmemek için direkt 0 diyoruz
        return "Sayının 16.tabandaki karşılığı 0" #sayının karşılığının 0 olduğunu bildirip fonksiyonu kapatıyoruz

    hex_harfleri = "0123456789ABCDEF"             #tüm hex sembollerini daha sonra kullanmak için tek bir stringte tutuyoruz
    sonuc = ""                                    #string toplama için önce boş bir string oluşturuyoruz
    isaret = 1                                    #varsayılan olarak işaretimizi + olarak atıyoruz

    if sayı < 0:                                  #girilen değerin işaretini kontrol ediyoruz
        sayı = -sayı                              #işaret negatifse kolaylık olsun diye onu pozitife dönüştürüyoruz
        isaret = -1                               #işaretimizi - olarak değiştiriyoruz

    while sayı > 0:
        kalan = sayı % 16
        sonuc = hex_harfleri[kalan] + sonuc     #kalana göre stringin hangi elemanını aldığımızı belirliyoruz
        sayı //= 16

    if isaret == -1:                            #işaret - ise kodu buraya yönlendirme
        return "-" + sonuc                      #işaret - olduğunda sonucu - göstermek için string toplaması
    if isaret == +1:                            #işaret + ise kodu buraya yönlendirme
        return sonuc                            #işaret + olduğunda sonucu değiştirmeden dış dünyaya gönderme

print("Taban Dönüştürme Makinesi\n")

print("10'luk sayı sisteminde gireceğiniz sayıları seçeceğiniz sayı tabanlarına dönüştüren makina\n")

while True:                                                       #kullanıcıdan dönüştüreceğimiz sayıyı almak için döngü
    try:                                                          #hataları yakalayabilmek için try except
        sayı = int(input("10'luk tabandaki sayınızı giriniz : ")) #farklı tabanlara dönüştürülecek sayıyı kullanıcıdan alma
        break                                                     #sayı başarılı bir şekilde alındığında döngüden çıkmak için break
    except ValueError:                                            #sayı alınamadığında programın kapanması yerine kullanıcıya hata mesajı verme
        print("Lütfen 10'luk tabanda bir sayı giriniz!")          #hata mesajını bastırma
        continue                                                  #kullanıcıdan sayıyı yeniden almak için döngü başına dönme

while True:                                                       #kullanıcıdan dönüştüreceğimiz sayıyı almak için döngü
    try:                                                          #hataları yakalayabilmek için try except
        taban = int(input("Sayıyı dönüştürmek istediğiniz tabanı girin : ")) #dönüştüreceğimiz tabanı kullanıcıdan alma
        if taban != 2 and taban != 16:                            #tabanın 2 veya 16 olup olmadığını kontrol etme
            print("Lütfen geçerli bir taban giriniz!")            #taban 2 ya da 16 değilse kullanıcıya uyarı mesajını bastırma
            continue                                              #kullanıcıdan tabanı yeniden almak için döngü başına dönme
        else:                                                     #kullanıcıdan alınan taban 2 ya da 16 ise kodu buraya yönlendirme
            break                                                 #döngüden çıkma
    except ValueError:                                            #sayı alınamadığında programın kapanması yerine kullanıcıya hata mesajı verme
        print("Lütfen geçerli bir sayı giriniz!")                 #hata mesajını bastırma
        continue                                                  #kullanıcıdan tabanı yeniden almak için döngü başına dönme

if taban == 2:                                                    #kullanıcıdan alınan taban 2 ise kodu buraya yönlendirme
    print(binary_sayıya_dönüştürücü(sayı))                        #alınan taban 2 olduğu için sayıyı 2 tabanına çevirecek fonksiyonu çağırma
if taban == 16:                                                   #kullanıcıdan alınan taban 2 değil ise kodu buraya yönlendirme
    print(hex_sayıya_dönüştürücü(sayı))                           #alınan taban 16 olduğu için sayıyı 16 tabanına çevirecek fonksiyonu çağırma