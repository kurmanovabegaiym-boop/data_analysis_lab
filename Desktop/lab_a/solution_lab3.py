import numpy as np

sales = np.array([
    [120, 125, 130, 128, 135, 140, 138, 145],
    [80, 82, 79, 85, 88, 90, 86, 92],
    [150, 148, 155, 160, 158, 165, 220, 170],
    [60, 65, 62, 58, 64, 63, 61, 66],
    [100, 105, 102, 108, 110, 112, 109, 115]
])

regions = np.array(["Бишкек", "Ош", "Каракол", "Токмок", "Джалал-Абад"])

print("--- 1. Сравнение регионов ---")

sum_reg = np.sum(sales, axis=1)
mean_reg = np.mean(sales, axis=1)

mean_week = np.mean(sales, axis=0)

print("Сумма продаж по регионам:", sum_reg)
print("Среднее по регионам:", mean_reg)
print("Среднее по неделям:", mean_week)


leader_idx = np.argmax(sum_reg)
min_idx = np.argmin(sum_reg)

print("Лидер по продажам:", regions[leader_idx])
print("Меньше всего продаж:", regions[min_idx])
print("Объяснение: Каракол продает больше всех, а в Токмоке самые маленькие цифры.")
print()


print("--- 2. Разброс продаж ---")

std_reg = np.std(sales, axis=1, ddof=1)
q1 = np.percentile(sales, 25, axis=1)
q3 = np.percentile(sales, 75, axis=1)
iqr = q3 - q1

cv = (std_reg / mean_reg) * 100

print("Стандартное отклонение:", std_reg)
print("IQR (межквартильный размах):", iqr)
print("Процент разброса (CV):", cv)
print("Вывод: В Токмоке и Оше продажи стабильнее, а в Караколе скачут.")
print()

print("--- 3. Поиск выбросов ---")

low = q1 - 1.5 * iqr
high = q3 + 1.5 * iqr

outliers = (sales < low[:, None]) | (sales > high[:, None])

print("Есть ли аномалии по регионам:", np.any(outliers, axis=1))
print("Сами аномальные значения:", sales[outliers])
print("Объяснение: На 7 неделе в Караколе продали на 220 тыс. Это может быть оптовый заказ или ошибка кассы.")
print()


print("--- 4. Доля регионов ---")

all_sum = np.sum(sales)
shares = (sum_reg / all_sum) * 100

print("Доли регионов в процентах:", shares)
print("Вывод: Каракол и Бишкек приносят больше половины всей выручки.")
print()

print("--- 5. Сравнение 1 и 2 месяца ---")


m1 = np.mean(sales[:, :4], axis=1)
m2 = np.mean(sales[:, 4:], axis=1)

diff_abs = m2 - m1
diff_pct = (diff_abs / m1) * 100

print("Среднее 1-4 недели:", m1)
print("Среднее 5-8 недели:", m2)
print("Прирост в процентах:", diff_pct)
print("Вывод: Во всех регионах продажи подросли к концу периода.")
print()

print("--- 6. Без аномалий ---")

sales_clean = np.where(outliers, np.nan, sales)

clean_sum = np.nansum(sales_clean, axis=1)
clean_mean = np.nanmean(sales_clean, axis=1)

print("Сумма до:", sum_reg)
print("Сумма после удаления аномалий:", clean_sum)
print("Вывод: Без скачка в 220 тыс Каракол всё равно остаётся лидером.")
print()

print("--- 7. Проблемные регионы ---")

bad_growth = diff_pct < 5.0
bad_share = shares < 15.0

is_problem = bad_growth | bad_share
print("Проблемные регионы:", regions[is_problem])
print("Объяснение: У Токмока маленькая доля, но продажи там растут, так что закрывать его нельзя.")
print()

print("--- 8. Отчет ---")
print("Главный доход приносят Каракол и Бишкек.")
print("На 7 неделе в Караколе был подозрительный скачок до 220.")
print("Надо проверить чеки за 7 неделю и узнать почему в Токмоке малые объемы.")
print()

print("--- Доп задание ---")

r_total = np.argsort(-sum_reg) + 1
r_stab = np.argsort(cv) + 1

print("Ранг по продажам (1 место - самый большой):", r_total)
print("Ранг по стабильности (1 место - самый стабильный):", r_stab)
print("Вывод: Кто продает больше всех (Каракол), тот менее стабилен.")