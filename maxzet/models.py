from django.db import models
from django.contrib.auth.models import User

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

class Men(models.Model):
    KATEGORI = (
        ('A','Atasan'),
        ('K','Kemeja'),
	('B','Bawahan'),
	('O','Outerwear'),
    )
    kategori=models.CharField(max_length=1,choices=KATEGORI)
    kode_barang=models.CharField(max_length=14)
    nama=models.CharField(max_length=50)
    merk=models.CharField(max_length=30)
    harga= models.DecimalField(max_digits=10, decimal_places=2)
    gambar= models.URLField()
    deskripsi=models.TextField()
    def __unicode__(self):
        return self.nama

class Women(models.Model):
    KATEGORI = (
        ('D','Dress'),
        ('A','Atasan'),
	('B','Bawahan'),
	('O','Outerwear'),
    )
    kategori=models.CharField(max_length=1,choices=KATEGORI)
    kode_barang=models.CharField(max_length=14)
    nama=models.CharField(max_length=50)
    merk=models.CharField(max_length=30)
    harga= models.DecimalField(max_digits=10, decimal_places=2)
    gambar= models.URLField()
    deskripsi=models.TextField()
    def __unicode__(self):
        return self.nama

class TransaksiMen(models.Model):
    PEMBAYARAN =(('Transfer','Transfer'),('COD','Cash on Delivery'))
    barang=models.ForeignKey(Men,related_name="transaksi-men")
    pembeli=models.OneToOneField(User)
    alamat_pengiriman=models.TextField()
    jenis_pembayaran=models.CharField(max_length=17,choices=PEMBAYARAN)
    total_bayar=models.IntegerField()

class TransaksiWomen(models.Model):
    PEMBAYARAN =(('Transfer','Transfer'),('COD','Cash on Delivery'))
    barang=models.ForeignKey(Women,related_name="transaksi-women")
    pembeli=models.OneToOneField(User)
    alamat_pengiriman=models.TextField()
    jenis_pembayaran=models.CharField(max_length=17,choices=PEMBAYARAN)
    total_bayar=models.IntegerField()
