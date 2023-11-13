from django.contrib import admin
from .models import GameList,Reviews,Pros,Cons,Genera,AdditionalImages

# Register your models here.

admin.site.register(GameList)
admin.site.register(Reviews)
admin.site.register(Pros)
admin.site.register(Cons)
admin.site.register(Genera)
admin.site.register(AdditionalImages)