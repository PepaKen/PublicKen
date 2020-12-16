D = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input("Введите сумму вклада:"))
depositTKB = float(money / 100 * D['ТКБ']) + money
depositSKB = float(money / 100 * D['СКБ']) + money
depositVTB = float(money / 100 * D['ВТБ']) + money
depositSBER = float(money / 100 * D['СБЕР']) + money
deposits = [depositTKB, depositSKB, depositVTB, depositSBER]
print(list(map(int, deposits)))
print("Максимальная сумма, которую вы можете заработать -", max(map(int, deposits)))


















