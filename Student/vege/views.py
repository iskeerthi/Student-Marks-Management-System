from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User,Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Sum, Q


def index(request):
    return render(request,'index2.html')

def job(request):
    return render(request,'job.html')

def freelancer(request):
    return render(request,'freelancer.html')

def about(request):
    return render(request,'about.html')


def login_page2(request):

    if request.user.is_authenticated:
        logout(request)
   
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username = username).exists():
            messages.info(request,'Invalid Username')
            return redirect('/login2/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request,'Invalid Password')
            return redirect('/login2/')
        
        else:

            if(user.last_name == 'Teacher'):
                login(request, user)
                return redirect('/first_page/Teacher')
            if(user.last_name == 'Student'):
                login(request, user)
                return redirect('/first_page/Student')
        
    return render(request, 'login2.html')




def register2(request):

    if request.user.is_authenticated:
        logout(request)

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        repassword = request.POST.get('repassword')
        group = request.POST.get('group')

        user = User.objects.filter(username= username)
        if user.exists():
            messages.info(request,'Username already taken')
            return redirect('/register/')
        if repassword == password:
            user = User.objects.create(
                first_name = first_name,
                last_name = group,
                username = username,
                password = password
            
            )

            user.set_password(password)
            user.save()



            messages.info(request,'Account created successfully')
        else:
            messages.error(request,"Passwords do not match")
            return redirect('/register2/')

        return redirect('/login2/')


    return render(request, 'register2.html')


def forgot_password(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password_new = request.POST.get('password')
        user = User.objects.get(username= username)
        user.set_password(password_new)
        user.save()
        messages.info(request,'Password changed successfully')
        return redirect('/login2/')

    return render(request, 'forgot_password.html')

def logout_page(request):
    logout(request)
    return redirect('/login2/')


def first_page(request,access):
    if access == "Teacher":
        return render(request, 'first_page.html')
    if access == "Student":
        return render(request, 'student_page.html')


def courses(request):
    return render(request, 'courses.html')

def contact(request):
    return render(request, 'contact.html')


def perform_action(request):
    action = request.GET.get('action', '')

    if request.user.is_authenticated:
        access = request.user.last_name
        
        if action == 'etc' and access == 'Teacher':
            return redirect('get_students', action='etc', access='Teacher')
        elif action == 'logout':
            return redirect('login')
        elif action == 'os' and access == 'Teacher':
            return redirect('get_students',action='os',access='Teacher')
        elif action == 'fa' and access == 'Teacher':
            return redirect('get_students',action='fa',access='Teacher')
        elif action == 'm3' and access == 'Teacher':
            return redirect('get_students',action='m3',access='Teacher')
        elif action == 'ss' and access == 'Teacher':
            return redirect('get_students',action='ss',access='Teacher')
        elif action == 'co' and access == 'Teacher':
            return redirect('get_students',action='co',access='Teacher')
        elif action == 'dbms' and access == 'Teacher':
            return redirect('get_students',action='dbms',access='Teacher')
        elif action == 'total' and access == 'Teacher':
            return redirect('get_students',action='total',access='Teacher')
        elif action == 'report' and access == 'Teacher':
            return redirect('report_student',action='report',access='Teacher')
        
        elif action == 'etc' and access == 'Student':
            return redirect('get_marks', action='etc', access='Student')
        elif action == 'logout':
            return redirect('login')
        elif action == 'os' and access == 'Student':
            return redirect('get_marks',action='os',access='Student')
        elif action == 'fa' and access == 'Student':
            return redirect('get_marks',action='fa',access='Student')
        elif action == 'm3' and access == 'Student':
            return redirect('get_marks',action='m3',access='Student')
        elif action == 'ss' and access == 'Student':
            return redirect('get_marks',action='ss',access='Student')
        elif action == 'co' and access == 'Student':
            return redirect('get_marks',action='co',access='Student')
        elif action == 'dbms' and access == 'Student':
            return redirect('get_marks',action='dbms',access='Student')
        elif action == 'report' and access == 'Student':
            return redirect('get_report',action='report',access='Student')
        else:
            return HttpResponse("Invalid action")
    else:
        return HttpResponse("User not authenticated")





#################### STUDENT ############################


@login_required
def get_marks(request, action, access):
    if request.user.is_authenticated:
        username = request.user.username
        access = request.user.last_name

    if access == "Student":
        if action == 'etc':
            sub = "ETC"

            queryset = StudentETC.objects.filter(rollno__icontains=username)
            

            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/marks.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access,'username':username})

        if action == 'os':
            sub = "OS"

            queryset = StudentOS.objects.filter(rollno__icontains=username)


            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/marks.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access,'username':username})


        if action == 'fa':
            sub = "FA"

            queryset = StudentFA.objects.filter(rollno__icontains=username)


            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/marks.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access,'username':username})

        if action == 'ss':
            sub = "S & S"

            queryset = StudentS_S.objects.filter(rollno__icontains=username)

            
            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/marks.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access,'username':username})

        if action == 'm3':
            sub = "M3"

            queryset = StudentM3.objects.filter(rollno__icontains=username)

            
            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/marks.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access,'username':username})
        
        if action == 'co':
            sub = "CO"

            queryset = StudentCO.objects.filter(rollno__icontains=username)

            
            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/marks.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access,'username':username})

        if action == 'dbms':
            sub = "DBMS"

            queryset = StudentDBMS.objects.filter(rollno__icontains=username)

            
            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/marks.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access,'username':username})




@login_required
def get_report(request,action, access):
    if request.user.is_authenticated:
        username = request.user.username
        access = request.user.last_name

        queryset = StudentETC.objects.filter(rollno__icontains=username).first()

        
        etc_marks = StudentETC.objects.filter(rollno__icontains=username)
        fa_marks = StudentFA.objects.filter(rollno__icontains=username)
        m3_marks = StudentM3.objects.filter(rollno__icontains=username)
        ss_marks = StudentS_S.objects.filter(rollno__icontains=username)
        os_marks = StudentOS.objects.filter(rollno__icontains=username)
        co_marks = StudentCO.objects.filter(rollno__icontains=username)
        dbms_marks = StudentDBMS.objects.filter(rollno__icontains=username)

        return render(request, 'report/reportcard.html',{'co_marks':co_marks,'dbms_marks':dbms_marks,'queryset':queryset,'etc_marks':etc_marks,'fa_marks':fa_marks,'m3_marks':m3_marks,'ss_marks':ss_marks,'os_marks':os_marks,'username':username,'access':access})



############################# TEACHER #######################################
@login_required
def report_student(request,action,access):
    print(action)
    print(access)

    if access == 'Teacher':

        if request.GET.get('search'):
            username = request.GET.get('search')
            

            queryset = StudentETC.objects.filter(rollno__icontains=username).first()

            
            etc_marks = StudentETC.objects.filter(rollno__icontains=username)
            fa_marks = StudentFA.objects.filter(rollno__icontains=username)
            m3_marks = StudentM3.objects.filter(rollno__icontains=username)
            ss_marks = StudentS_S.objects.filter(rollno__icontains=username)
            os_marks = StudentOS.objects.filter(rollno__icontains=username)
            co_marks = StudentCO.objects.filter(rollno__icontains=username)
            dbms_marks = StudentDBMS.objects.filter(rollno__icontains=username)

            return render(request, 'report/report_student.html',{'dbms_marks':dbms_marks,'co_marks':co_marks,'action':action,'queryset':queryset,'etc_marks':etc_marks,'fa_marks':fa_marks,'m3_marks':m3_marks,'ss_marks':ss_marks,'os_marks':os_marks,'username':username,'access':access})
        
        return render(request,'report/report_student.html',{'access':access,'action':action})
        



@login_required
def get_students(request, action, access):

    if access == "Teacher":
        if action == 'etc':
            sub = "ETC"

            queryset = StudentETC.objects.all()

            if request.GET.get('search'):
                search = request.GET.get('search')
                queryset = queryset.filter(
                    Q(student_name__icontains = search ) |
                    Q(rollno__icontains = search )
                    )

            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/students.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access})

        if access == "Teacher":
            if action == 'co':
                sub = "CO"

                queryset = StudentCO.objects.all()

                if request.GET.get('search'):
                    search = request.GET.get('search')
                    queryset = queryset.filter(
                        Q(student_name__icontains = search ) |
                        Q(rollno__icontains = search )
                        )

                paginator = Paginator(queryset, 10)
                page_number = request.GET.get("page",1)
                page_obj = paginator.get_page(page_number)
                return render(request, 'report/students.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access})

    if access == "Teacher":
        if action == 'dbms':
            sub = "DBMS"

            queryset = StudentDBMS.objects.all()

            if request.GET.get('search'):
                search = request.GET.get('search')
                queryset = queryset.filter(
                    Q(student_name__icontains = search ) |
                    Q(rollno__icontains = search )
                    )

            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/students.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access})

        if action == 'os':
            sub = "OS"

            queryset = StudentOS.objects.all()

            if request.GET.get('search'):
                search = request.GET.get('search')
                queryset = queryset.filter(
                    Q(student_name__icontains = search ) |
                    Q(rollno__icontains = search )
                    )

            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/students.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access})


        if action == 'fa':
            sub = "FA"

            queryset = StudentFA.objects.all()

            if request.GET.get('search'):
                search = request.GET.get('search')
                queryset = queryset.filter(
                    Q(student_name__icontains = search ) |
                    Q(rollno__icontains = search )
                    )

            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/students.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access})

        if action == 'ss':
            sub = "S & S"

            queryset = StudentS_S.objects.all()

            if request.GET.get('search'):
                search = request.GET.get('search')
                queryset = queryset.filter(
                    Q(student_name__icontains = search ) |
                    Q(rollno__icontains = search )
                    )

            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/students.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access})

        if action == 'm3':
            sub = "M3"

            queryset = StudentM3.objects.all()

            if request.GET.get('search'):
                search = request.GET.get('search')
                queryset = queryset.filter(
                    Q(student_name__icontains = search ) |
                    Q(rollno__icontains = search )
                    )

            paginator = Paginator(queryset, 10)
            page_number = request.GET.get("page",1)
            page_obj = paginator.get_page(page_number)
            return render(request, 'report/students.html',{'queryset':page_obj,'action':action,'sub':sub,'access':access})

        if action == "total":
            sub = "Total"

            queryset = StudentETC.objects.all()
    
            etc_rollnos = StudentETC.objects.values_list('rollno', flat=True).distinct()
            fa_rollnos = StudentFA.objects.values_list('rollno', flat=True).distinct()
            m3_rollnos = StudentM3.objects.values_list('rollno', flat=True).distinct()
            ss_rollnos = StudentS_S.objects.values_list('rollno', flat=True).distinct()
            os_rollnos = StudentOS.objects.values_list('rollno', flat=True).distinct()
            co_rollnos = StudentCO.objects.values_list('rollno', flat=True).distinct()
            dbms_rollnos = StudentDBMS.objects.values_list('rollno', flat=True).distinct()

            all_rollnos = set(etc_rollnos) | set(fa_rollnos) | set(m3_rollnos) | set(ss_rollnos) | set(os_rollnos) | set(co_rollnos) | set(dbms_rollnos)

            total_marks_dict = {}


            for dbms_rollno in dbms_rollnos:               
                total_marks_dict.setdefault(dbms_rollno, {}).setdefault('s1_total', 0)
                total_marks_dict[dbms_rollno].setdefault('s2_total', 0)
                total_marks_dict[dbms_rollno].setdefault('avg_s_total', 0)
                total_marks_dict[dbms_rollno].setdefault('i1_total', 0)
                total_marks_dict[dbms_rollno].setdefault('i2_total', 0)
                total_marks_dict[dbms_rollno].setdefault('avg_i_total', 0)

                dbms_student = StudentDBMS.objects.filter(rollno=dbms_rollno).first()
               
                dbms_student_name= StudentDBMS.objects.filter(rollno=dbms_rollno).first().student_name
               
                if dbms_student:
                    
                    total_marks_dict[dbms_rollno]['s1_total'] += dbms_student.s1_marks
                    total_marks_dict[dbms_rollno]['s2_total'] += dbms_student.s2_marks
                    total_marks_dict[dbms_rollno]['avg_s_total'] += dbms_student.avg_s_marks
                    total_marks_dict[dbms_rollno]['i1_total'] += dbms_student.i1_marks
                    total_marks_dict[dbms_rollno]['i2_total'] += dbms_student.i2_marks
                    total_marks_dict[dbms_rollno]['avg_i_total'] += dbms_student.avg_i_marks


            for co_rollno in co_rollnos:               
                total_marks_dict.setdefault(co_rollno, {}).setdefault('s1_total', 0)
                total_marks_dict[co_rollno].setdefault('s2_total', 0)
                total_marks_dict[co_rollno].setdefault('avg_s_total', 0)
                total_marks_dict[co_rollno].setdefault('i1_total', 0)
                total_marks_dict[co_rollno].setdefault('i2_total', 0)
                total_marks_dict[co_rollno].setdefault('avg_i_total', 0)

                co_student = StudentCO.objects.filter(rollno=co_rollno).first()
               
                co_student_name= StudentCO.objects.filter(rollno=co_rollno).first().student_name
               
                if co_student:
                    
                    total_marks_dict[co_rollno]['s1_total'] += co_student.s1_marks
                    total_marks_dict[co_rollno]['s2_total'] += co_student.s2_marks
                    total_marks_dict[co_rollno]['avg_s_total'] += co_student.avg_s_marks
                    total_marks_dict[co_rollno]['i1_total'] += co_student.i1_marks
                    total_marks_dict[co_rollno]['i2_total'] += co_student.i2_marks
                    total_marks_dict[co_rollno]['avg_i_total'] += co_student.avg_i_marks
           

            for os_rollno in os_rollnos:               
                total_marks_dict.setdefault(os_rollno, {}).setdefault('s1_total', 0)
                total_marks_dict[os_rollno].setdefault('s2_total', 0)
                total_marks_dict[os_rollno].setdefault('avg_s_total', 0)
                total_marks_dict[os_rollno].setdefault('i1_total', 0)
                total_marks_dict[os_rollno].setdefault('i2_total', 0)
                total_marks_dict[os_rollno].setdefault('avg_i_total', 0)

                os_student = StudentOS.objects.filter(rollno=os_rollno).first()
               
                os_student_name= StudentOS.objects.filter(rollno=os_rollno).first().student_name
               
                if os_student:
                    
                    total_marks_dict[os_rollno]['s1_total'] += os_student.s1_marks
                    total_marks_dict[os_rollno]['s2_total'] += os_student.s2_marks
                    total_marks_dict[os_rollno]['avg_s_total'] += os_student.avg_s_marks
                    total_marks_dict[os_rollno]['i1_total'] += os_student.i1_marks
                    total_marks_dict[os_rollno]['i2_total'] += os_student.i2_marks
                    total_marks_dict[os_rollno]['avg_i_total'] += os_student.avg_i_marks

                 

            for ss_rollno in ss_rollnos:
                total_marks_dict.setdefault(ss_rollno, {}).setdefault('s1_total', 0)
                total_marks_dict[ss_rollno].setdefault('s2_total', 0)
                total_marks_dict[ss_rollno].setdefault('avg_s_total', 0)
                total_marks_dict[ss_rollno].setdefault('i1_total', 0)
                total_marks_dict[ss_rollno].setdefault('i2_total', 0)
                total_marks_dict[ss_rollno].setdefault('avg_i_total', 0)

                ss_student = StudentS_S.objects.filter(rollno=ss_rollno).first()
                ss_student_name = StudentS_S.objects.filter(rollno=ss_rollno).first().student_name
                if ss_student:
                    total_marks_dict[ss_rollno]['name'] = ss_student_name
                    total_marks_dict[ss_rollno]['s1_total'] += ss_student.s1_marks
                    total_marks_dict[ss_rollno]['s2_total'] += ss_student.s2_marks
                    total_marks_dict[ss_rollno]['avg_s_total'] += ss_student.avg_s_marks
                    total_marks_dict[ss_rollno]['i1_total'] += ss_student.i1_marks
                    total_marks_dict[ss_rollno]['i2_total'] += ss_student.i2_marks
                    total_marks_dict[ss_rollno]['avg_i_total'] += ss_student.avg_i_marks

            for etc_rollno in etc_rollnos:
                total_marks_dict.setdefault(etc_rollno, {}).setdefault('s1_total', 0)
                total_marks_dict[etc_rollno].setdefault('s2_total', 0)
                total_marks_dict[etc_rollno].setdefault('avg_s_total', 0)
                total_marks_dict[etc_rollno].setdefault('i1_total', 0)
                total_marks_dict[etc_rollno].setdefault('i2_total', 0)
                total_marks_dict[etc_rollno].setdefault('avg_i_total', 0)

                etc_student = StudentETC.objects.filter(rollno=etc_rollno).first()
                if etc_student:
                    total_marks_dict[etc_rollno]['name'] = ss_student_name
                    total_marks_dict[etc_rollno]['s1_total'] += etc_student.s1_marks
                    total_marks_dict[etc_rollno]['s2_total'] += etc_student.s2_marks
                    total_marks_dict[etc_rollno]['avg_s_total'] += etc_student.avg_s_marks
                    total_marks_dict[etc_rollno]['i1_total'] += etc_student.i1_marks
                    total_marks_dict[etc_rollno]['i2_total'] += etc_student.i2_marks
                    total_marks_dict[etc_rollno]['avg_i_total'] += etc_student.avg_i_marks

            for fa_rollno in fa_rollnos:
                total_marks_dict.setdefault(fa_rollno, {}).setdefault('s1_total', 0)
                total_marks_dict[fa_rollno].setdefault('s2_total', 0)
                total_marks_dict[fa_rollno].setdefault('avg_s_total', 0)
                total_marks_dict[fa_rollno].setdefault('i1_total', 0)
                total_marks_dict[fa_rollno].setdefault('i2_total', 0)
                total_marks_dict[fa_rollno].setdefault('avg_i_total', 0)

                fa_student = StudentFA.objects.filter(rollno=fa_rollno).first()
                if fa_student:
                    total_marks_dict[fa_rollno]['name'] = ss_student_name
                    total_marks_dict[fa_rollno]['s1_total'] += fa_student.s1_marks
                    total_marks_dict[fa_rollno]['s2_total'] += fa_student.s2_marks
                    total_marks_dict[fa_rollno]['avg_s_total'] += fa_student.avg_s_marks
                    total_marks_dict[fa_rollno]['i1_total'] += fa_student.i1_marks
                    total_marks_dict[fa_rollno]['i2_total'] += fa_student.i2_marks
                    total_marks_dict[fa_rollno]['avg_i_total'] += fa_student.avg_i_marks


            for m3_rollno in m3_rollnos:
                total_marks_dict.setdefault(m3_rollno, {}).setdefault('s1_total', 0)
                total_marks_dict[m3_rollno].setdefault('s2_total', 0)
                total_marks_dict[m3_rollno].setdefault('avg_s_total', 0)
                total_marks_dict[m3_rollno].setdefault('i1_total', 0)
                total_marks_dict[m3_rollno].setdefault('i2_total', 0)
                total_marks_dict[m3_rollno].setdefault('avg_i_total', 0)

                m3_student = StudentM3.objects.filter(rollno=m3_rollno).first()
                if m3_student:
                    
                    total_marks_dict[m3_rollno]['s1_total'] += m3_student.s1_marks
                    total_marks_dict[m3_rollno]['s2_total'] += m3_student.s2_marks
                    total_marks_dict[m3_rollno]['avg_s_total'] += m3_student.avg_s_marks
                    total_marks_dict[m3_rollno]['i1_total'] += m3_student.i1_marks
                    total_marks_dict[m3_rollno]['i2_total'] += m3_student.i2_marks
                    total_marks_dict[m3_rollno]['avg_i_total'] += m3_student.avg_i_marks
                    total_marks_dict[m3_rollno]['name'] = m3_student.student_name 

           
            return render(request, 'report/totalmarks.html',{'queryset':queryset,'total_marks_dict':total_marks_dict,'action':action,'access':access,'sub':sub})

            
@login_required
def update_marks(request, student_id, action, access):
    if action == 'etc' and access == 'Teacher':
        queryset = StudentETC.objects.filter(rollno__icontains=student_id)
        student = StudentETC.objects.filter(rollno__icontains=student_id).first()

        if request.method == "POST" and student:
            s1 = request.POST.get('s1')
            s2 = request.POST.get('s2')
            i1 = request.POST.get('i1')
            i2 = request.POST.get('i2')

            if s1:
                if float(s1) <= 10:
                    student.s1_marks = s1
                    student.avg_s_marks = (float(s1) + student.s2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/etc/Teacher/?message=Marks+updated+successfully')


            if s2:
                if float(s2) <= 10:
                    student.s2_marks = s2
                    student.avg_s_marks = (float(s2) + student.s1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/etc/Teacher/?message=Marks+updated+successfully')

            if i1:
                if float(i1) <= 20:
                    student.i1_marks = i1
                    student.avg_i_marks = (float(i1) + student.i2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/etc/Teacher/?message=Marks+updated+successfully')

            if i2:
                if float(i2) <= 20:
                    student.i2_marks = i2
                    student.avg_i_marks = (float(i2) + student.i1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/etc/Teacher/?message=Marks+updated+successfully')

            if s1 and s2:
                student.avg_s_marks = (float(s1) + float(s2)) / 2

            if i1 and i2:
                student.avg_i_marks = (float(i1) + float(i2)) / 2

            student.total = student.avg_s_marks + student.avg_i_marks
            student.save()

            # Check if any marks are entered before redirecting
            if s1 or s2 or i1 or i2:
                messages.info(request, 'Marks updated successfully')
                return HttpResponseRedirect('/students/etc/Teacher/?message=Marks+updated+successfully')
            else:
                return HttpResponseRedirect('/students/etc/Teacher')

        return render(request, 'report/update_marks.html', {'queryset': queryset,'action':action,'access':access})

    if action == 'co' and access == 'Teacher':
        queryset = StudentCO.objects.filter(rollno__icontains=student_id)
        student = StudentCO.objects.filter(rollno__icontains=student_id).first()
        
        if request.method == "POST" and student:
            s1 = request.POST.get('s1')
            s2 = request.POST.get('s2')
            i1 = request.POST.get('i1')
            i2 = request.POST.get('i2')

            if s1:
                if float(s1) <= 10:
                    student.s1_marks = s1
                    student.avg_s_marks = (float(s1) + student.s2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/co/Teacher/?message=Marks+updated+successfully')


            if s2:
                if float(s2) <= 10:
                    student.s2_marks = s2
                    student.avg_s_marks = (float(s2) + student.s1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/co/Teacher/?message=Marks+updated+successfully')

            if i1:
                if float(i1) <= 20:
                    student.i1_marks = i1
                    student.avg_i_marks = (float(i1) + student.i2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/co/Teacher/?message=Marks+updated+successfully')

            if i2:
                if float(i2) <= 20:
                    student.i2_marks = i2
                    student.avg_i_marks = (float(i2) + student.i1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/co/Teacher/?message=Marks+updated+successfully')

            if s1 and s2:
                student.avg_s_marks = (float(s1) + float(s2)) / 2

            if i1 and i2:
                student.avg_i_marks = (float(i1) + float(i2)) / 2

            student.total = student.avg_s_marks + student.avg_i_marks
            student.save()

                # Check if any marks are entered before redirecting
            if s1 or s2 or i1 or i2:
                messages.info(request, 'Marks updated successfully')
                return HttpResponseRedirect('/students/co/Teacher/?message=Marks+updated+successfully')
            else:
                return HttpResponseRedirect('/students/co/Teacher')

        return render(request, 'report/update_marks.html', {'queryset': queryset,'action':action,'access':access})

    if action == 'dbms' and access == 'Teacher':
        queryset = StudentDBMS.objects.filter(rollno__icontains=student_id)
        student = StudentDBMS.objects.filter(rollno__icontains=student_id).first()
        
        if request.method == "POST" and student:
            s1 = request.POST.get('s1')
            s2 = request.POST.get('s2')
            i1 = request.POST.get('i1')
            i2 = request.POST.get('i2')

            if s1:
                if float(s1) <= 10:
                    student.s1_marks = s1
                    student.avg_s_marks = (float(s1) + student.s2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/dbms/Teacher/?message=Marks+updated+successfully')


            if s2:
                if float(s2) <= 10:
                    student.s2_marks = s2
                    student.avg_s_marks = (float(s2) + student.s1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/dbms/Teacher/?message=Marks+updated+successfully')

            if i1:
                if float(i1) <= 20:
                    student.i1_marks = i1
                    student.avg_i_marks = (float(i1) + student.i2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/dbms/Teacher/?message=Marks+updated+successfully')

            if i2:
                if float(i2) <= 20:
                    student.i2_marks = i2
                    student.avg_i_marks = (float(i2) + student.i1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/dbms/Teacher/?message=Marks+updated+successfully')

            if s1 and s2:
                student.avg_s_marks = (float(s1) + float(s2)) / 2

            if i1 and i2:
                student.avg_i_marks = (float(i1) + float(i2)) / 2

            student.total = student.avg_s_marks + student.avg_i_marks
            student.save()

                # Check if any marks are entered before redirecting
            if s1 or s2 or i1 or i2:
                messages.info(request, 'Marks updated successfully')
                return HttpResponseRedirect('/students/dbms/Teacher/?message=Marks+updated+successfully')
            else:
                return HttpResponseRedirect('/students/dbms/Teacher')

        return render(request, 'report/update_marks.html', {'queryset': queryset,'action':action,'access':access})

    if action == 'os' and access == 'Teacher':
        queryset = StudentOS.objects.filter(rollno__icontains=student_id)
        student = StudentOS.objects.filter(rollno__icontains=student_id).first()
        
        if request.method == "POST" and student:
            s1 = request.POST.get('s1')
            s2 = request.POST.get('s2')
            i1 = request.POST.get('i1')
            i2 = request.POST.get('i2')

            if s1:
                if float(s1) <= 10:
                    student.s1_marks = s1
                    student.avg_s_marks = (float(s1) + student.s2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/os/Teacher/?message=Marks+updated+successfully')


            if s2:
                if float(s2) <= 10:
                    student.s2_marks = s2
                    student.avg_s_marks = (float(s2) + student.s1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/os/Teacher/?message=Marks+updated+successfully')

            if i1:
                if float(i1) <= 20:
                    student.i1_marks = i1
                    student.avg_i_marks = (float(i1) + student.i2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/os/Teacher/?message=Marks+updated+successfully')

            if i2:
                if float(i2) <= 20:
                    student.i2_marks = i2
                    student.avg_i_marks = (float(i2) + student.i1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/os/Teacher/?message=Marks+updated+successfully')

            if s1 and s2:
                student.avg_s_marks = (float(s1) + float(s2)) / 2

            if i1 and i2:
                student.avg_i_marks = (float(i1) + float(i2)) / 2

            student.total = student.avg_s_marks + student.avg_i_marks
            student.save()

                # Check if any marks are entered before redirecting
            if s1 or s2 or i1 or i2:
                messages.info(request, 'Marks updated successfully')
                return HttpResponseRedirect('/students/os/Teacher/?message=Marks+updated+successfully')
            else:
                return HttpResponseRedirect('/students/os/Teacher')

        return render(request, 'report/update_marks.html', {'queryset': queryset,'action':action,'access':access})
    
    if action == 'ss' and access == 'Teacher':
        queryset = StudentS_S.objects.filter(rollno__icontains=student_id)
        student = StudentS_S.objects.filter(rollno__icontains=student_id).first()

        if request.method == "POST" and student:
            s1 = request.POST.get('s1')
            s2 = request.POST.get('s2')
            i1 = request.POST.get('i1')
            i2 = request.POST.get('i2')

            if s1:
                if float(s1) <= 10:
                    student.s1_marks = s1
                    student.avg_s_marks = (float(s1) + student.s2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/ss/Teacher/?message=Marks+updated+successfully')


            if s2:
                if float(s2) <= 10:
                    student.s2_marks = s2
                    student.avg_s_marks = (float(s2) + student.s1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/ss/Teacher/?message=Marks+updated+successfully')

            if i1:
                if float(i1) <= 20:
                    student.i1_marks = i1
                    student.avg_i_marks = (float(i1) + student.i2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/ss/Teacher/?message=Marks+updated+successfully')

            if i2:
                if float(i2) <= 20:
                    student.i2_marks = i2
                    student.avg_i_marks = (float(i2) + student.i1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/ss/Teacher/?message=Marks+updated+successfully')

            if s1 and s2:
                student.avg_s_marks = (float(s1) + float(s2)) / 2

            if i1 and i2:
                student.avg_i_marks = (float(i1) + float(i2)) / 2

            student.total = student.avg_s_marks + student.avg_i_marks
            student.save()

            # Check if any marks are entered before redirecting
            if s1 or s2 or i1 or i2:
                messages.info(request, 'Marks updated successfully')
                return HttpResponseRedirect('/students/ss/Teacher/?message=Marks+updated+successfully')
            else:
                return HttpResponseRedirect('/students/ss/Teacher')

        return render(request, 'report/update_marks.html', {'queryset': queryset,'action':action,'access':access})

    if action == 'fa' and access == 'Teacher':
        queryset = StudentFA.objects.filter(rollno__icontains=student_id)
        student = StudentFA.objects.filter(rollno__icontains=student_id).first()

        if request.method == "POST" and student:
            s1 = request.POST.get('s1')
            s2 = request.POST.get('s2')
            i1 = request.POST.get('i1')
            i2 = request.POST.get('i2')

            if s1:
                if float(s1) <= 10:
                    student.s1_marks = s1
                    student.avg_s_marks = (float(s1) + student.s2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/fa/Teacher/?message=Marks+updated+successfully')


            if s2:
                if float(s2) <= 10:
                    student.s2_marks = s2
                    student.avg_s_marks = (float(s2) + student.s1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/fa/Teacher/?message=Marks+updated+successfully')

            if i1:
                if float(i1) <= 20:
                    student.i1_marks = i1
                    student.avg_i_marks = (float(i1) + student.i2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/fa/Teacher/?message=Marks+updated+successfully')

            if i2:
                if float(i2) <= 20:
                    student.i2_marks = i2
                    student.avg_i_marks = (float(i2) + student.i1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/fa/Teacher/?message=Marks+updated+successfully')

            if s1 and s2:
                student.avg_s_marks = (float(s1) + float(s2)) / 2

            if i1 and i2:
                student.avg_i_marks = (float(i1) + float(i2)) / 2

            student.total = student.avg_s_marks + student.avg_i_marks
            student.save()

            # Check if any marks are entered before redirecting
            if s1 or s2 or i1 or i2:
                messages.info(request, 'Marks updated successfully')
                return HttpResponseRedirect('/students/fa/Teacher/?message=Marks+updated+successfully')
            else:
                return HttpResponseRedirect('/students/fa/Teacher')

        return render(request, 'report/update_marks.html', {'queryset': queryset,'action':action,'access':access})

    if action == 'm3' and access=='Teacher':
        queryset = StudentM3.objects.filter(rollno__icontains=student_id)
        student = StudentM3.objects.filter(rollno__icontains=student_id).first()

        if request.method == "POST" and student:
            s1 = request.POST.get('s1')
            s2 = request.POST.get('s2')
            i1 = request.POST.get('i1')
            i2 = request.POST.get('i2')

            if s1:
                if float(s1) <= 10:
                    student.s1_marks = s1
                    student.avg_s_marks = (float(s1) + student.s2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/m3/Teacher/?message=Marks+updated+successfully')


            if s2:
                if float(s2) <= 10:
                    student.s2_marks = s2
                    student.avg_s_marks = (float(s2) + student.s1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/m3/Teacher/?message=Marks+updated+successfully')

            if i1:
                if float(i1) <= 20:
                    student.i1_marks = i1
                    student.avg_i_marks = (float(i1) + student.i2_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/m3/Teacher/?message=Marks+updated+successfully')

            if i2:
                if float(i2) <= 20:
                    student.i2_marks = i2
                    student.avg_i_marks = (float(i2) + student.i1_marks) / 2
                else:
                    messages.info(request, 'Marks not updated ')
                    return HttpResponseRedirect('/students/m3/Teacher/?message=Marks+updated+successfully')

            if s1 and s2:
                student.avg_s_marks = (float(s1) + float(s2)) / 2

            if i1 and i2:
                student.avg_i_marks = (float(i1) + float(i2)) / 2

            student.total = student.avg_s_marks + student.avg_i_marks
            student.save()

            # Check if any marks are entered before redirecting
            if s1 or s2 or i1 or i2:
                messages.info(request, 'Marks updated successfully')
                return HttpResponseRedirect('/students/m3/Teacher/?message=Marks+updated+successfully')
            else:
                return HttpResponseRedirect('/students/m3/Teacher')

        return render(request, 'report/update_marks.html', {'queryset': queryset,'action':action,'access':access})


    ######
    
