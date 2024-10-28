from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class Kantin(models.Model):
    nama = models.CharField(max_length=250)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}', message="min 8 digit")
    telpon = models.CharField(validators=[phone_regex], max_length = 15, blank=  True)

    def __str__(self):
        return self.nama

    def __unicode__(self):
        return self.nama

class Makanan(models.Model):
    nama = models.CharField(max_length=250)
    harga = models.IntegerField()
    gambar = models.ImageField(upload_to='makan/images')
    stok = models.IntegerField()
    kantin = models.ForeignKey(Kantin,on_delete=models.CASCADE)
    TERSEDIA = (
        ('0', 'Tidak Tersedia'),
        ('1', 'Tersedia')
    )
    tersedia = models.CharField(max_length=1,choices=TERSEDIA)

    def __str__(self):
        return self.nama

    def __unicode__(self):
        return self.nama
