# loaders/image_loader.py

from PIL import Image


def validate_image(path):

    try:

        img = Image.open(path)

        img.verify()

        return True

    except Exception:

        return False


def validate_images(paths):

    valid_paths = []

    invalid_paths = []

    for path in paths:

        if validate_image(path):

            valid_paths.append(path)

        else:

            invalid_paths.append(path)

    return {

        "valid": valid_paths,

        "invalid": invalid_paths

    }