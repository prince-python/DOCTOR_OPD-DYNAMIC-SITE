from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250, blank='True')
    pwd = models.CharField(max_length=250)
    category = models.CharField(max_length=250, choices=(
        ('lungs', 'lungs'), ('Brain', 'Brain'), ('Bone', 'Bone'), ('heart', 'heart')))
    exp = models.CharField(max_length=250)
    def __str__(self):
        return self.name




class Patient(models.Model):
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=250,blank=True)
    address = models.CharField(max_length=250)
    Doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE,max_length=1050)
    apoinment= models.TimeField(max_length=40)
    date=models.DateField(max_length=50)
    issue=models.CharField(max_length=250)
    def __str__(self):
        return self.name
    
    
    
class activity(models.Model):
    Patient=models.OneToOneField(Patient,primary_key=True,on_delete=models.CASCADE)
    confirm = models.BooleanField(max_length=20,default=False)
    date_time= models.DateTimeField()
    data=models.FileField(upload_to='files', max_length=100,blank=True)
    

    

    