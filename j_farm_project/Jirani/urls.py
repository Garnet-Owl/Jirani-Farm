from django.urls import path
from . import views

app_name = 'jirani'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('tractors/', views.tractors, name='tractors'),
    path('tractors/<int:tractor_id>/', views.tractor_detail, name='tractor_detail'),
    path('tractors/add/', views.add_tractor, name='add_tractor'),
    path('tractors/edit/<int:tractor_id>/', views.edit_tractor, name='edit_tractor'),
    path('tractors/delete/<int:tractor_id>/', views.delete_tractor, name='delete_tractor'),
    path('leases/', views.leases, name='leases'),
    path('leases/<int:lease_id>/', views.lease_detail, name='lease_detail'),
    path('leases/create/<int:tractor_id>/', views.create_lease, name='create_lease'),
    path('leases/cancel/<int:lease_id>/', views.cancel_lease, name='cancel_lease'),
    path('leases/confirm/<int:lease_id>/', views.confirm_lease, name='confirm_lease'),
    path('leases/complete/<int:lease_id>/', views.complete_lease, name='complete_lease'),
]
