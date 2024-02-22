from django.urls import path
from userapp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    path("home",views.home,name="hom"),
    path("features",views.Features,name="fetrs"),
    path("drinks",views.drinks,name="drks"),
    path("Order",views.Order,name="odr"),
    #path("Login",views.SignIn,name="logreg"),
    path("pricing",views.price,name="pris"),
    path("create",views.createaccount,name="crtaccount"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)