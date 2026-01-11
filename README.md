BLM0101 Donem Projesi 

Ogrenci Adi : Fatih Murathan

Ogrenci Soyadi : Ucar

Ogrenci Numarası : 25360859015

Proje Konusu : Veri Depolama ve Sayısal Sistemler

Youtube Linki : https://youtu.be/HM1lUhmMpZw

Proje Açıklaması :

1. Genel Bakış

Bu program kullanıcıdan bir onluk (decimal) sayı, dönüştürmek istediği taban (2 veya 16) ve tercih ettiği bit sayısını alır. Girilen sayıyı istenen tabana çevirir ve sayının bellekteki (byte düzeyindeki) gösterimini verir. Program etkileşimli bir konsol uygulamasıdır; kullanıcıdan giriş alır ve sonuçları ekrana yazdırır.

Desteklenen tabanlar: 2 (binary) ve 16 (hexadecimal)

Bellek gösterimi: Verilen bitsayisi'na göre byte'lara bölünerek, her byte için 8 bitlik gösterim elde edilir.

Negatif sayılar: Dönüştürücülerde işaret ayrı tutulur (ör. -1011), bellek gösteriminde ise sayi % (2**bitsayisi) kullanılarak iki's tamamlayanı (two's complement) andıran bir bit kalıbı elde edilir.

Program herhangi bir dış kütüphane kullanmaz — yalnızca Python'un yerleşik tip ve operatörlerini kullanır.

2. Kullanılan Fonksiyonlar
binary_uzunluk(sayi)

Amaç: Verilen sayının (mutlak değerinin) ikili (binary) gösterimde kaç bit gerektirdiğini döndürür.
Parametreler: sayi (int) — pozitif, negatif veya sıfır.
Dönüş: int — gerekli bit sayısı (sıfır için 1).

Davranış:

sayi == 0 için 1 döner.

Negatif sayı gelirse -sayi alınır (mutlak değer).

sayi 0 olana dek sayi //= 2 işlemi ile bölünerek bit sayısı hesaplanır.

Zaman karmaşıklığı: O(b) — b = sayı için gerekli bit sayısı.

binary_sayiya_donusturucu(sayi)

Amaç: Onluk (decimal) sayi'yı binary (string) gösterime çevirmek ve başında açıklama metni ile döndürmek.
Parametreler: sayi (int)
Dönüş: str — örn. "Sayının binary karşılığı : 1011" veya negatif için "-1011" şeklinde.

Davranış:

sayi == 0 için "Sayının binary karşılığı : 0" döner.

Negatifse isaret = -1 olarak kaydedilir ve sayi mutlak değere çevrilir.

Mod 2 ile kalanlar bir string başına eklenerek (str toplama) binary oluşturulur.

Negatifse - işareti stringin başına konur.

Not: Python'un yerleşik bin() fonksiyonu veya format() ile daha kısa yazılabilir; burada eğitim amaçlı string toplama algoritması kullanılmış.

Zaman karmaşıklığı: O(b) — b = bit sayısı.

hex_sayiya_donusturucu(sayi)

Amaç: Onluk sayi'yı hexadecimal (16'lık) gösterime çevirir ve açıklama metni ile döndürür.
Parametreler: sayi (int)
Dönüş: str — örn. "Sayının hex karşılığı : 1A3F" veya negatif için "-1A3F".

Davranış:

sayi == 0 için "Sayının 16.tabandaki karşılığı 0" döner.

hex_sembolleri = "0123456789ABCDEF" kullanılarak kalan indeksleriyle sembol seçimi yapılır.

Negatifse isaret tutulur, sayı mutlak değere çevrilir.

sayi % 16 ile kalan alınır, karşılık gelen hex karakter başa eklenir, sonrasında sayi //= 16.

Negatifse başa - eklenir.

Zaman karmaşıklığı: O(h) — h = hex basamak sayısı.

bellek_gosterimi(sayi, bitsayisi)

Amaç: Verilen sayi'nın bellekte bitsayisi bitlik alanda nasıl tutulduğunu byte byte (8-bit bloklar) gösterir. Her byte köşeli parantez içinde ve büyükten küçüğe (MSB -> LSB) sırayla yazılır.
Parametreler:

sayi (int) — negatif veya pozitif olabilir.

bitsayisi (int) — gösterimde kullanılacak toplam bit sayısı (program, girilen değiyi 8'in katına yuvarlar).

Dönüş: str — örn. "[00000000] [00001010]"

Davranış ve önemli noktalar:

mod değeri 2 ** bitsayisi olacak şekilde hesaplanır (koddaki döngü ile oluşturulmuş).

val = sayi % mod ifadesi kullanılarak, sayının bitsayisi bit içerisindeki karşılığı elde edilir. Bu, negatif sayılar için iki's tamamlayana benzer bir bit örüntüsü üretir (Python mod davranışı nedeniyle).

byte_sayisi = bitsayisi // 8 ile kaç byte gösterileceği hesaplanır.

Döngü içinde en düşük anlamlı byte'tan başlayarak (val % 256) byte'lar çıkarılır; fakat kutular.insert(0, "[b]") ile liste başına eklenir — sonuçta gösterim MSB -> LSB (yani büyük uçtan küçük uca) olarak ekrana verilir.

Her byte için 8 bit elde etmek için ayrı bir iç döngü kullanılır (for _ in range(8)), bitler string olarak başa eklenerek doğru sıra korunur.

Zaman karmaşıklığı: O(byte_sayisi * 8) = O(bitsayisi).

Not: val = sayi % mod kullanımı bellek gösterimini doğal iki's tamamlayana (two's complement) benzetir; ancak program açıkça iki's tamamlayanı hesaplamıyor, Python mod sonucu gösterimi sağlar.

3. Program Akışı (Ana Döngü)

Kullanıcıdan sayi (int) alınır — giriş hatalıysa yeniden sorulur.

Kullanıcıdan taban (2 veya 16) alınır — sadece 2 veya 16 kabul edilir.

Kullanıcıdan bitsayisi (pozitif int) alınır:

Eğer bitsayisi < gerekli_bit ise (gerekli_bit = binary_uzunluk(sayi)), bitsayisi otomatik olarak artırılır ve bilgi verilir.

bitsayisi 8'in katı değilse, bir sonraki 8'in katına yuvarlanır (ör. 10 -> 16) ve kullanıcı bilgilendirilir.

Girilen taban e göre uygun dönüştürme fonksiyonu çağrılır ve bellek_gosterimi ile bellek gösterimi yazdırılır.

Döngü sonsuzdur — kullanıcı programı Ctrl+C ile durdurabilir veya kod genişletilerek çıkış seçeneği eklenebilir.

4. Örnekler

Örnek 1: sayi = 10, taban = 2, bitsayisi = 8

Binary dönüşüm: Sayının binary karşılığı : 1010

Bellek gösterimi: [00000000] [00001010] (MSB -> LSB)

Örnek 2: sayi = -5, taban = 16, bitsayisi = 8

Hex dönüşüm: Sayının hex karşılığı : -5 (negatif işaret ayrı gösteriliyor)

Bellek gösterimi (8 bit): val = -5 % 256 = 251 → [11111011] (iki's tamamlayana benzeyen gösterim)

Not: Hex dönüşüm fonksiyonu negatif işareti sayıdan ayrı gösterdiği için -5 → "-5" (tek basamak olarak) gözükür; istenirse bellek_gosterimi çıktısının hex karşılığı ayrıca hesaplanabilir.

5. Hata Yönetimi ve Kullanıcı Geri Bildirimleri

Girdi hataları (ValueError) için try/except kullanılmış; hatalı giriş durumunda kullanıcı bilgilendirilir ve tekrar sorulur.

bitsayisi için negatif girişler reddedilir.

taban için 2 veya 16 dışındaki değerler reddedilir.

bitsayisi yetersizse otomatik olarak arttırılır ve kullanıcı bilgilendirilir.

bitsayisi 8'in katına yuvarlanır; bu da bellek gösteriminde tam byte blokları sağlar.
