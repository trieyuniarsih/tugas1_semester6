model.py


from django.db import models

class Penerbit(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class Pengarang(models.Model):
    nama = models.CharField(max_length=100)
    alamat = models.CharField(max_length=200)

    def __str__(self):
        return self.nama

class Buku(models.Model):
    judul = models.CharField(max_length=100)
    pengarang = models.ForeignKey(Pengarang, on_delete=models.CASCADE)
    penerbit = models.ForeignKey(Penerbit, on_delete=models.CASCADE)
    tahun_terbit = models.IntegerField()

    def __str__(self):
        return self.judul

class RakBuku(models.Model):
    nomor = models.CharField(max_length=10)
    lokasi = models.CharField(max_length=100)

    def __str__(self):
        return self.nomor

class Anggota(models.Model):
    nama = models.CharField(max_length=100)
    nim = models.CharField(max_length=10, unique=True)
    alamat = models.CharField(max_length=200)

    def __str__(self):
        return self.nama
