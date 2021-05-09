from django.shortcuts import render, get_object_or_404
from .models import Equ_Model


#ListView(CRUDのRにあたる)をインポート
from django.views.generic import ListView
#ListView(CRUDのRにあたる)をインポート
from django.views.generic import DetailView
#loginfucn
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
#signup func
from django.contrib.auth.models import User





class Equ_List(ListView):
    template_name='list.html'
    model = Equ_Model

class Equ_Detail(DetailView):
    template_name='detail.html'
    model = Equ_Model

class Mypage(DetailView):
    template_name='mypage.html'
    queryset = User.objects.all()
    def get_object(self):
        UserName = self.kwargs.get("username")
        return get_object_or_404(User, username=UserName)


class Equ_How_to_lend(ListView):
    template_name='how_to_lend.html'
    model = Equ_Model


def loginfunc(request):
    if request.method== 'POST':
        username2 = request.POST['username']
        password2 = request.POST['password']
        user = authenticate(request,username = username2 , password = password2)
        if user is not None:
            login(request, user)
            return redirect('list')
        else:
            return redirect('login')
    else:
        return render(request,'login.html')

def signupfunc(request):
    #プロンプトに表示する(確認用)
    user2 = User.objects.all()
    print(user2)
    user3 = User.objects.get(username='maeyama')
    print(user3.email)

    if request.method== 'POST':
        # POSTでもってきた、'username'(htmlファイルのタグの中のnameの部分)をusername2変数に格納
        username2 = request.POST['username']
        password = request.POST['password']
        try:
            #すでにusername2の名前で登録がなされている時
            User.objects.get(username=username2)
            return render(request, 'signup.html', {'error','このユーザは登録されています'})
        except:
            # create_user関数を使用して、Userオブジェクトを作成する。公式ドキュメントより
            user = User.objects.create_user(username2, '', password)
            return redirect('login')

    return render(request,'signup.html')

def change_book_status_func(request, pk):
    post = Equ_Model.objects.get(pk=pk)
    if post.status == 0:
        post.status = post.status + 1
        post.save()
        return render(request, 'thanks_to_lend.html', {"object":post})
    else:
        return render(request, 'sorry_already_lent.html', {"object":post})


