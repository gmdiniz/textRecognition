import cv2
import numpy as np
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Users\gabri\AppData\Local\Tesseract-OCR\tesseract.exe'

def main(pathImg):
    img = cv2.imread(pathImg)
    imagemTratada = trataImagem(img)
    imagemPlotada = plotaElementoTxt(img)
    convertImg(imagemTratada)
    exibeImg(imagemPlotada)
    exibeImg(imagemTratada)
    logOutput(convertImg(imagemTratada))

def trataImagem(img):
    #Redimensionamento
    img = cv2.resize(img, None, fx=0.8, fy=0.8)

    #GreyScale
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Ajustar Ruido
    # adaptive_threshold = cv2.adaptiveThreshold(grey, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 95, 11)
    adaptive_threshold = cv2.Canny(grey, 50, 200)
    return adaptive_threshold

def plotaElementoTxt(img):
    #Plotar caracter
    hImg, wImg,_ = img.shape
    boxes = pytesseract.image_to_boxes(img)
    file1 = open("lines","w")

    for b in boxes.splitlines():
        print(b)
        line = str(b) + "\n"
        file1.writelines(line)
        b = b.split(' ')
        print(b)
        line = str(b) + "\n"
        file1.writelines(line)
        x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
        cv2.rectangle(img, (x,hImg-y), (w,hImg-h), (0,0,255), 2)

    file1.close()
    return img

def convertImg(img):
    text = pytesseract.image_to_string(img)
    print("\nSaída: \n" + text)
    return text

def exibeImg(img):
    cv2.imshow("adaptive th", img)
    cv2.waitKey(0)

def logOutput(text):
    File_object = open(r"Registro","w")
    File_object.write(text)
    File_object.close()

main("images/img5.jpg")