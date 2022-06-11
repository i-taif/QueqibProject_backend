from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('create-city',views.add_city,name='create-city'),
   path('update-city/<slug>',views.update_city,name='update-city'),
   path('list-cities',views.list_city,name='list-cities'),
   path('delete-city/<slug>',views.delete_city,name='delete-city'),
   path('create-profile',views.create_profile,name='create-profile'),




   #path('create-post',views.create_post,name='create-post')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)