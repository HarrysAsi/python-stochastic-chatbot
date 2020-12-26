import csv
from django.http.response import HttpResponse
from django.shortcuts import render

from main import models

def index(request):
    """ Returns the index/landing page """
    return render(request, "main/index.html") 


def add_data(request):
    """ Returns the add-data view and also handles the question/tag addition"""
    if request.POST:
        # handles the data addition request
        if 'add-data' in request.POST:
            data = request.POST
            question = data.get("question", None)
            answer = data.get("answer", None)
            tags = data.getlist("tags", None)

            tag_qr = models.Tag.objects.filter(id__in=tags)
            qst = models.Question.objects.create(
                question = question,
                answer= answer
            )
            qst.tags.add(*tag_qr)
        # handles the tag addition request
        elif 'add-tag' in request.POST:
            data = request.POST
            tag_name = data.get("tag-name", None)
            tag_descr = data.get("tag-description", None)
            models.Tag.objects.create(
                name=tag_name,
                description=tag_descr
            )
        else:
            return HttpResponse("Something went wrong", 400)

    tags = models.Tag.objects.all()
    context = {
        "tags": tags
    }
    return render(request, "main/add-data.html", context=context) 


def collected_data(request):
    """ Returns all the collected data """
    questions = models.Question.objects.all()
    context = {
        "questions": questions,
    }
    return render(request, "main/collected-data.html", context) 


def export_data(request):
    """ View which returns the data"""
    response =  HttpResponse()
    writer = csv.writer(response)
    field_names = [field.name for field in models.Question._meta.fields]
    field_names.append("tags")
    writer.writerow(field_names)
    for qstn in models.Question.objects.all():
        writer.writerow([qstn.id, qstn.question, qstn.answer, qstn.created_date, qstn.modified_date, qstn.tags_as_str()])
    response["Content-Disposition"] = "attachment; filename=data.csv"
    return response