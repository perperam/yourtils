from pathlib import Path
import cv2

def resize_img(raw_path, size):

    resized_path = raw_path.parent / (raw_path.name + "-resized")
    resized_path.mkdir(parents=True, exist_ok=True)

    for img_path in raw_path.glob("*.jpg"):
        img = cv2.imread(img_path.as_posix())
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        zesized_img = cv2.resize(img, size)
        cv2.imwrite((resized_path / img_path.name).as_posix(), zesized_img)

raw_path = Path("C:\\Users\\<user>\\Desktop\\images")
resize_img(raw_path, (256, 256))
