import requests
import pandas as pd
import xml.etree.ElementTree as et

count = s_value_max = s_value_average = 0
s_value_min = 9999
# we announce the date we need
for m in range(10, 13):
    for d in range(0, 31):
        v_date = str(d) + '.' + str(m) + '.' + '2020'

        # Here is adress of our API
        url = 'https://www.cbr.ru/scripts/XML_daily_eng.asp'
        params = {
            'date_req': v_date
        }

        # Sendind get request
        response = requests.get(url, params)

        tree = et.ElementTree(et.fromstring(response.text))
        root = tree.getroot()

        # working w our values to find max/min/average
        for node in root:
            s_name = node.find('Name').text if node is not None else None
            s_value = node.find('Value').text if node is not None else None
            count += 1
            s_value_float = float(s_value.replace(",", "."))
            s_value_average += s_value_float
            if s_value_float > s_value_max:
                s_value_max = s_value_float
                name_of_max = s_name
                true_max_date = v_date
            elif s_value_float < s_value_min:
                s_value_min = s_value_float
                name_of_min = s_name
                true_min_date = v_date

print(s_value_average/count, 'среднее значение курса рубля за весь период по всем валютам')
print(s_value_min, name_of_min, true_min_date, 'значение и дата минимального курса валюты')
print(s_value_max, name_of_max, true_max_date, 'значение и дата максимального курса валюты')
