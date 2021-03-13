from django.db import models
'''
Models are going to be a way of creating a python class that is going 
to represent data that i want django to store inside of a database.
when you create a model, django is going to figure out what SQL syntax 
it needs to use it to create that table, manipulate that table.

Every model is going to be a python class. you can think of this as having 
one model for each of the main tables we care about storing information  about

For every model added or changed, we must make migrations and migrate. 
We can then register the model in admin.py and visit the admin page
to create some info!'''

# Create your models here.

'''class Airport(models.Model):
	code = models.CharField(max_length= 3)
	#city = models.CharField(max_length= 64)

	def __str__(self):

 To Create and save a new flight from the django shell into the Flight table:
# Create some new airports
jfk = Airport.objects.get(city="New York")
cdg = Airport.objects.get(city="Paris")

# Save the airports to the database
jfk.save()
cdg.save()
'''


class Flight(models.Model):
	origin = models.CharField(max_length= 64)#you can add other param such as ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
	destination = models.CharField(max_length= 64)#ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
	#duration = models.IntegerField()


	def __str__(self):
		return f"{self.id}: {self.origin} to {self.destination}"

'''
# Add a flight and save it to the database
f = Flight(origin=jfk, destination=cdg, duration=435)
f.save() '''


'''Many-to-Many Relationships
Now, let’s work on integrating 
passengers into our models. We’ll create a passenger model to start:'''

class Passenger(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    flights = models.ManyToManyField(Flight, blank=True, related_name="passengers")# blank=True which means a passenger can have no flights

    def __str__(self):
        return f"{self.id} {self.first} {self.last}"



'''Django Admin
Since it is so common for developers to have to create new objects like we’ve 
been doing in the shell, Django comes with a default admin interface that allows
 us to do this more easily. To begin using this tool, we must first create an 
 administrative user: python manage.py createsuperuser '''

class Book_record(models.Model):
    first = models.CharField(max_length=64)
    last = models.CharField(max_length=64)
    gender = models.CharField(max_length=64)
    origin = models.CharField(max_length=64)
    destination = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    phone = models.IntegerField()
    
    def __str__(self):
        return f"{self.id} {self.first} {self.last} {self.gender} {self.origin} {self.destination} {self.email} {self.phone}"
    

    
   