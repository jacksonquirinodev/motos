from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from motorcycles.views import MotorcyclesListView, NewMotorcycleView, MotorcycleDetailView, MotorcycleUpdateView, MotorcycleDeleteView
from accounts.views import register_view, login_view, logout_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('motorcycles/', MotorcyclesListView.as_view(), name='motorcycles_list'),
    path('new_motorcycle/', NewMotorcycleView.as_view(), name='new_motorcycle'),
    path('motorcycle/<int:pk>/', MotorcycleDetailView.as_view(), name='motorcycle_detail'),
    path('motorcycle/<int:pk>/update/',MotorcycleUpdateView.as_view(),name='motorcycle_update'),
    path('motorcycle/<int:pk>/delete/', MotorcycleDeleteView.as_view(), name='motorcycle_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

