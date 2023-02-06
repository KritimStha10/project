from django.shortcuts import render
from django.views.generic import TemplateView
import pandas as pd
import io
import csv

from django.http import HttpResponse
from django.views import View
# Create your views here.
class CsvUploader(TemplateView):
    template_name = 'csv.html'

    def post(self, request):
        context = {
            'messages':[]
        }

        csv = request.FILES['csv']
        csv_data = pd.read_csv(
            io.StringIO(
                csv.read().decode("utf-8")
            )
        )

        for record in csv_data.to_dict(orient="records"):
           
         
                return render(request, self.template_name, context)


class MyView(View):
    def get(self, request, *args, **kwargs):
        data = []
        with open('a.csv', 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                data.append(row)

        return render(request, 'form.html', {'data': data})