import csv
from csv import DictReader
from datetime import datetime
from .models import * 
import os


def import_etcmarks():
    
        try:
            file_path = "C:\\Users\\sindi\\OneDrive\\Documents\\Student_django_v3\\student\\vege\\ETC.csv"
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
               
                for row in reader:
                    StudentETC.objects.create(

                        sno = row['ï»¿SNo'],
                        rollno = row['Roll_Number'],
                        student_name = row['Name_of_the_Student'],
                        s1_marks = row['S1'],
                        s2_marks = row['S2'],
                        avg_s_marks = row['AVG_S'],
                        i1_marks = row['I-1'],
                        i2_marks = row['I-2'],
                        avg_i_marks = row['AVG_I'],
                        total = row['TOTAL'],
                        )
            print("success")
        except Exception as e:
            print("exception",e)


def import_osmarks():
    
        try:
            file_path = "C:\\Users\\sindi\\OneDrive\\Documents\\Student_django_v3\\student\\vege\\OS.csv"
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    StudentOS.objects.create(

                        sno = row['ï»¿SNo'],
                        rollno = row['Roll_Number'],
                        student_name = row['Name_of_the_Student'],
                        s1_marks = row['S1'],
                        s2_marks = row['S2'],
                        avg_s_marks = row['AVG_S'],
                        i1_marks = row['I-1'],
                        i2_marks = row['I-2'],
                        avg_i_marks = row['AVG_I'],
                        total = row['TOTAL'],
                        )
            print("success")
        except Exception as e:
            print("exception",e)

         

def import_famarks():
    
        try:
            file_path = "C:\\Users\\sindi\\OneDrive\\Documents\\Student_django_v3\\student\\vege\\FA.csv"
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    StudentFA.objects.create(

                        sno = row['ï»¿SNo'],
                        rollno = row['Roll_Number'],
                        student_name = row['Name_of_the_Student'],
                        s1_marks = row['S1'],
                        s2_marks = row['S2'],
                        avg_s_marks = row['AVG_S'],
                        i1_marks = row['I-1'],
                        i2_marks = row['I-2'],
                        avg_i_marks = row['AVG_I'],
                        total = row['TOTAL'],
                        )
            print("success")
        except Exception as e:
            print("exception",e)

def import_m3marks():
    
        try:
            file_path = "C:\\Users\\sindi\\OneDrive\\Documents\\Student_django_v3\\student\\vege\\m3.csv"
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    StudentM3.objects.create(

                        sno = row['ï»¿SNo'],
                        rollno = row['Roll_Number'],
                        student_name = row['Name_of_the_Student'],
                        s1_marks = row['S1'],
                        s2_marks = row['S2'],
                        avg_s_marks = row['AVG_S'],
                        i1_marks = row['I-1'],
                        i2_marks = row['I-2'],
                        avg_i_marks = row['AVG_I'],
                        total = row['TOTAL'],
                        )
            print("success")
        except Exception as e:
            print("exception",e)

def import_ssmarks():
    
        try:
            file_path = "C:\\Users\\sindi\\OneDrive\\Documents\\Student_django_v3\\student\\vege\\s&s.csv"
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                
                for row in reader:
                    StudentS_S.objects.create(

                        sno = row['ï»¿SNo'],
                        rollno = row['Roll_Number'],
                        student_name = row['Name_of_the_Student'],
                        s1_marks = row['S1'],
                        s2_marks = row['S2'],
                        avg_s_marks = row['AVG_S'],
                        i1_marks = row['I-1'],
                        i2_marks = row['I-2'],
                        avg_i_marks = row['AVG_I'],
                        total = row['TOTAL'],
                        )
            print("success")
        except Exception as e:
            print("exception",e)

def import_comarks():
    
        try:
            file_path = "C:\\Users\\sindi\\OneDrive\\Documents\\Student_django_v3\\student\\vege\\CO.csv"
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    StudentCO.objects.create(

                        sno = row['S.No'],
                        rollno = row['Roll_Number'],
                        student_name = row['Name_of_the_Student'],
                        s1_marks = row['S1'],
                        s2_marks = row['S2'],
                        avg_s_marks = row['AVG_S'],
                        i1_marks = row['I-1'],
                        i2_marks = row['I-2'],
                        avg_i_marks = row['AVG_I'],
                        total = row['TOTAL'],
                        )
            print("success")
        except Exception as e:
            print("exception",e)

def import_dbmsmarks():
    
        try:
            file_path = "C:\\Users\\sindi\\OneDrive\\Documents\\Student_django_v3\\student\\vege\\DBMS.csv"
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    StudentDBMS.objects.create(

                        sno = row['S.No'],
                        rollno = row['Roll_Number'],
                        student_name = row['Name_of_the_Student'],
                        s1_marks = row['S1'],
                        s2_marks = row['S2'],
                        avg_s_marks = row['AVG_S'],
                        i1_marks = row['I-1'],
                        i2_marks = row['I-2'],
                        avg_i_marks = row['AVG_I'],
                        total = row['Total'],
                        )
            print("success")
        except Exception as e:
            print("exception",e)