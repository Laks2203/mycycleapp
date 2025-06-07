import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title="MyCycle - PCOS Tracker", layout="centered")

# --- Title and Description ---
st.title("MyCycle")
st.write("_Your personal PCOS & menstrual health tracker._")


import streamlit as st

# Custom style for rectangular background
st.markdown("""
    <style>
    .name-input {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #d3d3d3;
        width: 100%;
        margin-bottom: 10px;
    }
    .input-label {
        font-weight: 600;
        font-size: 16px;
        color: #333;
    }
    </style>
""", unsafe_allow_html=True)

# Label and input field
st.markdown('<div class="input-label">Your Name</div>', unsafe_allow_html=True)
user_name = st.text_input("", key="user_name", placeholder="Enter your name", label_visibility="collapsed")

# Display for testing
# st.write("You entered:", user_name)
if st.button("Submit"):
    if user_name:
        st.success(f"Welcome, {user_name}!")
    else:
        st.warning("Please enter your name.")

# --- Age Input ---
age = st.number_input("Enter Your Age", min_value=10, max_value=100, step=1, help="Enter your age in years")

# --- Symptom Tracker ---
st.header("Select Your Symptoms Today:")
symptom_options = ["Acne", "Fatigue", "Mood Swings", "Hair Loss", "Bloating"]
selected_symptoms = st.multiselect("Click to select symptoms", symptom_options)

# --- Mood Tracker ---
st.header("How Are You Feeling?")
moods = {
    "Happy": "😊",
    "Sad": "😔",
    "Angry": "😡",
    "Tired": "😴"
}
col1, col2, col3, col4 = st.columns(4)
selected_mood = None
if col1.button(moods["Happy"]):
    selected_mood = "Happy"
if col2.button(moods["Sad"]):
    selected_mood = "Sad"
if col3.button(moods["Angry"]):
    selected_mood = "Angry"
if col4.button(moods["Tired"]):
    selected_mood = "Tired"

if selected_mood:
    st.success(f"Mood selected: {selected_mood}")

# --- Mood Diagnostic Images and Info ---
st.header("How Is Your Mind Today?")
st.write("Select what you're experiencing to get insights")

# For images, use placeholder URLs or free images from the web
# These URLs should be replaced with your own image URLs or hosted images

mood_images = {
    "Brain Fog": ("https://cdn-icons-png.flaticon.com/512/2933/2933180.png", "Brain Fog"),
    "Fatigue": ("https://cdn-icons-png.flaticon.com/512/2917/2917990.png", "Fatigue"),
    "Irritability": ("https://cdn-icons-png.flaticon.com/512/1828/1828843.png", "Irritability"),
    "Anxiety": ("https://cdn-icons-png.flaticon.com/512/2917/2917991.png", "Anxiety"),
    "Calm": ("https://cdn-icons-png.flaticon.com/512/616/616408.png", "Calm")
}

mood_selected = st.radio(
    "Pick a mood symptom for insights",
    options=list(mood_images.keys()),
    format_func=lambda x: f"{mood_images[x][1]}"
)

if mood_selected:
    st.image(mood_images[mood_selected][0], width=100)
    mood_diagnostics = {
        "Brain Fog": "Brain fog can be a result of hormonal imbalance in PCOS. Ensure proper sleep, hydration, and omega-3 intake.",
        "Fatigue": "Chronic fatigue is often tied to insulin resistance or cortisol spikes in PCOS. Try mindful rest and protein-rich meals.",
        "Irritability": "Mood swings and irritability may increase around ovulation or luteal phase. Track hormone shifts closely.",
        "Anxiety": "PCOS is linked with higher cortisol levels. Deep breathing, magnesium, and journaling help calm anxiety.",
        "Calm": "You're in a good space! Keeping your hormones in check with healthy habits supports mental clarity."
    }
    st.info(f"🧬 Diagnostic Insight: {mood_diagnostics[mood_selected]}")

# --- Get Diagnostic Suggestion ---
if st.button("Get Diagnostic Suggestion"):
    suggestion = ""

    if not age or age < 10 or age > 100:
        st.error("Please enter a valid age to get a proper suggestion.")
    else:
        isPreMenopause = age < 45
        isPostMenopause = age >= 45

        if "Mood Swings" in selected_symptoms and selected_mood == "Angry":
            suggestion += "Frequent mood swings and irritability may suggest hormonal imbalances. "
            suggestion += ("You might be experiencing fluctuations related to PCOS or stress."
                           if isPreMenopause else
                           "Post-menopause, mood changes may indicate estrogen drop or thyroid issues. ")

        if "Fatigue" in selected_symptoms:
            suggestion += " Persistent fatigue can be linked to insulin resistance or sleep disruptions common in PCOS. "

        if "Hair Loss" in selected_symptoms:
            suggestion += " Hair loss may be due to elevated androgens, a common symptom in PCOS."

        if suggestion == "":
            suggestion = "Your selected mood and symptoms don't show major concerns, but continue regular tracking!"

        st.markdown(f"### Health Insight:\n{suggestion}")

# --- Period Prediction ---
st.header("📅 Predict Your Cycle")
last_period_date = st.date_input("Enter your last period start date")
cycle_length = st.number_input("Cycle length (days)", min_value=20, max_value=40, value=28, step=1)

if st.button("Predict Next Cycle"):
    if not last_period_date or not cycle_length:
        st.error("Please enter a valid date and cycle length (20–40 days).")
    else:
        next_period = last_period_date + timedelta(days=cycle_length)
        ovulation = last_period_date + timedelta(days=(cycle_length - 14))
        today = datetime.today().date()
        days_since_last = (today - last_period_date).days

        if days_since_last < (cycle_length - 14):
            phase = "Follicular Phase"
        elif days_since_last == (cycle_length - 14):
            phase = "Ovulation Day!"
        else:
            phase = "Luteal Phase"

        st.markdown(f"""
        🩸 **Next Period Start:** {next_period.strftime('%a, %b %d, %Y')}  
        💡 **Estimated Ovulation:** {ovulation.strftime('%a, %b %d, %Y')}  
        🔄 **Current Phase:** {phase}
        """)

st.header ('Did You Know?')
st.write('PCOS is a major determinant of cognitive decline in women post menopause and can lead towards further progression in neurodegenerative diseases.')
st.write('Managing PCOS effectively can help mitigate these risks.')
# --- Daily Tip ---
if st.button("Get a Daily Health Tip"):
    st.info("Tip: Drink spearmint tea daily to help manage PCOS symptoms.")

# --- Cycle Progress Bar (simulate 60% progress) ---
st.header("Cycle Progress")
progress_value = 0.6
st.progress(progress_value)

# --- Footer ---
st.markdown("""
---
&copy; 2025 MyCycle App | Made with 💖 for women's health
""")
