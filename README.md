# 🎯 Career Aspiration Predictor

Welcome to the **Career Aspiration Predictor** web application! 🚀 This app uses machine learning to predict a student’s most suitable career path based on their academic performance and personal background.

## 📌 Features

- 🎓 Predicts the most suitable career from 17+ options
- 📊 Uses student subject scores and other factors
- ✨ Interactive and user-friendly UI with Streamlit
- 💡 Motivational quotes for every predicted career
- 📈 Beautifully designed score summary dashboard

## 🧠 How It Works

1. 📝The user inputs :
   - Gender
   - Part-time job status
   - Absence days
   - Extracurricular activities
   - Weekly self-study hours
   - Scores in 7 subjects 📚

2. The model :
   - Applies encoding & scaling 🔁
   - Uses a trained Random Forest Classifier 🌲
   - Predicts the most likely career path 👨‍💻👩‍🏫🧑‍🔬

3. The app :
   - Displays your career with quote 🎉
   - Summarizes your total and average scores in a neat layout 📈

## 🛠️ Tech stack

| 🛠️ **Tool/Library**      | 🎯 **Purpose**                              |
| ------------------------- | ------------------------------------------- |
| 🌐 **Streamlit**          | Interactive web UI for recommendations      |
| 🐼 **Pandas**             | Data loading, cleaning & manipulation       |
| 📚 **Scikit-learn**       | Model training & evaluation (ML algorithms) |
| 🧺 **Pickle**             | Saving and loading trained models           |
| 📊 **CSV** (Dataset)      | Contains student features and preferences   |


## 🚀 How to Run

1. Clone the repository :

        git clone https://github.com/Amrutha-Poojary/Education_Recommendation_Web_App.git
2. Install dependencies :

       pip install streamlit pandas scikit-learn

3. Run the app :

        streamlit run app.py

## 🏷️ Conclusion
This project provides a user-friendly interface to help students reflect on potential career paths based on academic data. It combines machine learning, education insights, and creative UI to make the experience both informative and motivating.

