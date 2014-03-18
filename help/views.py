from django.shortcuts import render
from django.views.generic import ListView
from help.models import Ask


class ListContactView(ListView):
    model = Ask
    template_name = 'ask_list.html'


