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