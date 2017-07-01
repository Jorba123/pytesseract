try:
    from pytesseract import image_to_string, TesseractError
except ImportError:
    from pytesseract.pytesseract import image_to_string
