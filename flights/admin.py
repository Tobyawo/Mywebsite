from django.contrib import admin

''' Now, we must add our models to the admin application by entering the
admin.py file within our app, and importing and registering our models. 
This tells Django which models/tables we would like to have access to in the
admin app. Now, when we visit our site and add /admin to the url,
we can log into a page that looks like this'''



from .models import *
# you can Register your models here this way.
#admin.site.register(Flight)
#admin.site.register(Book_record)
admin.site.register(Passenger)


'''Another advantage of using the Django admin app is that it is customizable.
For example, if we wish to see all aspects of a flight in the admin interface, 
we can create a new class within admin.py and add it as an argument when registering 
he Flight model instead of registering the flight model direct as above: '''

class FlightAdmin(admin.ModelAdmin):
    list_display = ("id", "origin", "destination")

# Register your models here.
admin.site.register(Flight, FlightAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ("id","first","last", "origin", "destination","email","phone")

# Register your models here.
admin.site.register(Book_record, BookAdmin)