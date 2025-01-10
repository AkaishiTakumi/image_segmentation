from PIL import Image
import os

def split_image(image_path, n, m, output_dir):
    # �摜���J��
    img = Image.open(image_path)
    img_width, img_height = img.size

    # ������̊e�摜�̕��ƍ������v�Z
    tile_width = img_width // n
    tile_height = img_height // m

    # �o�̓f�B���N�g�������݂��Ȃ��ꍇ�͍쐬
    os.makedirs(output_dir, exist_ok=True)

    # �������ĕۑ�
    for i in range(m):  # �c����
        for j in range(n):  # ������
            # �����̈�̌v�Z
            left = j * tile_width
            upper = i * tile_height
            right = left + tile_width
            lower = upper + tile_height

            # �摜��؂���
            cropped_img = img.crop((left, upper, right, lower))

            # �t�@�C�������w�肵�ĕۑ�
            output_path = os.path.join(output_dir, f"tile_{i}_{j}.png")
            cropped_img.save(output_path)
            print(f"Saved: {output_path}")

    print("�摜�̕������������܂����B")

# �g�p��
if __name__ == "__main__":
    image_path = "input_image.jpg"  # ��������摜�̃p�X
    n = 4  # �������̕�����
    m = 3  # �c�����̕�����
    output_dir = "output_tiles"  # �o�͐�f�B���N�g��

    split_image(image_path, n, m, output_dir)
