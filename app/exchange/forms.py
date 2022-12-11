import requests
from django import forms


class ExchangeForm(forms.Form):
    response = requests.get(
        "https://api.currencyapi.com/v3/latest?apikey=Gn2mNO4kBzM1KD7tkrk1kj7Utle9k33as8pcwZCf").json()

    res_list = []

    for i in response['data']:
        res_list.append((response['data'][i]["code"], response['data'][i]["code"]))

    value = forms.IntegerField(label="Сумма")
    currency_from = forms.ChoiceField(choices=res_list, label="Отдаем")
    currency_to = forms.ChoiceField(choices=res_list, label="Получаем")
