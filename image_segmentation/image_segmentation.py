from wsgiref.validate import InputWrapper
from PIL import Image
import os

def split_image(image_path, n, m, output_dir,input_without_ext_nxm):
    # 画像を開く
    Image.MAX_IMAGE_PIXELS=2000000000 #20億 NULL:無制限
    img = Image.open(image_path)
    img_width, img_height = img.size

    # 分割後の各画像の幅と高さを計算
    tile_width = img_width // n
    tile_height = img_height // m

    # 出力ディレクトリが存在しない場合は作成
    os.makedirs(output_dir, exist_ok=True)

    # 分割して保存
    for i in range(m):  # 縦方向
        for j in range(n):  # 横方向
            # 分割領域の計算
            left = j * tile_width
            upper = i * tile_height
            right = left + tile_width
            lower = upper + tile_height

            # 画像を切り取る
            cropped_img = img.crop((left, upper, right, lower))

            # ファイル名を指定して保存
            output_path = os.path.join(output_dir, f"{input_without_ext_nxm}_tile_{i}_{j}.png")
            cropped_img.save(output_path)
            print(f"Saved: {output_path}")

    print("画像の分割が完了しました。")

# 使用例
if __name__ == "__main__":
    # 入力ディレクトリが存在しない場合は作成
    os.makedirs("image", exist_ok=True)
    input("imageディレクトリに分割したい画像を入れてください。\n"+
          "分割したい画像をimageディレクトリに入れたらEnterを押してください。\n"+
          "分割する画像のパスを入力してください。")
    for file in os.listdir("image"):
        if os.path.isfile(os.path.join("image", file)):  # ファイルのみ表示
            print(file)
    image_path=input("コピーして使用:\n")
    n=int(input("横方向の分割数を入力:"))
    m=int(input("縦方向の分割数を入力:"))
    input_without_ext_nxm=os.path.splitext(os.path.basename(image_path))[0]+f"_{n}x{m}"
    output_dir="output_tiles\\"+input_without_ext_nxm

    split_image(image_path, n, m, output_dir,input_without_ext_nxm)
