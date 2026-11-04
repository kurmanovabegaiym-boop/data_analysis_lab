import numpy as np

gen = np.random.default_rng(seed=2026)

nedelya1 = gen.integers(low=500, high=2000, size=(7, 3))
nedelya2 = gen.integers(low=500, high=2000, size=(7, 3))
kat = np.array(["Electronics", "Clothing", "Home"])

print("вот первая неделя:")
print(nedelya1)
print("а это вторая:")
print(nedelya2)
print("категории товаров:", kat)

print("форма первой недели:", nedelya1.shape)
print("измерения:", nedelya1.ndim)
print("размер:", nedelya1.size)
print("тип данных:", nedelya1.dtype)

print("продажи в первый день:", nedelya1[0])
print("в последний день:", nedelya1[6])
print("электроника за всю неделю:", nedelya1[:, 0])
print("одежда за первые 3 дня:", nedelya1[0:3, 1])
print("дни с 3 по 5:", nedelya1[2:5])

mnogo = nedelya1[nedelya1 > 1500]
print("больше 1500:", mnogo)

malo = nedelya1[nedelya1 < 800]
print("меньше 800:", malo)

sredne = nedelya1[(nedelya1 >= 1000) & (nedelya1 <= 1500)]
print("между 1000 и 1500:", sredne)

elec_stolbik = nedelya1[:, 0]
skolko_raz = elec_stolbik > 1200
print("дни когда электроника > 1200:", np.sum(skolko_raz))

vsego_deneg = np.sum(nedelya1)
print("общая сумма за неделю:", vsego_deneg)

srednee_v_den = np.mean(nedelya1)
print("среднее за день:", srednee_v_den)

print("максимум:", np.max(nedelya1))
print("минимум:", np.min(nedelya1))

po_kat = np.sum(nedelya1, axis=0)
print("по категориям сумма:", po_kat)

po_dnyam = np.mean(nedelya1, axis=1)
print("среднее по дням:", po_dnyam)

dnevnie_summy = np.sum(nedelya1, axis=1)
kassa = np.cumsum(dnevnie_summy)
print("суммы по дням:", dnevnie_summy)
print("накопительная сумма:", kassa)

polovina = np.sum(nedelya1) / 2
kuda = np.where(kassa > polovina)
den_polovini = kuda[0][0] + 1
print("половина прошла на каком дне:", den_polovini)

kopia = nedelya1.copy()
dorozhe = kopia * 1.12
print("старые:", nedelya1)
print("новые с плюсом 12 процентов:", dorozhe)

krasivo = np.round(dorozhe)
print("округлили:", krasivo)

maska = nedelya1 > 1500
tablica_slovami = np.where(nedelya1 > 1500, "High", "Low")
print("словесная таблица:\n", tablica_slovami)

odnomerniy = nedelya1.reshape(-1)
print("в одну строчку:", odnomerniy)
print("сколько элементов:", odnomerniy.size)
obratno = odnomerniy.reshape(7, 3)
print("вернули обратно в 7 на 3:\n", obratno)

print("reshape с -1 (7):\n", nedelya1.reshape(7, -1))
print("reshape с -1 (-1, 3):\n", nedelya1.reshape(-1, 3))

demo = np.arange(1, 21)
print(demo.reshape(4, 5))
print(demo.reshape(5, 4))
print(demo.reshape(2, 10))

all_sales = np.vstack([nedelya1, nedelya2])
print("обе недели вместе:\n", all_sales)
print("какая форма стала:", all_sales.shape)

obshiy_2_nedeli = np.sum(all_sales, axis=0)
srednee_2_nedeli = np.mean(all_sales, axis=0)
procenti = (obshiy_2_nedeli / np.sum(all_sales)) * 100

print("сумма по категориям за две недели:", obshiy_2_nedeli)
print("среднее:", srednee_2_nedeli)
print("проценты:", procenti)

samiy_top_ind = np.argmax(obshiy_2_nedeli)
print("самая крутая категория:", kat[samiy_top_ind])

vse_dni_summa = np.sum(all_sales, axis=1)
luchshiy_den = np.argmax(vse_dni_summa) + 1
hudshiy_den = np.argmin(vse_dni_summa) + 1

print("суммы по всем 14 дням:", vse_dni_summa)
print("самый лучший день:", luchshiy_den)
print("самый худший день:", hudshiy_den)

itog1 = np.sum(nedelya1)
itog2 = np.sum(nedelya2)
sred1 = np.mean(nedelya1)
sred2 = np.mean(nedelya2)

raznica = itog2 - itog1
procent_izmeneniya = (raznica / itog1) * 100

print("итог неделя 1:", itog1)
print("итог неделя 2:", itog2)
print("разница:", raznica)
print("в процентах:", procent_izmeneniya)

if itog2 > itog1:
    print("вторая неделя лучше прошла")
else:
    print("первая неделя лучше")

obshaya_sredняя_dnya = np.mean(vse_dni_summa)
plohie_dni = np.where(vse_dni_summa < obshaya_sredняя_dnya)[0] + 1
print("дни когда было ниже среднего:", plohie_dni)
