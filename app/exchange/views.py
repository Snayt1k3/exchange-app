import requests
from django.shortcuts import render
from django.views.generic.edit import FormView

from .forms import ExchangeForm


# Create your views here.


class ExchangeView(FormView):
    form_class = ExchangeForm
    template_name = "exchange/index.html"

    def post(self, request, *args, **kwargs):
        form = ExchangeForm(request.POST)

        from_curr = request.POST.get("currency_from")
        to_curr = request.POST.get("currency_to")
        value = request.POST.get("value")
        context = {"form": form, 'from_curr': from_curr,
                   'to_curr': to_curr, "value": value}
        if from_curr != to_curr:
            res = requests.get(
                "https://api.currencyapi.com/v3/latest?apikey=Gn2mNO4kBzM1KD7tkrk1kj7Utle9k33as8pcwZCf").json()
            converted_curr = round((res['data'][to_curr]["value"] / res['data'][from_curr]["value"]) * float(value), 2)

            context.update({'converted_curr': converted_curr})

        return render(request, "exchange/index.html", context=context)
