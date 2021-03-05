from django.shortcuts import render, reverse, redirect
from rest_framework import viewsets
from .serializers import *
from .models import *
from django.db.models import Avg
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django import forms
from django.views.generic.edit import FormMixin

# Create your views here.
class MovieView(viewsets.ModelViewSet):
	serializer_class = MovieSerializer

	def get_queryset(self):
		queryset = Movie.objects.annotate(rating=Avg('review__rating')).order_by('-released_on','-rating')
		return queryset

class MovieListView(ListView):
	"""Show all movies."""
	model = Movie

	def get_queryset(self):
		return Movie.objects.annotate(rating=Avg('review__rating')).order_by('-released_on','-rating')

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		exclude = ('movie','user')

class MovieDetailView(FormMixin,DetailView):
	"""Show the requested movie."""
	model = Movie
	form_class = ReviewForm

	def get_queryset(self):
		return Movie.objects.annotate(rating=Avg('review__rating')).order_by('-released_on','-rating')

	def get_context_data(self, **kwargs):
		context = super(MovieDetailView, self).get_context_data(**kwargs)
		context['form'] = ReviewForm
		context['reviews'] = Review.objects.filter(movie = self.object)
		return context
	   
	def post(self, request, *args, **kwargs):
		self.object = self.get_object()
		form = self.get_form()
		if form.is_valid():
			return self.form_valid(form)
		else:
			return self.form_invalid(form)
	
	def form_valid(self, form):
		review = form.save(commit=False)
		review.user = self.request.user
		review.movie = self.object
		review.save()
		return super(MovieDetailView, self).form_valid(form)
	
	def get_success_url(self):
		return reverse('detail', kwargs={'pk': self.object.pk})


class MovieCreateView(CreateView):
	"""Create a new movie."""
	model = Movie
	fields = ['title','year', 'rated', 'released_on', 'genre', 'director', 'plot']

	def get_success_url(self):
		return reverse('index')

class MovieUpdateView(UpdateView):
	"""Update the requested movie."""
	model = Movie
	fields = ['title','year', 'rated', 'released_on', 'genre', 'director', 'plot']

	def get_success_url(self):
		return reverse('index')


class MovieDeleteView(DeleteView):
	"""Delete the requested movie."""
	model = Movie
	success_url = reverse_lazy('index')