from django.contrib import admin
from .models import City,Profile,Post,Comment
# Register your models here.


admin.site.register(City)

class Profileadmin(admin.ModelAdmin):
   list_display = ('name','user','bio','image')
admin.site.register(Profile,Profileadmin)

class Postadmin(admin.ModelAdmin):
   list_display = ('title','body','image','profile')
admin.site.register(Post,Postadmin)

class Commentadmin(admin.ModelAdmin):
   list_display = ('user','post','content')
admin.site.register(Comment,Commentadmin)
