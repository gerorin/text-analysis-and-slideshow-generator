# text-analysis-and-slideshow-generator
A Python script to automate the creation of word clouds from text data, followed by generating a 2x2 slideshow of the word clouds. Includes steps for text cleaning, merging, and morphological analysis using MeCab, with real-time logging for progress tracking.

了解しました！以下の内容をそのまま`README.md`にコピー＆ペーストして、必要に応じてユーザー名やメールアドレスを変更するだけで完成します。

```markdown
# text-analysis-and-slideshow-generator

A Python script to automate the creation of word clouds from text data, followed by generating a 2x2 slideshow of the word clouds. This project includes steps for text cleaning, merging, and morphological analysis using MeCab, with real-time logging for progress tracking.

## インストール手順

1. リポジトリをクローンします。
   ```bash
   git clone https://github.com/username/text-analysis-and-slideshow-generator.git
   ```

2. 必要なライブラリをインストールします。
   ```bash
   pip install -r requirements.txt
   ```

## 使い方

以下のコマンドでプロセスを実行します。
```bash
python src/main_process.py
```

## ファイル構成

```
├─ data
│   ├─ input
│   │   ├─ text_A
│   │   ├─ text_B
│   │   ├─ text_C
│   │   ├─ text_D
│   │   └─ word_filters
│   │           ├─ stopword.txt
│   │           └─ targetword.txt
│   └─ output
│       ├─ error_log
│       ├─ text_merge_A
│       ├─ text_merge_B
│       ├─ text_merge_C
│       ├─ text_merge_D
│       ├─ wordcloud_4x4
│       ├─ wordcloud_A
│       ├─ wordcloud_B
│       ├─ wordcloud_C
│       └─ wordcloud_D
└─ src
        ├─ 01_text_cleanup_A.py
        ├─ 01_text_cleanup_B.py
        ├─ 01_text_cleanup_C.py
        ├─ 01_text_cleanup_D.py
        ├─ 02_text_merge_A.py
        ├─ 02_text_merge_B.py
        ├─ 02_text_merge_C.py
        ├─ 02_text_merge_D.py
        ├─ 03_mecab_ipadic_A.py
        ├─ 03_mecab_ipadic_B.py
        ├─ 03_mecab_ipadic_C.py
        ├─ 03_mecab_ipadic_D.py
        └─ 04_slideshow_4x4.py
```

## ライセンス

このプロジェクトはMITライセンスの下で提供されています。

## 貢献

プルリクエストを歓迎します。提案やバグ報告は大歓迎です。

## 連絡先

何か質問があれば、以下のメールアドレスまでご連絡ください。

- [your-email@example.com](mailto:your-email@example.com)
