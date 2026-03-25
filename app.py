from flask import Flask, render_template, request, jsonify
import base64
import cv2
import numpy as np
import mediapipe as mp
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("modell.joblib")

labels_dict = {0: '1', 1: '2', 2: '3', 3: '4', 4: '5', 5: '6', 6: '7', 7: '8', 8: '9', 9: 'A', 10: 'B', 11: 'C', 12: 'D', 13: 'E',
                14: 'F', 15: 'G', 16: 'H', 17: 'I', 18: 'J', 19: 'K', 20: 'L', 21: 'M', 22: 'N', 23: 'O', 24: 'P', 25: 'Q', 26: 'R',
                27: 'S', 28: 'T', 29: 'U', 30: 'V', 31: 'W', 32: 'X', 33: 'Y', 34: 'Z', 35: 'Hello', 36: 'Indian', 37: 'Namasthe', 38: 'Man',
                39: 'Woman', 40: 'Again', 41: 'Me', 42: 'You', 43: 'Deaf', 44: 'Blind', 45: 'Happy',46:'Thankyou',47:'Beautiful',48:'Difficult',
                49:'Food',50:'Nice',51:'House',52:'Flower',53:'Fool',54:'What',55:'When',56:'Good',57:'Sleep',58:'Badsmell',59:'Headache'
}

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,
    min_detection_confidence=0.3
)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json["image"]
    img_bytes = base64.b64decode(data)
    np_img = np.frombuffer(img_bytes, np.uint8)
    frame = cv2.imdecode(np_img, cv2.IMREAD_COLOR)

    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(frame_rgb)

    prediction_text = "No hand detected"

    if results.multi_hand_landmarks:
        landmarks = results.multi_hand_landmarks[0].landmark
        x_coords = [lm.x for lm in landmarks]
        y_coords = [lm.y for lm in landmarks]

        min_x, max_x = min(x_coords), max(x_coords)
        min_y, max_y = min(y_coords), max(y_coords)

        data_aux = []
        for lm in landmarks:
            data_aux.extend([
                (lm.x - min_x) / (max_x - min_x + 1e-6),
                (lm.y - min_y) / (max_y - min_y + 1e-6)
            ])

        if len(data_aux) == 42:
            pred = model.predict([data_aux])[0]
            prediction_text = labels_dict.get(int(pred), "Unknown")

    return jsonify({"prediction": prediction_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
