import os
from PIL import Image, ImageDraw, ImageFont
from tqdm import tqdm

# フォントパスを指定
font_path = 'C:\\Windows\\Fonts\\msgothic.ttc'

def save_combined_image_with_labels(folders, folder_labels, save_dir, margin=20):
    # フォルダ内の画像ファイル名を取得 (ファイル名が同一であることを前提)
    image_files = sorted([f for f in os.listdir(folders[0]) if f.endswith('.png')])

    # フォルダごとに4枚の画像を組み合わせて保存
    for image_file in tqdm(image_files, desc="Processing images"):
        # 画像を格納するリスト
        images = []

        # 各フォルダから同名の画像を読み込み
        for folder in folders:
            img_path = os.path.join(folder, image_file)
            if os.path.exists(img_path):
                img = Image.open(img_path)
                images.append(img)

        # 4つの画像が揃っている場合に処理を行う
        if len(images) == 4:
            # 4x4のグリッドで画像サイズを計算
            grid_size = 2  # 2x2のグリッド
            image_width, image_height = images[0].size  # 画像のサイズ（すべて同じと仮定）
            label_height = 60  # ラベルの高さ（フォントサイズに合わせて増加）
            total_width = (image_width * grid_size) + (margin * (grid_size - 1))  # 全体の幅
            total_height = (image_height * grid_size) + (margin * (grid_size - 1)) + (label_height * grid_size)  # ラベル込みの高さ

            # 結合用の空の画像を作成
            combined_image = Image.new('RGB', (total_width, total_height), (255, 255, 255))  # 背景は白

            # フォント設定
            try:
                font_size = 30  # フォントサイズ
                font = ImageFont.truetype(font_path, font_size)  # 指定したフォントを使用
            except IOError:
                print("指定したフォントが見つかりません。デフォルトフォントを使用します。")
                font = ImageFont.load_default()

            # 画像を貼り付けてフォルダ名をラベルとして描画
            draw = ImageDraw.Draw(combined_image)
            for idx, (img, folder_label) in enumerate(zip(images, folder_labels)):
                x_offset = (idx % grid_size) * (image_width + margin)
                y_offset = (idx // grid_size) * (image_height + margin + label_height)

                # 画像を貼り付ける
                combined_image.paste(img, (x_offset, y_offset + label_height))

                # フォルダ名を描画
                bbox = draw.textbbox((0, 0), folder_label, font=font)  # テキストのバウンディングボックスを取得
                text_width = bbox[2] - bbox[0]  # テキストの幅
                text_height = bbox[3] - bbox[1]  # テキストの高さ
                text_x = x_offset + (image_width - text_width) // 2  # 中央に配置
                text_y = y_offset  # 画像の上に配置
                draw.text((text_x, text_y), folder_label, font=font, fill=(0, 0, 0))  # 黒色で描画

            # ファイル名を指定して保存
            save_path = os.path.join(save_dir, image_file)  # 元のファイル名で保存
            combined_image.save(save_path)
            print(f'Saved combined image: {save_path}')

# フォルダのパスを指定
folders = [
    r'data\output\wordcloud_A',
    r'data\output\wordcloud_B',
    r'data\output\wordcloud_C',
    r'data\output\wordcloud_D'
]

# フォルダラベルを指定
folder_labels = [
    "総合計画＋地方創生＋ICT&DX＋各種計画",
    "総合計画＋地方創生＋ICT&DX",
    "総合計画＋ICT&DX",
    "総合計画"
]

# 保存先のディレクトリを指定
save_dir = r'data\output\wordcloud_4x4'

# 画像を結合して保存
save_combined_image_with_labels(folders, folder_labels, save_dir, margin=20)
