from django.db import models


class Test(models.Model):
    patient_id = models.CharField(max_length=32, null=True, blank=True, default='guest')
    pregnancies = models.IntegerField()
    glucose = models.IntegerField()
    blood_pressure = models.IntegerField(verbose_name='Blood Pressure(Diastolic)')
    skin_thickness = models.IntegerField(verbose_name='Skin Thickness(Tricep skinfold thickness(mm))')
    insulin = models.IntegerField(verbose_name='Insulin Level(U/ml)')
    BMI = models.DecimalField(decimal_places=2, max_digits=4)
    age = models.IntegerField()
    outcome = models.IntegerField(default=9,)##  verbose_name='Constant(Ignore this)')

    def __str__(self):
        return f'{self.patient_id} - {self.pk}'
