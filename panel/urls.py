from django.urls import path

from . import views

app_name = 'panel'

urlpatterns = [
    path('', views.index, name='index'),
    path('news', views.news, name='news'),
    path('news/<int:year>/<int:month>/<int:day>/<slug:post>', views.post_detail, name='post_detail'),
]