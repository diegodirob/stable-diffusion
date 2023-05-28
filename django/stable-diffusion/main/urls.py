from django.contrib import admin
from django.urls import path

from stable.views import StableFormView, ResultView, StableRecordListView

urlpatterns = [
    path('stable/', StableFormView.as_view()),
    path('stable/<str:service>/', StableFormView.as_view()),
    path('stable/result/<int:pk>/', ResultView.as_view(), name='stable-result'),
    path('stable/list/', StableRecordListView.as_view(), name='stable-list'),


    path('admin/', admin.site.urls),
]
