class animal:
    def make_sound(self):
      print("generic animal sound")
      
class dog(animal):
    def make_sound(self):
       print("Dog barks")      
       
class cat(animal):
    def make_sound(self):
       print("Cat meows")
       
def animal_sound_in_zoo(animal_obj):
    animal_obj.make_sound()
       
my_dog=dog() #dog instance

my_cat=cat() #cat instance

print("Sounds of the animals in the zoo")
animal_sound_in_zoo(my_dog)
animal_sound_in_zoo(my_cat)
