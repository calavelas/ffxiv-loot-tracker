from django.urls import path
from loot_tracker.views import CheckItem, Index,CharacterView,Bis
from . import views

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('check/', CheckItem.as_view(), name='Check Item'),
    path('character/<str:name>', CharacterView.as_view(), name="Character Information"),
    path('brd/', views.brd, name='Bard'),
    path('blm/', views.blm, name='Black Mage'),
    path('bis/', Bis.as_view(), name='Best in slot')
]