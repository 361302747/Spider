import zxing

reader = zxing.BarCodeReader("/var/opt/zxing")

barcode = reader.decode("/tmp/image.jpg")
(barcode1, barcode2) = reader.decode(["/tmp/1.png", "/tmp/2.png"])
code_list = reader.decode("/tmp/barcodes", True)
