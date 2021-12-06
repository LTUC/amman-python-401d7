from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Thing


class ThingsListView(ListView):
    template_name = "home.html"
    model = Thing


class ThingDetailView(DetailView):
    template_name = "thing_detail.html"
    model = Thing