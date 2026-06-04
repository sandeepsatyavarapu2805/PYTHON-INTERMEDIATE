from pathlib import Path
from PIL import Image

BASE_DIR = Path(__file__).resolve().parent
PNG_DIR = BASE_DIR / "PNGS"
RESIZE_DIR = BASE_DIR / "PHOTOS 200 SIZE"
SIZE_200 = (200, 200)

def prepare_folder(folder_path):
    """Creates a folder, or empties it if it already exists."""
    if folder_path.exists():
        for old_file in folder_path.iterdir():
            if old_file.is_file():
                old_file.unlink()
    else:
        folder_path.mkdir(parents=True, exist_ok=True)

# Prepare both output directories
prepare_folder(PNG_DIR)
prepare_folder(RESIZE_DIR)


demo_img = next(BASE_DIR.glob("*.jpg"), None)
if demo_img:
    with Image.open(demo_img) as img1:
        img1.show() # Pops the image up on your screen to inspect it
        print(f"Demo complete: Displayed {demo_img.name} on screen.")
else:
    print("No .jpg images found in the base folder to demo.")


for img_path in BASE_DIR.rglob("*.jpg"):

    # Safety check: skip files that are already inside our output folders
    if "PNGS" in img_path.parts or "PHOTOS 200 SIZE" in img_path.parts:
        continue
        
    try:
        with Image.open(img_path) as i:
            # Convert and save as PNG
            png_save_path = PNG_DIR / f"{img_path.stem}.png"
            i.save(png_save_path)
            print(f"Converted : {img_path.name} -> {png_save_path.name}")
            
            # Resize and save as JPG
            resized_img = i.copy()
            resized_img.thumbnail(SIZE_200)
            
            resized_save_path = RESIZE_DIR / f"{img_path.stem}_200{img_path.suffix}"
            resized_img.save(resized_save_path, quality=85)
            print(f"Resized image: {img_path.name} -> {resized_save_path.name}")
            
    except Exception as e:
        print(f"Failed to process {img_path.name}: {e}")

'''
from PIL import ImageFilter

# you can also do this for images
i.rotate(90)
i.convert(mode='L') # this converts the image into black and white
i.filter(ImageFilter.GaussianBlur(15)) # it blurs the image to the set radius use the import for this function

'''