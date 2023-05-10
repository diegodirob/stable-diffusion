from django.contrib import admin
from django.urls import path

from stable.views import TextToImageFormView, ResultView, StableRecordListView

urlpatterns = [
    path('', TextToImageFormView.as_view()),

    path('stable/result/<int:pk>/', ResultView.as_view(), name='stable-result'),
    path('stable/list/', StableRecordListView.as_view(), name='stable-list'),


    path('admin/', admin.site.urls),
]
