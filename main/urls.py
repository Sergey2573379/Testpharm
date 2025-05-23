from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
                  path('', views.index, name='home'),
                  path('index2', views.index2, name='home2'),
                  path('index3', views.index3, name='home3'),
                  path('cabinet/<int:id>/', views.cabinet, name='cabinet'),
                  path('edituser/<int:id>/', views.edituser, name='edituser'),
                  path('dellsession', views.dellsession, name='dellsession'),
                  path('dorixona', views.dorixona, name='dorixona'),
                  path('dorixonapage', views.dorixonapage, name='dorixonapage'),
                  path('dorixonadrug/<int:dori_id>/', views.dorixonadrug, name='dorixonadrug'),
                  path('drugcreate', views.drugcreate, name='drugcreate'),
                  path('drugedit/<int:dori_id>/', views.drugedit, name='drugedit'),
                  path('drugdelete/<int:id>/', views.drugdelete, name='drugdelete'),
                  path('categorucreate', views.categorucreate, name='categorucreate'),
                  path('categoredit/<int:tid>/', views.categoredit, name='categoredit'),
                  path('categordrug/<int:cid>/', views.categordrug, name='categordrug'),
                  path('catdrug/<int:cid>/', views.catdrug, name='catdrug'),
                  path('drugdetail/<int:cid>/', views.drugdetail, name='drugdetail'),
                  path("addcart/<int:id>/<int:farm_id>", views.addcart, name="addcart"),
                  path('plus/', views.plus, name='plus'),
                  path('minus/', views.minus, name='minus'),
                  path('card', views.card, name='card'),
                  path('cardpage', views.cardpage, name='cardpage'),
                  path('addajax/', views.addajax, name='addajax'),
                  path('poiskpage', views.poiskpage, name='poiskpage'),
                  path('werajax/<int:id>', views.werajax, name='werajax'),
                  path('dellproduct/<int:drug_id>', views.dellproduct, name='dellproduct'),
                  path('clear_cart/', views.clear_cart, name='clear_cart'),
                  path('registrpage', views.registrpage, name='registrpage'),
                  path('login', views.login, name='login'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
