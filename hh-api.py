import requests
import json

def vacancies(text, area=1, per_page=5):
    url = "https://api.hh.ru/vacancies"
    params = {
        "text": text,
        "area": area,         
        "per_page": per_page 
    }
    response = requests.get(url, params=params)
    data = response.json()
    for item in data.get('items', []):
        name = item.get('name')
        employer = item.get('employer', {}).get('name')
        city = item.get('area', {}).get('name')
        salary = item.get('salary')
        if salary:
            salary_str = f"{salary.get('from', '')} - {salary.get('to', '')} {salary.get('currency', '')}"
        else:
            salary_str = "Не указана"
        employment = item.get('employment', {}).get('name', 'Не указано')
        experience = item.get('experience', {}).get('name', 'Не указано')
        url = item.get('alternate_url')

        print(f"Вакансия: {name}")
        print(f"Работодатель: {employer}")
        print(f"Город: {city}")
        print(f"Зарплата: {salary_str}")
        print(f"Тип занятости: {employment}")
        print(f"Опыт: {experience}")
        print(f"Ссылка: {url}")
        print("-" * 50)

vacancies("Python developer")