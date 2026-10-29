
from pathlib import Path
from PIL import Image
import hashlib
import random
import shutil

# Original dataset location
DATASET_DIR = Path(r"D:\potato")

# Project location
BASE_DIR = Path(__file__).resolve().parent
PROCESSED_DIR = BASE_DIR / "processed_data"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}
SPLIT_RATIOS = (0.70, 0.15, 0.15)
RANDOM_SEED = 42


def clean_data():

    if not DATASET_DIR.exists():
        raise FileNotFoundError(
            f"Dataset folder not found: {DATASET_DIR}"
        )

    # Each immediate subfolder is a disease class
    class_folders = sorted(
        folder for folder in DATASET_DIR.iterdir()
        if folder.is_dir()
    )

    if not class_folders:
        raise ValueError("No class folders found inside D:\\potato")

    # Remove the previous processed dataset
    if PROCESSED_DIR.exists():
        shutil.rmtree(PROCESSED_DIR)

    rng = random.Random(RANDOM_SEED)
    total_images = 0

    for class_folder in class_folders:

        valid_images = []
        seen_hashes = set()

        # Read images from this class folder
        for image_path in class_folder.rglob("*"):

            if not image_path.is_file():
                continue

            if image_path.suffix.lower() not in IMAGE_EXTENSIONS:
                continue

            try:
                # Check that the image is readable
                with Image.open(image_path) as image:
                    image.verify()

                # Remove exact duplicates within this class
                image_hash = hashlib.sha256(
                    image_path.read_bytes()
                ).hexdigest()

                if image_hash not in seen_hashes:
                    seen_hashes.add(image_hash)
                    valid_images.append(image_path)

            except Exception:
                print("Skipping invalid image:", image_path)

        rng.shuffle(valid_images)
        count = len(valid_images)

        if count < 3:
            raise ValueError(
                f"Class '{class_folder.name}' has only {count} "
                "valid unique images. Add more images."
            )

        train_end = int(count * SPLIT_RATIOS[0])
        val_end = train_end + int(count * SPLIT_RATIOS[1])

        split_data = {
            "train": valid_images[:train_end],
            "validation": valid_images[train_end:val_end],
            "test": valid_images[val_end:]
        }

        for split_name, image_paths in split_data.items():

            output_folder = (
                PROCESSED_DIR / split_name / class_folder.name
            )
            output_folder.mkdir(parents=True, exist_ok=True)

            for index, source_path in enumerate(image_paths):

                # Avoid filename collisions
                output_name = (
                    f"{index}_{source_path.name}"
                )

                shutil.copy2(
                    source_path,
                    output_folder / output_name
                )

        class_total = sum(
            len(paths) for paths in split_data.values()
        )
        total_images += class_total

        print(f"\nClass: {class_folder.name}")
        print("  Training:", len(split_data["train"]))
        print("  Validation:", len(split_data["validation"]))
        print("  Testing:", len(split_data["test"]))

    print("\nData cleaning and splitting completed.")
    print("Total images:", total_images)
    print("Processed data:", PROCESSED_DIR)


if __name__ == "__main__":
    clean_data()
