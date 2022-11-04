# pycamp.landing_page
![publish workflow](https://github.com/pyconjp/pycamp.landing_page/actions/workflows/publish.yml/badge.svg)

「Python Boot Campで全国にPythonの環を広げよう！」 https://pycamp-lp.pycon.jp/ のソースリポジトリです。  
GitHub Pages https://pyconjp.github.io/pycamp.landing_page/ をカスタムドメインで運用しています。

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
