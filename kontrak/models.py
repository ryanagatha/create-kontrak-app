from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Client(models.Model):
  name = models.CharField('Nama Klien', max_length=255, db_index=True)
  address = models.CharField(max_length=255)
  phone = models.CharField(max_length=20, blank=True)
  email = models.EmailField(blank=True)

  def __str__(self):
    return self.name

class Project(models.Model):
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)
  name = models.CharField('Nama Proyek',max_length=255, db_index=True)
  client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
  project_address = models.CharField(max_length=255)
  start_date = models.DateTimeField(blank=True)
  description = models.TextField(blank=True)

  def __str__(self):
    return self.name

class CostAcc(models.Model):
  name = models.CharField('Pos Biaya',max_length=50, db_index=True)
  description = models.CharField(max_length=255)

  def __str__(self):
    return self.name

class Unit(models.Model):
  name = models.CharField('Nama Satuan',max_length=50, db_index=True)
  abbreviation = models.CharField(max_length=10, db_index=True, blank=True)

  def __str__(self):
    return self.name


class WorkItem(models.Model):
  name = models.CharField('Nama Pekerjaan',max_length=255, db_index=True)
  cost_acc = models.ForeignKey(CostAcc, on_delete=models.DO_NOTHING, null=True)
  unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)
  unit_price = models.DecimalField(max_digits=20, decimal_places=0)
  unit_budget= models.DecimalField(max_digits=20, decimal_places=0)
  city = models.CharField(max_length=255, blank=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  created_by = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return self.name

class Rab(models.Model):
  project = models.OneToOneField(Project, on_delete=models.CASCADE)
  work_item = models.ForeignKey(WorkItem, on_delete=models.DO_NOTHING, null=True)
  unit = models.ForeignKey(Unit, on_delete=models.DO_NOTHING, null=True)
  volume = models.DecimalField(max_digits=10, decimal_places=2)
  start_date = models.DateTimeField(blank=True, null=True)
  duration = models.IntegerField(blank=True, null=True)

  def __str__(self):
    return self.project.name + ' ' + self.work_item.name
