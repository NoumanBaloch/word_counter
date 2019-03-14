

from django.urls import path
from . import view
urlpatterns = [
    path('', view.homepage),
    path('count/', view.count, name="count"),
    path('about/', view.about, name='about')
]
