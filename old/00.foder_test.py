import os
import cv2


def list_full_paths_in_subfolders(test_dir):
    file_details = []
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            full_path = os.path.join(root, file)
            file_details.append((root, file, full_path))
    return file_details

# testディレクトリへのパスを設定してください
test_dir = "../00.Datasets/"
file_info = list_full_paths_in_subfolders(test_dir)


# 結果を表示
for path, file, full_path in file_info:
    print(f"Path: {path}, File: {file}, Full Path: {full_path}")

    img_src = cv2.imread(full_path, 0)
    img_dst = cv2.equalizeHist(img_src)

    #new path name
    new_pathname = os.path.join(path,"equilized_hist")
    os.makedirs(new_pathname, exist_ok=True)

    cv2.imwrite(os.path.join(new_pathname, file), img_dst)


