from django.urls import path
from .views import Equ_List, Equ_Detail

urlpatterns = [
    #todoリストを表示させる画面用のurl
    #クラスで呼び出しするので.as_view()メソッドを使用する。(メソッドorクラスで呼び出す。)
    path('list/', Equ_List.as_view(), name='list'),
    path('detail/<int:pk>', Equ_Detail.as_view(), name='detail'),
]