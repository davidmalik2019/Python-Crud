from django.shortcuts import render
from .models import Teacher
from django.contrib import messages
from django.db.models import Q


def indextech(request):
    teachers = Teacher.objects.all()
    search_query = ""
    if request.method == "POST": 
        if "create" in request.POST:
            tname = request.POST.get("tname")
            taddress = request.POST.get("taddress")
            subject = request.POST.get("subject")
            classrom = request.POST.get("classrom")
            Teacher.objects.create(
                tname=tname,
                taddress=taddress,
                subject=subject,
                classrom=classrom,
            )
            messages.success(request, "Teacher added successfully")
    
        elif "update" in request.POST:
            id = request.POST.get("id")
            tname = request.POST.get("tname")
            taddress = request.POST.get("taddress")
            subject = request.POST.get("subject")
            classrom = request.POST.get("classrom")
            
            teacher = Teacher.objects.get(id=id)
            teacher.tname = tname
            teacher.taddress = taddress
            teacher.subject = subject
            teacher.classrom = classrom
            teacher.save()
            messages.success(request, "teacher updated successfully")
    
        elif "delete" in request.POST:
            id = request.POST.get("id")
            Teacher.objects.get(id=id).delete()
            messages.success(request, "teacher deleted successfully")
        
        elif "search" in request.POST:
            search_query = request.POST.get("query")
            teachers = Teacher.objects.filter(Q(tname__icontains=search_query) | Q(taddress__icontains=search_query)|Q(subject__icontains=search_query)|Q(classrom__icontains=search_query))

    context = {"teachers": teachers, "search_query": search_query}
    return render(request, "indextech.html", context=context)
