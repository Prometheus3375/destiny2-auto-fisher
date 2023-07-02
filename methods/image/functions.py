from PIL.Image import Image, open as _open_image
from numpy import asarray, ndarray


def open_image(path: str, /) -> Image:
    """
    Takes a path to an image file and loads it into RAM.
    """
    return _open_image(path, 'r', ['png'])


def image_matrix(image: Image, /) -> ndarray:
    """
    Takes an image, converts it to grayscale and returns its matrix.
    """
    return asarray(image.convert('L'), int)


def difference_images(im1: Image, im2: Image, /) -> ndarray:
    """
    Takes two images, converts them to grayscale and returns absolute difference between
    their matrices. **Note**: matrices must have identical shape.
    """
    return abs(image_matrix(im1) - image_matrix(im2))


def difference_matrix_image(matrix: ndarray, im2: Image, /) -> ndarray:
    """
    Takes a matrix and an image, converts the image to grayscale and evaluates its matrix.
    Returns absolute difference between matrices. **Note**: matrices must have identical shape.
    """
    return abs(matrix - image_matrix(im2))


__all__ = 'open_image', 'image_matrix', 'difference_images', 'difference_matrix_image'
