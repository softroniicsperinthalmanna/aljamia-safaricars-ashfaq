from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from .views import index, activate 


urlpatterns = [
    path('', views.index, name="home"),
    path('car_preview/<int:pk>', views.car_prvw.as_view(), name="car_preview"),
    path('bike_preview/<int:pk>', views.bike_prvw.as_view(), name="bike_preview"),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  
        activate, name='activate'), 
    # path("category-title/<val>",views.CarPreviewTitle.as_view(), name='car_preview-title'),
    # path("product-detail/<int:pk>",views.ProductDetail.as_view(), name='product-detail'),
    path('car_accessories/', views.accessories, name="car_accessories"), 
    path('sell_your_car/', views.SellCarView.as_view(), name="sell_car"), 
    path('service/', views.service, name="services"),
    path('garage/', views.garage, name="garages"),
    path('feedback/', views.feeds, name="feedbacks"),
    # path('login/', views.login, name="login"),
    path('register/', views.registration, name="sign_up"),
    path('otp/', views.otp, name="otp"),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='user/log.html',authentication_form=LoginForm), name='login'),
    path('see_more/', views.seemore, name="seemore"),
    path("accounts/logout/",auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout' ),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('user_address/', views.addressandcart, name="user_address"),
    path('test_drive_book/', views.test_drive, name="testdrive"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='reset_password'),
    path('reset_password_send/',auth_views.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    # path("password_change", views.password_change, name="password_change"),
    # path("password_reset", views.password_reset_request, name="password_reset"),
    # path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
    # path('order_details/', views.order_details, name='order_details'),
    path('service_details/',views.service_details, name='service_details'),
    path('test_details/',views.test_details, name='test_drive_details'),
    path('paymentdone/',views.payment_done, name='paymentdone'),
    path('payment/',views.payment, name='paypal'),
    path('orders/',views.index, name='orders'),
    path('checkout/',views.checkout.as_view(), name='checkout'),
    path('cart/',views.show_cart, name='showcart'),
    path('add-to-cart/<int:pk>',views.add_to_cart, name='add-to-cart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    path("product-detail/<int:pk>",views.ProductDetail.as_view(), name='product-detail'),
    path("updateAddress/<int:pk>",views.updateAddress.as_view(), name='updateAddress'),
    path('deleteAddress/<int:pk>',views.deleteAddress, name='deleteAddress'),

   
]