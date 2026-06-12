from django.db import models
from django.contrib.auth.models import User


class StudentETC(models.Model):
    sno = models.IntegerField()
    rollno = models.CharField(max_length=200)  # Adjust the max_length based on your needs
    student_name = models.CharField(max_length=500)
    s1_marks = models.FloatField()
    s2_marks = models.FloatField()
    avg_s_marks = models.FloatField()
    i1_marks = models.FloatField()
    i2_marks = models.FloatField()
    avg_i_marks = models.FloatField()
    total = models.FloatField()

    def __str__(self) -> str:
        return self.rollno

    class Meta:
        ordering = ['rollno']


class StudentOS(models.Model):
    sno = models.IntegerField()
    rollno = models.CharField(max_length=200)  # Adjust the max_length based on your needs
    student_name = models.CharField(max_length=500)
    s1_marks = models.FloatField()
    s2_marks = models.FloatField()
    avg_s_marks = models.FloatField()
    i1_marks = models.FloatField()
    i2_marks = models.FloatField()
    avg_i_marks = models.FloatField()
    total = models.FloatField()

    def __str__(self) -> str:
        return self.rollno

    class Meta:
        ordering = ['rollno']


class StudentM3(models.Model):
    sno = models.IntegerField()
    rollno = models.CharField(max_length=200)  # Adjust the max_length based on your needs
    student_name = models.CharField(max_length=500)
    s1_marks = models.FloatField()
    s2_marks = models.FloatField()
    avg_s_marks = models.FloatField()
    i1_marks = models.FloatField()
    i2_marks = models.FloatField()
    avg_i_marks = models.FloatField()
    total = models.FloatField()

    def __str__(self) -> str:
        return self.rollno

    class Meta:
        ordering = ['rollno']

class StudentFA(models.Model):
    sno = models.IntegerField()
    rollno = models.CharField(max_length=200)  # Adjust the max_length based on your needs
    student_name = models.CharField(max_length=500)
    s1_marks = models.FloatField()
    s2_marks = models.FloatField()
    avg_s_marks = models.FloatField()
    i1_marks = models.FloatField()
    i2_marks = models.FloatField()
    avg_i_marks = models.FloatField()
    total = models.FloatField()

    def __str__(self) -> str:
        return self.rollno

    class Meta:
        ordering = ['rollno']

class StudentS_S(models.Model):
    sno = models.IntegerField()
    rollno = models.CharField(max_length=200)  # Adjust the max_length based on your needs
    student_name = models.CharField(max_length=500)
    s1_marks = models.FloatField()
    s2_marks = models.FloatField()
    avg_s_marks = models.FloatField()
    i1_marks = models.FloatField()
    i2_marks = models.FloatField()
    avg_i_marks = models.FloatField()
    total = models.FloatField()

    def __str__(self) -> str:
        return self.rollno

    class Meta:
        ordering = ['rollno']


class StudentCO(models.Model):
    sno = models.IntegerField()
    rollno = models.CharField(max_length=200)  # Adjust the max_length based on your needs
    student_name = models.CharField(max_length=500)
    s1_marks = models.FloatField()
    s2_marks = models.FloatField()
    avg_s_marks = models.FloatField()
    i1_marks = models.FloatField()
    i2_marks = models.FloatField()
    avg_i_marks = models.FloatField()
    total = models.FloatField()

    def __str__(self) -> str:
        return self.rollno

    class Meta:
        ordering = ['rollno']


class StudentDBMS(models.Model):
    sno = models.IntegerField()
    rollno = models.CharField(max_length=200)  # Adjust the max_length based on your needs
    student_name = models.CharField(max_length=500)
    s1_marks = models.FloatField()
    s2_marks = models.FloatField()
    avg_s_marks = models.FloatField()
    i1_marks = models.FloatField()
    i2_marks = models.FloatField()
    avg_i_marks = models.FloatField()
    total = models.FloatField()

    def __str__(self) -> str:
        return self.rollno

    class Meta:
        ordering = ['rollno']















