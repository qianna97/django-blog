from django.contrib import admin
from .models import Post,Contact
# Register your models here.
class PostModelAdmin(admin.ModelAdmin):
	list_display = ("title","category","subtitle","timestamp","updated")
	list_display_links = ["title"]
	list_filter = ["updated","timestamp"]
	search_fields = ["title","content"]

	class Meta:
		model = Post

class ContactModelAdmin(admin.ModelAdmin):
	list_display = ("name","email","phone","timestamp")
	list_display_links = ["name"]
	list_filter = ["timestamp"]
	search_fields = ["name","email"]

	class Meta:
		model = Contact

admin.site.register(Post, PostModelAdmin)
admin.site.register(Contact, ContactModelAdmin)