from django.urls import path,include
from .import views

urlpatterns = [
    path('',views.home,name="home"),
    path('signup/',views.signup,name="signup"),
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('sellerhome/',views.sellerhome,name="sellerhome"),
    path('sellersignup/',views.sellersignup,name="sellersignup"),
    path('seller_adddetails/',views.seller_adddetails,name="seller_adddetails"),
    path('seller_viewdetails/',views.seller_viewdetails,name="seller_viewdetails"),
    path('seller_Editdetails/<int:pk>/',views.seller_Editdetails,name="seller_Editdetails"),
    path('seller_Deletedetails/<int:pk>/',views.seller_Deletedetails,name="seller_Deletedetails"),
    path('user_view_all_details/',views.user_view_all_details,name="user_view_all_details"),

 ]