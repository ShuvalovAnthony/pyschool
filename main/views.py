from django.contrib import messages
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView
from .models import Lesson, Category, Profile
from .forms import UserLoginForm, UserForm, ProfileForm, ContactForm, OrderForm
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.views.generic.edit import FormMixin


class Home(ListView):
    model = Category
    template_name = 'main/courses/courses_list.html'
    context_object_name = 'courses'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Курсы'
        return context


class GetSelfCourses(ListView):
    model = Category
    template_name = 'main/courses/my_courses.html'
    context_object_name = 'courses'
    paginate_by = 9

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Мои курсы'
        return context


class GetLesson(DetailView):
    model = Lesson
    template_name = 'main/single_lesson.html'
    context_object_name = 'lesson'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.all()
        return context


class GetCourse(FormMixin, DetailView):
    model = Category
    form_class = OrderForm

    template_name = 'main/courses/single_course.html'
    context_object_name = 'single_course'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['lessons'] = Lesson.objects.filter(category__slug=self.kwargs['slug'])
        return context

    def get_success_url(self):
        return redirect('courses')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            sbjct = form.cleaned_data['name'] + ' --- ' + form.cleaned_data['email'] + ' --- ' + form.cleaned_data['phone']
            cntnt = 'Название курса: ' + str(self.object)
            mail = send_mail(
                sbjct,
                cntnt,
                'pyschool@mail.ru',
                ['anthony.shuvalov@mail.ru'],
                fail_silently=True,
                )
            if mail:
                messages.success(request, 'Заявка успешно отправлена')
                return redirect('courses')
            else:
                messages.error(request, 'Ошибка отправки заявкия')
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)



def index(request):
    return render(request, 'main/index.html', {'courses': Category.objects.all()} )


def tutors(request):
    return render(request, 'main/tutors.html')


def pricing(request):
    return render(request, 'main/pricing.html')


def lk(request):
    return render(request, 'main/lk.html')


def lesson_redirect(request):
    print(request)
    pass


def contact(request):
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            sbjct = contact_form.cleaned_data['subject'] + ' from: ' + contact_form.cleaned_data['email']
            cntnt = contact_form.cleaned_data['name'] + ' отправил: ' + contact_form.cleaned_data['content']
            mail = send_mail(
                sbjct,
                cntnt,
                'pyschool@mail.ru',
                ['anthony.shuvalov@mail.ru'],
                fail_silently=True,
                )
            if mail:
                messages.success(request, 'Сообщение успешно отправлено')
                return redirect('contact')
            else:
                messages.error(request, 'Ошибка отправки сообщения')
        else:
            messages.error(request, 'Ошибка отправки сообщения')
    else:
        contact_form = ContactForm()
    return render(request, 'main/contact.html', {'contact_form': contact_form},)


@transaction.atomic
def register(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Вы успешно зарегистрировались')
            return redirect('login')
        else:
            messages.error(request, 'Ошибка регистрации')
    else:
        user_form = UserForm()
    return render(request, 'main/register.html', {'user_form': user_form})


def profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('home')
    else:
        profile_form = ProfileForm()
    return render(request, 'main/profile.html', {'profile_form': profile_form})


def user_login(request):
    if request.method == "POST":
        user_form = UserLoginForm(data=request.POST)
        if user_form.is_valid():
            user_form = user_form.get_user()
            login(request, user_form)
            return redirect('home')
    else:
        user_form = UserLoginForm()
    return render(request, 'main/login.html', {"user_form": user_form})


def user_logout(request):
    logout(request)
    return redirect('login')


@csrf_exempt
def lesson_complete(request):
    if request.POST:
        user_profile_id = request.POST.get('user_profile_id')
        course_slug = request.POST.get('course_slug')
        last_lesson = request.POST.get('last_lesson')
        user_profile = Profile.objects.get(pk=user_profile_id)
        if course_slug == 'python':
            user_profile.last_lesson_python = last_lesson
        elif course_slug == 'ege-po-informatike':
            user_profile.last_lesson_ege = last_lesson
        elif course_slug == 'sozdanie-telegram-botov':
            user_profile.last_lesson_bots = last_lesson
        else:
            pass
        user_profile.save()
        return HttpResponse('complete', content_type='text/html')
    else:
        return HttpResponse('Error', content_type='text/html')


'''
class LessonsByCourse(ListView):
    template_name = 'main/courses/lessons_list.html'
    context_object_name = 'lessons'
    paginate_by = 9
    allow_empty = True

    def get_queryset(self):
        return Lesson.objects.filter(category__slug=self.kwargs['slug'], slug=self.kwargs['lesson_slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = Category.objects.get(slug=self.kwargs['slug'])
        return context
'''
