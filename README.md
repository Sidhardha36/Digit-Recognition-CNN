# Handwritten Digit Recognition (CNN + Pygame UI)

This project is an interactive **digit recognition application** where users can draw digits (0–9) on a canvas, and a trained **Convolutional Neural Network (CNN)** predicts the number in real-time.

It combines:
- **TensorFlow/Keras** → Deep learning model  
- **Pygame** → Drawing & UI  
- **MNIST Dataset** → Training data  

---

## 🚀 Features

- 🎨 Draw digits on a canvas  
- ⚡ Real-time CNN prediction  
- 🔄 Reset button to clear canvas  
- 🖥️ Clean and modern UI  
- 💡 Easy to extend and customize  
- 📦 Well-organized, production-ready structure  

---

## 📂 Project Structure

Digit-Recognition/
│── app/
│   └── recognition.py        # Pygame UI for drawing and prediction
│
│── model/
│   ├── model.py              # Script to train the CNN
│   └── model.h5              # Saved CNN model
│
├── requirements.txt
└── README.md




## 🧰 Technologies Used

- Python 3.x  
- TensorFlow / Keras  
- NumPy  
- Pygame  
- MNIST Dataset  



## 🔧 Installation & Setup

## 1. Clone the repository
git clone https://github.com/<your-username>/Digit-Recognition-CNN.git
cd Digit-Recognition-CNN

## 2. Create a virtual environment (recommended)
python -m venv venv

For Windows
venv\Scripts\activate
For Mac / Linux
source venv/bin/activate

## 3. Install dependencies
pip install -r requirements.txt

## Train the CNN (Optional)
If you want to retrain the model:
cd model
python model.py
This will generate:
model/model.h5
🎮 Run the Digit Recognition App
cd app
python recognition.py
A window will open where you can draw digits and get predictions.

## How the Model Works:

User draws a digit on a 300×300 canvas
Image is:
1.Converted to grayscale
2.Orientation fixed
3.Resized to 28×28 pixels
4.Input is normalized and passed to the CNN
5.Model outputs prediction (0–9)

## 📈 Model Performance
Trained on MNIST dataset with:

-99% Training Accuracy
-98–99% Validation Accuracy

## 🤝 Contributing
Contributions are welcome!
Feel free to open issues or submit pull requests.

## 📜 License
This project is open-source and free for personal or academic use.

## 👤 Author
Sidhardha Varma
Passionate about AI, Deep Learning.