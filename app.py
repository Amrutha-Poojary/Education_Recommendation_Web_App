import streamlit as st
import pickle
import pandas as pd

# Load models
encoder = pickle.load(open("models/encoder.pkl", 'rb'))
scaler = pickle.load(open("models/scaler.pkl", 'rb'))
model_rfc = pickle.load(open("models/model_rfc.pkl", 'rb'))

# Career map with emojis
career_aspiration_map = {
    0: '👨‍💻 Software Engineer', 1: '💼 Business Owner', 2: '❓ Unknown', 3: '🏦 Banker',
    4: '⚖️ Lawyer', 5: '📊 Accountant', 6: '🩺 Doctor', 7: '🏘️ Real Estate Developer',
    8: '📈 Stock Investor', 9: '🏗️ Construction Engineer', 10: '🎨 Artist',
    11: '🕹️ Game Developer', 12: '🏛️ Government Officer', 13: '👩‍🏫 Teacher',
    14: '🖌️ Designer', 15: '🔬 Scientist', 16: '✍️ Writer'
}

# Motivational quotes
career_quotes = {
    "👨‍💻 Software Engineer": "Build the future, one line of code at a time.",
    "🩺 Doctor": "Your hands will heal lives.",
    "👩‍🏫 Teacher": "You shape the minds of tomorrow.",
    "🔬 Scientist": "Explore the unknown and challenge the impossible.",
    "🎨 Artist": "Paint the world with your imagination.",
    "🕹️ Game Developer": "Create worlds people will escape to.",
    "💼 Business Owner": "Lead with vision, grow with passion.",
    "✍️ Writer": "Turn your thoughts into timeless words.",
    "🏘️ Real Estate Developer": "Build dreams from the ground up.",
    "🏛️ Government Officer": "Serve the nation with pride.",
    "📊 Accountant": "Numbers are your second language.",
    "🏦 Banker": "Power the economy with your insight.",
    "📈 Stock Investor": "Risk-taker. Visionary. Wealth creator.",
    "🏗️ Construction Engineer": "Design strong foundations for generations.",
    "🖌️ Designer": "Turn creativity into functionality.",
    "⚖️ Lawyer": "Voice of justice and defender of truth.",
    "❓ Unknown": "Keep learning. Your path will emerge."
}

# Prediction function
def predict_career(gender, part_time_job, absence_days, extracurricular_activities, weekly_self_study_hours,
                   math_score, history_score, physics_score, chemistry_score, biology_score, english_score,
                   geography_score, total_score, average_score):
    
    input_data = pd.DataFrame([[gender, part_time_job, absence_days, extracurricular_activities,
                                weekly_self_study_hours, math_score, history_score, physics_score,
                                chemistry_score, biology_score, english_score, geography_score,
                                total_score, average_score]],
                              columns=['gender', 'part_time_job', 'absence_days', 'extracurricular_activities',
                                       'weekly_self_study_hours', 'math_score', 'history_score', 'physics_score',
                                       'chemistry_score', 'biology_score', 'english_score', 'geography_score',
                                       'total_score', 'average_score'])
    
    # Encode categorical
    input_data['gender'] = encoder.transform(input_data['gender'])
    input_data['part_time_job'] = encoder.transform(input_data['part_time_job'])
    input_data['extracurricular_activities'] = encoder.transform(input_data['extracurricular_activities'])

    # Scale numeric
    input_data[['absence_days', 'weekly_self_study_hours', 'math_score', 'history_score',
                'physics_score', 'chemistry_score', 'biology_score',
                'english_score', 'geography_score']] = scaler.transform(
        input_data[['absence_days', 'weekly_self_study_hours', 'math_score', 'history_score',
                    'physics_score', 'chemistry_score', 'biology_score',
                    'english_score', 'geography_score']])
    
    result = model_rfc.predict(input_data)
    return career_aspiration_map[result[0]]

# Streamlit UI
st.set_page_config(page_title="Career Aspiration Predictor", layout="centered")
st.markdown("<h1 style='text-align: center; color: #4CAF50;'>🎯 Career Aspiration Predictor</h1>", unsafe_allow_html=True)
st.markdown("#### Enter your academic and personal background to see your predicted career path.")

# Personal background inputs
st.markdown("###  Personal & Background Info")
col1, col2 = st.columns(2)
with col1:
    gender = st.selectbox("Gender", ['male', 'female'])
    part_time_job = st.selectbox("Part-time Job", ['Yes', 'No'])
with col2:
    extracurricular_activities = st.selectbox("Extracurricular Activities", ['Yes', 'No'])
    absence_days = st.slider("Absence Days", 0, 30, 2)

# Academic scores
st.markdown("### 📚 Academic Scores ")
col3, col4 = st.columns(2)
with col3:
    math_score = st.number_input("Math", 0, 100, 80)
    physics_score = st.number_input("Physics", 0, 100, 75)
    chemistry_score = st.number_input("Chemistry", 0, 100, 70)
    biology_score = st.number_input("Biology", 0, 100, 85)

with col4:
    history_score = st.number_input("History", 0, 100, 90)
    english_score = st.number_input("English", 0, 100, 95)
    geography_score = st.number_input("Geography", 0, 100, 88)
    weekly_self_study_hours = st.slider("Weekly Self Study Hours", 0, 40, 10)

# Calculate scores
subject_scores = [math_score, history_score, physics_score, chemistry_score, biology_score, english_score, geography_score]
total_score = sum(subject_scores)
average_score = round(total_score / len(subject_scores), 2)

# Centered Score Summary
st.markdown("<h3 style='text-align: center;'>📊 Score Summary</h3>", unsafe_allow_html=True)
center_col = st.columns(3)
with center_col[1]:
    st.metric(label="Total Score", value=total_score)
    st.metric(label="Average Score", value=average_score)

# Predict button
if st.button("🔍 Predict Career"):
    # Convert Yes/No to model-expected format
    part_time_job_input = 'True' if part_time_job == 'Yes' else 'False'
    extra_activities_input = 'True' if extracurricular_activities == 'Yes' else 'False'

    prediction = predict_career(
        gender, part_time_job_input, absence_days, extra_activities_input,
        weekly_self_study_hours, math_score, history_score, physics_score,
        chemistry_score, biology_score, english_score, geography_score,
        total_score, average_score
    )

    # Pretty prediction box
    st.markdown(
        f"""
        <div style='
            background: linear-gradient(to right, #e0f2f1, #b2dfdb);
            border-radius: 16px;
            padding: 30px 20px;
            margin-top: 30px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.15);
        '>
            <h2 style='color:#00695c; text-align:center; font-size:28px; margin-bottom:10px;'>🎓 <strong>{prediction}</strong></h2>
            <p style='font-size:17px; color:#333; text-align:center; font-style: italic;'>
                {career_quotes.get(prediction, "Your future is bright—keep exploring!")}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )
