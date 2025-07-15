

# 🩺 Multiple Disease Prediction System using Machine Learning

This project is a **Streamlit-based web application** that allows users to predict **Diabetes** and **Heart Disease** risks using pre-trained Machine Learning models.

## 🚀 Features

- 🔍 **Diabetes Prediction** using key health metrics like:
  - Pregnancies
  - Glucose
  - Blood Pressure
  - Skin Thickness
  - Insulin
  - BMI
  - Diabetes Pedigree Function
  - Age

- ❤️ **Heart Disease Prediction** using metrics such as:
  - Age, Sex, Chest Pain Type
  - Blood Pressure, Cholesterol
  - Fasting Blood Sugar
  - Resting ECG, Max Heart Rate
  - Exercise Induced Angina
  - ST Depression, Slope, CA, Thal

- 🖱️ Simple and interactive UI using **Streamlit**
- 📦 Models are loaded from `.sav` files via `pickle`

## 📁 Project Structure

```
.
├── mpwb.py                  # Main Streamlit application
├── trained_model.sav        # Diabetes prediction model
├── heart_model (4).sav      # Heart disease prediction model
├── requirements.txt         # Python dependencies
```

## ▶️ How to Run

1. Clone this repository:
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:
```bash
streamlit run mpwb.py
```

## 📦 Dependencies

- `streamlit`
- `pickle`
- `streamlit-option-menu`
- `scikit-learn` (for training and saving models)

Make sure your `requirements.txt` includes:
```txt
streamlit
streamlit-option-menu
scikit-learn
```

## 🧠 Models

Models were trained offline and saved using `pickle`. You can retrain and update them with your own datasets as needed.

## 📸 Screenshots

*(Optional: Include UI screenshots here for better presentation.)*

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
