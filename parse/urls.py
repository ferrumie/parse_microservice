from django.urls import path
from . import views


app_name = 'parse'


urlpatterns = [
    path('', views.index, name='index'),
    path('excel', views.form_upload, name='parse'),
    path('convert', views.excel_parse_to_json, name='convert')
]
