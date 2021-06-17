from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.shortcuts import render
from django.views.generic import ListView

from .models import Entry


class TopView(ListView):
	model=Entry
	template_name='mlog/topview.html'

	def get_queryset(self):
		try:
			qs=Entry.objects.all().order_by('-id')
		except ObjectDoesNotExist:
			qs=Entry.objects.none()
		return qs