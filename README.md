# README

adminのはmaeyamaといつものパスワード

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



### ネック？
- 著者テーブルが必要では？(ヘルマン・ヘッセとヘッセが存在してしまいそう)
- 会員をクリックして、借りている図書一覧を表示させる
- ジャンルやタイトルなどでの絞り込み


## 設計

### データ(model)

貸し出し図書のインスタンス

- 図書(ISBN?)
- 借りた人
- 期限
- 貸し出し日時

