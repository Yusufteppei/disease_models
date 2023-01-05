from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diabetes.urls')),
    #path('mammogram/', include('mammogram.urls'))
]
