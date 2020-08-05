from django.shortcuts import render

from .models import Equ_Model


#ListView(CRUDのRにあたる)をインポート
from django.views.generic import ListView
#ListView(CRUDのRにあたる)をインポート
from django.views.generic import DetailView


class Equ_List(ListView):
    template_name='list.html'
    model = Equ_Model

class Equ_Detail(DetailView):
    template_name='detail.html'
    model = Equ_Model