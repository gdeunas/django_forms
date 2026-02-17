from django.urls import path
from blogs.apps import BlogsConfig
from . import views
from .views import RecordDetailView, RecordListView, RecordCreateView, RecordUpdateView, RecordDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path('', RecordListView.as_view(), name='records_list'),
    path('record_detail/<int:pk>/', RecordDetailView.as_view(), name='record_detail'),
    path('records_list/', RecordListView.as_view(), name='records_list'),
    path('add_record/', RecordCreateView.as_view(), name='add_record'),
    path('record_update/<int:pk>/', RecordUpdateView.as_view(), name='record_update'),
    path('record/delete/<int:pk>/', RecordDeleteView.as_view(), name='record_delete'),

]
