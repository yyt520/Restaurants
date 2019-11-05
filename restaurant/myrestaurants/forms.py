from django.forms import ModelForm,  TextInput, URLInput, ClearableFileInput
from .models import Restaurant, Dish


class RestaurantForm(ModelForm):
    class Meta:
        model = Restaurant
        exclude = ('user', 'date',)

        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'telephone': TextInput(attrs={'class': 'form-control'}),
            'url': URLInput(attrs={'class': 'form-control'}),
        }

        labels = {
            'name': '名称',
            'address': '地址',
            'telephone': '电话',
            'url': '网站',
        }