import os
import chardet
import unicodedata
import re
from tqdm import tqdm
import MeCab
from sklearn.feature_extraction.text import TfidfVectorizer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.font_manager as fm

# フォントとファイルパスの設定
font_path = 'C:\\Windows\\Fonts\\msgothic.ttc'
text_dir = r'data\output\text_merge_C'  # テキストファイルのディレクトリ
stop_words_path = r'data\input\word_filters\stopword.txt'  # ストップワードのパス
target_words_path = r'data\input\word_filters\targetword.txt'  # ターゲットワードのパス

# MeCabの辞書パスを指定
dictionary_path = r"C:\Program Files\MeCab\dic\ipadic"
mecab = MeCab.Tagger(f"-d \"{dictionary_path}\"")

# ストップワードリストの読み込み
with open(stop_words_path, 'r', encoding='utf-8') as file:
    stop_words = file.read().splitlines()

# ターゲットワードリストの読み込み
with open(target_words_path, 'r', encoding='utf-8') as file:
    target_words = file.read().splitlines()

# テキスト処理関数
def preprocess_text(text_dir, stop_words, target_words):
    text_files = [f for f in os.listdir(text_dir) if f.endswith('.txt')]
    texts = []

    for text_file in tqdm(text_files, desc="Processing text files"):
        try:
            with open(os.path.join(text_dir, text_file), 'rb') as file:
                binary_data = file.read()
                result = chardet.detect(binary_data)
                encoding = result['encoding'] if result['encoding'] is not None else 'utf-8'
                text = binary_data.decode(encoding)
                
                # 形態素解析段階での前処理
                text = unicodedata.normalize('NFKC', text)  # 文字表現の正規化
                text = re.sub(r'http[s]?://\S+', '', text)  # URLテキストの除外
                text = re.sub('<[^>]*?>', '', text)  # HTMLタグの削除
                text = re.sub(r'[^\w\s]', '', text)  # 記号の削除（英字も含む）
                text = re.sub(r'\d+', '0', text)  # すべての数字を「0」に変換
                text = re.sub(r'[\x00-\x1F\x7F-\x9F]', '', text)  # 制御文字の除去
                text = re.sub(r'\s+', ' ', text).strip()  # 複数の空白を1つに、前後の空白を削除

                # ターゲットワードを一時的に置換
                for word in target_words:
                    text = re.sub(r'\b' + re.escape(word) + r'\b', word, text)
                
                # 形態素解析
                text = mecab.parse(text)
                tokens = [line.split('\t')[0] for line in text.splitlines() if line and not line.startswith('EOS')]

                # 名詞のみを抽出し、ストップワードを除外
                words = [token for token in tokens if token not in stop_words]
                text = ' '.join(words)
                texts.append(text)
        except Exception as e:
            print(f"Error processing file {text_file}: {e}")

    return texts, text_files

# 動的なTF-IDF計算関数
def calculate_tfidf(texts, stop_words, max_df=1.0, min_df=0.1, ngram_range=(1, 2), max_features=500):
    tfidf_vectorizer = TfidfVectorizer(max_df=max_df, min_df=min_df, stop_words=stop_words, ngram_range=ngram_range, max_features=max_features)
    tfidf = tfidf_vectorizer.fit_transform(texts)
    words = tfidf_vectorizer.get_feature_names_out()
    return tfidf, words

# ワードクラウド生成関数の修正
def generate_wordclouds(texts, text_files, tfidf, words, font_path, png_dir):
    if not os.path.exists(png_dir):
        os.makedirs(png_dir)

    # フォントプロパティの設定
    font_prop = fm.FontProperties(fname=font_path)

    for i, text_file in enumerate(tqdm(text_files, desc="Generating wordclouds")):
        try:
            frequencies = tfidf.toarray()[i]
            word_frequencies = dict(zip(words, frequencies))

            # ワードクラウドの生成
            if max(frequencies) > 0:
                wordcloud = WordCloud(
                    background_color="white", 
                    font_path=font_path, 
                    width=800, height=600, 
                    margin=3,
                    max_words=300
                ).generate_from_frequencies(word_frequencies)

                # ワードクラウドの描画
                fig, ax = plt.subplots(figsize=(8, 6))
                ax.imshow(wordcloud, interpolation='bilinear')
                ax.axis("off")

                # ファイル名表示用のテキストを上部に追加
                plt.text(0.5, 1.03, text_file.replace('.txt', ''), ha='center', va='top', fontsize=12, color='black', fontproperties=font_prop, transform=ax.transAxes)

                # ワードクラウドの保存
                plt.savefig(os.path.join(png_dir, text_file.replace('.txt', '.png')), format='png', bbox_inches='tight', pad_inches=0.1)
                plt.close()
            else:
                print(f"Skipping wordcloud for {text_file}: no valid frequencies found.")
        except Exception as e:
            print(f"Error generating wordcloud for {text_file}: {e}")

# メイン処理
texts, text_files = preprocess_text(text_dir, stop_words, target_words)
tfidf, words = calculate_tfidf(texts, stop_words, max_df=0.9, min_df=0.1, ngram_range=(1, 2), max_features=500)
png_dir = r'data\output\wordcloud_C'  # PNG出力先ディレクトリ
generate_wordclouds(texts, text_files, tfidf, words, font_path, png_dir)