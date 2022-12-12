from django.contrib import admin
from django.urls import path, include
from raquel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('usuarios.urls')),
    path('', views.Base.as_view(), name='base'),
    path('form/', views.FormsView.as_view(), name='form'),
    path('lista/', views.GeneratePdf.as_view(), name='tabela'),
    path('compro/<id>', views.GeneratePdf.view_pdf, name='comprovante'),
]
