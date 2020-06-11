from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view,name="login"),
    path('logout',views.logout_view, name='logout'),
    path('submitorderpizza',views.submitorderpizza,name="submitorderpizza"),
    path('submitordersub',views.submitordersub,name="submitordersub"),
    path('cart',views.cart_view,name="cart"),
    path('delete',views.delete_from_cart,name='delete'),
    path('submitcart',views.submitcart,name='submitcart'),
    path('trackorders',views.trackorder_view,name='trackorders'),
    path('completeorder',views.complete_order, name='completeorder'),
    path('submitordersalads',views.submitordersalads,name='submitordersalads'),
    path('submitorderpasta',views.submitorderpasta,name='submitorderpasta'),
    path('submitorderdinnerplatter',views.submitorderdinnerplatter,name='submitorderdinnerplatter')
]
