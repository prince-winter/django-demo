from django.contrib import admin
from .models import Post, Author, Date, UserProfileInfo


# Register your models here.
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(Date)
admin.site.register(UserProfileInfo)

