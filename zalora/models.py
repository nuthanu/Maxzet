from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
	JENIS_KELAMIN = (
		('L','Laki-Laki'),
		('P','Perempuan')
	)
	user = models.OneToOneField(User)
	nama_lengkap=models.CharField(max_length=30)
	jenis_kelamin=models.CharField(max_length=1,choices=JENIS_KELAMIN)
	tanggal_lahir=models.DateField(auto_now_add=False)
	no_hp=models.CharField(max_length=12)
	alamat=models.CharField(max_length=50)
	kode_pos=models.CharField(max_length=5)
	def __unicode__(self):
		return self.user.username

class Barang(models.Model):
	nama=models.CharField(max_length=50)
	merk=models.CharField(max_length=30)
	harga= models.DecimalField(max_digits=10, decimal_places=2)
	gambar= models.URLField()
	deskripsi=models.TextField()
	def __unicode__(self):
		return self.nama
