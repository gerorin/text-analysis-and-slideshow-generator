import os
import subprocess
import time

# ログファイルの保存先を設定
log_directory = os.path.join('data', 'output', 'error_log')
log_file_path = os.path.join(log_directory, 'process_log.txt')

# ログディレクトリの作成（存在しない場合）
os.makedirs(log_directory, exist_ok=True)

# ログを初期化
def init_log():
    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        log_file.write("進捗ログ\n\n")

# 進捗をログに記録
def log_progress(message):
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")
    print(message)  # コンソールにも出力

# テキストのクリーニング処理
def text_cleanup():
    log_progress("テキストのクリーニングを開始します...")
    scripts = [
        os.path.join('src', '01_text_cleanup_A.py'),
        os.path.join('src', '01_text_cleanup_B.py'),
        os.path.join('src', '01_text_cleanup_C.py'),
        os.path.join('src', '01_text_cleanup_D.py')
    ]
    for script in scripts:
        log_progress(f"スクリプト {script} を実行中...")
        try:
            subprocess.run(['python', script], check=True)  # エラー発生時に例外を投げる
            log_progress(f"スクリプト {script} が完了しました。\n")
        except subprocess.CalledProcessError as e:
            log_progress(f"エラーが発生しました: {e}\n")
    log_progress("テキストのクリーニングが完了しました。\n")

# テキストのマージ処理
def text_merge():
    log_progress("テキストのマージを開始します...")
    scripts = [
        os.path.join('src', '02_text_merge_A.py'),
        os.path.join('src', '02_text_merge_B.py'),
        os.path.join('src', '02_text_merge_C.py'),
        os.path.join('src', '02_text_merge_D.py')
    ]
    for script in scripts:
        log_progress(f"スクリプト {script} を実行中...")
        try:
            subprocess.run(['python', script], check=True)
            log_progress(f"スクリプト {script} が完了しました。\n")
        except subprocess.CalledProcessError as e:
            log_progress(f"エラーが発生しました: {e}\n")
    log_progress("テキストのマージが完了しました。\n")

# MeCabによる形態素解析処理
def mecab_processing():
    log_progress("MeCabでの形態素解析を開始します...")
    scripts = [
        os.path.join('src', '03_mecab_ipadic_A.py'),
        os.path.join('src', '03_mecab_ipadic_B.py'),
        os.path.join('src', '03_mecab_ipadic_C.py'),
        os.path.join('src', '03_mecab_ipadic_D.py')
    ]
    for script in scripts:
        log_progress(f"スクリプト {script} を実行中...")
        try:
            subprocess.run(['python', script], check=True)
            log_progress(f"スクリプト {script} が完了しました。\n")
        except subprocess.CalledProcessError as e:
            log_progress(f"エラーが発生しました: {e}\n")
    log_progress("MeCabでの形態素解析が完了しました。\n")

# スライドショー生成処理
def generate_slideshow():
    log_progress("スライドショーの生成を開始します...")
    slideshow_script = os.path.join('src', '04_slideshow_4x4.py')
    log_progress(f"スクリプト {slideshow_script} を実行中...")
    try:
        subprocess.run(['python', slideshow_script], check=True)
        log_progress(f"スクリプト {slideshow_script} が完了しました。\n")
    except subprocess.CalledProcessError as e:
        log_progress(f"エラーが発生しました: {e}\n")
    log_progress("スライドショーの生成が完了しました。\n")

# メイン処理
if __name__ == "__main__":
    log_progress("全体のプロセスを開始します。\n")

    # ステップ1: ログの初期化
    init_log()

    # ステップ2: テキストのクリーニング
    text_cleanup()

    # ステップ3: テキストのマージ
    text_merge()

    # ステップ4: MeCabによる形態素解析
    mecab_processing()

    # ステップ5: スライドショー生成
    generate_slideshow()

    log_progress("全ての処理が完了しました。")
