D = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму вклада:"))
depositTKB = int(money / 100 * D['ТКБ'])
depositSKB = int(money / 100 * D['СКБ'])
depositVTB = int(money / 100 * D['ВТБ'])
depositSBER = int(money / 100 * D['СБЕР'])
deposits = [depositTKB, depositSKB, depositVTB, depositSBER]
print(deposits)
print("Максимальная сумма, которую вы можете заработать -", max(deposits))


















