from django.conf.urls import url,include
import views

urlpatterns = [
 
	url(r'^userlogin/', views.user_login, name='login_data'),
	url(r'^registerdata/', views.register_data, name="reg"),
   #url(r'^logout/',views.user_logout,name='logout')
	
]
