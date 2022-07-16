from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.

# register model


def user_register(request):
    message = ''
    form = UserCreationForm()
    if request.method == "POST":
        print(request.POST)
        username = request.POST.get('username')  # 取得前端的name
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # 密碼問題
        if password1 != password2:
            message = '兩次密碼輸入不同'
        # 密碼過短
        elif len(password1) < 8:
            message = '密碼過短(至少8個字元)'
        else:
            # 帳號重複
            if User.objects.filter(username=username).exists():
                message = 'user重複'
            else:
                user = User.objects.create_user(username=username,
                                                password=password1)
                if user is not None:
                    user.save()
                    print('註冊成功！！')

    return render(request, './user/register.html', locals())


def user_profile(request):
    return render(request, './user/profile.html')
