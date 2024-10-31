from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone


from .forms import MemberForm
from .models import Member
# Create your views here.

def index(request):
    member_list = Member.objects.order_by('-create_date')
    context = {'member_list' : member_list}
    return render(request,'board/member_list.html', context)

def detail(request, member_id):
    #member = Member.objects.get(id=member_id)
    member = get_object_or_404(Member,pk=member_id)
    context = { 'member': member}
    return render(request,'board/member_detail.html', context)

def input(request):
    return render(request,'board/member_input.html')

def create(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    profile = request.POST.get('profile')
    new_member = Member(name=name, email=email, profile=profile,create_date=timezone.now())
    new_member.save()
    return redirect('board:detail',member_id=new_member.id)

def delete(request,member_id):
    member = get_object_or_404(Member, pk=member_id)
    member.delete()
    return redirect('board:index')

def editform(request,member_id):
    member = get_object_or_404(Member, pk=member_id)
    context = {'member': member}
    return render(request, 'board/member_edit.html', context)

def edit(request):
    id = request.POST.get('id')
    name = request.POST.get('name')
    email = request.POST.get('email')
    profile = request.POST.get('profile')
    member = get_object_or_404(Member, pk=id)
    member.name = name
    member.email = email
    member.profile = profile
    member.save()

    return redirect('board:index')

def member_create(request):
    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            member = form.save(commit=False)
            member.create_date=timezone.now()
            member.save()
            return redirect('board:index')
    else :
        form = MemberForm()

    return render(request, 'board/member_form.html', {'form': form})