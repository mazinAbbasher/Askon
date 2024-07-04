from django.contrib import admin
from .models import House,State,Image,Region,Owner,Message,Order

class HouseAdmin(admin.ModelAdmin):
    list_display = ["pk","sequence",'region','rooms','ready','price','for_sale','for_rent','is_available','area','owner',"date"]

class StateAdmin(admin.ModelAdmin):
    list_display = ["name"]

class ImageAdmin(admin.ModelAdmin):
    list_display = ["house", 'image']

class RegionAdmin(admin.ModelAdmin):
    list_display = ["name", 'state']

class MessageAdmin(admin.ModelAdmin):
    list_display = ["phone", 'message',"date"]

class OrderAdmin(admin.ModelAdmin):
    list_display = ["phone", 'name',"house","date"]

class OwnerAdmin(admin.ModelAdmin):
    list_display = ["name", 'phone',"another_phone"]


admin.site.register(House,HouseAdmin)
admin.site.register(State,StateAdmin)
admin.site.register(Image,ImageAdmin)
admin.site.register(Region,RegionAdmin)
admin.site.register(Owner,OwnerAdmin)
admin.site.register(Message,MessageAdmin)
admin.site.register(Order,OrderAdmin)

# Register your models here.
