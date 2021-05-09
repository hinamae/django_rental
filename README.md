# README

adminのはmaey***といつものパスワード

## ？？
- Browserバック問題
    - detail画面から、貸し出しボタンを押して、貸出中のステータスにしたあと、ブラウザバックすると、Browserのキャッシュ保持機能によって、貸し出し可能ステータスの画面が表示されてしまう
    - Browserのキャッシュ機能を無効にする
    - バックボタンが押されても不整合が怒らないようにアプリケーションを設計する←こうしよう
    - 貸し出ししたら、貸し出しありがとうございます画面に遷移する。
    - ブラウザバックして、貸し出しボタンが押されたら、すでに貸し出されていることを伝える。    

## 環境

- Django 3.0.8.
- Python 3.8 !!!!!!

```
conda activate py36
```

```
python3.8 manage.py runserver
```


127.0.0.1:8000/loginでアクセス


```
python3.8 manage.py makemigrations

python3.8 manage.py migrate
```


## memo 

### 実装するもの

- 貸し出し本の予約・取り消しをする(Cretae・ Delete)
- 予約図書一覧を出力する(Read)
- 取り置き期限を確認する(Read)
- 貸し出し図書の返却を登録する(Update)
- 取り置き図書を貸し出しに出す(Update)
- 買い物かごに図書を貯める(Update)
- 買い物かごから図書を貸し出す(Update)




### 実装したこと
- adminで図書を登録・編集・削除する(Create・Update・Delete)
- 図書一覧を表示する(Read)
- 図書の詳細を表示する(Read)
- 図書の借り方を表示する(Read)
- 貸し出しボタンを設置(Update)
- マイページの作成(Read)
- 一般ユーザを作成する(Create)
- adminユーザで一般ユーザの更新をする(Update・Delete)
- 一般ユーザ・adminユーザでログインする

### ネック？
- 著者テーブルが必要では？(ヘルマン・ヘッセとヘッセが存在してしまNいそう)
- 会員をクリックして、借りている図書一覧を表示させる
- ジャンルやタイトルなどでの絞り込み


## 設計

### テーブル(model)

- 本のインスタンス(equ_model)
    - title
    - author
    - memo
    - isbn
    - status
        - 0:貸し出し可能
        - 1:貸出中



- ユーザ(デフォルト)


- 貸し出しインスタンス(Lending_Book)
    - user
        - ユーザテーブルを参照する外部キー(参照しているユーザレコードが削除された場合にLending_Bookテーブルのレコードを残す)
    - equ_model 
        - 本テーブルを参照する外部キー(参照しているユーザレコードが削除された場合にLending_Bookテーブルのレコードを削除する)
    - rental_date
        - 貸し出した日
    - due_date
        - 返却期限
    - return_date
        - 返した日






## エラー
- エラー：Using the URLconf defined in rentalproject.urls, Django tried these URL patterns, in this order:
- 解決：http://127.0.0.1:8000/{表示のあるパス}でアクセスする


## 参考

- headerのbootstrap
https://stackoverflow.com/questions/41513463/bootstrap-4-align-navbar-items-to-the-right

のanswerのやつ！