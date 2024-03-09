from django.contrib import admin

# Register your models here.

from wagtail.contrib.modeladmin.options import modeladmin_register
from wagtail_localize.modeladmin.options import TranslatableModelAdmin

from .models import Team

class TeamMember(TranslatableModelAdmin):
    model = Team

    menu_label = "Team Member"
    add_to_settings_menu = False
    list_display = ('full_name', 'designation', 'contact',)
    search_fields = ('full_name',)

modeladmin_register(TeamMember)