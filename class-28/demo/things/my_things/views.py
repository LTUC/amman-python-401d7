from django.db import models
from django.shortcuts import render
from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    DeleteView,
                                    UpdateView,
                                    View
                                    )

from .models import Thing
from django.urls import reverse_lazy

class ListThingView(ListView):
    template_name = 'thing_list.html'
    model = Thing


class DetailThingView(DetailView):
    template_name = 'thing_detail.html'
    model = Thing

# class DetailThingView(View):
#     template_name = 'thing_detail.html'
#     model = Thing

#     def post(self):
#         pass
#     def get(self):
#         pass
#     def delete(self):
#         pass

class CreateThingView(CreateView):
    template_name = 'thing_create.html'
    model = Thing
    fields = ['name', 'rate', 'description', 'rater']

class DeleteThingView(DeleteView):
    template_name = 'thing_confirm_delete.html'
    model = Thing
    success_url = reverse_lazy('thing_list')


class UpdateThingView(UpdateView):
    template_name = 'thing_update.html'
    model = Thing
    fields = ['name', 'rate', 'description']

