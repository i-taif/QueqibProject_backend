from django.urls import  path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('list-user/<id>',views.list_user_info,name='list-user'),
   path('list-user',views.list_all_user,name='list-user'),
   path('delete-user/<id>',views.delete_user,name='delete-user'),
   path('create-city',views.add_city,name='create-city'),
   path('update-city/<slug>',views.update_city,name='update-city'),
   path('list-cities',views.list_cities,name='list-cities'),
   path('city-details/<id>',views.city_details,name='city-details'),
   path('search-city/<name>',views.search_city,name='search-city'),  
   path('delete-city/<slug>',views.delete_city,name='delete-city'),
   path('create-profile',views.create_profile,name='create-profile'),
   path('list-profile',views.list_all_profile,name='list-profile'),
   path('update-profile/<slug>',views.update_profile,name='update-profile'),
   path('delete-profile/<slug>',views.delete_profile,name='delete-profile'),
   path('profile-details/<user_id>',views.profile_details,name='profile-details'),
   path('create-post',views.add_post,name='create-post'),
   path('post-details/<slug>',views.post_details,name='post-details'),
   path('update-post/<slug>',views.update_post,name='update-post'),
   path('list-post',views.list_post,name='list-post'),
   path('delete-post/<slug>',views.delete_post,name='delete-post'),
   path('create-comment',views.add_comment,name='create-comment'),
   path('update-comment/<slug>',views.update_comment,name='update-comment'),
   path('list-comment/<post_id>',views.list_comments,name='list-comment'),
   path('list-all-comment',views.list_all_comments,name='list-all-comment'),
   path('delete-comment/<slug>',views.delete_comment,name='delete-comment'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)