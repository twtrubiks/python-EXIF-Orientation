import os
import uuid
from PIL import Image, ExifTags

# Map EXIF orientation values to corresponding Pillow transpose methods
ORIENTATION_TO_TRANSPOSE = {
    1: None,  # Normal
    2: Image.Transpose.FLIP_LEFT_RIGHT,
    3: Image.Transpose.ROTATE_180, # 180
    4: Image.Transpose.FLIP_TOP_BOTTOM,
    5: Image.Transpose.TRANSPOSE,
    6: Image.Transpose.ROTATE_270, # -90
    7: Image.Transpose.TRANSVERSE,
    8: Image.Transpose.ROTATE_90, # 90
}


def rotate_image(image_path):
    """
    Rotates an image based on its EXIF orientation tag.

    Args:
        image_path (str): The path to the image file.

    Returns:
        PIL.Image.Image or None: The rotated image object, or None if the file is not a valid image.
    """
    try:
        with Image.open(image_path) as img:
            try:
                exif = {
                    ExifTags.TAGS[k]: v
                    for k, v in img._getexif().items()
                    if k in ExifTags.TAGS
                }
                orientation = exif.get('Orientation', 1)
            except (AttributeError, KeyError, IndexError):
                # Cases: image has no EXIF info, or Orientation tag is missing
                # 當圖片沒有 EXIF 資訊或 `Orientation` 標籤遺失的情況
                orientation = 1

            transpose_method = ORIENTATION_TO_TRANSPOSE.get(orientation)

            if transpose_method is not None:
                return img.transpose(transpose_method)
            return img.copy() # Return a copy to avoid issues with the original file object
    except IOError:
        print(f"Cannot open {image_path}. It might be a corrupted or unsupported file.")
        return None


def main():
    """
    Processes all JPEG images in the input directory, rotates them according to their
    EXIF orientation, and saves them to the output directory.
    """
    input_dir = "input_img"
    output_dir = "output_img"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(('jpg', 'jpeg')):
            print(f"Processing img {filename}......")
            input_path = os.path.join(input_dir, filename)
            rotated_img = rotate_image(input_path)

            if rotated_img:
                output_filename = f"output_TurnRight_{uuid.uuid4()}.jpg"
                output_path = os.path.join(output_dir, output_filename)
                rotated_img.save(output_path, "JPEG")

    print("All images have been processed.")


if __name__ == "__main__":
    main()
