from django.shortcuts import render
from django.views.generic import ListView,DetailView #CBV로 페이지 만들기
from .models import Student
from django.views.generic import ListView,DetailView #CBV로 페이지 만들기
from .models import Student

# Create your views here.
def reference(request):
    return render(
        request,
        'exam/reference.html'
    )
class St_List(ListView):
    model = Student
    template_name = 'exam/st_list.html'
class St_Detail(DetailView):
    model = Student
    template_name = 'exam/st_card.html'
# def st_list(request):
#     st_list = Student.objects.all()
#     return render(
#         request,
#         'exam/st_list.html',
#         {
#           'st_list' : st_list,
#         }
#     )
# def st_card(request, pk):
#         st_card = Student.objects.get(pk=pk)
#         return render(
#         request,
#         'exam/st_card.html',
#         {
#           'st_card' : st_card,
#         }
#         )