### Handwritten Digit Recognition (CNN + Pygame UI)

This project is an interactive digit recognition application where users can draw digits (0–9) on a canvas, and a trained Convolutional Neural Network (CNN) predicts the number in real-time.

It combines:

TensorFlow/Keras → Deep learning model

Pygame → Drawing UI

MNIST Dataset → Training data

🚀 Features

🎨 Draw digits on a canvas

⚡ Real-time CNN predictions

🔄 Reset button

🖥️ Clean & simple UI

🔧 Easy to extend and customize

📦 Well-organized, production-ready structure

📂 Project Structure
Digit-Recognition/
│── app/
│   └── recognition.py        # Pygame UI for drawing & prediction
│
│── model/
│   ├── model.py              # Script to train the CNN
│   └── model.h5              # Saved trained model
│
├── requirements.txt
└── README.md

🧰 Technologies Used

Python 3.x

TensorFlow / Keras

NumPy

Pygame

MNIST Dataset

🔧 Installation & Setup
1. Clone the repository
git clone https://github.com/<your-username>/Digit-Recognition-CNN.git
cd Digit-Recognition-CNN

2. Create a virtual environment (recommended)
python -m venv venv


Activate environment:

Windows

venv\Scripts\activate


Mac / Linux

source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

📚 Train the CNN (Optional)

If you want to retrain the model:

cd model
python model.py


This will generate a new:

model/model.h5

🎮 Run the Digit Recognition App
cd app
python recognition.py


A Pygame window will open — draw a digit and click Classify to get prediction.

🧠 How the Model Works

User draws a digit on a 300×300 canvas

Image is converted to grayscale

Rotated and flipped to match MNIST format

Downsampled to 28×28

Normalized (0–1)

Passed to CNN

CNN outputs probability distribution (0–9)

📈 Model Performance

Trained on MNIST dataset:

✅ ~99% Training Accuracy

✅ 98–99% Validation Accuracy

🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

📜 License

This project is open-source and free for personal or academic use.

👤 Author

Sidhardha Varma
Passionate about AI, Deep Learning, and real-world ML projects.