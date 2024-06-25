from django.db import models

class cliente :
    nombre_apellido= models.CharField (max_length= 50)
    email= models.CharField (max_length= 20)
    ingreso= models.CharField (max_length= 15)
    