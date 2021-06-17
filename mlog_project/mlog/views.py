from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Entry
from accounts.models import User, Follow


class TopView(ListView):
	model=Entry
	template_name='mlog/topview.html'

	def get_queryset(self):
		try:
			qs=Entry.objects.all().order_by('-id')
		except ObjectDoesNotExist:
			qs=Entry.objects.none()
		return qs


class TimelineView(LoginRequiredMixin, ListView):
	model=Entry
	template_name='mlog/timeline.html'

	def get_queryset(self):
		follows=Follow.objects.filter(user__username=self.request.user.username).values('follower__username')
		
		try:
			qs=Entry.objects.filter(writer__username__in=follows)
			print(qs)
		except ObjectDoesNotExist:
			qs=Entry.objects.none()
		return qs


class EntryDetailView(DetailView):
	template_name='mlog/entrydetail.html'

	def get_object(self):
		return get_object_or_404(Entry,id=self.kwargs['pk'])