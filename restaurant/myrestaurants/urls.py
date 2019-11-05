from django.urls import path, re_path

from myrestaurants import views

app_name = 'myrestaurants'

urlpatterns = [
    #  查看所有餐厅列表
    path('', views.RestaurantList.as_view(), name='restaurant_List'),
    # 注意re_path乒拼写
    # 查看餐厅详情url,因为需要传参所以用到了re_path
    # 这里因为上面指定了命名空间，所以访问为/myrestaurants/restaurant/1/这样
    re_path(r'^restaurantList/(?P<pk>\d+)/$', views.RestaurantDetail.as_view(), name='restaurant_Detail'),
    # 创建餐厅, 如：/myrestaurants/restaurant/create/
    re_path(r'^restaurant/create/$', views.RestaurantCreate.as_view(), name='restaurant_create'),
    # 编辑餐厅详情, 如: /myrestaurants/restaurant/1/edit/
    re_path(r'^restaurant/(?P<pk>\d+)/edit/$', views.RestaurantEdit.as_view(), name='restaurant_edit'),
]
