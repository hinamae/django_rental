# README

adminのはmaeyamaといつものパスワード

## 環境

- Django 3.0.8.
- Python 3.8.3 

```
conda activate py36
```

127.0.0.1:8000/loginでアクセス


## memo 

### 実装するもの

- 貸し出し本の予約・取り消しをする(Cretae・ Delete)
- 予約図書一覧を出力する(Read)
- 取り置き期限を確認する(Read)
- 貸し出し図書の返却を登録する(Update)
- 取り置き図書を貸し出しに出す(Update)


### 実装したこと
- adminで図書を登録・編集・削除する(Create・Update・Delete)
- 図書一覧を表示する(Read)
- 図書の詳細を表示する(Read)

- 一般ユーザを作成する(Create)
- adminユーザで一般ユーザの更新をする(Update・Delete)
- 一般ユーザ・adminユーザでログインする

### ネック？
- 著者テーブルが必要では？(ヘルマン・ヘッセとヘッセが存在してしまNいそう)
- 会員をクリックして、借りている図書一覧を表示させる
- ジャンルやタイトルなどでの絞り込み


## 設計

### DB用データ(model)

- 貸し出し図書のインスタンス(equ_model)
    - title
    - author
    - memo
    - isbn
    - status

- 


##



## エラー
- エラー：Using the URLconf defined in rentalproject.urls, Django tried these URL patterns, in this order:
- 解決：http://127.0.0.1:8000/{表示のあるパス}でアクセスする