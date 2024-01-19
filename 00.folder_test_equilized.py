import os
import cv2

def list_full_paths_in_subfolders(test_dir):
    file_details = []
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            # 画像ファイルのみを処理 (Process only image files)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff', '.gif')):
                full_path = os.path.join(root, file)
                file_details.append((root, file, full_path))
    return file_details

# testディレクトリへのパスを設定 (Set the path to the test directory)
test_dir = "./00.Datasets/"
file_info = list_full_paths_in_subfolders(test_dir)

# 結果を処理 (Process the results)
for path, file, full_path in file_info:
    print(f"Path: {path}, File: {file}, Full Path: {full_path}")
    # グレースケールで画像を読み込む (Read the image in grayscale)
    img_src = cv2.imread(full_path, 0)
    if img_src is not None:
        img_dst = cv2.equalizeHist(img_src)  # ヒストグラム均一化 (Histogram equalization)

        # ユニークなファイル名を生成 (Generate a unique file name)
        base, ext = os.path.splitext(file)
        new_filename = f"{base}_equalized{ext}"

        # 新しいパス名を生成 (Generate a new pathname)
        new_pathname = os.path.join(path, "equilized_hist")
        os.makedirs(new_pathname, exist_ok=True)

        # 画像を新しいパスに保存 (Save the image to the new path)
        cv2.imwrite(os.path.join(new_pathname, new_filename), img_dst)
    else:
        # 読み込みに失敗した場合の警告 (Warning if failed to read the image)
        print(f"Warning: Unable to read image file {full_path}")

