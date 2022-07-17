import aspose.words as aw

def PngToPdf(pngPath:str,pdfPath:str):
    doc = aw.Document()
    builder = aw.DocumentBuilder(doc)

    builder.insert_image(pngPath)

    doc.save(pdfPath)


PngToPdf('D:\MyNode\github\opencv\其他\OET.png', 'D:\MyNode\github\opencv\其他\OET.pdf')
