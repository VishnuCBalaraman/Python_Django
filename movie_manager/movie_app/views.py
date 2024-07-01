from django.shortcuts import render
from . models import MovieInfo
from . forms import MovieForm

# Create your views here.

def create(request):
#    if request.POST:
#        title = request.POST.get('title')
#        year = request.POST.get('year')
#        summary = request.POST.get('summary')
#        movie_obj = MovieInfo(title=title,year=year,summary=summary)
#        movie_obj.save()

    if request.POST:
        frm=MovieForm(request.POST)
        if frm.is_valid():
            frm.save()
    else:
        frm=MovieForm()

    return render(request,'create.html',{'frm':frm})


def list(request):
    movie_set = MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})


def edit(request,pk):
    instance_to_be_edited = MovieInfo.objects.get(pk=pk)
    if request.POST:
        frm = MovieForm(request.POST,instance=instance_to_be_edited)
        if frm.is_valid():
            instance_to_be_edited.save()
    else:
        frm = MovieForm(instance=instance_to_be_edited)

    return render(request,'create.html',{'frm':frm})


def delete(request,pk):
    instance_to_be_deleted = MovieInfo.objects.get(pk=pk)
    instance_to_be_deleted.delete()
    movie_set = MovieInfo.objects.all()
    return render(request,'list.html',{'movies':movie_set})