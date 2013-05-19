# we need to tell the admin that Poll objects have an admin interface. 
# To do this, this file registers our Model with some custom options
from django.contrib import admin
from polls.models import Choice, Poll

# this tells django: "Choice objects are edited on the Poll admin page. By default, 
# provide enough fields for 3 choices."
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

# In order to customize how the admin form looks and works. 
# This is done by telling Django the options you want when the object is registered
class PollAdmin(admin.ModelAdmin):
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

admin.site.register(Poll, PollAdmin)
