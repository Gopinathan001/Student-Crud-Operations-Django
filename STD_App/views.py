from django.shortcuts import redirect, render, get_object_or_404
from .models import Section, Student

# Create your views here.
def home(request):
    return render(request, "home.html")

# Section
def section(request):
    if request.method == 'POST':
        sec_name = request.POST['section_name']
        Section.objects.create(name = sec_name)
        print("Section is created")
        return redirect('All_section')
    return render(request, "section/section_in.html")

# Section views
def All_section(request):
    view_section = Section.objects.all()
    return render(request, "section/All_section.html", {'view_section' : view_section})

def view_section(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    list_student = section.students.all()
    return render(request, 'section/view_section.html', {'section': section, 'list_student' : list_student,'section_id': section_id})

# Edit Section
def edit_section(request, sec_id):
    edit_section = get_object_or_404(Section, id = sec_id)
    if request.method == 'POST':
        edit_section.name = request.POST.get('section_name')
        edit_section.save()
        print("Section is update")
        return redirect("All_section")
    return render(request, "section/Edit_section.html", {'edit_section' : edit_section})

# Delete Section
def delete_section(request, sec_id):
    del_section = get_object_or_404(Section, id = sec_id)
    if request.method == 'POST':
        del_section.delete()
        print("Section is Deleted")
        return redirect('All_section')
    return render(request, "section/delete_section.html", {'del_section' : del_section})



# Student-------------------------------------------------------------------------------------------------------------------------

# Create student details
def student_data(request, section_id):
    section = get_object_or_404(Section, pk=section_id)
    if request.method == 'POST':
        std_name = request.POST['Student_name']
        dob = request.POST['DOB']
        place = request.POST['place']
        section.students.create(name=std_name, birth_date=dob, place=place)
        print("datas saved")
        return redirect('view_section', section_id=section_id)
    return render(request, "student/Create_student.html", {'sec_for_std' : section})


# update_student 
def update_student(request, section_id, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.name = request.POST.get('Student_name')
        student.birth_date = request.POST.get('DOB')
        student.place = request.POST.get('place')
        student.save()
        return redirect('view_section', section_id=section_id)
    return render(request, 'student/Edit_student.html', {'student': student, 'section_id': section_id})

# delete_student 
def delete_student(request, section_id, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        print("Student data is Deleted")
        return redirect('view_section', section_id=section_id)
    return render(request, "student/delete_student.html", {'student' : student, 'section_id': section_id})
