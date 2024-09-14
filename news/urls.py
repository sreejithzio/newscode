from django.urls import path,include
from .views import ArticleListView,RetrieveNews,GetByTitle

urlpatterns = [
    path('', ArticleListView.as_view(),name='list_news'),
    path('get',RetrieveNews.as_view(),name='retrive_news'),
    path('get_by_title/',GetByTitle.as_view(),name='get_by_name')
]       