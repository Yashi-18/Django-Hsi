from django.urls import path
from . import views

urlpatterns = [
    # halaman / = awal = index
    path('', views.portal_view),
    #halaman moba/ = mobile legends
    path('moba/', views.moba_view),
    #halaman genshin/ = genshin impact
    path('genshin/', views.genshin_view),
    #halaman dota/ = dota
    path('dota/', views.dota_view),
    
] 