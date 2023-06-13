# подключаем библиотеку компьютерного зрения 
import cv2

# функция определения лиц
def highlightFace(net, frame, conf_threshold=0.7):
    # делаем копию текущего кадра
    frameOpencvDnn=frame.copy()
    # высота и ширина кадра
    frameHeight=frameOpencvDnn.shape[0]
    frameWidth=frameOpencvDnn.shape[1]
    # преобразуем картинку в двоичный пиксельный объект
    blob=cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)
    # устанавливаем этот объект как входной параметр для нейросети
    net.setInput(blob)
    # выполняем прямой проход для распознавания лиц
    detections=net.forward()
    # переменная для рамок вокруг лица
    faceBoxes=[]
    # перебираем все блоки после распознавания
    for i in range(detections.shape[2]):
        # получаем результат вычислений для очередного элемента
        confidence=detections[0,0,i,2]
        # если результат превышает порог срабатывания — это лицо
        if confidence>conf_threshold:
            # формируем координаты рамки
            x1=int(detections[0,0,i,3]*frameWidth)
            y1=int(detections[0,0,i,4]*frameHeight)
            x2=int(detections[0,0,i,5]*frameWidth)
            y2=int(detections[0,0,i,6]*frameHeight)
            # добавляем их в общую переменную
            faceBoxes.append([x1,y1,x2,y2])
            # рисуем рамку на кадре
            cv2.rectangle(frameOpencvDnn, (x1,y1), (x2,y2), (0,255,0), int(round(frameHeight/150)), 8)
    # возвращаем кадр с рамками
    return frameOpencvDnn,faceBoxes

def findFaces(img_path=None):

    faceProto = "opencv_face_detector.pbtxt"
    faceModel = "opencv_face_detector_uint8.pb"
    faceNet = cv2.dnn.readNet(faceModel, faceProto)

    if img_path:
        img = cv2.imread(img_path)
        resultImg, faceBoxes = highlightFace(faceNet, img)
        while cv2.waitKey(1) < 0:
            cv2.imshow("Face recognition", resultImg)

    else:
        video = cv2.VideoCapture(0)

        while cv2.waitKey(1) < 0:
            hasFrame, frame = video.read()

            if not hasFrame:
                cv2.waitKey
                break

            resultImg, faceBoxes = highlightFace(faceNet, frame)
    
            cv2.imshow("Face recognition", resultImg)

if __name__ == '__main__':
    findFaces('face.jpeg')

    