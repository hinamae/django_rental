from django.urls import path
from .views import Equ_List, Equ_Detail, Mypage, Equ_How_to_lend,loginfunc, signupfunc, change_book_status_func

urlpatterns = [
    #todoリストを表示させる画面用のurl
    #クラスで呼び出しするので.as_view()メソッドを使用する。(メソッドorクラスで呼び出す。)
    path('list/', Equ_List.as_view(), name='list'),
    path('detail/<int:pk>', Equ_Detail.as_view(), name='detail'),
    path('mypage/<str:username>', Mypage.as_view(), name='mypage'),
    path('how_to_lend/', Equ_How_to_lend.as_view(), name='how_to_lend'),
    path('login/', loginfunc, name='login'),
    path('signup/', signupfunc, name='signup'),
    path('status/<int:pk>' , change_book_status_func, name='status')
]