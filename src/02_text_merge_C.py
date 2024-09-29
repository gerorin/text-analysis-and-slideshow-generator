import os
from datetime import datetime

def merge_text_files_in_subfolders(parent_folder, output_folder, error_log_folder):
    # エラーログフォルダが存在しない場合は作成
    os.makedirs(error_log_folder, exist_ok=True)

    # 現在の日時を取得してログファイル名を作成
    current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file_name = f'merge_log_{current_time}.txt'
    log_file_path = os.path.join(error_log_folder, log_file_name)

    # ログファイルを初期化
    with open(log_file_path, 'w', encoding='utf-8') as log_file:
        log_file.write("マージ処理ログ開始\n")

    # 出力フォルダが存在しない場合は作成
    os.makedirs(output_folder, exist_ok=True)

    # 親フォルダ内の全サブフォルダをリスト化
    for subfolder, _, files in os.walk(parent_folder):
        # サブフォルダ内の全テキストファイルをフィルタリング
        txt_files = [f for f in files if f.endswith('.txt')]

        if txt_files:  # テキストファイルが存在する場合
            subfolder_name = os.path.basename(subfolder)
            output_file_path = os.path.join(output_folder, f"{subfolder_name}.txt")

            try:
                with open(output_file_path, mode='w', encoding='utf-8') as output_file:
                    for file_name in sorted(txt_files):
                        file_path = os.path.join(subfolder, file_name)
                        try:
                            with open(file_path, mode='r', encoding='utf-8') as input_file:
                                content = input_file.read()

                                # ファイル名をタグとして追加し、マージ後のテキストを書き込む
                                output_file.write(f"\n### {file_name} ###\n{content}")

                            # 成功したファイルの処理をログに記録
                            with open(log_file_path, 'a', encoding='utf-8') as log_file:
                                log_file.write(f"成功: {file_name} を {output_file_path} にマージしました。\n")
                        except Exception as e:
                            # エラーが発生した場合、そのファイルをエラーログに記録
                            with open(log_file_path, 'a', encoding='utf-8') as log_file:
                                log_file.write(f"エラー: ファイル {file_name} の読み込み中にエラーが発生しました - {e}\n")
            except Exception as e:
                # 出力ファイルの作成に失敗した場合
                with open(log_file_path, 'a', encoding='utf-8') as log_file:
                    log_file.write(f"エラー: 出力ファイル {output_file_path} の作成中にエラーが発生しました - {e}\n")

    # マージ処理が完了したことをログに記録
    with open(log_file_path, 'a', encoding='utf-8') as log_file:
        log_file.write("マージ処理が正常に終了しました。\n")

    print("すべてのサブフォルダの処理が完了しました。ログファイルを確認してください。")

# 相対パスを使用してフォルダのパスを指定
parent_folder = os.path.join('data', 'input', 'text_C')
output_folder = os.path.join('data', 'output', 'text_merge_C')
error_log_folder = os.path.join('data', 'output', 'error_log')

# マージ処理を実行
merge_text_files_in_subfolders(parent_folder, output_folder, error_log_folder)
