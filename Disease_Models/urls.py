from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diabetes/', include('diabetes.urls')),
    #path('mammogram/', include('mammogram.urls'))
]
