from reportlab.pdfgen import canvas
import os

def writeReport(fileName, args):

    # Crea un oggetto canvas per il report
    c = canvas.Canvas('reports/'+fileName+'.pdf')
    yPosition = 800 #startPosition
    xPosition = 50 #startPosition
    imgHeight = 300

    for arg in args:
        if(arg.endswith('.png')):
            yPosition = yPosition - imgHeight
            c.drawImage(arg, xPosition, yPosition, width=300, height=imgHeight)
            yPosition = yPosition - 15
            try:
                os.remove(arg)
            except FileNotFoundError:
                print("Il file non esiste")
        else:
            c.drawString(xPosition, yPosition, arg)
            yPosition = yPosition - 15

    # Salva il report
    c.save()