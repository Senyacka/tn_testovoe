from django.db import models


class AZS(models.Model):
    id = models.AutoField(primary_key=True)
    coordinates = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)


class Service(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.CharField(max_length=100)


class AZSService(models.Model):
    azs = models.ForeignKey(AZS, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    status = models.BooleanField()


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    url = models.URLField(max_length=200)


class AZSImage(models.Model):
    id = models.AutoField(primary_key=True)
    azs = models.ForeignKey(AZS, on_delete=models.CASCADE, default=None, null=True)
    image = models.ForeignKey(Image, on_delete=models.CASCADE, default=None, null=True)
