"""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех
предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования
предприятий, чья прибыль ниже среднего.
"""
from collections import defaultdict, Counter


def print_helper(companies):
    for company, stats in companies:
        print(f"{company}\t\t\t(Годовая прибыль: {stats['year_profit']})")


companies = defaultdict(Counter)
company_count = int(input("Введите кол-во предприятий:\n"))

for i in range(1, company_count + 1):
    company_name = input(f"Введите наименование предприятия № {i}:\n")
    for quarter in (1, 2, 3, 4,):
        profit = int(input(f"Введите прибыль предприятия '{company_name}' в {quarter} квартале\n"))
        companies[company_name]['year_profit'] += profit

avg_profit = sum([i['year_profit'] for i in companies.values()]) / len(companies)
companies_below_avg = [i for i in companies.items() if i[1]['year_profit'] < avg_profit]
companies_above_avg = [i for i in companies.items() if i[1]['year_profit'] > avg_profit]

print(f"Средняя годовая прибыль по всем предприятиям: {avg_profit}\n")
print(f"Предприятия c годовой прибылью выше средней:")
print_helper(companies_above_avg)
print(f"Предприятия c годовой прибылью ниже средней:")
print_helper(companies_below_avg)


# Вариант с сортировкой по убыванию
print("-" * 50)
print(f"Предприятия c годовой прибылью выше средней:")
print_helper(sorted(companies_above_avg, key=lambda c: c[1]['year_profit'], reverse=True))
print(f"Предприятия c годовой прибылью ниже средней:")
print_helper(sorted(companies_below_avg, key=lambda c: c[1]['year_profit'], reverse=True))
