from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView

from myrestaurants.forms import RestaurantForm
from myrestaurants.models import Restaurant, RestaurantReview


class RestaurantList(ListView):
    queryset = Restaurant.objects.all().order_by('-date')
    context_object_name = 'latest_restaurant_list'
    template_name = 'myrestaurants/restaurant_list.html'


class RestaurantDetail(DetailView):
    model = Restaurant
    template_name = 'myrestaurants/restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super(RestaurantDetail, self).get_context_data(**kwargs)
        context['RATING_CHOICES'] = RestaurantReview.RATING_CHOICES
        return context


class RestaurantCreate(CreateView):
    model = Restaurant
    template_name = 'myrestaurants/form.html'
    form_class = RestaurantForm

    # Associate form.instance.user with self.request.user
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(RestaurantCreate, self).form_valid(form)


class RestaurantEdit(UpdateView):
    model = Restaurant
    template_name = 'myrestaurants/form.html'
    form_class = RestaurantForm
