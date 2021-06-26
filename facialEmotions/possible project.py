from keras.preprocessing.image import img_to_array
import imutils
import cv2
from keras.models import load_model
import numpy as np
import h5py

mini = "_mini_.hdf5"
with h5py.File(mini, "r") as f:
    print("Keys: %s" % f.keys())
    a_group_key = list(f.keys())[0]

    data = list(f[a_group_key])

    data_matrix = np.random.uniform(-1, 1, size=(10, 3))

dectection_model_path = 'facialhaar.xml'
emotion_model_path = "_mini_.hdf5"

face_detection = cv2.CascadeClassifier(dectection_model_path)
emotion_classifer = load_model(emotion_model_path, compile=False)
EMOTIONS = ['angry', 'sad', 'disgust', 'scared', 'happy', 'surprised', 'neutral']

cv2.namedWindow('Face')
camera = cv2.VideoCapture(0)
while True:
    frame = camera.read()[1]
    frame = imutils.resize(frame,width=400)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detection.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30),
                                            flags=cv2.CASCADE_SCALE_IMAGE)

    canvas = np.zeros((250, 300, 3), dtype="uint8")
    frameClone = frame.copy()
    if len(faces) > 0:
        faces = sorted(faces, reverse=True,
                       key=lambda x: (x[2] - x[0]) * (x[3] - x[1]))[0]
        (fX, fY, fW, fH) = faces
        roi = gray[fY:fY + fH, fX:fX + fW]
        roi = cv2.resize(roi, (48, 48))
        roi = roi.astype("float") / 255.0
        roi = img_to_array(roi)
        roi = np.expand_dims(roi, axis=0)

        preds = emotion_classifer.predict(roi)[0]
        emotion_probabilty = np.max(preds)
        label = EMOTIONS[preds.argmax()]

        for (i, (emotion, prob)) in enumerate(zip(EMOTIONS, preds)):
            text = "{}: {:.2f}%".format(emotion, prob * 100)
            w = int(prob * 300)
            cv2.rectangle(canvas, (7, (i * 35) + 5),
                          (w, (i * 35) + 35), (0, 0, 255), -1)
            cv2.putText(canvas, text, (10, (i * 35) + 23),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)
            cv2.rectangle(frameClone, (fX, fY), (fX + fW, fY + fH),
                                       (0, 0, 255), 2)

            cv2.imshow('your_face', frameClone)
            cv2.imshow('Probabilities', canvas)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        camera.release()
        cv2.destroyAllWindows()
