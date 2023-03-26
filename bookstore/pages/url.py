from django.urls import path
from .views import HomePageView, ArianPageView
urlpatterns = [

    path('', HomePageView.as_view(), name='home'),
    path('arian/', ArianPageView.as_view(), name='arianPage')

    #  path('account/', include('django.urls')),
]