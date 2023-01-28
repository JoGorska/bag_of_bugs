from django.urls import path
from .views import BugsList, BugDetail


urlpatterns = [
    path('', BugsList.as_view(), name='bugs_list'),
    path('<str:slug>/', BugDetail.as_view(), name='bug_detail'),

]
