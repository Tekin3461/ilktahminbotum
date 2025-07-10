import random

print("🔮 Tahmin Botuna Hoş Geldin!")
input("Bir tuşa bas ve kaderini öğren...")

tahminler = [
    "Bugün güzel bir haber alacaksın.",
    "Kendine dikkat et, biri seni kıskanıyor.",
    "Şans seninle, ama fazla güvenme.",
    "Gizli bir düşmanın olabilir...",
    "Bu hafta güzel sürprizler seni bekliyor.",
    "Sevdiğin biri seni düşünüyor."
]

print("\nTahminin: " + random.choice(tahminler))
import random

print("🎯 Tahmin Oyununa Hoş Geldin!")
print("1 ile 100 arasında bir sayı tuttum. Bakalım tahmin edebilecek misin?")
print("Toplam 5 tahmin hakkın var. Başlayalım!\n")

sayi = random.randint(1, 100)
hak = 5

while hak > 0:
    try:
        tahmin = int(input(f"Kalan hakkın: {hak} - Tahminin: "))
    except ValueError:
        print("Lütfen sadece sayı gir.")
        continue

    if tahmin == sayi:
        print("🎉 Tebrikler! Doğru tahmin ettin!")
        break
    elif tahmin < sayi:
        print("⬆️ Daha büyük bir sayı dene.")
    else:
        print("⬇️ Daha küçük bir sayı dene.")

    hak -= 1

if hak == 0:
    print(f"💀 Üzgünüm! Tahmin hakkın bitti. Doğru sayı: {sayi}")