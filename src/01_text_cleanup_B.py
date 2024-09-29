import os
from datetime import datetime

# 親フォルダのパスを設定
parent_folder_path = os.path.join('data', 'input', 'text_B')

# エラーログを保存するフォルダのパス（ここにログを保存する）
error_log_folder = os.path.join('data', 'output', 'error_log')

# 現在の日時を取得してエラーログファイル名を作成
current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
log_file_name = f'process_log_{current_time}.txt'
log_file_path = os.path.join(error_log_folder, log_file_name)

# ログファイルを初期化
with open(log_file_path, 'w', encoding='utf-8') as log_file:
    log_file.write(f"処理ログ - 開始時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")

# 指定した親フォルダ内のすべてのサブフォルダとファイルを処理
for root, dirs, files in os.walk(parent_folder_path):
    for file_name in files:
        if file_name.endswith('.txt'):
            try:
                file_path = os.path.join(root, file_name)

                # ファイルを読み込む
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # 改行、全角空白、半角空白を削除
                content_processed = content.replace('\n', '').replace('　', '').replace(' ', '')

                # 元のファイルに上書き保存
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content_processed)

                # 成功ログを記録
                with open(log_file_path, 'a', encoding='utf-8') as log_file:
                    log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - ファイル {file_name} を正常に処理しました。\n")

            except Exception as e:
                # エラー情報をログファイルに記録
                with open(log_file_path, 'a', encoding='utf-8') as log_file:
                    log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - ファイル {file_name} の処理中にエラーが発生しました: {e}\n")

# 終了時刻をログに記録
with open(log_file_path, 'a', encoding='utf-8') as log_file:
    log_file.write(f"\n処理完了 - 終了時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

print("処理が完了しました。ログファイルに記録されています。")
