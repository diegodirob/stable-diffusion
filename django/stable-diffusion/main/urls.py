from django.contrib import admin
from django.urls import path

from stable.views import TextToImageFormView, ResultView

urlpatterns = [
    path('', TextToImageFormView.as_view()),
    path('result/<int:pk>/', ResultView.as_view(), name='result'),

    path('admin/', admin.site.urls),
]
