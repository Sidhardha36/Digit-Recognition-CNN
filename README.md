<img width="624" height="572" alt="Screenshot 2025-11-23 230457" src="https://github.com/user-attachments/assets/62fcc836-0a5c-406d-ad2f-c4d7f632898b" />
<img width="638" height="569" alt="Screenshot 2025-11-23 230303" src="https://github.com/user-attachments/assets/09155025-1e39-45cd-8a91-cbb855b598c4" />
<img width="646" height="578" alt="Screenshot 2025-11-23 230347" src="https://github.com/user-attachments/assets/59dcc0b7-1e10-451e-b303-3f4b1bbb9eea" />



# Handwritten Digit Recognition (CNN + Pygame UI)

This project is an interactive digit recognition application where users can draw digits (0–9) on a canvas, and a trained Convolutional Neural Network (CNN) predicts the number in real-time.

It combines:
- TensorFlow/Keras for the deep learning model
- Pygame for the drawing interface
- MNIST dataset for training

## Features

- Draw digits on a canvas
- Real-time CNN prediction
- Reset functionality
- Simple and clean UI
- Modular and customizable codebase

## Project Structure

```
Digit-Recognition/
│── app/
│   └── recognition.py        # Pygame UI for drawing and prediction
│
│── model/
│   ├── model.py              # Script to train the CNN
│   └── model.h5              # Saved trained model
│
├── requirements.txt
└── README.md
```

## Technologies Used

- Python 3.x
- TensorFlow / Keras
- NumPy
- Pygame

## Installation & Setup

### 1. Clone the repository
```
git clone https://github.com/<your-username>/Digit-Recognition-CNN.git
cd Digit-Recognition-CNN
```

### 2. Create a virtual environment
```
python -m venv venv
```

Activate environment:

Windows:
```
venv\Scripts\activate
```

Mac / Linux:
```
source venv/bin/activate
```

### 3. Install dependencies
```
pip install -r requirements.txt
```

## Training the CNN (Optional)

If you want to retrain the model, run:
```
cd model
python model.py
```

This generates a new:
```
model/model.h5
```

## Running the Application

```
cd app
python recognition.py
```

A window will open where you can draw digits and classify them.

## How the Model Works

1. The user draws a digit on a 300×300 canvas.
2. The image is converted to grayscale.
3. The orientation is adjusted to match MNIST format.
4. The image is resized to 28×28 pixels.
5. The pixel values are normalized.
6. The CNN predicts the most likely digit.

## Model Performance

- Approximately 99% training accuracy
- 98–99% validation accuracy on MNIST

## Contributing

Contributions are welcome. Feel free to open issues or submit pull requests.

## License

This project is open-source and free for personal or academic use.

## Author

Sidhardha Varma
