from django.conf.urls import url,include
import views

urlpatterns = [
 
    url(r'^register_data/', views.login, name="reg")
]
