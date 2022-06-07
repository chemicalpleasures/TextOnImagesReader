Idea: use OCR to read all product images using PyTesseract or a comparable library.
Need to train Tesseract using the appropriate font files, which are included.

Program should do this:

1. Import all product images
2. Programmatically edit all images using OpenCV to be more machine-readable
3. Use PyTesseract to create bounding boxes around text and read all text on images
4. Using Pandas, create a dataframe which receives a.) the SKU and b.) the text from the images
5. Upload text to Salsify