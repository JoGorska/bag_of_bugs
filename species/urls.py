from django.urls import path
from .views import BugsList, CategoryList, SizeList, EnviromentList


urlpatterns = [
    path('', BugsList.as_view(), name='bugs_list'),
    # path('<str:slug>/', BugDetail.as_view(), name='bug_detail'),
    path('category/', CategoryList.as_view(), name='category_list'),
    path('size/', SizeList.as_view(), name='size_list'),
    path('enviroment/', EnviromentList.as_view(), name='enviroment_list'),

]
