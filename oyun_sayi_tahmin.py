import random

print("🎮 Sayı Tahmin Oyununa Hoş Geldin!")
print("1 ile 100 arasında bir sayı tuttum, bakalım tahmin edebilecek misin?")

sayi = random.randint(1, 100)
tahmin_sayisi = 0

while True:
    tahmin = int(input("Tahminini gir: "))
    tahmin_sayisi += 1

    if tahmin < sayi:
        print("🔼 Daha büyük bir sayı söyle!")
    elif tahmin > sayi:
        print("🔽 Daha küçük bir sayı söyle!")
    else:
        print(f"🎉 Tebrikler! {tahmin_sayisi} denemede doğru tahmin ettin!")
        break