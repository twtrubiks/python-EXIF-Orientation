# python-EXIF-Orientation
自動判斷照片是否有被旋轉過，如有被旋轉，將照片轉正 📝

* [Youtube Demo]()


## 特色
* 透過 JPG/JPEG 裡的 EXIF Orientation 屬性，判斷照片是否有被旋轉過。
* 透過 [pillow](https://pillow.readthedocs.io/en/4.0.x/) 將照片轉正。


## 安裝套件
確定電腦有安裝 [Python](https://www.python.org/) 之後

clone 我的簡單範例

```
git clone https://github.com/twtrubiks/python-EXIF-Orientation.git
```

接著請在  cmd (命令提示字元) 輸入以下指令
```
pip install pillow
```

## 說明

關於 JPG/JPEG 裡的 EXIF-Orientation 參數，可以參考這張圖

![alt tag](http://i.imgur.com/jRcq0kC.jpg)

從上圖可以發現

8 代表順時針轉90度

3 代表旋轉180度

6 代表逆時針90度

程式碼思路，只要先找到他們的 EXIF-Orientation 參數 (編號)，也就是往哪個方向旋轉幾度，

再用 [pillow](https://pillow.readthedocs.io/en/4.0.x/) 反方向旋轉回來即可。

## 使用方法

將要轉正的圖片放在 [input_img]() 資料夾裡

執行
```
python app.py
```

會將轉正的圖片輸出在 [output_img]() 資料夾裡

## 其他說明

這個方法只適用在 JPG/JPEG 裡，並不適用在 PNG裡面。

如果有一張圖片是從 PNG 轉成 JPG/JPEG，裡面的 EXIF-Orientation 這個參數也會消失。


## 執行環境
* Python 3.4.3

## Reference
* [pillow](https://pillow.readthedocs.io/en/4.0.x/)
* [exif-orientation](http://www.impulseadventure.com/photo/exif-orientation.html)

## License
MIT license
