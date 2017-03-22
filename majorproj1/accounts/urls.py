from django.conf.urls import url,include
import views

urlpatterns = [
 
	url(r'^userlogin/', views.user_login, name='login_data'),
	url(r'^register_data/', views.login, name="reg")
]
