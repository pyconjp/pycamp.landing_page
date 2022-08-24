# pycamp.landing_page

## 開発環境構築

```shell
$ git clone git@github.com:pyconjp/pycamp.landing_page.git
$ cd pycamp.landing_page

$ python3.10 -m venv venv --upgrade-deps
$ source venv/bin/activate
(venv) $ pip install -r requirements.in

(venv) $ make singlehtml
```

### メモ：プロジェクト作成（手元では実行不要）

```shell
(venv) $ sphinx-quickstart \
    --sep \
    -p 'pycamp landing page' \
    -a 'PyCon JP Committee' \
    -l ja \
    -r '' \
    --ext-githubpages
```

## 「過去の開催回で集まった人数」の追加方法

[participants_count.csv](https://github.com/pyconjp/pycamp.landing_page/blob/main/source/sections/participants_count.csv)に行を追加してください。

以下の3つの項目が必須です

- 開催地
- （connpassの）URL
- 参加人数

上記CSVファイルを**GitHub上で編集**してかまいません。  
mainブランチに直接push（またはプルリクエストをマージ）で、GitHub Actionsでビルドされます。  
（思ったようにいかなければ戻せばいいと思います）
