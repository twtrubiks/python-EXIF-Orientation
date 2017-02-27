import os, uuid
from PIL import Image, ExifTags

dic_exif = {
    1: 0,
    8: 90,
    3: 180,
    6: -90
}
for filename in os.listdir("input_img"):
    if filename.endswith('jpg') or filename.endswith('jpeg'):
        print('Processing img {}......'.format(filename))
        img = Image.open('input_img/' + filename)
        try:
            exif = {
                ExifTags.TAGS[k]: v
                for k, v in img._getexif().items()
                if k in ExifTags.TAGS
                }
        except:
            exif = {
                'Orientation': 1
            }
        degree = dic_exif[exif['Orientation']]
        # 圖片選轉 ， expand 要設定 (不然旋轉後會有黑邊)
        img_clip = img.rotate(degree, expand=1)
        name = "output_img/output_TurnRight_{}.jpg".format(str(uuid.uuid4()))
        img_clip.save(name, "JPEG")
print('All Image Have Been Turn Right')
