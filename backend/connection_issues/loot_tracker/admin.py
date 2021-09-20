from django.contrib import admin
from loot_tracker.models import Patch, Item, Job, Character, Static, StaticLootHistory, StaticMember, StaticBIS

admin.site.register(Patch)
admin.site.register(Item)
admin.site.register(Job)
admin.site.register(Character)
admin.site.register(Static)
admin.site.register(StaticMember)
admin.site.register(StaticBIS)
admin.site.register(StaticLootHistory)
# Register your models here.
