# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd
# import sys, os

# sys.path.insert(0, os.path.dirname(__file__))
# from src.explainer import explain

# st.set_page_config(page_title="MediScan AI", page_icon="🧬", layout="centered")

# # ── SYMPTOM TRANSLATIONS (Tamil) ──────────────────────
# SYMPTOM_TA = {
#     'abdominal_pain': 'வயிற்று வலி',
#     'abnormal_menstruation': 'அசாதாரண மாதவிடாய்',
#     'acidity': 'அமிலத்தன்மை',
#     'acute_liver_failure': 'கடுமையான கல்லீரல் செயலிழப்பு',
#     'altered_sensorium': 'மாற்றப்பட்ட உணர்வு நிலை',
#     'anxiety': 'கவலை',
#     'back_pain': 'முதுகு வலி',
#     'belly_pain': 'வயிற்று வலி',
#     'blackheads': 'கரும்புள்ளிகள்',
#     'bladder_discomfort': 'சிறுநீர்ப்பை அசௌகரியம்',
#     'blister': 'கொப்புளம்',
#     'blood_in_sputum': 'சளியில் இரத்தம்',
#     'bloody_stool': 'இரத்தம் கலந்த மலம்',
#     'blurred_and_distorted_vision': 'மங்கலான மற்றும் திரிந்த பார்வை',
#     'breathlessness': 'மூச்சுத் திணறல்',
#     'brittle_nails': 'உடையும் நகங்கள்',
#     'bruising': 'சிராய்ப்பு',
#     'burning_micturition': 'எரிச்சலுடன் சிறுநீர் கழித்தல்',
#     'chest_pain': 'நெஞ்சு வலி',
#     'chills': 'குளிர் நடுக்கம்',
#     'cold_hands_and_feets': 'கை மற்றும் கால் குளிர்ச்சி',
#     'coma': 'கோமா',
#     'congestion': 'மூக்கடைப்பு',
#     'constipation': 'மலச்சிக்கல்',
#     'continuous_feel_of_urine': 'தொடர்ச்சியான சிறுநீர் உணர்வு',
#     'continuous_sneezing': 'தொடர்ச்சியான தும்மல்',
#     'cough': 'இருமல்',
#     'cramps': 'தசைப்பிடிப்பு',
#     'dark_urine': 'அடர் நிற சிறுநீர்',
#     'dehydration': 'நீர்ச்சத்து குறைபாடு',
#     'depression': 'மனச்சோர்வு',
#     'diarrhoea': 'வயிற்றுப்போக்கு',
#     'dischromic _patches': 'நிற மாற்றப் புள்ளிகள்',
#     'distention_of_abdomen': 'வயிறு உப்புசம்',
#     'dizziness': 'தலை சுற்றல்',
#     'drying_and_tingling_lips': 'உதடுகள் உலர்வு மற்றும் கூச்சம்',
#     'enlarged_thyroid': 'விரிந்த தைரொய்டு',
#     'excessive_hunger': 'அதிகப்படியான பசி',
#     'extra_marital_contacts': 'திருமண வெளி தொடர்புகள்',
#     'family_history': 'குடும்ப வரலாறு',
#     'fast_heart_rate': 'வேகமான இதய துடிப்பு',
#     'fatigue': 'சோர்வு',
#     'fluid_overload': 'திரவ அதிகளவு',
#     'foul_smell_of urine': 'சிறுநீரின் துர்நாற்றம்',
#     'headache': 'தலைவலி',
#     'high_fever': 'அதிக காய்ச்சல்',
#     'hip_joint_pain': 'இடுப்பு மூட்டு வலி',
#     'history_of_alcohol_consumption': 'மது அருந்திய வரலாறு',
#     'increased_appetite': 'அதிகரித்த பசி',
#     'indigestion': 'அஜீரணம்',
#     'inflammatory_nails': 'அழற்சியுள்ள நகங்கள்',
#     'internal_itching': 'உள் அரிப்பு',
#     'irregular_sugar_level': 'ஒழுங்கற்ற சர்க்கரை அளவு',
#     'irritability': 'எரிச்சல்',
#     'irritation_in_anus': 'ஆசனவாயில் எரிச்சல்',
#     'itching': 'அரிப்பு',
#     'joint_pain': 'மூட்டு வலி',
#     'knee_pain': 'முழங்கால் வலி',
#     'lack_of_concentration': 'கவனக்குறைவு',
#     'lethargy': 'சுணக்கம்',
#     'loss_of_appetite': 'பசியின்மை',
#     'loss_of_balance': 'சமநிலை இழப்பு',
#     'loss_of_smell': 'மணம் உணரும் திறன் இழப்பு',
#     'malaise': 'உடல் நலக்குறைவு',
#     'mild_fever': 'லேசான காய்ச்சல்',
#     'mood_swings': 'மனநிலை மாற்றங்கள்',
#     'movement_stiffness': 'நகர்வு விறைப்பு',
#     'mucoid_sputum': 'சளி நிறைந்த சளி',
#     'muscle_pain': 'தசை வலி',
#     'muscle_wasting': 'தசை அழிவு',
#     'muscle_weakness': 'தசை பலவீனம்',
#     'nausea': 'குமட்டல்',
#     'neck_pain': 'கழுத்து வலி',
#     'nodal_skin_eruptions': 'முடிச்சு தோல் வெடிப்புகள்',
#     'obesity': 'உடல் பருமன்',
#     'pain_behind_the_eyes': 'கண்களுக்கு பின் வலி',
#     'pain_during_bowel_movements': 'மலம் கழிக்கும் போது வலி',
#     'pain_in_anal_region': 'ஆசன வாய் பகுதியில் வலி',
#     'painful_walking': 'வலியுடன் நடத்தல்',
#     'palpitations': 'படபடப்பு',
#     'passage_of_gases': 'வாயு வெளியேற்றம்',
#     'patches_in_throat': 'தொண்டையில் புள்ளிகள்',
#     'phlegm': 'சளி',
#     'polyuria': 'அதிக சிறுநீர் கழித்தல்',
#     'prominent_veins_on_calf': 'கன்னலில் நரம்புகள் தெரிதல்',
#     'puffy_face_and_eyes': 'முகம் மற்றும் கண்கள் வீக்கம்',
#     'pus_filled_pimples': 'சீழ் நிறைந்த பருக்கள்',
#     'receiving_blood_transfusion': 'இரத்தமாற்றம் பெறுதல்',
#     'receiving_unsterile_injections': 'கிருமி நீக்கமற்ற ஊசி பெறுதல்',
#     'red_sore_around_nose': 'மூக்கைச் சுற்றி சிவந்த புண்',
#     'red_spots_over_body': 'உடலில் சிவந்த புள்ளிகள்',
#     'redness_of_eyes': 'கண்கள் சிவத்தல்',
#     'restlessness': 'அமைதியின்மை',
#     'runny_nose': 'மூக்கு ஒழுகுதல்',
#     'rusty_sputum': 'துரு நிற சளி',
#     'scurring': 'தழும்பு',
#     'shivering': 'நடுக்கம்',
#     'silver_like_dusting': 'வெள்ளி போன்ற தூசு',
#     'sinus_pressure': 'சைனஸ் அழுத்தம்',
#     'skin_peeling': 'தோல் உரிதல்',
#     'skin_rash': 'தோல் தடிப்பு',
#     'slurred_speech': 'தடுமாறும் பேச்சு',
#     'small_dents_in_nails': 'நகங்களில் சிறிய குழிகள்',
#     'spinning_movements': 'சுழலும் உணர்வு',
#     'spotting_ urination': 'துளி சிறுநீர் கழித்தல்',
#     'stiff_neck': 'கழுத்து விறைப்பு',
#     'stomach_bleeding': 'வயிற்று இரத்தப்போக்கு',
#     'stomach_pain': 'வயிற்று வலி',
#     'sunken_eyes': 'கண்கள் உள்ளே சென்றிருத்தல்',
#     'sweating': 'வியர்வை',
#     'swelled_lymph_nodes': 'நிணநீர் முனைகள் வீக்கம்',
#     'swelling_joints': 'மூட்டுகள் வீக்கம்',
#     'swelling_of_stomach': 'வயிறு வீக்கம்',
#     'swollen_blood_vessels': 'இரத்த நாளங்கள் வீக்கம்',
#     'swollen_extremeties': 'கைகால்கள் வீக்கம்',
#     'swollen_legs': 'கால்கள் வீக்கம்',
#     'throat_irritation': 'தொண்டை எரிச்சல்',
#     'toxic_look_(typhos)': 'நச்சு தோற்றம் (டைபஸ்)',
#     'ulcers_on_tongue': 'நாக்கில் புண்கள்',
#     'unsteadiness': 'தளர்வான நடை',
#     'visual_disturbances': 'பார்வை இடையூறுகள்',
#     'vomiting': 'வாந்தி',
#     'watering_from_eyes': 'கண்ணீர் வடிதல்',
#     'weakness_in_limbs': 'கைகால்களில் பலவீனம்',
#     'weakness_of_one_body_side': 'உடலின் ஒரு பக்கம் பலவீனம்',
#     'weight_gain': 'எடை அதிகரிப்பு',
#     'weight_loss': 'எடை குறைப்பு',
#     'yellow_crust_ooze': 'மஞ்சள் நிற மேல் படிவம்',
#     'yellow_urine': 'மஞ்சள் சிறுநீர்',
#     'yellowing_of_eyes': 'கண்கள் மஞ்சளாதல்',
#     'yellowish_skin': 'மஞ்சள் தோல்',
# }

# # ── TRANSLATIONS ───────────────────────────────────────
# T = {
#     "en": {
#         "tagline": "AI-POWERED DIAGNOSTICS",
#         "hero_sub": "Advanced symptom analysis using machine learning — trained on thousands of clinical cases to help you understand what your body might be telling you.",
#         "stat1_label": "Diseases Detected",
#         "stat2_label": "Symptom Inputs",
#         "stat3_label": "Model Accuracy",
#         "step1": "Profile",
#         "step2": "Age",
#         "step3": "Symptoms",
#         "name_label": "Your full name",
#         "name_placeholder": "e.g. Santhiya S",
#         "continue": "Continue",
#         "back": "← Back",
#         "welcome": "Welcome,",
#         "profile_sub": "Let's build your health profile",
#         "age_heading": "How old are you?",
#         "age_sub": "Age helps our model provide more contextual and accurate predictions.",
#         "age_label": "Your age",
#         "age_placeholder": "e.g. 24",
#         "symptom_greeting_sub": "Select all symptoms you are currently experiencing",
#         "symptom_label": "Current symptoms",
#         "symptom_placeholder": "Search — e.g. fatigue, headache, nausea...",
#         "analyse": "Analyse Symptoms",
#         "results_header": "Analysis results for",
#         "rank1": "#1 Most Likely",
#         "rank2": "#2 Possible",
#         "rank3": "#3 Consider",
#         "diag1": "Primary diagnosis",
#         "diag2": "Secondary possibility",
#         "diag3": "Alternative consideration",
#         "shap_title": "Why this was predicted",
#         "legend_pos": "Strongly linked to diagnosis",
#         "legend_neg": "Not typical for this condition",
#         "disclaimer": "⚠ For educational purposes only. Not a substitute for professional medical advice. Always consult a licensed physician.",
#         "warn_name": "Please enter your name to continue.",
#         "warn_age": "Please enter a valid age.",
#         "warn_symptom": "Please select at least one symptom.",
#         "no_desc": "No clinical description available.",
#         "lang_label": "Language",
#     },
#     "ta": {
#         "tagline": "செயற்கை நுண்ணறிவு நோயறிதல்",
#         "hero_sub": "இயந்திர கற்றல் தொழில்நுட்பம் மூலம் அறிகுறிகளை ஆய்வு செய்து, உங்கள் உடல் என்ன சொல்கிறது என்பதை புரிந்துகொள்ள உதவுகிறோம்.",
#         "stat1_label": "கண்டறியப்பட்ட நோய்கள்",
#         "stat2_label": "அறிகுறி உள்ளீடுகள்",
#         "stat3_label": "மாதிரி துல்லியம்",
#         "step1": "சுயவிவரம்",
#         "step2": "வயது",
#         "step3": "அறிகுறிகள்",
#         "name_label": "உங்கள் முழு பெயர்",
#         "name_placeholder": "எ.கா. சந்தியா ச",
#         "continue": "தொடரவும்",
#         "back": "← திரும்பு",
#         "welcome": "வணக்கம்,",
#         "profile_sub": "உங்கள் உடல்நல சுயவிவரத்தை உருவாக்குவோம்",
#         "age_heading": "உங்களுக்கு எத்தனை வயது?",
#         "age_sub": "வயது தகவல் மூலம் எங்கள் மாதிரி மிகவும் துல்லியமான முடிவுகளை வழங்க முடியும்.",
#         "age_label": "உங்கள் வயது",
#         "age_placeholder": "எ.கா. 24",
#         "symptom_greeting_sub": "நீங்கள் தற்போது அனுபவிக்கும் அறிகுறிகளை தேர்ந்தெடுக்கவும்",
#         "symptom_label": "தற்போதைய அறிகுறிகள்",
#         "symptom_placeholder": "தேடவும் — எ.கா. சோர்வு, தலைவலி, குமட்டல்...",
#         "analyse": "அறிகுறிகளை பகுப்பாய்வு செய்",
#         "results_header": "பகுப்பாய்வு முடிவுகள் —",
#         "rank1": "#1 மிகவும் சாத்தியம்",
#         "rank2": "#2 சாத்தியம்",
#         "rank3": "#3 கருத்தில் கொள்க",
#         "diag1": "முதன்மை நோயறிதல்",
#         "diag2": "இரண்டாம் நிலை சாத்தியம்",
#         "diag3": "மாற்று கருத்து",
#         "shap_title": "இந்த முடிவு ஏன் வந்தது",
#         "legend_pos": "நோயறிதலுடன் வலுவாக தொடர்புடையது",
#         "legend_neg": "இந்த நிலைக்கு வழக்கமற்றது",
#         "disclaimer": "⚠ கல்வி நோக்கங்களுக்காக மட்டுமே. தொழில்முறை மருத்துவ ஆலோசனைக்கு மாற்றாகாது. எப்போதும் தகுதிவாய்ந்த மருத்துவரை அணுகவும்.",
#         "warn_name": "தொடர உங்கள் பெயரை உள்ளிடவும்.",
#         "warn_age": "சரியான வயதை உள்ளிடவும்.",
#         "warn_symptom": "குறைந்தது ஒரு அறிகுறியையாவது தேர்ந்தெடுக்கவும்.",
#         "no_desc": "இந்த நிலைக்கு மருத்துவ விளக்கம் கிடைக்கவில்லை.",
#         "lang_label": "மொழி",
#     }
# }

# # ── Session state ──────────────────────────────────────
# for k, v in [("step", 1), ("name", ""), ("age", ""), ("lang", "en")]:
#     if k not in st.session_state:
#         st.session_state[k] = v

# lang = st.session_state.lang
# tx = T[lang]

# # ── Build symptom display options based on language ────
# ALL_SYMPTOMS_EN = sorted([
#     'abdominal_pain','abnormal_menstruation','acidity','acute_liver_failure',
#     'altered_sensorium','anxiety','back_pain','belly_pain','blackheads',
#     'bladder_discomfort','blister','blood_in_sputum','bloody_stool',
#     'blurred_and_distorted_vision','breathlessness','brittle_nails','bruising',
#     'burning_micturition','chest_pain','chills','cold_hands_and_feets','coma',
#     'congestion','constipation','continuous_feel_of_urine','continuous_sneezing',
#     'cough','cramps','dark_urine','dehydration','depression','diarrhoea',
#     'dischromic _patches','distention_of_abdomen','dizziness',
#     'drying_and_tingling_lips','enlarged_thyroid','excessive_hunger',
#     'extra_marital_contacts','family_history','fast_heart_rate','fatigue',
#     'fluid_overload','foul_smell_of urine','headache','high_fever',
#     'hip_joint_pain','history_of_alcohol_consumption','increased_appetite',
#     'indigestion','inflammatory_nails','internal_itching','irregular_sugar_level',
#     'irritability','irritation_in_anus','itching','joint_pain','knee_pain',
#     'lack_of_concentration','lethargy','loss_of_appetite','loss_of_balance',
#     'loss_of_smell','malaise','mild_fever','mood_swings','movement_stiffness',
#     'mucoid_sputum','muscle_pain','muscle_wasting','muscle_weakness','nausea',
#     'neck_pain','nodal_skin_eruptions','obesity','pain_behind_the_eyes',
#     'pain_during_bowel_movements','pain_in_anal_region','painful_walking',
#     'palpitations','passage_of_gases','patches_in_throat','phlegm','polyuria',
#     'prominent_veins_on_calf','puffy_face_and_eyes','pus_filled_pimples',
#     'receiving_blood_transfusion','receiving_unsterile_injections',
#     'red_sore_around_nose','red_spots_over_body','redness_of_eyes','restlessness',
#     'runny_nose','rusty_sputum','scurring','shivering','silver_like_dusting',
#     'sinus_pressure','skin_peeling','skin_rash','slurred_speech',
#     'small_dents_in_nails','spinning_movements','spotting_ urination','stiff_neck',
#     'stomach_bleeding','stomach_pain','sunken_eyes','sweating',
#     'swelled_lymph_nodes','swelling_joints','swelling_of_stomach',
#     'swollen_blood_vessels','swollen_extremeties','swollen_legs',
#     'throat_irritation','toxic_look_(typhos)','ulcers_on_tongue','unsteadiness',
#     'visual_disturbances','vomiting','watering_from_eyes','weakness_in_limbs',
#     'weakness_of_one_body_side','weight_gain','weight_loss','yellow_crust_ooze',
#     'yellow_urine','yellowing_of_eyes','yellowish_skin'
# ])

# # For Tamil: show Tamil label but value is still the English key (for model)
# if lang == "ta":
#     SYMPTOM_OPTIONS = {SYMPTOM_TA.get(s, s.replace('_', ' ')): s for s in ALL_SYMPTOMS_EN}
#     SYMPTOM_DISPLAY_LIST = sorted(SYMPTOM_OPTIONS.keys())
# else:
#     SYMPTOM_OPTIONS = {s: s for s in ALL_SYMPTOMS_EN}
#     SYMPTOM_DISPLAY_LIST = ALL_SYMPTOMS_EN

# st.markdown("""
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=DM+Serif+Display:ital@0;1&display=swap');

# *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
# html, body, .stApp { background: #07090f !important; color: #dde1f0; font-family: 'Sora', sans-serif; }
# #MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
# .block-container { padding: 0 1rem !important; max-width: 760px !important; margin: 0 auto !important; }
# section[data-testid="stSidebar"] { display: none; }

# /* ── BG ORBS ── */
# .orb { position: fixed; border-radius: 50%; filter: blur(100px); pointer-events: none; z-index: 0; }
# .o1 { width:700px;height:700px;background:rgba(56,189,248,0.055);top:-250px;right:-250px; }
# .o2 { width:500px;height:500px;background:rgba(139,92,246,0.045);bottom:-150px;left:-200px; }
# .o3 { width:350px;height:350px;background:rgba(20,184,166,0.035);top:45%;left:25%; }

# /* ── PAGE WRAP ── */
# .pw { position:relative;z-index:1;padding:40px 0 100px; }

# /* ── TOP BAR ── */
# .topbar {
#     display: flex;
#     align-items: center;
#     justify-content: flex-end;
#     margin-bottom: 0px;
#     padding-bottom: 0px;
# }

# /* ── BRAND HEADER (centered) ── */
# .brand-header {
#     text-align: center;
#     padding: 32px 0 20px;
#     margin-bottom: 8px;
# }
# .brand {
#     font-family: 'DM Serif Display', serif;
#     font-size: clamp(3rem, 8vw, 5.5rem);
#     color: #ffffff;
#     letter-spacing: -2px;
#     line-height: 1;
#     margin-bottom: 8px;
# }
# .brand span { color: #7c3aed; }
# .brand-sub {
#     font-size: 0.72rem;
#     letter-spacing: 3px;
#     text-transform: uppercase;
#     color: rgba(124,58,237,0.75);
#     margin-bottom: 20px;
#     font-weight: 500;
# }
# .hero-desc {
#     font-size: 0.97rem;
#     color: rgba(221,225,240,0.5);
#     line-height: 1.8;
#     font-weight: 300;
#     max-width: 520px;
#     margin: 0 auto 0;
# }

# /* ── STATS ── */
# .stats {
#     display: grid;
#     grid-template-columns: repeat(3,1fr);
#     gap: 10px;
#     margin-bottom: 44px;
#     margin-top: 36px;
# }
# .stat {
#     padding: 22px 12px;
#     background: rgba(255,255,255,0.025);
#     border: 1px solid rgba(255,255,255,0.06);
#     border-radius: 20px;
#     text-align: center;
# }
# .stat-n {
#     font-family: 'DM Serif Display', serif;
#     font-size: 2.2rem;
#     color: #fff;
#     line-height: 1;
#     margin-bottom: 6px;
# }
# .stat-n em { font-style: normal; color: #7c3aed; }
# .stat-l { font-size: 0.7rem; color: rgba(221,225,240,0.35); letter-spacing: 0.5px; }

# /* ── STEP PILL ── */
# .spill {
#     display: flex;
#     align-items: center;
#     gap: 4px;
#     background: rgba(255,255,255,0.03);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 100px;
#     padding: 5px;
#     width: fit-content;
#     margin: 0 auto 44px;
# }
# .si {
#     display: flex; align-items: center; gap: 8px;
#     padding: 9px 22px; border-radius: 100px;
#     font-size: 0.78rem; font-weight: 500;
#     color: rgba(255,255,255,0.28);
#     transition: all 0.3s;
#     white-space: nowrap;
# }
# .si.active { background: linear-gradient(135deg,#7c3aed,#a855f7); color:#fff; box-shadow:0 4px 20px rgba(124,58,237,0.3); }
# .si.done { color: #a855f7; }
# .sn {
#     width:20px;height:20px;border-radius:50%;
#     border:1.5px solid currentColor;
#     display:flex;align-items:center;justify-content:center;
#     font-size:0.62rem;flex-shrink:0;
# }
# .si.active .sn { background:rgba(255,255,255,0.22);border-color:white; }

# /* ── GLASS CARD ── */
# .gc {
#     background: rgba(255,255,255,0.028);
#     border: 1px solid rgba(255,255,255,0.07);
#     border-radius: 28px;
#     padding: 40px 44px;
#     margin-bottom: 16px;
# }

# /* ── FORM LABEL ── */
# .fl {
#     font-size: 0.68rem; font-weight: 600;
#     letter-spacing: 1.5px; text-transform: uppercase;
#     color: rgba(221,225,240,0.35); margin-bottom: 10px; display: block;
# }

# /* ── INPUT ── */
# .stTextInput > div > div > input {
#     background: rgba(255,255,255,0.04) !important;
#     border: 1.5px solid rgba(255,255,255,0.08) !important;
#     border-radius: 16px !important;
#     color: #fff !important;
#     font-family: 'Sora', sans-serif !important;
#     font-size: 1.05rem !important;
#     padding: 18px 22px !important;
#     height: auto !important;
#     transition: all 0.25s !important;
#     caret-color: #a855f7 !important;
# }
# .stTextInput > div > div > input:focus {
#     border-color: rgba(168,85,247,0.45) !important;
#     background: rgba(124,58,237,0.04) !important;
#     box-shadow: 0 0 0 4px rgba(124,58,237,0.08) !important;
#     outline: none !important;
# }
# .stTextInput > div > div > input::placeholder { color: rgba(221,225,240,0.18) !important; }
# .stTextInput label { display: none !important; }

# /* ── MULTISELECT ── */
# .stMultiSelect > div > div {
#     background: rgba(255,255,255,0.04) !important;
#     border: 1.5px solid rgba(255,255,255,0.08) !important;
#     border-radius: 16px !important;
#     min-height: 58px !important;
#     transition: all 0.25s !important;
# }
# .stMultiSelect > div > div:focus-within {
#     border-color: rgba(168,85,247,0.45) !important;
#     box-shadow: 0 0 0 4px rgba(124,58,237,0.08) !important;
# }
# .stMultiSelect span[data-baseweb="tag"] {
#     background: rgba(124,58,237,0.15) !important;
#     border: 1px solid rgba(168,85,247,0.3) !important;
#     border-radius: 10px !important;
#     color: #c4b5fd !important;
#     font-size: 0.8rem !important;
# }
# [data-baseweb="select"] input { color: rgba(221,225,240,0.5) !important; font-family: 'Sora',sans-serif !important; }
# [data-baseweb="menu"] {
#     background: #111420 !important;
#     border: 1px solid rgba(255,255,255,0.08) !important;
#     border-radius: 16px !important;
#     box-shadow: 0 20px 60px rgba(0,0,0,0.5) !important;
# }
# [data-baseweb="option"] { color: rgba(221,225,240,0.7) !important; font-family: 'Sora',sans-serif !important; }
# [data-baseweb="option"]:hover { background: rgba(124,58,237,0.1) !important; color: #fff !important; }
# .stMultiSelect label { display: none !important; }

# /* ── BUTTONS — base reset ── */
# .stButton > button {
#     font-family: 'Sora', sans-serif !important;
#     font-weight: 600 !important;
#     font-size: 0.9rem !important;
#     border-radius: 14px !important;
#     padding: 15px 28px !important;
#     border: none !important;
#     transition: all 0.25s ease !important;
#     height: auto !important;
#     letter-spacing: 0.3px !important;
#     width: 100% !important;
# }

# /* Back button — ghost */
# div[data-testid="column"]:first-child .stButton > button {
#     background: rgba(255,255,255,0.05) !important;
#     color: rgba(221,225,240,0.6) !important;
#     border: 1.5px solid rgba(255,255,255,0.1) !important;
# }
# div[data-testid="column"]:first-child .stButton > button:hover {
#     background: rgba(255,255,255,0.09) !important;
#     color: rgba(221,225,240,0.9) !important;
# }

# /* Primary CTA */
# div[data-testid="column"]:last-child .stButton > button {
#     background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
#     color: #fff !important;
#     box-shadow: 0 8px 32px rgba(124,58,237,0.35) !important;
# }
# div[data-testid="column"]:last-child .stButton > button:hover {
#     transform: translateY(-2px) !important;
#     box-shadow: 0 14px 44px rgba(124,58,237,0.48) !important;
# }

# /* Single full-width primary (step 1) */
# div[data-testid="stVerticalBlock"] > div > div > div > div > div:only-child .stButton > button {
#     background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
#     color: #fff !important;
#     box-shadow: 0 8px 32px rgba(124,58,237,0.35) !important;
# }

# /* ── LANGUAGE SELECTBOX — top right ── */
# .lang-wrap { display: flex; justify-content: flex-end; margin-bottom: 16px; }
# .lang-wrap .stSelectbox > div > div {
#     background: rgba(124,58,237,0.1) !important;
#     border: 1.5px solid rgba(168,85,247,0.3) !important;
#     border-radius: 100px !important;
#     color: #c4b5fd !important;
#     font-family: 'Sora', sans-serif !important;
#     font-size: 0.82rem !important;
#     font-weight: 600 !important;
#     min-height: unset !important;
#     padding: 0 !important;
#     width: 160px !important;
#     cursor: pointer !important;
# }
# .lang-wrap .stSelectbox > div > div > div {
#     padding: 8px 18px !important;
#     color: #c4b5fd !important;
# }
# .lang-wrap .stSelectbox svg { fill: #c4b5fd !important; }
# .lang-wrap .stSelectbox label { display: none !important; }
# [data-baseweb="popover"] [data-baseweb="menu"] {
#     background: #1a1030 !important;
#     border: 1px solid rgba(168,85,247,0.25) !important;
#     border-radius: 14px !important;
# }
# [data-baseweb="popover"] [data-baseweb="option"] { color: #c4b5fd !important; font-size: 0.85rem !important; }
# [data-baseweb="popover"] [data-baseweb="option"]:hover { background: rgba(124,58,237,0.15) !important; color: #fff !important; }

# /* ── GREETING ── */
# .greet {
#     display:flex;align-items:center;gap:16px;
#     padding:20px 24px;
#     background:rgba(124,58,237,0.06);
#     border:1px solid rgba(168,85,247,0.12);
#     border-radius:18px;margin-bottom:28px;
# }
# .av {
#     width:50px;height:50px;border-radius:50%;flex-shrink:0;
#     background:linear-gradient(135deg,#7c3aed,#a855f7);
#     display:flex;align-items:center;justify-content:center;
#     font-family:'DM Serif Display',serif;font-size:1.3rem;color:#fff;
# }
# .gn { font-weight:600;color:#fff;font-size:1rem; }
# .gs { font-size:0.82rem;color:rgba(221,225,240,0.4);margin-top:3px; }

# /* ── SECTION HEADING ── */
# .sec-head {
#     font-size:0.68rem;font-weight:600;
#     letter-spacing:2px;text-transform:uppercase;
#     color:rgba(221,225,240,0.3);margin-bottom:22px;
# }

# /* ── RESULT CARDS ── */
# .dc {
#     padding:26px 30px;border-radius:20px;margin-bottom:14px;
#     border:1px solid rgba(255,255,255,0.06);
#     background:rgba(255,255,255,0.022);
#     position:relative;overflow:hidden;
# }
# .dc::before {
#     content:'';position:absolute;left:0;top:0;bottom:0;
#     width:3px;border-radius:3px 0 0 3px;
# }
# .dc.r1::before{background:linear-gradient(180deg,#7c3aed,#a855f7);}
# .dc.r2::before{background:rgba(168,85,247,0.45);}
# .dc.r3::before{background:rgba(148,163,184,0.25);}
# .drl{font-size:0.65rem;font-weight:600;letter-spacing:1.8px;text-transform:uppercase;margin-bottom:6px;}
# .r1 .drl{color:#c4b5fd;} .r2 .drl{color:rgba(168,85,247,0.8);} .r3 .drl{color:rgba(148,163,184,0.5);}
# .dn{font-family:'DM Serif Display',serif;font-size:1.55rem;color:#fff;margin-bottom:8px;line-height:1.2;}
# .dd{font-size:0.85rem;color:rgba(221,225,240,0.4);line-height:1.75;font-weight:300;margin-bottom:16px;}
# .cr{display:flex;align-items:center;gap:14px;}
# .cbw{flex:1;height:3px;background:rgba(255,255,255,0.06);border-radius:3px;overflow:hidden;}
# .cb{height:100%;background:linear-gradient(90deg,#7c3aed,#a855f7);border-radius:3px;}
# .cl{font-size:0.78rem;font-weight:700;color:#c4b5fd;min-width:44px;text-align:right;}

# /* ── SHAP ── */
# .shap-box {
#     background:rgba(255,255,255,0.022);
#     border:1px solid rgba(255,255,255,0.06);
#     border-radius:20px;padding:28px 30px;
# }
# .sh{display:flex;align-items:center;gap:12px;margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid rgba(255,255,255,0.05);}
# .si2{width:34px;height:34px;border-radius:10px;background:rgba(124,58,237,0.12);display:flex;align-items:center;justify-content:center;font-size:1rem;}
# .st2{font-size:0.88rem;font-weight:500;color:rgba(221,225,240,0.55);}
# .pw2{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px;}
# .pill{padding:7px 18px;border-radius:100px;font-size:0.78rem;font-weight:500;letter-spacing:0.3px;}
# .pp{background:rgba(20,184,166,0.1);border:1px solid rgba(20,184,166,0.22);color:#2dd4bf;}
# .pn{background:rgba(239,68,68,0.07);border:1px solid rgba(239,68,68,0.18);color:#f87171;}
# .leg{display:flex;flex-wrap:wrap;gap:20px;font-size:0.72rem;color:rgba(221,225,240,0.3);}
# .ld{width:7px;height:7px;border-radius:50%;display:inline-block;margin-right:6px;vertical-align:middle;}

# /* ── DISCLAIMER ── */
# .disc{font-size:0.75rem;color:rgba(221,225,240,0.22);line-height:1.7;
#     padding:14px 18px;background:rgba(255,255,255,0.018);
#     border-radius:12px;border:1px solid rgba(255,255,255,0.04);margin-top:12px;}

# /* ── PROGRESS / SPINNER / ALERT ── */
# .stProgress>div>div{background:rgba(255,255,255,0.04)!important;border-radius:4px!important;}
# .stProgress>div>div>div{background:linear-gradient(90deg,#7c3aed,#a855f7)!important;border-radius:4px!important;}
# .stSpinner>div{border-top-color:#a855f7!important;}
# .stAlert{background:rgba(239,68,68,0.07)!important;border:1px solid rgba(239,68,68,0.18)!important;border-radius:14px!important;color:#f87171!important;}
# </style>
# """, unsafe_allow_html=True)

# # ── Load artifacts ─────────────────────────────────────
# @st.cache_resource
# def load_artifacts():
#     model     = joblib.load("models/logreg_model.joblib")
#     tfidf     = joblib.load("models/tfidf_vectorizer.joblib")
#     label_map = joblib.load("models/label_map.joblib")
#     desc_df   = pd.read_csv("data/raw/symptom_Description.csv")
#     desc_df.columns = desc_df.columns.str.strip()
#     desc_map  = dict(zip(desc_df["Disease"].str.strip(), desc_df["Description"].str.strip()))
#     return model, tfidf, label_map, desc_map

# model, tfidf, label_map, desc_map = load_artifacts()

# # ── BG orbs ────────────────────────────────────────────
# st.markdown('<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div><div class="pw">', unsafe_allow_html=True)

# # ══════════════════════════════════════════════════════
# # TOP BAR — Brand (center) + Language (right)
# # ══════════════════════════════════════════════════════
# col_title, col_lang = st.columns([5, 1])
# with col_title:
#     s = st.session_state.step
#     # Only show big brand on step 1
#     if s == 1:
#         st.markdown(f"""
#         <div class="brand-header">
#             <div class="brand">Medi<span>Scan</span></div>
#             <div class="brand-sub">{tx['tagline']}</div>
#             <p class="hero-desc">{tx['hero_sub']}</p>
#         </div>
#         """, unsafe_allow_html=True)
#     else:
#         st.markdown(f"""
#         <div style="text-align:center; padding: 20px 0 8px;">
#             <div style="font-family:'DM Serif Display',serif; font-size:1.8rem; color:#fff; letter-spacing:-1px;">
#                 Medi<span style="color:#7c3aed">Scan</span>
#             </div>
#         </div>
#         """, unsafe_allow_html=True)

# with col_lang:
#     st.markdown('<div class="lang-wrap">', unsafe_allow_html=True)
#     lang_choice = st.selectbox(
#         "lang",
#         options=["English", "தமிழ்"],
#         index=0 if st.session_state.lang == "en" else 1,
#         label_visibility="collapsed",
#         key="lang_select"
#     )
#     new_lang = "en" if lang_choice == "English" else "ta"
#     if new_lang != st.session_state.lang:
#         st.session_state.lang = new_lang
#         st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)

# # refresh after possible rerun
# lang = st.session_state.lang
# tx = T[lang]
# s = st.session_state.step

# def sc(n):
#     if s > n: return "done"
#     if s == n: return "active"
#     return ""

# # ══════════════════════════════════════════════════════
# # STEP 1 — Name
# # ══════════════════════════════════════════════════════
# if s == 1:
#     # Stats
#     st.markdown(f"""
#     <div class="stats">
#         <div class="stat"><div class="stat-n">41<em>+</em></div><div class="stat-l">{tx['stat1_label']}</div></div>
#         <div class="stat"><div class="stat-n">132<em>+</em></div><div class="stat-l">{tx['stat2_label']}</div></div>
#         <div class="stat"><div class="stat-n">99<em>%</em></div><div class="stat-l">{tx['stat3_label']}</div></div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Step pill
#     st.markdown(f"""
#     <div class="spill">
#         <div class="si {sc(1)}"><div class="sn">1</div>{tx['step1']}</div>
#         <div class="si {sc(2)}"><div class="sn">2</div>{tx['step2']}</div>
#         <div class="si {sc(3)}"><div class="sn">3</div>{tx['step3']}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Form
#     st.markdown('<div class="gc">', unsafe_allow_html=True)
#     st.markdown(f'<span class="fl">{tx["name_label"]}</span>', unsafe_allow_html=True)
#     name = st.text_input("n", placeholder=tx["name_placeholder"], label_visibility="collapsed", key="name_field")
#     st.markdown("<br>", unsafe_allow_html=True)
#     col1, col2 = st.columns([1, 2])
#     with col2:
#         if st.button(tx["continue"] + "  →", key="btn1"):
#             if not name.strip():
#                 st.warning(tx["warn_name"])
#             else:
#                 st.session_state.name = name.strip()
#                 st.session_state.step = 2
#                 st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="disc">{tx["disclaimer"]}</div>', unsafe_allow_html=True)

# # ══════════════════════════════════════════════════════
# # STEP 2 — Age
# # ══════════════════════════════════════════════════════
# elif s == 2:
#     initials = ''.join([w[0].upper() for w in st.session_state.name.split()[:2]])

#     st.markdown(f"""
#     <div class="spill">
#         <div class="si {sc(1)}"><div class="sn">✓</div>{tx['step1']}</div>
#         <div class="si {sc(2)}"><div class="sn">2</div>{tx['step2']}</div>
#         <div class="si {sc(3)}"><div class="sn">3</div>{tx['step3']}</div>
#     </div>
#     <div class="greet">
#         <div class="av">{initials}</div>
#         <div>
#             <div class="gn">{tx['welcome']} {st.session_state.name}</div>
#             <div class="gs">{tx['profile_sub']}</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="gc">', unsafe_allow_html=True)
#     st.markdown(f'<span class="fl">{tx["age_label"]}</span>', unsafe_allow_html=True)
#     age = st.text_input("a", placeholder=tx["age_placeholder"], label_visibility="collapsed", key="age_field")
#     st.markdown("<br>", unsafe_allow_html=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button(tx["back"], key="back2"):
#             st.session_state.step = 1
#             st.rerun()
#     with col2:
#         if st.button(tx["continue"] + "  →", key="btn2"):
#             if not age.strip() or not age.strip().isdigit():
#                 st.warning(tx["warn_age"])
#             else:
#                 st.session_state.age = age.strip()
#                 st.session_state.step = 3
#                 st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="disc">{tx["disclaimer"]}</div>', unsafe_allow_html=True)

# # ══════════════════════════════════════════════════════
# # STEP 3 — Symptoms + Results
# # ══════════════════════════════════════════════════════
# elif s == 3:
#     initials = ''.join([w[0].upper() for w in st.session_state.name.split()[:2]])

#     st.markdown(f"""
#     <div class="spill">
#         <div class="si done"><div class="sn">✓</div>{tx['step1']}</div>
#         <div class="si done"><div class="sn">✓</div>{tx['step2']}</div>
#         <div class="si active"><div class="sn">3</div>{tx['step3']}</div>
#     </div>
#     <div class="greet">
#         <div class="av">{initials}</div>
#         <div>
#             <div class="gn">{st.session_state.name} · {st.session_state.age} {tx['step2'].lower()}</div>
#             <div class="gs">{tx['symptom_greeting_sub']}</div>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="gc">', unsafe_allow_html=True)
#     st.markdown(f'<span class="fl">{tx["symptom_label"]}</span>', unsafe_allow_html=True)

#     # Show Tamil labels in multiselect when Tamil is selected
#     selected_display = st.multiselect(
#         "sym",
#         options=SYMPTOM_DISPLAY_LIST,
#         placeholder=tx["symptom_placeholder"],
#         label_visibility="collapsed",
#         key="sym_field"
#     )

#     # Map display labels back to English keys for the model
#     if lang == "ta":
#         selected_en = [SYMPTOM_OPTIONS[d] for d in selected_display]
#     else:
#         selected_en = selected_display

#     symptoms_input = " ".join(selected_en)
#     st.markdown("<br>", unsafe_allow_html=True)

#     col1, col2 = st.columns(2)
#     with col1:
#         if st.button(tx["back"], key="back3"):
#             st.session_state.step = 2
#             st.rerun()
#     with col2:
#         analyse = st.button(tx["analyse"] + "  →", key="analyse")

#     st.markdown(f'<div class="disc" style="margin-top:20px">{tx["disclaimer"]}</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     if analyse:
#         if not selected_display:
#             st.warning(tx["warn_symptom"])
#         else:
#             with st.spinner(""):
#                 X     = tfidf.transform([symptoms_input])
#                 probs = model.predict_proba(X)[0]
#                 top3  = np.argsort(probs)[::-1][:3]

#             ranks  = [tx["diag1"], tx["diag2"], tx["diag3"]]
#             medals = [tx["rank1"], tx["rank2"], tx["rank3"]]
#             rclass = ["r1", "r2", "r3"]

#             st.markdown(f'<div class="sec-head">{tx["results_header"]} {st.session_state.name}</div>', unsafe_allow_html=True)

#             for i, idx in enumerate(top3):
#                 disease = label_map[idx]
#                 conf    = probs[idx] * 100
#                 desc    = desc_map.get(disease, tx["no_desc"])
#                 st.markdown(f"""
#                 <div class="dc {rclass[i]}">
#                     <div class="drl">{medals[i]} · {ranks[i]}</div>
#                     <div class="dn">{disease}</div>
#                     <div class="dd">{desc}</div>
#                     <div class="cr">
#                         <div class="cbw"><div class="cb" style="width:{int(conf)}%"></div></div>
#                         <div class="cl">{conf:.1f}%</div>
#                     </div>
#                 </div>
#                 """, unsafe_allow_html=True)

#             # SHAP
#             disease_shap, top_words = explain(symptoms_input)
#             pills_html = '<div class="pw2">'
#             for word, score in top_words:
#                 cls   = "pp" if score >= 0 else "pn"
#                 arrow = "↑" if score >= 0 else "↓"
#                 display_word = SYMPTOM_TA.get(word, word.replace("_", " ")) if lang == "ta" else word.replace("_", " ")
#                 pills_html += f'<span class="pill {cls}">{arrow} {display_word}</span>'
#             pills_html += '</div>'

#             st.markdown(f"""
#             <div class="shap-box">
#                 <div class="sh">
#                     <div class="si2">🔬</div>
#                     <div class="st2">{tx['shap_title']} — <strong style="color:#fff">{disease_shap}</strong></div>
#                 </div>
#                 {pills_html}
#                 <div class="leg">
#                     <span><span class="ld" style="background:#2dd4bf"></span>{tx['legend_pos']}</span>
#                     <span><span class="ld" style="background:#f87171"></span>{tx['legend_neg']}</span>
#                 </div>
#             </div>
#             """, unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)


# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd
# import sys, os

# sys.path.insert(0, os.path.dirname(__file__))
# from src.explainer import explain

# st.set_page_config(page_title="MediScan AI", page_icon="🧬", layout="centered")

# SYMPTOM_TA = {
#     'abdominal_pain':'வயிற்று வலி','abnormal_menstruation':'அசாதாரண மாதவிடாய்',
#     'acidity':'அமிலத்தன்மை','acute_liver_failure':'கடுமையான கல்லீரல் செயலிழப்பு',
#     'altered_sensorium':'மாற்றப்பட்ட உணர்வு நிலை','anxiety':'கவலை',
#     'back_pain':'முதுகு வலி','belly_pain':'வயிற்று வலி','blackheads':'கரும்புள்ளிகள்',
#     'bladder_discomfort':'சிறுநீர்ப்பை அசௌகரியம்','blister':'கொப்புளம்',
#     'blood_in_sputum':'சளியில் இரத்தம்','bloody_stool':'இரத்தம் கலந்த மலம்',
#     'blurred_and_distorted_vision':'மங்கலான பார்வை','breathlessness':'மூச்சுத் திணறல்',
#     'brittle_nails':'உடையும் நகங்கள்','bruising':'சிராய்ப்பு',
#     'burning_micturition':'எரிச்சலுடன் சிறுநீர்','chest_pain':'நெஞ்சு வலி',
#     'chills':'குளிர் நடுக்கம்','cold_hands_and_feets':'கை மற்றும் கால் குளிர்ச்சி',
#     'coma':'கோமா','congestion':'மூக்கடைப்பு','constipation':'மலச்சிக்கல்',
#     'continuous_feel_of_urine':'தொடர்ச்சியான சிறுநீர் உணர்வு',
#     'continuous_sneezing':'தொடர்ச்சியான தும்மல்','cough':'இருமல்','cramps':'தசைப்பிடிப்பு',
#     'dark_urine':'அடர் நிற சிறுநீர்','dehydration':'நீர்ச்சத்து குறைபாடு',
#     'depression':'மனச்சோர்வு','diarrhoea':'வயிற்றுப்போக்கு',
#     'dischromic _patches':'நிற மாற்றப் புள்ளிகள்','distention_of_abdomen':'வயிறு உப்புசம்',
#     'dizziness':'தலை சுற்றல்','drying_and_tingling_lips':'உதடுகள் உலர்வு',
#     'enlarged_thyroid':'விரிந்த தைரொய்டு','excessive_hunger':'அதிகப்படியான பசி',
#     'extra_marital_contacts':'திருமண வெளி தொடர்புகள்','family_history':'குடும்ப வரலாறு',
#     'fast_heart_rate':'வேகமான இதய துடிப்பு','fatigue':'சோர்வு',
#     'fluid_overload':'திரவ அதிகளவு','foul_smell_of urine':'சிறுநீரின் துர்நாற்றம்',
#     'headache':'தலைவலி','high_fever':'அதிக காய்ச்சல்','hip_joint_pain':'இடுப்பு மூட்டு வலி',
#     'history_of_alcohol_consumption':'மது அருந்திய வரலாறு','increased_appetite':'அதிகரித்த பசி',
#     'indigestion':'அஜீரணம்','inflammatory_nails':'அழற்சியுள்ள நகங்கள்',
#     'internal_itching':'உள் அரிப்பு','irregular_sugar_level':'ஒழுங்கற்ற சர்க்கரை அளவு',
#     'irritability':'எரிச்சல்','irritation_in_anus':'ஆசனவாயில் எரிச்சல்','itching':'அரிப்பு',
#     'joint_pain':'மூட்டு வலி','knee_pain':'முழங்கால் வலி',
#     'lack_of_concentration':'கவனக்குறைவு','lethargy':'சுணக்கம்',
#     'loss_of_appetite':'பசியின்மை','loss_of_balance':'சமநிலை இழப்பு',
#     'loss_of_smell':'மணம் உணரும் திறன் இழப்பு','malaise':'உடல் நலக்குறைவு',
#     'mild_fever':'லேசான காய்ச்சல்','mood_swings':'மனநிலை மாற்றங்கள்',
#     'movement_stiffness':'நகர்வு விறைப்பு','mucoid_sputum':'சளி நிறைந்த சளி',
#     'muscle_pain':'தசை வலி','muscle_wasting':'தசை அழிவு','muscle_weakness':'தசை பலவீனம்',
#     'nausea':'குமட்டல்','neck_pain':'கழுத்து வலி','nodal_skin_eruptions':'முடிச்சு தோல் வெடிப்பு',
#     'obesity':'உடல் பருமன்','pain_behind_the_eyes':'கண்களுக்கு பின் வலி',
#     'pain_during_bowel_movements':'மலம் கழிக்கும் போது வலி',
#     'pain_in_anal_region':'ஆசன வாய் பகுதியில் வலி','painful_walking':'வலியுடன் நடத்தல்',
#     'palpitations':'படபடப்பு','passage_of_gases':'வாயு வெளியேற்றம்',
#     'patches_in_throat':'தொண்டையில் புள்ளிகள்','phlegm':'சளி','polyuria':'அதிக சிறுநீர்',
#     'prominent_veins_on_calf':'கன்னலில் நரம்புகள் தெரிதல்',
#     'puffy_face_and_eyes':'முகம் மற்றும் கண்கள் வீக்கம்','pus_filled_pimples':'சீழ் நிறைந்த பருக்கள்',
#     'receiving_blood_transfusion':'இரத்தமாற்றம்','receiving_unsterile_injections':'கிருமி நீக்கமற்ற ஊசி',
#     'red_sore_around_nose':'மூக்கைச் சுற்றி சிவந்த புண்','red_spots_over_body':'உடலில் சிவந்த புள்ளிகள்',
#     'redness_of_eyes':'கண்கள் சிவத்தல்','restlessness':'அமைதியின்மை',
#     'runny_nose':'மூக்கு ஒழுகுதல்','rusty_sputum':'துரு நிற சளி','scurring':'தழும்பு',
#     'shivering':'நடுக்கம்','silver_like_dusting':'வெள்ளி போன்ற தூசு',
#     'sinus_pressure':'சைனஸ் அழுத்தம்','skin_peeling':'தோல் உரிதல்','skin_rash':'தோல் தடிப்பு',
#     'slurred_speech':'தடுமாறும் பேச்சு','small_dents_in_nails':'நகங்களில் சிறிய குழிகள்',
#     'spinning_movements':'சுழலும் உணர்வு','spotting_ urination':'துளி சிறுநீர்',
#     'stiff_neck':'கழுத்து விறைப்பு','stomach_bleeding':'வயிற்று இரத்தப்போக்கு',
#     'stomach_pain':'வயிற்று வலி','sunken_eyes':'கண்கள் உள்ளே சென்றிருத்தல்',
#     'sweating':'வியர்வை','swelled_lymph_nodes':'நிணநீர் முனைகள் வீக்கம்',
#     'swelling_joints':'மூட்டுகள் வீக்கம்','swelling_of_stomach':'வயிறு வீக்கம்',
#     'swollen_blood_vessels':'இரத்த நாளங்கள் வீக்கம்','swollen_extremeties':'கைகால்கள் வீக்கம்',
#     'swollen_legs':'கால்கள் வீக்கம்','throat_irritation':'தொண்டை எரிச்சல்',
#     'toxic_look_(typhos)':'நச்சு தோற்றம்','ulcers_on_tongue':'நாக்கில் புண்கள்',
#     'unsteadiness':'தளர்வான நடை','visual_disturbances':'பார்வை இடையூறு',
#     'vomiting':'வாந்தி','watering_from_eyes':'கண்ணீர் வடிதல்',
#     'weakness_in_limbs':'கைகால்களில் பலவீனம்','weakness_of_one_body_side':'உடலின் ஒரு பக்கம் பலவீனம்',
#     'weight_gain':'எடை அதிகரிப்பு','weight_loss':'எடை குறைப்பு',
#     'yellow_crust_ooze':'மஞ்சள் நிற மேல் படிவம்','yellow_urine':'மஞ்சள் சிறுநீர்',
#     'yellowing_of_eyes':'கண்கள் மஞ்சளாதல்','yellowish_skin':'மஞ்சள் தோல்',
# }

# T = {
#     "en": {
#         "tagline": "AI-POWERED DIAGNOSTICS",
#         "hero_sub": "Advanced symptom analysis using machine learning — trained on thousands of clinical cases to help you understand what your body might be telling you.",
#         "stat1_label":"Diseases Detected","stat2_label":"Symptom Inputs","stat3_label":"Model Accuracy",
#         "step1":"Profile","step2":"Age","step3":"Symptoms",
#         "name_label":"Your full name","name_placeholder":"e.g. Santhiya S",
#         "continue":"Continue","back":"← Back","welcome":"Welcome,",
#         "profile_sub":"Let's build your health profile",
#         "age_label":"Your age","age_placeholder":"e.g. 24",
#         "symptom_greeting_sub":"Select all symptoms you are currently experiencing",
#         "symptom_label":"Current symptoms","symptom_placeholder":"Search symptoms — e.g. fatigue, headache...",
#         "analyse":"Analyse Symptoms","results_header":"Analysis results for",
#         "rank1":"#1 Most Likely","rank2":"#2 Possible","rank3":"#3 Consider",
#         "diag1":"Primary Diagnosis","diag2":"Secondary Possibility","diag3":"Alternative",
#         "shap_title":"Why this was predicted","legend_pos":"Strongly linked to diagnosis",
#         "legend_neg":"Not typical for this condition",
#         "disclaimer":"⚠  For educational purposes only. Not a substitute for professional medical advice. Always consult a licensed physician.",
#         "warn_name":"Please enter your name to continue.","warn_age":"Please enter a valid age.",
#         "warn_symptom":"Please select at least one symptom.","no_desc":"No clinical description available.",
#     },
#     "ta": {
#         "tagline":"செயற்கை நுண்ணறிவு நோயறிதல்",
#         "hero_sub":"இயந்திர கற்றல் தொழில்நுட்பம் மூலம் அறிகுறிகளை ஆய்வு செய்து, உங்கள் உடல் என்ன சொல்கிறது என்பதை புரிந்துகொள்ள உதவுகிறோம்.",
#         "stat1_label":"கண்டறியப்பட்ட நோய்கள்","stat2_label":"அறிகுறி உள்ளீடுகள்","stat3_label":"மாதிரி துல்லியம்",
#         "step1":"சுயவிவரம்","step2":"வயது","step3":"அறிகுறிகள்",
#         "name_label":"உங்கள் முழு பெயர்","name_placeholder":"எ.கா. சந்தியா ச",
#         "continue":"தொடரவும்","back":"← திரும்பு","welcome":"வணக்கம்,",
#         "profile_sub":"உங்கள் உடல்நல சுயவிவரத்தை உருவாக்குவோம்",
#         "age_label":"உங்கள் வயது","age_placeholder":"எ.கா. 24",
#         "symptom_greeting_sub":"நீங்கள் தற்போது அனுபவிக்கும் அறிகுறிகளை தேர்ந்தெடுக்கவும்",
#         "symptom_label":"தற்போதைய அறிகுறிகள்","symptom_placeholder":"தேடவும் — எ.கா. சோர்வு, தலைவலி...",
#         "analyse":"அறிகுறிகளை பகுப்பாய்வு செய்","results_header":"பகுப்பாய்வு முடிவுகள் —",
#         "rank1":"#1 மிகவும் சாத்தியம்","rank2":"#2 சாத்தியம்","rank3":"#3 கருத்தில் கொள்க",
#         "diag1":"முதன்மை நோயறிதல்","diag2":"இரண்டாம் நிலை சாத்தியம்","diag3":"மாற்று கருத்து",
#         "shap_title":"இந்த முடிவு ஏன் வந்தது","legend_pos":"நோயறிதலுடன் வலுவாக தொடர்புடையது",
#         "legend_neg":"இந்த நிலைக்கு வழக்கமற்றது",
#         "disclaimer":"⚠  கல்வி நோக்கங்களுக்காக மட்டுமே. தொழில்முறை மருத்துவ ஆலோசனைக்கு மாற்றாகாது. எப்போதும் தகுதிவாய்ந்த மருத்துவரை அணுகவும்.",
#         "warn_name":"தொடர உங்கள் பெயரை உள்ளிடவும்.","warn_age":"சரியான வயதை உள்ளிடவும்.",
#         "warn_symptom":"குறைந்தது ஒரு அறிகுறியையாவது தேர்ந்தெடுக்கவும்.","no_desc":"மருத்துவ விளக்கம் கிடைக்கவில்லை.",
#     }
# }

# for k, v in [("step",1),("name",""),("age",""),("lang","en")]:
#     if k not in st.session_state:
#         st.session_state[k] = v

# lang = st.session_state.lang
# tx = T[lang]

# ALL_SYMPTOMS_EN = sorted([
#     'abdominal_pain','abnormal_menstruation','acidity','acute_liver_failure',
#     'altered_sensorium','anxiety','back_pain','belly_pain','blackheads',
#     'bladder_discomfort','blister','blood_in_sputum','bloody_stool',
#     'blurred_and_distorted_vision','breathlessness','brittle_nails','bruising',
#     'burning_micturition','chest_pain','chills','cold_hands_and_feets','coma',
#     'congestion','constipation','continuous_feel_of_urine','continuous_sneezing',
#     'cough','cramps','dark_urine','dehydration','depression','diarrhoea',
#     'dischromic _patches','distention_of_abdomen','dizziness',
#     'drying_and_tingling_lips','enlarged_thyroid','excessive_hunger',
#     'extra_marital_contacts','family_history','fast_heart_rate','fatigue',
#     'fluid_overload','foul_smell_of urine','headache','high_fever',
#     'hip_joint_pain','history_of_alcohol_consumption','increased_appetite',
#     'indigestion','inflammatory_nails','internal_itching','irregular_sugar_level',
#     'irritability','irritation_in_anus','itching','joint_pain','knee_pain',
#     'lack_of_concentration','lethargy','loss_of_appetite','loss_of_balance',
#     'loss_of_smell','malaise','mild_fever','mood_swings','movement_stiffness',
#     'mucoid_sputum','muscle_pain','muscle_wasting','muscle_weakness','nausea',
#     'neck_pain','nodal_skin_eruptions','obesity','pain_behind_the_eyes',
#     'pain_during_bowel_movements','pain_in_anal_region','painful_walking',
#     'palpitations','passage_of_gases','patches_in_throat','phlegm','polyuria',
#     'prominent_veins_on_calf','puffy_face_and_eyes','pus_filled_pimples',
#     'receiving_blood_transfusion','receiving_unsterile_injections',
#     'red_sore_around_nose','red_spots_over_body','redness_of_eyes','restlessness',
#     'runny_nose','rusty_sputum','scurring','shivering','silver_like_dusting',
#     'sinus_pressure','skin_peeling','skin_rash','slurred_speech',
#     'small_dents_in_nails','spinning_movements','spotting_ urination','stiff_neck',
#     'stomach_bleeding','stomach_pain','sunken_eyes','sweating',
#     'swelled_lymph_nodes','swelling_joints','swelling_of_stomach',
#     'swollen_blood_vessels','swollen_extremeties','swollen_legs',
#     'throat_irritation','toxic_look_(typhos)','ulcers_on_tongue','unsteadiness',
#     'visual_disturbances','vomiting','watering_from_eyes','weakness_in_limbs',
#     'weakness_of_one_body_side','weight_gain','weight_loss','yellow_crust_ooze',
#     'yellow_urine','yellowing_of_eyes','yellowish_skin'
# ])

# if lang == "ta":
#     SYMPTOM_OPTIONS = {SYMPTOM_TA.get(s, s.replace('_',' ')): s for s in ALL_SYMPTOMS_EN}
#     SYMPTOM_DISPLAY_LIST = sorted(SYMPTOM_OPTIONS.keys())
# else:
#     SYMPTOM_OPTIONS = {s: s for s in ALL_SYMPTOMS_EN}
#     SYMPTOM_DISPLAY_LIST = ALL_SYMPTOMS_EN

# CSS = """
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Figtree:wght@300;400;500;600;700&display=swap');

# :root {
#   --bg:#060810; --surface:#0c0f1a; --border:rgba(255,255,255,0.06);
#   --border-h:rgba(99,102,241,0.35); --text:#e2e5f0; --muted:rgba(226,229,240,0.38);
#   --accent:#6366f1; --accent2:#818cf8; --accent3:#a5b4fc;
#   --teal:#2dd4bf; --red:#f87171;
# }

# *,*::before,*::after{box-sizing:border-box;margin:0;padding:0;}
# html,body,.stApp{background:var(--bg)!important;color:var(--text);font-family:'Figtree',sans-serif;}
# #MainMenu,footer,header,.stDeployButton{visibility:hidden!important;}
# section[data-testid="stSidebar"]{display:none!important;}
# .block-container{padding:0 1.25rem!important;max-width:780px!important;margin:0 auto!important;}

# /* MESH */
# .mesh{position:fixed;inset:0;z-index:0;pointer-events:none;overflow:hidden;}
# .mesh-blob{position:absolute;border-radius:50%;filter:blur(120px);opacity:0.5;animation:drift 18s ease-in-out infinite alternate;}
# .mb1{width:600px;height:600px;background:radial-gradient(circle,rgba(99,102,241,0.18),transparent 70%);top:-200px;right:-180px;animation-delay:0s;}
# .mb2{width:500px;height:500px;background:radial-gradient(circle,rgba(45,212,191,0.09),transparent 70%);bottom:-100px;left:-150px;animation-delay:-6s;}
# .mb3{width:400px;height:400px;background:radial-gradient(circle,rgba(129,140,248,0.08),transparent 70%);top:40%;left:20%;animation-delay:-12s;}
# @keyframes drift{from{transform:translate(0,0) scale(1);}to{transform:translate(40px,30px) scale(1.08);}}

# .grain{position:fixed;inset:0;z-index:1;pointer-events:none;opacity:0.022;
# background-image:url("data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noise'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noise)'/%3E%3C/svg%3E");
# background-size:200px;}

# /* PAGE */
# .pw{position:relative;z-index:2;padding:48px 0 120px;}

# /* WORDMARK */
# .wordmark{font-family:'Instrument Serif',serif;font-size:1.45rem;color:#fff;letter-spacing:-0.5px;}
# .wordmark em{font-style:italic;color:var(--accent3);}

# /* HERO */
# .hero{text-align:center;margin-bottom:56px;}
# .hero-eyebrow{display:inline-flex;align-items:center;gap:8px;
#   background:rgba(99,102,241,0.08);border:1px solid rgba(99,102,241,0.2);
#   border-radius:100px;padding:6px 18px;
#   font-size:0.68rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;
#   color:var(--accent3);margin-bottom:30px;}
# .eyedot{width:6px;height:6px;border-radius:50%;background:var(--accent);
#   animation:pdot 2s ease-in-out infinite;}
# @keyframes pdot{0%,100%{opacity:1;transform:scale(1);}50%{opacity:0.35;transform:scale(0.65);}}
# .hero-title{font-family:'Instrument Serif',serif;font-size:clamp(3.2rem,9vw,6rem);
#   color:#fff;line-height:1.0;letter-spacing:-2px;margin-bottom:10px;}
# .hero-title .it{font-style:italic;color:var(--accent3);}
# .hero-desc{font-size:0.97rem;color:var(--muted);line-height:1.85;
#   font-weight:400;max-width:500px;margin:0 auto;}

# /* DIVIDER */
# .hdiv{display:flex;align-items:center;gap:16px;margin:40px 0 20px;}
# .hdiv-line{flex:1;height:1px;background:var(--border);}
# .hdiv-text{font-size:0.62rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:var(--muted);}

# /* STATS */
# .stats{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin-bottom:48px;}
# .stat{padding:28px 16px;background:var(--surface);border:1px solid var(--border);
#   border-radius:24px;text-align:center;position:relative;overflow:hidden;
#   transition:border-color 0.3s,transform 0.3s;}
# .stat:hover{border-color:var(--border-h);transform:translateY(-3px);}
# .stat::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(99,102,241,0.04),transparent);}
# .stat-n{font-family:'Instrument Serif',serif;font-size:2.6rem;color:#fff;line-height:1;margin-bottom:8px;}
# .stat-n em{font-style:normal;color:var(--accent3);}
# .stat-l{font-size:0.66rem;color:var(--muted);letter-spacing:0.5px;text-transform:uppercase;}

# /* STEP PILL */
# .spill{display:flex;align-items:center;gap:0;background:var(--surface);
#   border:1px solid var(--border);border-radius:100px;padding:5px;
#   width:fit-content;margin:0 auto 48px;box-shadow:0 4px 24px rgba(0,0,0,0.25);}
# .si{display:flex;align-items:center;gap:9px;padding:10px 24px;border-radius:100px;
#   font-size:0.77rem;font-weight:600;color:rgba(255,255,255,0.25);transition:all 0.3s;white-space:nowrap;}
# .si.active{background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;
#   box-shadow:0 4px 20px rgba(99,102,241,0.4);}
# .si.done{color:var(--accent3);}
# .sn{width:20px;height:20px;border-radius:50%;border:1.5px solid currentColor;
#   display:flex;align-items:center;justify-content:center;font-size:0.6rem;flex-shrink:0;font-weight:700;}
# .si.active .sn{background:rgba(255,255,255,0.2);border-color:rgba(255,255,255,0.5);}

# /* GLASS CARD */
# .gc{background:linear-gradient(145deg,rgba(255,255,255,0.035),rgba(255,255,255,0.018));
#   border:1px solid var(--border);border-radius:28px;padding:44px 48px;margin-bottom:16px;
#   backdrop-filter:blur(12px);
#   box-shadow:0 24px 64px rgba(0,0,0,0.3),inset 0 1px 0 rgba(255,255,255,0.06);
#   position:relative;overflow:hidden;}
# .gc::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;
#   background:linear-gradient(90deg,transparent,rgba(99,102,241,0.4),transparent);}

# /* FORM LABEL */
# .fl{font-size:0.64rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;
#   color:var(--muted);margin-bottom:12px;display:block;}

# /* INPUTS */
# .stTextInput>div>div>input{background:rgba(255,255,255,0.03)!important;
#   border:1.5px solid rgba(255,255,255,0.07)!important;border-radius:16px!important;
#   color:#fff!important;font-family:'Figtree',sans-serif!important;
#   font-size:1.05rem!important;font-weight:400!important;padding:18px 22px!important;
#   height:auto!important;transition:all 0.25s!important;caret-color:var(--accent3)!important;
#   letter-spacing:0.2px!important;}
# .stTextInput>div>div>input:focus{border-color:var(--border-h)!important;
#   background:rgba(99,102,241,0.04)!important;
#   box-shadow:0 0 0 4px rgba(99,102,241,0.08),0 2px 16px rgba(99,102,241,0.1)!important;outline:none!important;}
# .stTextInput>div>div>input::placeholder{color:rgba(226,229,240,0.15)!important;}
# .stTextInput label{display:none!important;}

# /* MULTISELECT */
# .stMultiSelect>div>div{background:rgba(255,255,255,0.03)!important;
#   border:1.5px solid rgba(255,255,255,0.07)!important;border-radius:16px!important;
#   min-height:58px!important;transition:all 0.25s!important;}
# .stMultiSelect>div>div:focus-within{border-color:var(--border-h)!important;
#   box-shadow:0 0 0 4px rgba(99,102,241,0.08)!important;}
# .stMultiSelect span[data-baseweb="tag"]{background:rgba(99,102,241,0.15)!important;
#   border:1px solid rgba(129,140,248,0.3)!important;border-radius:10px!important;
#   color:var(--accent3)!important;font-size:0.8rem!important;font-family:'Figtree',sans-serif!important;}
# [data-baseweb="select"] input{color:rgba(226,229,240,0.5)!important;font-family:'Figtree',sans-serif!important;}
# [data-baseweb="menu"]{background:#0f1220!important;border:1px solid rgba(255,255,255,0.07)!important;
#   border-radius:16px!important;box-shadow:0 24px 64px rgba(0,0,0,0.6)!important;}
# [data-baseweb="option"]{color:rgba(226,229,240,0.7)!important;font-family:'Figtree',sans-serif!important;font-size:0.88rem!important;}
# [data-baseweb="option"]:hover{background:rgba(99,102,241,0.1)!important;color:#fff!important;}
# .stMultiSelect label{display:none!important;}

# /* LANG SELECT */
# .lang-wrap .stSelectbox>div>div{background:rgba(99,102,241,0.08)!important;
#   border:1px solid rgba(129,140,248,0.25)!important;border-radius:100px!important;min-height:unset!important;}
# .lang-wrap .stSelectbox>div>div>div{padding:8px 20px!important;color:var(--accent3)!important;
#   font-family:'Figtree',sans-serif!important;font-size:0.8rem!important;font-weight:600!important;}
# .lang-wrap .stSelectbox svg{fill:var(--accent3)!important;}
# .lang-wrap .stSelectbox label{display:none!important;}

# /* BUTTONS */
# .stButton>button{font-family:'Figtree',sans-serif!important;font-weight:600!important;
#   font-size:0.88rem!important;border-radius:14px!important;padding:15px 28px!important;
#   border:none!important;transition:all 0.22s ease!important;height:auto!important;
#   letter-spacing:0.4px!important;width:100%!important;}
# div[data-testid="column"]:first-child .stButton>button{background:rgba(255,255,255,0.04)!important;
#   color:rgba(226,229,240,0.5)!important;border:1.5px solid rgba(255,255,255,0.07)!important;}
# div[data-testid="column"]:first-child .stButton>button:hover{background:rgba(255,255,255,0.08)!important;
#   color:rgba(226,229,240,0.9)!important;border-color:rgba(255,255,255,0.12)!important;}
# div[data-testid="column"]:last-child .stButton>button{
#   background:linear-gradient(135deg,var(--accent),var(--accent2))!important;color:#fff!important;
#   box-shadow:0 8px 28px rgba(99,102,241,0.35),inset 0 1px 0 rgba(255,255,255,0.12)!important;}
# div[data-testid="column"]:last-child .stButton>button:hover{transform:translateY(-2px)!important;
#   box-shadow:0 14px 40px rgba(99,102,241,0.48)!important;}
# div[data-testid="stVerticalBlock"]>div>div>div>div>div:only-child .stButton>button{
#   background:linear-gradient(135deg,var(--accent),var(--accent2))!important;color:#fff!important;
#   box-shadow:0 8px 28px rgba(99,102,241,0.35),inset 0 1px 0 rgba(255,255,255,0.12)!important;}

# /* GREETING */
# .greet{display:flex;align-items:center;gap:18px;padding:20px 26px;
#   background:rgba(99,102,241,0.05);border:1px solid rgba(99,102,241,0.12);
#   border-radius:20px;margin-bottom:32px;}
# .av{width:52px;height:52px;border-radius:50%;flex-shrink:0;
#   background:linear-gradient(135deg,var(--accent),var(--accent2));
#   display:flex;align-items:center;justify-content:center;
#   font-family:'Instrument Serif',serif;font-size:1.35rem;color:#fff;
#   box-shadow:0 4px 16px rgba(99,102,241,0.35);}
# .gn{font-weight:600;color:#fff;font-size:1rem;letter-spacing:-0.2px;}
# .gs{font-size:0.81rem;color:var(--muted);margin-top:3px;}

# /* SECTION HEADING */
# .sec-head{font-size:0.64rem;font-weight:700;letter-spacing:2.5px;text-transform:uppercase;
#   color:var(--muted);margin-bottom:24px;}

# /* RESULT CARDS */
# .dc{padding:28px 32px;border-radius:22px;margin-bottom:14px;border:1px solid var(--border);
#   background:linear-gradient(145deg,rgba(255,255,255,0.028),rgba(255,255,255,0.012));
#   position:relative;overflow:hidden;transition:border-color 0.3s,transform 0.3s;}
# .dc:hover{transform:translateX(4px);}
# .dc.r1{border-left:3px solid var(--accent);}
# .dc.r2{border-left:3px solid rgba(129,140,248,0.5);}
# .dc.r3{border-left:3px solid rgba(148,163,184,0.25);}
# .dc.r1::before{content:'';position:absolute;top:0;right:0;bottom:0;width:200px;
#   background:radial-gradient(ellipse at right,rgba(99,102,241,0.07),transparent);pointer-events:none;}
# .drl{font-size:0.62rem;font-weight:700;letter-spacing:2px;text-transform:uppercase;margin-bottom:8px;}
# .r1 .drl{color:var(--accent3);} .r2 .drl{color:rgba(165,180,252,0.65);} .r3 .drl{color:rgba(148,163,184,0.45);}
# .dn{font-family:'Instrument Serif',serif;font-size:1.65rem;color:#fff;margin-bottom:10px;line-height:1.15;}
# .dd{font-size:0.84rem;color:var(--muted);line-height:1.8;font-weight:400;margin-bottom:18px;}
# .cr{display:flex;align-items:center;gap:14px;}
# .cbw{flex:1;height:4px;background:rgba(255,255,255,0.05);border-radius:4px;overflow:hidden;}
# .cb{height:100%;background:linear-gradient(90deg,var(--accent),var(--accent2));border-radius:4px;}
# .cl{font-size:0.78rem;font-weight:700;color:var(--accent3);min-width:44px;text-align:right;}

# /* SHAP */
# .shap-box{background:linear-gradient(145deg,rgba(255,255,255,0.028),rgba(255,255,255,0.012));
#   border:1px solid var(--border);border-radius:22px;padding:30px 32px;margin-top:8px;}
# .sh{display:flex;align-items:center;gap:14px;margin-bottom:22px;padding-bottom:18px;
#   border-bottom:1px solid rgba(255,255,255,0.05);}
# .si2{width:36px;height:36px;border-radius:12px;background:rgba(99,102,241,0.12);
#   border:1px solid rgba(99,102,241,0.2);display:flex;align-items:center;justify-content:center;font-size:1rem;}
# .st2{font-size:0.86rem;font-weight:400;color:var(--muted);}
# .pw2{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:20px;}
# .pill{padding:7px 16px;border-radius:100px;font-size:0.76rem;font-weight:600;letter-spacing:0.2px;}
# .pp{background:rgba(45,212,191,0.09);border:1px solid rgba(45,212,191,0.22);color:var(--teal);}
# .pn{background:rgba(248,113,113,0.07);border:1px solid rgba(248,113,113,0.18);color:var(--red);}
# .leg{display:flex;flex-wrap:wrap;gap:20px;font-size:0.7rem;color:rgba(226,229,240,0.28);}
# .ld{width:7px;height:7px;border-radius:50%;display:inline-block;margin-right:6px;vertical-align:middle;}

# /* DISCLAIMER */
# .disc{font-size:0.72rem;color:rgba(226,229,240,0.2);line-height:1.75;padding:14px 20px;
#   background:rgba(255,255,255,0.015);border-radius:14px;border:1px solid rgba(255,255,255,0.04);margin-top:14px;}

# /* MISC */
# .stProgress>div>div{background:rgba(255,255,255,0.04)!important;border-radius:4px!important;}
# .stProgress>div>div>div{background:linear-gradient(90deg,var(--accent),var(--accent2))!important;border-radius:4px!important;}
# .stSpinner>div{border-top-color:var(--accent3)!important;}
# .stAlert{background:rgba(248,113,113,0.07)!important;border:1px solid rgba(248,113,113,0.18)!important;
#   border-radius:14px!important;color:var(--red)!important;}
# ::-webkit-scrollbar{width:4px;}
# ::-webkit-scrollbar-track{background:transparent;}
# ::-webkit-scrollbar-thumb{background:rgba(99,102,241,0.25);border-radius:4px;}
# </style>
# """

# st.markdown(CSS, unsafe_allow_html=True)

# @st.cache_resource
# def load_artifacts():
#     model     = joblib.load("models/logreg_model.joblib")
#     tfidf     = joblib.load("models/tfidf_vectorizer.joblib")
#     label_map = joblib.load("models/label_map.joblib")
#     desc_df   = pd.read_csv("data/raw/symptom_Description.csv")
#     desc_df.columns = desc_df.columns.str.strip()
#     desc_map = dict(zip(desc_df["Disease"].str.strip(), desc_df["Description"].str.strip()))
#     return model, tfidf, label_map, desc_map

# model, tfidf, label_map, desc_map = load_artifacts()

# st.markdown("""
# <div class="mesh">
#   <div class="mesh-blob mb1"></div>
#   <div class="mesh-blob mb2"></div>
#   <div class="mesh-blob mb3"></div>
# </div>
# <div class="grain"></div>
# <div class="pw">
# """, unsafe_allow_html=True)

# # TOP ROW
# col_logo, col_lang = st.columns([5, 1])
# with col_logo:
#     st.markdown('<div class="wordmark">Medi<em>Scan</em></div>', unsafe_allow_html=True)
# with col_lang:
#     st.markdown('<div class="lang-wrap">', unsafe_allow_html=True)
#     lang_choice = st.selectbox("lang", options=["English","தமிழ்"],
#         index=0 if st.session_state.lang=="en" else 1,
#         label_visibility="collapsed", key="lang_select")
#     new_lang = "en" if lang_choice == "English" else "ta"
#     if new_lang != st.session_state.lang:
#         st.session_state.lang = new_lang
#         st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)

# st.markdown('<div style="height:52px"></div>', unsafe_allow_html=True)

# lang = st.session_state.lang
# tx = T[lang]
# s = st.session_state.step

# def sc(n):
#     if s > n: return "done"
#     if s == n: return "active"
#     return ""

# # STEP 1
# if s == 1:
#     st.markdown(f"""
#     <div class="hero">
#       <div class="hero-eyebrow"><div class="eyedot"></div>{tx['tagline']}</div>
#       <div class="hero-title">Know your body,<br><span class="it">better.</span></div>
#       <p class="hero-desc">{tx['hero_sub']}</p>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="stats">
#       <div class="stat"><div class="stat-n">41<em>+</em></div><div class="stat-l">{tx['stat1_label']}</div></div>
#       <div class="stat"><div class="stat-n">132<em>+</em></div><div class="stat-l">{tx['stat2_label']}</div></div>
#       <div class="stat"><div class="stat-n">99<em>%</em></div><div class="stat-l">{tx['stat3_label']}</div></div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown(f"""
#     <div class="spill">
#       <div class="si {sc(1)}"><div class="sn">1</div>{tx['step1']}</div>
#       <div class="si {sc(2)}"><div class="sn">2</div>{tx['step2']}</div>
#       <div class="si {sc(3)}"><div class="sn">3</div>{tx['step3']}</div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="gc">', unsafe_allow_html=True)
#     st.markdown(f'<span class="fl">{tx["name_label"]}</span>', unsafe_allow_html=True)
#     name = st.text_input("n", placeholder=tx["name_placeholder"], label_visibility="collapsed", key="name_field")
#     st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)
#     c1, c2 = st.columns([1,2])
#     with c2:
#         if st.button(tx["continue"]+"  →", key="btn1"):
#             if not name.strip(): st.warning(tx["warn_name"])
#             else:
#                 st.session_state.name = name.strip()
#                 st.session_state.step = 2; st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="disc">{tx["disclaimer"]}</div>', unsafe_allow_html=True)

# # STEP 2
# elif s == 2:
#     initials = ''.join([w[0].upper() for w in st.session_state.name.split()[:2]])
#     st.markdown(f"""
#     <div class="spill">
#       <div class="si {sc(1)}"><div class="sn">✓</div>{tx['step1']}</div>
#       <div class="si {sc(2)}"><div class="sn">2</div>{tx['step2']}</div>
#       <div class="si {sc(3)}"><div class="sn">3</div>{tx['step3']}</div>
#     </div>
#     <div class="greet">
#       <div class="av">{initials}</div>
#       <div><div class="gn">{tx['welcome']} {st.session_state.name}</div><div class="gs">{tx['profile_sub']}</div></div>
#     </div>
#     """, unsafe_allow_html=True)
#     st.markdown('<div class="gc">', unsafe_allow_html=True)
#     st.markdown(f'<span class="fl">{tx["age_label"]}</span>', unsafe_allow_html=True)
#     age = st.text_input("a", placeholder=tx["age_placeholder"], label_visibility="collapsed", key="age_field")
#     st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)
#     c1, c2 = st.columns(2)
#     with c1:
#         if st.button(tx["back"], key="back2"): st.session_state.step=1; st.rerun()
#     with c2:
#         if st.button(tx["continue"]+"  →", key="btn2"):
#             if not age.strip() or not age.strip().isdigit(): st.warning(tx["warn_age"])
#             else:
#                 st.session_state.age = age.strip()
#                 st.session_state.step = 3; st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="disc">{tx["disclaimer"]}</div>', unsafe_allow_html=True)

# # STEP 3
# elif s == 3:
#     initials = ''.join([w[0].upper() for w in st.session_state.name.split()[:2]])
#     st.markdown(f"""
#     <div class="spill">
#       <div class="si done"><div class="sn">✓</div>{tx['step1']}</div>
#       <div class="si done"><div class="sn">✓</div>{tx['step2']}</div>
#       <div class="si active"><div class="sn">3</div>{tx['step3']}</div>
#     </div>
#     <div class="greet">
#       <div class="av">{initials}</div>
#       <div><div class="gn">{st.session_state.name} · {st.session_state.age} {tx['step2'].lower()}</div><div class="gs">{tx['symptom_greeting_sub']}</div></div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="gc">', unsafe_allow_html=True)
#     st.markdown(f'<span class="fl">{tx["symptom_label"]}</span>', unsafe_allow_html=True)
#     selected_display = st.multiselect("sym", options=SYMPTOM_DISPLAY_LIST,
#         placeholder=tx["symptom_placeholder"], label_visibility="collapsed", key="sym_field")
#     selected_en = [SYMPTOM_OPTIONS[d] for d in selected_display] if lang=="ta" else selected_display
#     symptoms_input = " ".join(selected_en)
#     st.markdown('<div style="height:12px"></div>', unsafe_allow_html=True)
#     c1, c2 = st.columns(2)
#     with c1:
#         if st.button(tx["back"], key="back3"): st.session_state.step=2; st.rerun()
#     with c2:
#         analyse = st.button(tx["analyse"]+"  →", key="analyse")
#     st.markdown(f'<div class="disc" style="margin-top:18px">{tx["disclaimer"]}</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     if analyse:
#         if not selected_display:
#             st.warning(tx["warn_symptom"])
#         else:
#             with st.spinner(""):
#                 X     = tfidf.transform([symptoms_input])
#                 probs = model.predict_proba(X)[0]
#                 top3  = np.argsort(probs)[::-1][:3]

#             medals = [tx["rank1"],tx["rank2"],tx["rank3"]]
#             ranks  = [tx["diag1"],tx["diag2"],tx["diag3"]]
#             rclass = ["r1","r2","r3"]

#             st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)
#             st.markdown(f'<div class="sec-head">{tx["results_header"]} {st.session_state.name}</div>', unsafe_allow_html=True)

#             for i, idx in enumerate(top3):
#                 disease = label_map[idx]
#                 conf    = probs[idx] * 100
#                 desc    = desc_map.get(disease, tx["no_desc"])
#                 st.markdown(f"""
#                 <div class="dc {rclass[i]}">
#                   <div class="drl">{medals[i]} · {ranks[i]}</div>
#                   <div class="dn">{disease}</div>
#                   <div class="dd">{desc}</div>
#                   <div class="cr">
#                     <div class="cbw"><div class="cb" style="width:{int(conf)}%"></div></div>
#                     <div class="cl">{conf:.1f}%</div>
#                   </div>
#                 </div>
#                 """, unsafe_allow_html=True)

#             disease_shap, top_words = explain(symptoms_input)
#             pills_html = '<div class="pw2">'
#             for word, score in top_words:
#                 cls   = "pp" if score >= 0 else "pn"
#                 arrow = "↑" if score >= 0 else "↓"
#                 dw = SYMPTOM_TA.get(word, word.replace("_"," ")) if lang=="ta" else word.replace("_"," ")
#                 pills_html += f'<span class="pill {cls}">{arrow} {dw}</span>'
#             pills_html += '</div>'

#             st.markdown(f"""
#             <div class="shap-box">
#               <div class="sh">
#                 <div class="si2">🔬</div>
#                 <div class="st2">{tx['shap_title']} — <strong style="color:#fff;font-weight:600">{disease_shap}</strong></div>
#               </div>
#               {pills_html}
#               <div class="leg">
#                 <span><span class="ld" style="background:var(--teal)"></span>{tx['legend_pos']}</span>
#                 <span><span class="ld" style="background:var(--red)"></span>{tx['legend_neg']}</span>
#               </div>
#             </div>
#             """, unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)

# import streamlit as st
# import joblib
# import numpy as np
# import pandas as pd
# import sys, os

# sys.path.insert(0, os.path.dirname(__file__))
# from src.explainer import explain

# st.set_page_config(page_title="MediScan AI", page_icon="🧬", layout="wide")

# SYMPTOM_TA = {
#     'abdominal_pain':'வயிற்று வலி','abnormal_menstruation':'அசாதாரண மாதவிடாய்',
#     'acidity':'அமிலத்தன்மை','acute_liver_failure':'கடுமையான கல்லீரல் செயலிழப்பு',
#     'altered_sensorium':'மாற்றப்பட்ட உணர்வு நிலை','anxiety':'கவலை',
#     'back_pain':'முதுகு வலி','belly_pain':'வயிற்று வலி','blackheads':'கரும்புள்ளிகள்',
#     'bladder_discomfort':'சிறுநீர்ப்பை அசௌகரியம்','blister':'கொப்புளம்',
#     'blood_in_sputum':'சளியில் இரத்தம்','bloody_stool':'இரத்தம் கலந்த மலம்',
#     'blurred_and_distorted_vision':'மங்கலான பார்வை','breathlessness':'மூச்சுத் திணறல்',
#     'brittle_nails':'உடையும் நகங்கள்','bruising':'சிராய்ப்பு',
#     'burning_micturition':'எரிச்சலுடன் சிறுநீர்','chest_pain':'நெஞ்சு வலி',
#     'chills':'குளிர் நடுக்கம்','cold_hands_and_feets':'கை மற்றும் கால் குளிர்ச்சி',
#     'coma':'கோமா','congestion':'மூக்கடைப்பு','constipation':'மலச்சிக்கல்',
#     'continuous_feel_of_urine':'தொடர்ச்சியான சிறுநீர் உணர்வு',
#     'continuous_sneezing':'தொடர்ச்சியான தும்மல்','cough':'இருமல்','cramps':'தசைப்பிடிப்பு',
#     'dark_urine':'அடர் நிற சிறுநீர்','dehydration':'நீர்ச்சத்து குறைபாடு',
#     'depression':'மனச்சோர்வு','diarrhoea':'வயிற்றுப்போக்கு',
#     'dischromic _patches':'நிற மாற்றப் புள்ளிகள்','distention_of_abdomen':'வயிறு உப்புசம்',
#     'dizziness':'தலை சுற்றல்','drying_and_tingling_lips':'உதடுகள் உலர்வு',
#     'enlarged_thyroid':'விரிந்த தைரொய்டு','excessive_hunger':'அதிகப்படியான பசி',
#     'extra_marital_contacts':'திருமண வெளி தொடர்புகள்','family_history':'குடும்ப வரலாறு',
#     'fast_heart_rate':'வேகமான இதய துடிப்பு','fatigue':'சோர்வு',
#     'fluid_overload':'திரவ அதிகளவு','foul_smell_of urine':'சிறுநீரின் துர்நாற்றம்',
#     'headache':'தலைவலி','high_fever':'அதிக காய்ச்சல்','hip_joint_pain':'இடுப்பு மூட்டு வலி',
#     'history_of_alcohol_consumption':'மது அருந்திய வரலாறு','increased_appetite':'அதிகரித்த பசி',
#     'indigestion':'அஜீரணம்','inflammatory_nails':'அழற்சியுள்ள நகங்கள்',
#     'internal_itching':'உள் அரிப்பு','irregular_sugar_level':'ஒழுங்கற்ற சர்க்கரை அளவு',
#     'irritability':'எரிச்சல்','irritation_in_anus':'ஆசனவாயில் எரிச்சல்','itching':'அரிப்பு',
#     'joint_pain':'மூட்டு வலி','knee_pain':'முழங்கால் வலி',
#     'lack_of_concentration':'கவனக்குறைவு','lethargy':'சுணக்கம்',
#     'loss_of_appetite':'பசியின்மை','loss_of_balance':'சமநிலை இழப்பு',
#     'loss_of_smell':'மணம் உணரும் திறன் இழப்பு','malaise':'உடல் நலக்குறைவு',
#     'mild_fever':'லேசான காய்ச்சல்','mood_swings':'மனநிலை மாற்றங்கள்',
#     'movement_stiffness':'நகர்வு விறைப்பு','mucoid_sputum':'சளி நிறைந்த சளி',
#     'muscle_pain':'தசை வலி','muscle_wasting':'தசை அழிவு','muscle_weakness':'தசை பலவீனம்',
#     'nausea':'குமட்டல்','neck_pain':'கழுத்து வலி','nodal_skin_eruptions':'முடிச்சு தோல் வெடிப்பு',
#     'obesity':'உடல் பருமன்','pain_behind_the_eyes':'கண்களுக்கு பின் வலி',
#     'pain_during_bowel_movements':'மலம் கழிக்கும் போது வலி',
#     'pain_in_anal_region':'ஆசன வாய் பகுதியில் வலி','painful_walking':'வலியுடன் நடத்தல்',
#     'palpitations':'படபடப்பு','passage_of_gases':'வாயு வெளியேற்றம்',
#     'patches_in_throat':'தொண்டையில் புள்ளிகள்','phlegm':'சளி','polyuria':'அதிக சிறுநீர்',
#     'prominent_veins_on_calf':'கன்னலில் நரம்புகள் தெரிதல்',
#     'puffy_face_and_eyes':'முகம் மற்றும் கண்கள் வீக்கம்','pus_filled_pimples':'சீழ் நிறைந்த பருக்கள்',
#     'receiving_blood_transfusion':'இரத்தமாற்றம்','receiving_unsterile_injections':'கிருமி நீக்கமற்ற ஊசி',
#     'red_sore_around_nose':'மூக்கைச் சுற்றி சிவந்த புண்','red_spots_over_body':'உடலில் சிவந்த புள்ளிகள்',
#     'redness_of_eyes':'கண்கள் சிவத்தல்','restlessness':'அமைதியின்மை',
#     'runny_nose':'மூக்கு ஒழுகுதல்','rusty_sputum':'துரு நிற சளி','scurring':'தழும்பு',
#     'shivering':'நடுக்கம்','silver_like_dusting':'வெள்ளி போன்ற தூசு',
#     'sinus_pressure':'சைனஸ் அழுத்தம்','skin_peeling':'தோல் உரிதல்','skin_rash':'தோல் தடிப்பு',
#     'slurred_speech':'தடுமாறும் பேச்சு','small_dents_in_nails':'நகங்களில் சிறிய குழிகள்',
#     'spinning_movements':'சுழலும் உணர்வு','spotting_ urination':'துளி சிறுநீர்',
#     'stiff_neck':'கழுத்து விறைப்பு','stomach_bleeding':'வயிற்று இரத்தப்போக்கு',
#     'stomach_pain':'வயிற்று வலி','sunken_eyes':'கண்கள் உள்ளே சென்றிருத்தல்',
#     'sweating':'வியர்வை','swelled_lymph_nodes':'நிணநீர் முனைகள் வீக்கம்',
#     'swelling_joints':'மூட்டுகள் வீக்கம்','swelling_of_stomach':'வயிறு வீக்கம்',
#     'swollen_blood_vessels':'இரத்த நாளங்கள் வீக்கம்','swollen_extremeties':'கைகால்கள் வீக்கம்',
#     'swollen_legs':'கால்கள் வீக்கம்','throat_irritation':'தொண்டை எரிச்சல்',
#     'toxic_look_(typhos)':'நச்சு தோற்றம்','ulcers_on_tongue':'நாக்கில் புண்கள்',
#     'unsteadiness':'தளர்வான நடை','visual_disturbances':'பார்வை இடையூறு',
#     'vomiting':'வாந்தி','watering_from_eyes':'கண்ணீர் வடிதல்',
#     'weakness_in_limbs':'கைகால்களில் பலவீனம்','weakness_of_one_body_side':'உடலின் ஒரு பக்கம் பலவீனம்',
#     'weight_gain':'எடை அதிகரிப்பு','weight_loss':'எடை குறைப்பு',
#     'yellow_crust_ooze':'மஞ்சள் நிற மேல் படிவம்','yellow_urine':'மஞ்சள் சிறுநீர்',
#     'yellowing_of_eyes':'கண்கள் மஞ்சளாதல்','yellowish_skin':'மஞ்சள் தோல்',
# }

# T = {
#     "en": {
#         "tagline": "AI-POWERED DIAGNOSTICS",
#         "hero_sub": "Advanced symptom analysis using machine learning — trained on thousands of clinical cases to help you understand what your body might be telling you.",
#         "stat1_label":"Diseases Detected","stat2_label":"Symptom Inputs","stat3_label":"Model Accuracy",
#         "step1":"Profile","step2":"Age","step3":"Symptoms",
#         "name_label":"Full Name","name_placeholder":"e.g. Santhiya S",
#         "continue":"Continue","back":"Back","welcome":"Welcome back,",
#         "profile_sub":"Let's build your health profile",
#         "age_heading":"How old are you?",
#         "age_sub":"Your age helps our model deliver more accurate predictions.",
#         "age_label":"Age","age_placeholder":"e.g. 24",
#         "symptom_heading":"Select Your Symptoms",
#         "symptom_greeting_sub":"Select all symptoms you are currently experiencing",
#         "symptom_label":"Current Symptoms","symptom_placeholder":"Search — fatigue, headache, nausea...",
#         "analyse":"Run Diagnosis","results_header":"Diagnosis Report",
#         "rank1":"#1 Most Likely","rank2":"#2 Possible","rank3":"#3 Consider",
#         "diag1":"Primary Diagnosis","diag2":"Secondary Possibility","diag3":"Alternative",
#         "shap_title":"Key predictive factors","legend_pos":"Strongly linked to diagnosis",
#         "legend_neg":"Not typical for this condition",
#         "disclaimer":"For educational purposes only. Not a substitute for professional medical advice. Always consult a licensed physician.",
#         "warn_name":"Please enter your name to continue.","warn_age":"Please enter a valid age.",
#         "warn_symptom":"Please select at least one symptom.","no_desc":"No clinical description available.",
#         "new_scan": "Start New Scan",
#         "lang_en": "English", "lang_ta": "தமிழ்",
#     },
#     "ta": {
#         "tagline":"செயற்கை நுண்ணறிவு நோயறிதல்",
#         "hero_sub":"இயந்திர கற்றல் தொழில்நுட்பம் மூலம் அறிகுறிகளை ஆய்வு செய்து, உங்கள் உடல் என்ன சொல்கிறது என்பதை புரிந்துகொள்ள உதவுகிறோம்.",
#         "stat1_label":"கண்டறியப்பட்ட நோய்கள்","stat2_label":"அறிகுறி உள்ளீடுகள்","stat3_label":"மாதிரி துல்லியம்",
#         "step1":"சுயவிவரம்","step2":"வயது","step3":"அறிகுறிகள்",
#         "name_label":"முழு பெயர்","name_placeholder":"எ.கா. சந்தியா ச",
#         "continue":"தொடரவும்","back":"திரும்பு","welcome":"வணக்கம்,",
#         "profile_sub":"உங்கள் உடல்நல சுயவிவரத்தை உருவாக்குவோம்",
#         "age_heading":"உங்கள் வயது என்ன?",
#         "age_sub":"வயது தகவல் மூலம் துல்லியமான முடிவுகளை வழங்க முடியும்.",
#         "age_label":"வயது","age_placeholder":"எ.கா. 24",
#         "symptom_heading":"அறிகுறிகளை தேர்ந்தெடுக்கவும்",
#         "symptom_greeting_sub":"நீங்கள் தற்போது அனுபவிக்கும் அறிகுறிகளை தேர்ந்தெடுக்கவும்",
#         "symptom_label":"தற்போதைய அறிகுறிகள்","symptom_placeholder":"தேடவும் — சோர்வு, தலைவலி...",
#         "analyse":"நோயறிதல் இயக்கு","results_header":"நோயறிதல் அறிக்கை",
#         "rank1":"#1 மிகவும் சாத்தியம்","rank2":"#2 சாத்தியம்","rank3":"#3 கருத்தில் கொள்க",
#         "diag1":"முதன்மை நோயறிதல்","diag2":"இரண்டாம் நிலை","diag3":"மாற்று கருத்து",
#         "shap_title":"முக்கிய காரணிகள்","legend_pos":"நோயறிதலுடன் வலுவாக தொடர்புடையது",
#         "legend_neg":"இந்த நிலைக்கு வழக்கமற்றது",
#         "disclaimer":"கல்வி நோக்கங்களுக்காக மட்டுமே. தகுதிவாய்ந்த மருத்துவரை எப்போதும் அணுகவும்.",
#         "warn_name":"தொடர உங்கள் பெயரை உள்ளிடவும்.","warn_age":"சரியான வயதை உள்ளிடவும்.",
#         "warn_symptom":"குறைந்தது ஒரு அறிகுறியையாவது தேர்ந்தெடுக்கவும்.","no_desc":"மருத்துவ விளக்கம் கிடைக்கவில்லை.",
#         "new_scan": "புதிய ஸ்கேன்",
#         "lang_en": "English", "lang_ta": "தமிழ்",
#     }
# }

# for k, v in [("step",1),("name",""),("age",""),("lang","en"),("direction","forward")]:
#     if k not in st.session_state:
#         st.session_state[k] = v

# lang = st.session_state.lang
# tx = T[lang]

# ALL_SYMPTOMS_EN = sorted([
#     'abdominal_pain','abnormal_menstruation','acidity','acute_liver_failure',
#     'altered_sensorium','anxiety','back_pain','belly_pain','blackheads',
#     'bladder_discomfort','blister','blood_in_sputum','bloody_stool',
#     'blurred_and_distorted_vision','breathlessness','brittle_nails','bruising',
#     'burning_micturition','chest_pain','chills','cold_hands_and_feets','coma',
#     'congestion','constipation','continuous_feel_of_urine','continuous_sneezing',
#     'cough','cramps','dark_urine','dehydration','depression','diarrhoea',
#     'dischromic _patches','distention_of_abdomen','dizziness',
#     'drying_and_tingling_lips','enlarged_thyroid','excessive_hunger',
#     'extra_marital_contacts','family_history','fast_heart_rate','fatigue',
#     'fluid_overload','foul_smell_of urine','headache','high_fever',
#     'hip_joint_pain','history_of_alcohol_consumption','increased_appetite',
#     'indigestion','inflammatory_nails','internal_itching','irregular_sugar_level',
#     'irritability','irritation_in_anus','itching','joint_pain','knee_pain',
#     'lack_of_concentration','lethargy','loss_of_appetite','loss_of_balance',
#     'loss_of_smell','malaise','mild_fever','mood_swings','movement_stiffness',
#     'mucoid_sputum','muscle_pain','muscle_wasting','muscle_weakness','nausea',
#     'neck_pain','nodal_skin_eruptions','obesity','pain_behind_the_eyes',
#     'pain_during_bowel_movements','pain_in_anal_region','painful_walking',
#     'palpitations','passage_of_gases','patches_in_throat','phlegm','polyuria',
#     'prominent_veins_on_calf','puffy_face_and_eyes','pus_filled_pimples',
#     'receiving_blood_transfusion','receiving_unsterile_injections',
#     'red_sore_around_nose','red_spots_over_body','redness_of_eyes','restlessness',
#     'runny_nose','rusty_sputum','scurring','shivering','silver_like_dusting',
#     'sinus_pressure','skin_peeling','skin_rash','slurred_speech',
#     'small_dents_in_nails','spinning_movements','spotting_ urination','stiff_neck',
#     'stomach_bleeding','stomach_pain','sunken_eyes','sweating',
#     'swelled_lymph_nodes','swelling_joints','swelling_of_stomach',
#     'swollen_blood_vessels','swollen_extremeties','swollen_legs',
#     'throat_irritation','toxic_look_(typhos)','ulcers_on_tongue','unsteadiness',
#     'visual_disturbances','vomiting','watering_from_eyes','weakness_in_limbs',
#     'weakness_of_one_body_side','weight_gain','weight_loss','yellow_crust_ooze',
#     'yellow_urine','yellowing_of_eyes','yellowish_skin'
# ])

# if lang == "ta":
#     SYMPTOM_OPTIONS = {SYMPTOM_TA.get(s, s.replace('_',' ')): s for s in ALL_SYMPTOMS_EN}
#     SYMPTOM_DISPLAY_LIST = sorted(SYMPTOM_OPTIONS.keys())
# else:
#     SYMPTOM_OPTIONS = {s: s for s in ALL_SYMPTOMS_EN}
#     SYMPTOM_DISPLAY_LIST = ALL_SYMPTOMS_EN

# direction = st.session_state.get("direction", "forward")
# anim = "slide-fwd" if direction == "forward" else "slide-bwd"

# CSS = """
# <style>
# @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;1,300&family=Fraunces:ital,opsz,wght@0,9..144,300;0,9..144,600;1,9..144,300;1,9..144,600&display=swap');

# :root {
#   --bg:       #080c14;
#   --bg-card:  #0d1220;
#   --bg-input: #111827;
#   --border:   rgba(255,255,255,0.07);
#   --border-a: rgba(99,179,237,0.3);
#   --text:     #e2e8f4;
#   --muted:    rgba(180,195,225,0.45);
#   --blue:     #63b3ed;
#   --blue2:    #90cdf4;
#   --teal:     #4fd1c5;
#   --green:    #68d391;
#   --red:      #fc8181;
#   --amber:    #f6ad55;
#   --white:    #ffffff;
#   --dur:      0.55s;
# }

# *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

# html, body, .stApp {
#   background: var(--bg) !important;
#   color: var(--text);
#   font-family: 'Plus Jakarta Sans', sans-serif;
# }

# #MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
# section[data-testid="stSidebar"] { display: none !important; }

# /* ── Full-width layout reset ── */
# .block-container {
#   padding: 0 !important;
#   max-width: 100% !important;
#   margin: 0 !important;
# }
# [data-testid="stAppViewContainer"] > .main {
#   padding: 0 !important;
# }

# /* ══════════════════════════════════
#    BACKGROUND
# ══════════════════════════════════ */
# .bg-layer {
#   position: fixed; inset: 0; z-index: 0; pointer-events: none; overflow: hidden;
# }
# .orb {
#   position: absolute; border-radius: 50%; filter: blur(90px);
#   animation: orb-float 22s ease-in-out infinite alternate;
# }
# .orb-1 {
#   width: 700px; height: 700px;
#   background: radial-gradient(circle, rgba(99,179,237,0.1) 0%, transparent 65%);
#   top: -200px; right: -200px; animation-delay: 0s;
# }
# .orb-2 {
#   width: 500px; height: 500px;
#   background: radial-gradient(circle, rgba(79,209,197,0.07) 0%, transparent 65%);
#   bottom: -100px; left: -150px; animation-delay: -8s;
# }
# .orb-3 {
#   width: 350px; height: 350px;
#   background: radial-gradient(circle, rgba(144,205,244,0.05) 0%, transparent 65%);
#   top: 40%; left: 35%; animation-delay: -14s;
# }
# @keyframes orb-float {
#   from { transform: translate(0,0) scale(1); }
#   to   { transform: translate(50px, 35px) scale(1.12); }
# }

# /* subtle dot grid */
# .dot-grid {
#   position: fixed; inset: 0; z-index: 0; pointer-events: none;
#   background-image: radial-gradient(rgba(99,179,237,0.12) 1px, transparent 1px);
#   background-size: 32px 32px;
#   mask-image: radial-gradient(ellipse 70% 70% at 50% 50%, black 30%, transparent 100%);
# }

# /* ══════════════════════════════════
#    SHELL
# ══════════════════════════════════ */
# .shell {
#   position: relative; z-index: 2;
#   min-height: 100vh;
#   display: flex;
#   flex-direction: column;
#   align-items: center;
# }

# /* ══════════════════════════════════
#    TOP NAV
# ══════════════════════════════════ */
# .topnav {
#   width: 100%;
#   display: flex;
#   align-items: center;
#   justify-content: space-between;
#   padding: 22px 60px 20px;
#   border-bottom: 1px solid var(--border);
#   background: rgba(8,12,20,0.8);
#   backdrop-filter: blur(16px);
#   position: sticky; top: 0; z-index: 100;
# }
# .brand {
#   font-family: 'Plus Jakarta Sans', sans-serif;
#   font-size: 1.15rem;
#   font-weight: 700;
#   color: var(--white);
#   letter-spacing: 0.5px;
# }
# .brand-dot { color: var(--blue); }
# .brand-tag {
#   display: block;
#   font-size: 0.52rem;
#   font-weight: 500;
#   letter-spacing: 3.5px;
#   text-transform: uppercase;
#   color: var(--muted);
#   margin-top: 2px;
# }

# /* ══════════════════════════════════
#    LANGUAGE TOGGLE  (no text cursor)
# ══════════════════════════════════ */
# .lang-toggle {
#   display: flex;
#   align-items: center;
#   background: rgba(255,255,255,0.04);
#   border: 1px solid var(--border);
#   border-radius: 100px;
#   padding: 4px;
#   gap: 2px;
#   cursor: default;
#   user-select: none;
# }
# .lang-btn {
#   padding: 7px 20px;
#   border-radius: 100px;
#   font-size: 0.78rem;
#   font-weight: 600;
#   cursor: pointer !important;
#   transition: all 0.25s;
#   color: var(--muted);
#   border: none;
#   background: transparent;
#   font-family: 'Plus Jakarta Sans', sans-serif;
# }
# .lang-btn:hover { color: var(--text); }
# .lang-btn.active {
#   background: linear-gradient(135deg, var(--blue), var(--teal));
#   color: #080c14;
#   box-shadow: 0 4px 16px rgba(99,179,237,0.3);
# }

# /* ══════════════════════════════════
#    STEPPER
# ══════════════════════════════════ */
# .stepper-wrap {
#   width: 100%;
#   max-width: 680px;
#   margin: 40px auto 0;
#   padding: 0 24px;
# }
# .stepper {
#   display: flex;
#   align-items: center;
#   width: 100%;
# }
# .step-node {
#   display: flex;
#   flex-direction: column;
#   align-items: center;
#   gap: 8px;
#   flex-shrink: 0;
# }
# .step-ring {
#   width: 36px; height: 36px;
#   border-radius: 50%;
#   border: 2px solid rgba(255,255,255,0.1);
#   background: rgba(255,255,255,0.03);
#   display: flex; align-items: center; justify-content: center;
#   font-size: 0.72rem; font-weight: 700;
#   color: var(--muted);
#   transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
#   position: relative;
# }
# .step-node.active .step-ring {
#   border-color: var(--blue);
#   background: rgba(99,179,237,0.1);
#   color: var(--blue);
#   box-shadow: 0 0 0 5px rgba(99,179,237,0.1), 0 0 24px rgba(99,179,237,0.25);
# }
# .step-node.done .step-ring {
#   border-color: var(--teal);
#   background: var(--teal);
#   color: #080c14;
#   box-shadow: 0 0 16px rgba(79,209,197,0.4);
# }
# .step-lbl {
#   font-size: 0.68rem;
#   font-weight: 600;
#   letter-spacing: 0.5px;
#   color: var(--muted);
#   text-align: center;
#   white-space: nowrap;
#   transition: color 0.3s;
# }
# .step-node.active .step-lbl { color: var(--blue); }
# .step-node.done   .step-lbl { color: rgba(79,209,197,0.8); }

# .step-line {
#   flex: 1;
#   height: 1px;
#   margin: 0 12px;
#   background: var(--border);
#   position: relative;
#   top: -12px;
#   transition: background 0.5s;
# }
# .step-line.done {
#   background: linear-gradient(90deg, var(--teal), var(--blue));
# }

# /* pulse on active */
# @keyframes step-pulse {
#   0%,100% { box-shadow: 0 0 0 5px rgba(99,179,237,0.1), 0 0 24px rgba(99,179,237,0.25); }
#   50%      { box-shadow: 0 0 0 9px rgba(99,179,237,0.05), 0 0 32px rgba(99,179,237,0.35); }
# }
# .step-node.active .step-ring { animation: step-pulse 2.5s ease infinite; }

# /* ══════════════════════════════════
#    PAGE CONTENT  (centered column)
# ══════════════════════════════════ */
# .page-col {
#   width: 100%;
#   max-width: 560px;
#   margin: 0 auto;
#   padding: 48px 24px 100px;
# }

# /* ══════════════════════════════════
#    SLIDE ANIMATIONS
# ══════════════════════════════════ */
# .slide-fwd {
#   animation: sf var(--dur) cubic-bezier(0.22,1,0.36,1) both;
# }
# .slide-bwd {
#   animation: sb var(--dur) cubic-bezier(0.22,1,0.36,1) both;
# }
# @keyframes sf {
#   from { transform: translateX(60px) scale(0.97); opacity: 0; filter: blur(6px); }
#   to   { transform: translateX(0)    scale(1);    opacity: 1; filter: blur(0);   }
# }
# @keyframes sb {
#   from { transform: translateX(-60px) scale(0.97); opacity: 0; filter: blur(6px); }
#   to   { transform: translateX(0)     scale(1);    opacity: 1; filter: blur(0);   }
# }

# /* ══════════════════════════════════
#    HERO  (step 1 only)
# ══════════════════════════════════ */
# .hero {
#   text-align: center;
#   padding: 20px 0 44px;
# }
# .hero-badge {
#   display: inline-flex; align-items: center; gap: 8px;
#   padding: 6px 18px; border-radius: 100px;
#   background: rgba(99,179,237,0.07);
#   border: 1px solid rgba(99,179,237,0.2);
#   font-size: 0.62rem; font-weight: 700;
#   letter-spacing: 3px; text-transform: uppercase;
#   color: var(--blue);
#   margin-bottom: 28px;
# }
# .badge-dot {
#   width: 5px; height: 5px; border-radius: 50%;
#   background: var(--blue);
#   animation: blink 2.5s ease-in-out infinite;
# }
# @keyframes blink { 0%,100%{opacity:1;} 50%{opacity:0.2;} }

# .hero-h1 {
#   font-family: 'Fraunces', serif;
#   font-size: clamp(2.6rem, 7vw, 4.4rem);
#   font-weight: 600;
#   line-height: 1.08;
#   letter-spacing: -1.5px;
#   color: var(--white);
#   margin-bottom: 6px;
# }
# .hero-h1 .accent {
#   font-style: italic;
#   background: linear-gradient(135deg, var(--blue) 0%, var(--teal) 100%);
#   -webkit-background-clip: text;
#   -webkit-text-fill-color: transparent;
#   background-clip: text;
# }
# .hero-p {
#   font-size: 0.94rem;
#   color: var(--muted);
#   line-height: 1.85;
#   font-weight: 300;
#   max-width: 440px;
#   margin: 18px auto 0;
# }

# /* ── Stats ── */
# .stats {
#   display: grid;
#   grid-template-columns: repeat(3,1fr);
#   gap: 10px;
#   margin: 40px 0 44px;
# }
# .stat {
#   background: var(--bg-card);
#   border: 1px solid var(--border);
#   border-radius: 18px;
#   padding: 22px 14px;
#   text-align: center;
#   transition: border-color 0.3s, transform 0.3s;
# }
# .stat:hover { border-color: rgba(99,179,237,0.25); transform: translateY(-3px); }
# .stat-n {
#   font-family: 'Fraunces', serif;
#   font-size: 2.2rem; font-weight: 600;
#   color: var(--white); line-height: 1;
#   margin-bottom: 7px;
# }
# .stat-n em { font-style: normal; color: var(--blue); }
# .stat-l { font-size: 0.64rem; color: var(--muted); text-transform: uppercase; letter-spacing: 1px; }

# /* ══════════════════════════════════
#    GLASS CARD  (form container)
# ══════════════════════════════════ */
# .gcard {
#   background: var(--bg-card);
#   border: 1px solid var(--border);
#   border-radius: 24px;
#   padding: 40px 44px;
#   position: relative;
#   overflow: hidden;
#   box-shadow: 0 24px 64px rgba(0,0,0,0.35);
# }
# .gcard::before {
#   content: '';
#   position: absolute; top: 0; left: 0; right: 0; height: 1px;
#   background: linear-gradient(90deg, transparent, rgba(99,179,237,0.3), transparent);
# }

# /* greeting inside card */
# .greeting {
#   display: flex; align-items: center; gap: 14px;
#   padding: 16px 20px;
#   background: rgba(99,179,237,0.05);
#   border: 1px solid rgba(99,179,237,0.1);
#   border-radius: 16px;
#   margin-bottom: 28px;
# }
# .av {
#   width: 44px; height: 44px; border-radius: 50%; flex-shrink: 0;
#   background: linear-gradient(135deg, var(--blue), var(--teal));
#   display: flex; align-items: center; justify-content: center;
#   font-weight: 700; font-size: 1rem; color: #080c14;
#   box-shadow: 0 4px 16px rgba(99,179,237,0.25);
# }
# .av-name { font-weight: 600; color: var(--white); font-size: 0.95rem; }
# .av-sub  { font-size: 0.78rem; color: var(--muted); margin-top: 2px; }

# /* card heading */
# .card-h {
#   font-family: 'Fraunces', serif;
#   font-size: 1.55rem; font-weight: 600;
#   color: var(--white); letter-spacing: -0.5px;
#   margin-bottom: 4px;
# }
# .card-sub {
#   font-size: 0.84rem; color: var(--muted); font-weight: 300;
#   margin-bottom: 28px; line-height: 1.6;
# }

# /* field label */
# .flabel {
#   font-size: 0.61rem; font-weight: 700;
#   letter-spacing: 2.5px; text-transform: uppercase;
#   color: rgba(99,179,237,0.55);
#   display: block; margin-bottom: 10px;
# }

# /* ══════════════════════════════════
#    STREAMLIT WIDGET OVERRIDES
# ══════════════════════════════════ */
# /* text inputs */
# .stTextInput > div > div > input {
#   background: var(--bg-input) !important;
#   border: 1.5px solid rgba(255,255,255,0.08) !important;
#   border-radius: 14px !important;
#   color: var(--white) !important;
#   font-family: 'Plus Jakarta Sans', sans-serif !important;
#   font-size: 1rem !important;
#   font-weight: 400 !important;
#   padding: 17px 20px !important;
#   height: auto !important;
#   caret-color: var(--blue) !important;
#   transition: all 0.2s !important;
# }
# .stTextInput > div > div > input:focus {
#   border-color: var(--border-a) !important;
#   background: rgba(99,179,237,0.03) !important;
#   box-shadow: 0 0 0 3px rgba(99,179,237,0.07) !important;
#   outline: none !important;
# }
# .stTextInput > div > div > input::placeholder { color: rgba(180,195,225,0.2) !important; }
# .stTextInput label { display: none !important; }

# /* multiselect */
# .stMultiSelect > div > div {
#   background: var(--bg-input) !important;
#   border: 1.5px solid rgba(255,255,255,0.08) !important;
#   border-radius: 14px !important;
#   min-height: 56px !important;
#   transition: all 0.2s !important;
# }
# .stMultiSelect > div > div:focus-within {
#   border-color: var(--border-a) !important;
#   box-shadow: 0 0 0 3px rgba(99,179,237,0.07) !important;
# }
# .stMultiSelect span[data-baseweb="tag"] {
#   background: rgba(99,179,237,0.1) !important;
#   border: 1px solid rgba(99,179,237,0.28) !important;
#   border-radius: 10px !important;
#   color: var(--blue2) !important;
#   font-size: 0.79rem !important;
# }
# [data-baseweb="select"] input {
#   color: rgba(180,195,225,0.5) !important;
#   font-family: 'Plus Jakarta Sans', sans-serif !important;
# }
# [data-baseweb="menu"] {
#   background: #111827 !important;
#   border: 1px solid rgba(99,179,237,0.12) !important;
#   border-radius: 16px !important;
#   box-shadow: 0 24px 64px rgba(0,0,0,0.6) !important;
# }
# [data-baseweb="option"] {
#   color: rgba(180,195,225,0.8) !important;
#   font-family: 'Plus Jakarta Sans', sans-serif !important;
#   font-size: 0.87rem !important;
# }
# [data-baseweb="option"]:hover { background: rgba(99,179,237,0.08) !important; color: var(--white) !important; }
# .stMultiSelect label { display: none !important; }

# /* ── BUTTONS ── */
# .stButton > button {
#   font-family: 'Plus Jakarta Sans', sans-serif !important;
#   font-weight: 700 !important;
#   font-size: 0.84rem !important;
#   border-radius: 14px !important;
#   padding: 15px 28px !important;
#   border: none !important;
#   transition: all 0.2s cubic-bezier(0.34,1.56,0.64,1) !important;
#   height: auto !important;
#   letter-spacing: 0.4px !important;
#   width: 100% !important;
#   text-transform: uppercase !important;
#   cursor: pointer !important;
# }
# /* back / ghost */
# div[data-testid="column"]:first-child .stButton > button {
#   background: rgba(255,255,255,0.04) !important;
#   color: rgba(180,195,225,0.45) !important;
#   border: 1.5px solid rgba(255,255,255,0.07) !important;
# }
# div[data-testid="column"]:first-child .stButton > button:hover {
#   background: rgba(255,255,255,0.08) !important;
#   color: rgba(180,195,225,0.85) !important;
#   transform: translateY(-1px) !important;
# }
# /* primary CTA */
# div[data-testid="column"]:last-child .stButton > button {
#   background: linear-gradient(135deg, #63b3ed 0%, #4fd1c5 100%) !important;
#   color: #080c14 !important;
#   box-shadow: 0 8px 28px rgba(99,179,237,0.3), inset 0 1px 0 rgba(255,255,255,0.15) !important;
# }
# div[data-testid="column"]:last-child .stButton > button:hover {
#   transform: translateY(-3px) scale(1.015) !important;
#   box-shadow: 0 14px 40px rgba(99,179,237,0.45), inset 0 1px 0 rgba(255,255,255,0.15) !important;
# }
# div[data-testid="column"]:last-child .stButton > button:active {
#   transform: translateY(0) scale(0.98) !important;
# }
# /* single full-width */
# div[data-testid="stVerticalBlock"] > div > div > div > div > div:only-child .stButton > button {
#   background: linear-gradient(135deg, #63b3ed 0%, #4fd1c5 100%) !important;
#   color: #080c14 !important;
#   box-shadow: 0 8px 28px rgba(99,179,237,0.3), inset 0 1px 0 rgba(255,255,255,0.15) !important;
# }
# div[data-testid="stVerticalBlock"] > div > div > div > div > div:only-child .stButton > button:hover {
#   transform: translateY(-3px) scale(1.015) !important;
#   box-shadow: 0 14px 40px rgba(99,179,237,0.45) !important;
# }

# /* ══════════════════════════════════
#    RESULT CARDS
# ══════════════════════════════════ */
# .rc {
#   border-radius: 20px; margin-bottom: 12px;
#   border: 1px solid var(--border);
#   background: var(--bg-card);
#   overflow: hidden; position: relative;
#   transition: transform 0.3s, border-color 0.3s;
#   animation: rc-in 0.5s ease both;
# }
# .rc:hover { transform: translateX(5px); }
# .rc.r1 { border-left: 3px solid var(--blue); animation-delay: 0.08s; }
# .rc.r2 { border-left: 3px solid var(--teal); animation-delay: 0.18s; }
# .rc.r3 { border-left: 3px solid rgba(180,195,225,0.2); animation-delay: 0.28s; }
# .rc.r1::after {
#   content: ''; position: absolute; top:0; right:0; bottom:0; width:140px;
#   background: radial-gradient(ellipse at right, rgba(99,179,237,0.06), transparent);
# }
# @keyframes rc-in {
#   from { opacity:0; transform: translateY(20px); }
#   to   { opacity:1; transform: translateY(0); }
# }
# .rc-body { padding: 24px 28px; }
# .rc-rank { font-size: 0.6rem; font-weight: 700; letter-spacing: 2.5px; text-transform: uppercase; margin-bottom: 7px; }
# .r1 .rc-rank { color: var(--blue); }
# .r2 .rc-rank { color: var(--teal); }
# .r3 .rc-rank { color: var(--muted); }
# .rc-name {
#   font-family: 'Fraunces', serif;
#   font-size: 1.5rem; font-weight: 600;
#   color: var(--white); letter-spacing: -0.5px; margin-bottom: 9px;
# }
# .rc-desc { font-size: 0.83rem; color: var(--muted); line-height: 1.8; font-weight: 300; margin-bottom: 16px; }
# .rc-bar { display: flex; align-items: center; gap: 12px; }
# .rc-track { flex: 1; height: 3px; border-radius: 3px; background: rgba(255,255,255,0.05); overflow: hidden; }
# .rc-fill  { height: 100%; border-radius: 3px; }
# .r1 .rc-fill { background: linear-gradient(90deg, var(--blue), var(--blue2)); }
# .r2 .rc-fill { background: linear-gradient(90deg, var(--teal), #b2f5ea); }
# .r3 .rc-fill { background: rgba(180,195,225,0.25); }
# .rc-pct { font-size: 0.76rem; font-weight: 700; min-width: 44px; text-align: right; }
# .r1 .rc-pct { color: var(--blue); }
# .r2 .rc-pct { color: var(--teal); }
# .r3 .rc-pct { color: var(--muted); }

# /* ══════════════════════════════════
#    SHAP BOX
# ══════════════════════════════════ */
# .shap-box {
#   background: var(--bg-card); border: 1px solid var(--border);
#   border-radius: 20px; padding: 28px 30px; margin-top: 8px;
#   animation: rc-in 0.5s 0.4s ease both;
# }
# .shap-hd { display: flex; align-items: center; gap: 12px; margin-bottom: 18px; padding-bottom: 14px; border-bottom: 1px solid var(--border); }
# .shap-ico {
#   width: 34px; height: 34px; border-radius: 10px;
#   background: rgba(99,179,237,0.08); border: 1px solid rgba(99,179,237,0.18);
#   display: flex; align-items: center; justify-content: center; font-size: 0.95rem;
# }
# .shap-ttl { font-size: 0.84rem; color: var(--muted); }
# .shap-ttl strong { color: var(--white); font-weight: 600; }
# .pills { display: flex; flex-wrap: wrap; gap: 7px; margin-bottom: 18px; }
# .pill { padding: 6px 15px; border-radius: 100px; font-size: 0.75rem; font-weight: 600; letter-spacing: 0.2px; }
# .pp { background: rgba(104,211,145,0.08); border: 1px solid rgba(104,211,145,0.22); color: var(--green); }
# .pn { background: rgba(252,129,129,0.07); border: 1px solid rgba(252,129,129,0.18); color: var(--red); }
# .legend { display: flex; flex-wrap: wrap; gap: 18px; font-size: 0.69rem; color: rgba(180,195,225,0.28); }
# .leg-dot { width: 6px; height: 6px; border-radius: 50%; display: inline-block; margin-right: 5px; vertical-align: middle; }

# /* ══════════════════════════════════
#    MISC
# ══════════════════════════════════ */
# .sec-lbl {
#   font-size: 0.61rem; font-weight: 700; letter-spacing: 3px;
#   text-transform: uppercase; color: var(--muted);
#   display: flex; align-items: center; gap: 10px; margin-bottom: 18px;
# }
# .sec-lbl::after { content:''; flex:1; height:1px; background: var(--border); }

# .disc {
#   font-size: 0.69rem; color: rgba(180,195,225,0.2); line-height: 1.75;
#   padding: 12px 18px;
#   background: rgba(255,255,255,0.012);
#   border-radius: 12px; border: 1px solid rgba(255,255,255,0.04);
#   margin-top: 16px; text-align: center;
# }
# .disc::before { content: '⚠  '; }

# .stAlert {
#   background: rgba(252,129,129,0.06) !important;
#   border: 1px solid rgba(252,129,129,0.18) !important;
#   border-radius: 14px !important;
#   color: var(--red) !important;
# }
# .stProgress > div > div { background: rgba(255,255,255,0.04) !important; border-radius: 4px !important; }
# .stProgress > div > div > div { background: linear-gradient(90deg, var(--blue), var(--teal)) !important; border-radius: 4px !important; }
# .stSpinner > div { border-top-color: var(--blue) !important; }

# ::-webkit-scrollbar { width: 4px; }
# ::-webkit-scrollbar-track { background: transparent; }
# ::-webkit-scrollbar-thumb { background: rgba(99,179,237,0.2); border-radius: 4px; }
# </style>
# """

# st.markdown(CSS, unsafe_allow_html=True)

# @st.cache_resource
# def load_artifacts():
#     model     = joblib.load("models/logreg_model.joblib")
#     tfidf     = joblib.load("models/tfidf_vectorizer.joblib")
#     label_map = joblib.load("models/label_map.joblib")
#     desc_df   = pd.read_csv("data/raw/symptom_Description.csv")
#     desc_df.columns = desc_df.columns.str.strip()
#     desc_map  = dict(zip(desc_df["Disease"].str.strip(), desc_df["Description"].str.strip()))
#     return model, tfidf, label_map, desc_map

# model, tfidf, label_map, desc_map = load_artifacts()

# # ── BG ──────────────────────────────────────────────────
# st.markdown("""
# <div class="bg-layer">
#   <div class="orb orb-1"></div>
#   <div class="orb orb-2"></div>
#   <div class="orb orb-3"></div>
# </div>
# <div class="dot-grid"></div>
# <div class="shell">
# """, unsafe_allow_html=True)

# # ══════════════════════════════════════════════════════
# # TOP NAV  —  brand + language toggle (custom buttons)
# # ══════════════════════════════════════════════════════
# st.markdown(f"""
# <div class="topnav">
#   <div class="brand">MEDI<span class="brand-dot">.</span>SCAN
#     <span class="brand-tag">{tx['tagline']}</span>
#   </div>
#   <div class="lang-toggle">
#     <button class="lang-btn {'active' if lang=='en' else ''}"
#       onclick="window.location.href='?lang=en'" style="cursor:pointer">
#       English
#     </button>
#     <button class="lang-btn {'active' if lang=='ta' else ''}"
#       onclick="window.location.href='?lang=ta'" style="cursor:pointer">
#       தமிழ்
#     </button>
#   </div>
# </div>
# """, unsafe_allow_html=True)

# # URL-param language switching (backup via selectbox hidden)
# params = st.query_params
# if "lang" in params:
#     chosen = params["lang"]
#     if chosen in ("en","ta") and chosen != st.session_state.lang:
#         st.session_state.lang = chosen
#         st.rerun()

# lang = st.session_state.lang
# tx   = T[lang]
# s    = st.session_state.step

# # ══════════════════════════════════════════════════════
# # STEPPER
# # ══════════════════════════════════════════════════════
# def nc(n):
#     if s > n:  return "done"
#     if s == n: return "active"
#     return ""

# st.markdown(f"""
# <div class="stepper-wrap">
#   <div class="stepper">

#     <div class="step-node {nc(1)}">
#       <div class="step-ring">{'✓' if s>1 else '1'}</div>
#       <div class="step-lbl">{tx['step1']}</div>
#     </div>

#     <div class="step-line {'done' if s>1 else ''}"></div>

#     <div class="step-node {nc(2)}">
#       <div class="step-ring">{'✓' if s>2 else '2'}</div>
#       <div class="step-lbl">{tx['step2']}</div>
#     </div>

#     <div class="step-line {'done' if s>2 else ''}"></div>

#     <div class="step-node {nc(3)}">
#       <div class="step-ring">3</div>
#       <div class="step-lbl">{tx['step3']}</div>
#     </div>

#   </div>
# </div>
# """, unsafe_allow_html=True)

# # ══════════════════════════════════════════════════════
# # PAGE COLUMN  +  SLIDE WRAPPER
# # ══════════════════════════════════════════════════════
# st.markdown(f'<div class="page-col"><div class="{anim}">', unsafe_allow_html=True)

# # ──────────────────────────────────────────────────────
# # STEP 1 — Name
# # ──────────────────────────────────────────────────────
# if s == 1:
#     st.markdown(f"""
#     <div class="hero">
#       <div class="hero-badge"><div class="badge-dot"></div>{tx['tagline']}</div>
#       <div class="hero-h1">Know your body,<br><span class="accent">better.</span></div>
#       <p class="hero-p">{tx['hero_sub']}</p>
#     </div>
#     <div class="stats">
#       <div class="stat"><div class="stat-n">41<em>+</em></div><div class="stat-l">{tx['stat1_label']}</div></div>
#       <div class="stat"><div class="stat-n">132<em>+</em></div><div class="stat-l">{tx['stat2_label']}</div></div>
#       <div class="stat"><div class="stat-n">99<em>%</em></div><div class="stat-l">{tx['stat3_label']}</div></div>
#     </div>
#     """, unsafe_allow_html=True)

#     st.markdown('<div class="gcard">', unsafe_allow_html=True)
#     st.markdown(f'<span class="flabel">{tx["name_label"]}</span>', unsafe_allow_html=True)
#     name = st.text_input("n", placeholder=tx["name_placeholder"], label_visibility="collapsed", key="name_field")
#     st.markdown('<div style="height:10px"></div>', unsafe_allow_html=True)
#     c1, c2 = st.columns([1, 2])
#     with c2:
#         if st.button(f"{tx['continue']} →", key="btn1"):
#             if not name.strip():
#                 st.warning(tx["warn_name"])
#             else:
#                 st.session_state.name      = name.strip()
#                 st.session_state.direction = "forward"
#                 st.session_state.step      = 2
#                 st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="disc">{tx["disclaimer"]}</div>', unsafe_allow_html=True)

# # ──────────────────────────────────────────────────────
# # STEP 2 — Age
# # ──────────────────────────────────────────────────────
# elif s == 2:
#     initials = ''.join([w[0].upper() for w in st.session_state.name.split()[:2]])
#     st.markdown(f"""
#     <div class="gcard">
#       <div class="greeting">
#         <div class="av">{initials}</div>
#         <div>
#           <div class="av-name">{tx['welcome']} {st.session_state.name}</div>
#           <div class="av-sub">{tx['profile_sub']}</div>
#         </div>
#       </div>
#       <div class="card-h">{tx['age_heading']}</div>
#       <div class="card-sub">{tx['age_sub']}</div>
#     """, unsafe_allow_html=True)
#     st.markdown(f'<span class="flabel">{tx["age_label"]}</span>', unsafe_allow_html=True)
#     age = st.text_input("a", placeholder=tx["age_placeholder"], label_visibility="collapsed", key="age_field")
#     st.markdown('<div style="height:10px"></div>', unsafe_allow_html=True)
#     c1, c2 = st.columns(2)
#     with c1:
#         if st.button(f"← {tx['back']}", key="back2"):
#             st.session_state.direction = "backward"
#             st.session_state.step      = 1
#             st.rerun()
#     with c2:
#         if st.button(f"{tx['continue']} →", key="btn2"):
#             if not age.strip() or not age.strip().isdigit():
#                 st.warning(tx["warn_age"])
#             else:
#                 st.session_state.age       = age.strip()
#                 st.session_state.direction = "forward"
#                 st.session_state.step      = 3
#                 st.rerun()
#     st.markdown('</div>', unsafe_allow_html=True)
#     st.markdown(f'<div class="disc">{tx["disclaimer"]}</div>', unsafe_allow_html=True)

# # ──────────────────────────────────────────────────────
# # STEP 3 — Symptoms + Results
# # ──────────────────────────────────────────────────────
# elif s == 3:
#     initials = ''.join([w[0].upper() for w in st.session_state.name.split()[:2]])
#     st.markdown(f"""
#     <div class="gcard">
#       <div class="greeting">
#         <div class="av">{initials}</div>
#         <div>
#           <div class="av-name">{st.session_state.name} &nbsp;·&nbsp; {st.session_state.age} {tx['step2'].lower()}</div>
#           <div class="av-sub">{tx['symptom_greeting_sub']}</div>
#         </div>
#       </div>
#       <div class="card-h">{tx['symptom_heading']}</div>
#     """, unsafe_allow_html=True)

#     st.markdown(f'<span class="flabel">{tx["symptom_label"]}</span>', unsafe_allow_html=True)
#     selected_display = st.multiselect(
#         "sym", options=SYMPTOM_DISPLAY_LIST,
#         placeholder=tx["symptom_placeholder"],
#         label_visibility="collapsed", key="sym_field"
#     )
#     selected_en    = [SYMPTOM_OPTIONS[d] for d in selected_display] if lang == "ta" else selected_display
#     symptoms_input = " ".join(selected_en)

#     st.markdown('<div style="height:10px"></div>', unsafe_allow_html=True)
#     c1, c2 = st.columns(2)
#     with c1:
#         if st.button(f"← {tx['back']}", key="back3"):
#             st.session_state.direction = "backward"
#             st.session_state.step      = 2
#             st.rerun()
#     with c2:
#         analyse = st.button(f"{tx['analyse']} →", key="analyse")

#     st.markdown(f'<div class="disc" style="margin-top:16px">{tx["disclaimer"]}</div>', unsafe_allow_html=True)
#     st.markdown('</div>', unsafe_allow_html=True)

#     if analyse:
#         if not selected_display:
#             st.warning(tx["warn_symptom"])
#         else:
#             with st.spinner(""):
#                 X     = tfidf.transform([symptoms_input])
#                 probs = model.predict_proba(X)[0]
#                 top3  = np.argsort(probs)[::-1][:3]

#             medals = [tx["rank1"], tx["rank2"], tx["rank3"]]
#             ranks  = [tx["diag1"], tx["diag2"], tx["diag3"]]
#             rclass = ["r1", "r2", "r3"]

#             st.markdown('<div style="height:24px"></div>', unsafe_allow_html=True)
#             st.markdown(f'<div class="sec-lbl">{tx["results_header"]} — {st.session_state.name}</div>', unsafe_allow_html=True)

#             for i, idx in enumerate(top3):
#                 disease = label_map[idx]
#                 conf    = probs[idx] * 100
#                 desc    = desc_map.get(disease, tx["no_desc"])
#                 st.markdown(f"""
#                 <div class="rc {rclass[i]}">
#                   <div class="rc-body">
#                     <div class="rc-rank">{medals[i]} &nbsp;·&nbsp; {ranks[i]}</div>
#                     <div class="rc-name">{disease}</div>
#                     <div class="rc-desc">{desc}</div>
#                     <div class="rc-bar">
#                       <div class="rc-track"><div class="rc-fill" style="width:{int(conf)}%"></div></div>
#                       <div class="rc-pct">{conf:.1f}%</div>
#                     </div>
#                   </div>
#                 </div>
#                 """, unsafe_allow_html=True)

#             disease_shap, top_words = explain(symptoms_input)
#             pills_html = '<div class="pills">'
#             for word, score in top_words:
#                 cls   = "pp" if score >= 0 else "pn"
#                 arrow = "↑"  if score >= 0 else "↓"
#                 dw    = SYMPTOM_TA.get(word, word.replace("_"," ")) if lang=="ta" else word.replace("_"," ")
#                 pills_html += f'<span class="pill {cls}">{arrow} {dw}</span>'
#             pills_html += '</div>'

#             st.markdown(f"""
#             <div class="shap-box">
#               <div class="shap-hd">
#                 <div class="shap-ico">🔬</div>
#                 <div class="shap-ttl">{tx['shap_title']} — <strong>{disease_shap}</strong></div>
#               </div>
#               {pills_html}
#               <div class="legend">
#                 <span><span class="leg-dot" style="background:var(--green)"></span>{tx['legend_pos']}</span>
#                 <span><span class="leg-dot" style="background:var(--red)"></span>{tx['legend_neg']}</span>
#               </div>
#             </div>
#             """, unsafe_allow_html=True)

#             st.markdown('<div style="height:20px"></div>', unsafe_allow_html=True)
#             c1, c2 = st.columns([1,2])
#             with c2:
#                 if st.button(f"↺  {tx['new_scan']}", key="restart"):
#                     st.session_state.step      = 1
#                     st.session_state.direction = "backward"
#                     st.session_state.name      = ""
#                     st.session_state.age       = ""
#                     st.rerun()

# st.markdown('</div></div></div>', unsafe_allow_html=True)






import streamlit as st
import joblib
import numpy as np
import pandas as pd
import sys, os

sys.path.insert(0, os.path.dirname(__file__))
from src.explainer import explain

st.set_page_config(page_title="MediScan AI", page_icon="🧬", layout="centered")

# ── SYMPTOM TRANSLATIONS (Tamil) ──────────────────────
SYMPTOM_TA = {
    'abdominal_pain': 'வயிற்று வலி',
    'abnormal_menstruation': 'அசாதாரண மாதவிடாய்',
    'acidity': 'அமிலத்தன்மை',
    'acute_liver_failure': 'கடுமையான கல்லீரல் செயலிழப்பு',
    'altered_sensorium': 'மாற்றப்பட்ட உணர்வு நிலை',
    'anxiety': 'கவலை',
    'back_pain': 'முதுகு வலி',
    'belly_pain': 'வயிற்று வலி',
    'blackheads': 'கரும்புள்ளிகள்',
    'bladder_discomfort': 'சிறுநீர்ப்பை அசௌகரியம்',
    'blister': 'கொப்புளம்',
    'blood_in_sputum': 'சளியில் இரத்தம்',
    'bloody_stool': 'இரத்தம் கலந்த மலம்',
    'blurred_and_distorted_vision': 'மங்கலான மற்றும் திரிந்த பார்வை',
    'breathlessness': 'மூச்சுத் திணறல்',
    'brittle_nails': 'உடையும் நகங்கள்',
    'bruising': 'சிராய்ப்பு',
    'burning_micturition': 'எரிச்சலுடன் சிறுநீர் கழித்தல்',
    'chest_pain': 'நெஞ்சு வலி',
    'chills': 'குளிர் நடுக்கம்',
    'cold_hands_and_feets': 'கை மற்றும் கால் குளிர்ச்சி',
    'coma': 'கோமா',
    'congestion': 'மூக்கடைப்பு',
    'constipation': 'மலச்சிக்கல்',
    'continuous_feel_of_urine': 'தொடர்ச்சியான சிறுநீர் உணர்வு',
    'continuous_sneezing': 'தொடர்ச்சியான தும்மல்',
    'cough': 'இருமல்',
    'cramps': 'தசைப்பிடிப்பு',
    'dark_urine': 'அடர் நிற சிறுநீர்',
    'dehydration': 'நீர்ச்சத்து குறைபாடு',
    'depression': 'மனச்சோர்வு',
    'diarrhoea': 'வயிற்றுப்போக்கு',
    'dischromic _patches': 'நிற மாற்றப் புள்ளிகள்',
    'distention_of_abdomen': 'வயிறு உப்புசம்',
    'dizziness': 'தலை சுற்றல்',
    'drying_and_tingling_lips': 'உதடுகள் உலர்வு மற்றும் கூச்சம்',
    'enlarged_thyroid': 'விரிந்த தைரொய்டு',
    'excessive_hunger': 'அதிகப்படியான பசி',
    'extra_marital_contacts': 'திருமண வெளி தொடர்புகள்',
    'family_history': 'குடும்ப வரலாறு',
    'fast_heart_rate': 'வேகமான இதய துடிப்பு',
    'fatigue': 'சோர்வு',
    'fluid_overload': 'திரவ அதிகளவு',
    'foul_smell_of urine': 'சிறுநீரின் துர்நாற்றம்',
    'headache': 'தலைவலி',
    'high_fever': 'அதிக காய்ச்சல்',
    'hip_joint_pain': 'இடுப்பு மூட்டு வலி',
    'history_of_alcohol_consumption': 'மது அருந்திய வரலாறு',
    'increased_appetite': 'அதிகரித்த பசி',
    'indigestion': 'அஜீரணம்',
    'inflammatory_nails': 'அழற்சியுள்ள நகங்கள்',
    'internal_itching': 'உள் அரிப்பு',
    'irregular_sugar_level': 'ஒழுங்கற்ற சர்க்கரை அளவு',
    'irritability': 'எரிச்சல்',
    'irritation_in_anus': 'ஆசனவாயில் எரிச்சல்',
    'itching': 'அரிப்பு',
    'joint_pain': 'மூட்டு வலி',
    'knee_pain': 'முழங்கால் வலி',
    'lack_of_concentration': 'கவனக்குறைவு',
    'lethargy': 'சுணக்கம்',
    'loss_of_appetite': 'பசியின்மை',
    'loss_of_balance': 'சமநிலை இழப்பு',
    'loss_of_smell': 'மணம் உணரும் திறன் இழப்பு',
    'malaise': 'உடல் நலக்குறைவு',
    'mild_fever': 'லேசான காய்ச்சல்',
    'mood_swings': 'மனநிலை மாற்றங்கள்',
    'movement_stiffness': 'நகர்வு விறைப்பு',
    'mucoid_sputum': 'சளி நிறைந்த சளி',
    'muscle_pain': 'தசை வலி',
    'muscle_wasting': 'தசை அழிவு',
    'muscle_weakness': 'தசை பலவீனம்',
    'nausea': 'குமட்டல்',
    'neck_pain': 'கழுத்து வலி',
    'nodal_skin_eruptions': 'முடிச்சு தோல் வெடிப்புகள்',
    'obesity': 'உடல் பருமன்',
    'pain_behind_the_eyes': 'கண்களுக்கு பின் வலி',
    'pain_during_bowel_movements': 'மலம் கழிக்கும் போது வலி',
    'pain_in_anal_region': 'ஆசன வாய் பகுதியில் வலி',
    'painful_walking': 'வலியுடன் நடத்தல்',
    'palpitations': 'படபடப்பு',
    'passage_of_gases': 'வாயு வெளியேற்றம்',
    'patches_in_throat': 'தொண்டையில் புள்ளிகள்',
    'phlegm': 'சளி',
    'polyuria': 'அதிக சிறுநீர் கழித்தல்',
    'prominent_veins_on_calf': 'கன்னலில் நரம்புகள் தெரிதல்',
    'puffy_face_and_eyes': 'முகம் மற்றும் கண்கள் வீக்கம்',
    'pus_filled_pimples': 'சீழ் நிறைந்த பருக்கள்',
    'receiving_blood_transfusion': 'இரத்தமாற்றம் பெறுதல்',
    'receiving_unsterile_injections': 'கிருமி நீக்கமற்ற ஊசி பெறுதல்',
    'red_sore_around_nose': 'மூக்கைச் சுற்றி சிவந்த புண்',
    'red_spots_over_body': 'உடலில் சிவந்த புள்ளிகள்',
    'redness_of_eyes': 'கண்கள் சிவத்தல்',
    'restlessness': 'அமைதியின்மை',
    'runny_nose': 'மூக்கு ஒழுகுதல்',
    'rusty_sputum': 'துரு நிற சளி',
    'scurring': 'தழும்பு',
    'shivering': 'நடுக்கம்',
    'silver_like_dusting': 'வெள்ளி போன்ற தூசு',
    'sinus_pressure': 'சைனஸ் அழுத்தம்',
    'skin_peeling': 'தோல் உரிதல்',
    'skin_rash': 'தோல் தடிப்பு',
    'slurred_speech': 'தடுமாறும் பேச்சு',
    'small_dents_in_nails': 'நகங்களில் சிறிய குழிகள்',
    'spinning_movements': 'சுழலும் உணர்வு',
    'spotting_ urination': 'துளி சிறுநீர் கழித்தல்',
    'stiff_neck': 'கழுத்து விறைப்பு',
    'stomach_bleeding': 'வயிற்று இரத்தப்போக்கு',
    'stomach_pain': 'வயிற்று வலி',
    'sunken_eyes': 'கண்கள் உள்ளே சென்றிருத்தல்',
    'sweating': 'வியர்வை',
    'swelled_lymph_nodes': 'நிணநீர் முனைகள் வீக்கம்',
    'swelling_joints': 'மூட்டுகள் வீக்கம்',
    'swelling_of_stomach': 'வயிறு வீக்கம்',
    'swollen_blood_vessels': 'இரத்த நாளங்கள் வீக்கம்',
    'swollen_extremeties': 'கைகால்கள் வீக்கம்',
    'swollen_legs': 'கால்கள் வீக்கம்',
    'throat_irritation': 'தொண்டை எரிச்சல்',
    'toxic_look_(typhos)': 'நச்சு தோற்றம் (டைபஸ்)',
    'ulcers_on_tongue': 'நாக்கில் புண்கள்',
    'unsteadiness': 'தளர்வான நடை',
    'visual_disturbances': 'பார்வை இடையூறுகள்',
    'vomiting': 'வாந்தி',
    'watering_from_eyes': 'கண்ணீர் வடிதல்',
    'weakness_in_limbs': 'கைகால்களில் பலவீனம்',
    'weakness_of_one_body_side': 'உடலின் ஒரு பக்கம் பலவீனம்',
    'weight_gain': 'எடை அதிகரிப்பு',
    'weight_loss': 'எடை குறைப்பு',
    'yellow_crust_ooze': 'மஞ்சள் நிற மேல் படிவம்',
    'yellow_urine': 'மஞ்சள் சிறுநீர்',
    'yellowing_of_eyes': 'கண்கள் மஞ்சளாதல்',
    'yellowish_skin': 'மஞ்சள் தோல்',
}

# ── TRANSLATIONS ───────────────────────────────────────
T = {
    "en": {
        "tagline": "AI-POWERED DIAGNOSTICS",
        "hero_sub": "Advanced symptom analysis using machine learning — trained on thousands of clinical cases to help you understand what your body might be telling you.",
        "stat1_label": "Diseases Detected",
        "stat2_label": "Symptom Inputs",
        "stat3_label": "Model Accuracy",
        "step1": "Profile",
        "step2": "Age",
        "step3": "Symptoms",
        "name_label": "Your full name",
        "name_placeholder": "e.g. Santhiya S",
        "continue": "Continue",
        "back": "← Back",
        "welcome": "Welcome,",
        "profile_sub": "Let's build your health profile",
        "age_heading": "How old are you?",
        "age_sub": "Age helps our model provide more contextual and accurate predictions.",
        "age_label": "Your age",
        "age_placeholder": "e.g. 24",
        "symptom_greeting_sub": "Select all symptoms you are currently experiencing",
        "symptom_label": "Current symptoms",
        "symptom_placeholder": "Search — e.g. fatigue, headache, nausea...",
        "analyse": "Analyse Symptoms",
        "results_header": "Analysis results for",
        "rank1": "#1 Most Likely",
        "rank2": "#2 Possible",
        "rank3": "#3 Consider",
        "diag1": "Primary diagnosis",
        "diag2": "Secondary possibility",
        "diag3": "Alternative consideration",
        "shap_title": "Why this was predicted",
        "legend_pos": "Strongly linked to diagnosis",
        "legend_neg": "Not typical for this condition",
        "disclaimer": "⚠ For educational purposes only. Not a substitute for professional medical advice. Always consult a licensed physician.",
        "warn_name": "Please enter your name to continue.",
        "warn_age": "Please enter a valid age.",
        "warn_symptom": "Please select at least one symptom.",
        "no_desc": "No clinical description available.",
        "lang_label": "Language",
    },
    "ta": {
        "tagline": "செயற்கை நுண்ணறிவு நோயறிதல்",
        "hero_sub": "இயந்திர கற்றல் தொழில்நுட்பம் மூலம் அறிகுறிகளை ஆய்வு செய்து, உங்கள் உடல் என்ன சொல்கிறது என்பதை புரிந்துகொள்ள உதவுகிறோம்.",
        "stat1_label": "கண்டறியப்பட்ட நோய்கள்",
        "stat2_label": "அறிகுறி உள்ளீடுகள்",
        "stat3_label": "மாதிரி துல்லியம்",
        "step1": "சுயவிவரம்",
        "step2": "வயது",
        "step3": "அறிகுறிகள்",
        "name_label": "உங்கள் முழு பெயர்",
        "name_placeholder": "எ.கா. சந்தியா ச",
        "continue": "தொடரவும்",
        "back": "← திரும்பு",
        "welcome": "வணக்கம்,",
        "profile_sub": "உங்கள் உடல்நல சுயவிவரத்தை உருவாக்குவோம்",
        "age_heading": "உங்களுக்கு எத்தனை வயது?",
        "age_sub": "வயது தகவல் மூலம் எங்கள் மாதிரி மிகவும் துல்லியமான முடிவுகளை வழங்க முடியும்.",
        "age_label": "உங்கள் வயது",
        "age_placeholder": "எ.கா. 24",
        "symptom_greeting_sub": "நீங்கள் தற்போது அனுபவிக்கும் அறிகுறிகளை தேர்ந்தெடுக்கவும்",
        "symptom_label": "தற்போதைய அறிகுறிகள்",
        "symptom_placeholder": "தேடவும் — எ.கா. சோர்வு, தலைவலி, குமட்டல்...",
        "analyse": "அறிகுறிகளை பகுப்பாய்வு செய்",
        "results_header": "பகுப்பாய்வு முடிவுகள் —",
        "rank1": "#1 மிகவும் சாத்தியம்",
        "rank2": "#2 சாத்தியம்",
        "rank3": "#3 கருத்தில் கொள்க",
        "diag1": "முதன்மை நோயறிதல்",
        "diag2": "இரண்டாம் நிலை சாத்தியம்",
        "diag3": "மாற்று கருத்து",
        "shap_title": "இந்த முடிவு ஏன் வந்தது",
        "legend_pos": "நோயறிதலுடன் வலுவாக தொடர்புடையது",
        "legend_neg": "இந்த நிலைக்கு வழக்கமற்றது",
        "disclaimer": "⚠ கல்வி நோக்கங்களுக்காக மட்டுமே. தொழில்முறை மருத்துவ ஆலோசனைக்கு மாற்றாகாது. எப்போதும் தகுதிவாய்ந்த மருத்துவரை அணுகவும்.",
        "warn_name": "தொடர உங்கள் பெயரை உள்ளிடவும்.",
        "warn_age": "சரியான வயதை உள்ளிடவும்.",
        "warn_symptom": "குறைந்தது ஒரு அறிகுறியையாவது தேர்ந்தெடுக்கவும்.",
        "no_desc": "இந்த நிலைக்கு மருத்துவ விளக்கம் கிடைக்கவில்லை.",
        "lang_label": "மொழி",
    }
}

# ── Session state ──────────────────────────────────────
for k, v in [("step", 1), ("name", ""), ("age", ""), ("lang", "en")]:
    if k not in st.session_state:
        st.session_state[k] = v

lang = st.session_state.lang
tx = T[lang]

# ── Build symptom display options based on language ────
ALL_SYMPTOMS_EN = sorted([
    'abdominal_pain','abnormal_menstruation','acidity','acute_liver_failure',
    'altered_sensorium','anxiety','back_pain','belly_pain','blackheads',
    'bladder_discomfort','blister','blood_in_sputum','bloody_stool',
    'blurred_and_distorted_vision','breathlessness','brittle_nails','bruising',
    'burning_micturition','chest_pain','chills','cold_hands_and_feets','coma',
    'congestion','constipation','continuous_feel_of_urine','continuous_sneezing',
    'cough','cramps','dark_urine','dehydration','depression','diarrhoea',
    'dischromic _patches','distention_of_abdomen','dizziness',
    'drying_and_tingling_lips','enlarged_thyroid','excessive_hunger',
    'extra_marital_contacts','family_history','fast_heart_rate','fatigue',
    'fluid_overload','foul_smell_of urine','headache','high_fever',
    'hip_joint_pain','history_of_alcohol_consumption','increased_appetite',
    'indigestion','inflammatory_nails','internal_itching','irregular_sugar_level',
    'irritability','irritation_in_anus','itching','joint_pain','knee_pain',
    'lack_of_concentration','lethargy','loss_of_appetite','loss_of_balance',
    'loss_of_smell','malaise','mild_fever','mood_swings','movement_stiffness',
    'mucoid_sputum','muscle_pain','muscle_wasting','muscle_weakness','nausea',
    'neck_pain','nodal_skin_eruptions','obesity','pain_behind_the_eyes',
    'pain_during_bowel_movements','pain_in_anal_region','painful_walking',
    'palpitations','passage_of_gases','patches_in_throat','phlegm','polyuria',
    'prominent_veins_on_calf','puffy_face_and_eyes','pus_filled_pimples',
    'receiving_blood_transfusion','receiving_unsterile_injections',
    'red_sore_around_nose','red_spots_over_body','redness_of_eyes','restlessness',
    'runny_nose','rusty_sputum','scurring','shivering','silver_like_dusting',
    'sinus_pressure','skin_peeling','skin_rash','slurred_speech',
    'small_dents_in_nails','spinning_movements','spotting_ urination','stiff_neck',
    'stomach_bleeding','stomach_pain','sunken_eyes','sweating',
    'swelled_lymph_nodes','swelling_joints','swelling_of_stomach',
    'swollen_blood_vessels','swollen_extremeties','swollen_legs',
    'throat_irritation','toxic_look_(typhos)','ulcers_on_tongue','unsteadiness',
    'visual_disturbances','vomiting','watering_from_eyes','weakness_in_limbs',
    'weakness_of_one_body_side','weight_gain','weight_loss','yellow_crust_ooze',
    'yellow_urine','yellowing_of_eyes','yellowish_skin'
])

# For Tamil: show Tamil label but value is still the English key (for model)
if lang == "ta":
    SYMPTOM_OPTIONS = {SYMPTOM_TA.get(s, s.replace('_', ' ')): s for s in ALL_SYMPTOMS_EN}
    SYMPTOM_DISPLAY_LIST = sorted(SYMPTOM_OPTIONS.keys())
else:
    SYMPTOM_OPTIONS = {s: s for s in ALL_SYMPTOMS_EN}
    SYMPTOM_DISPLAY_LIST = ALL_SYMPTOMS_EN

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Sora:wght@300;400;500;600;700;800&family=DM+Serif+Display:ital@0;1&display=swap');

*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
html, body, .stApp { background: #07090f !important; color: #dde1f0; font-family: 'Sora', sans-serif; }
#MainMenu, footer, header, .stDeployButton { visibility: hidden !important; }
.block-container { padding: 0 1rem !important; max-width: 760px !important; margin: 0 auto !important; }
section[data-testid="stSidebar"] { display: none; }

/* ── BG ORBS ── */
.orb { position: fixed; border-radius: 50%; filter: blur(100px); pointer-events: none; z-index: 0; }
.o1 { width:700px;height:700px;background:rgba(56,189,248,0.055);top:-250px;right:-250px; }
.o2 { width:500px;height:500px;background:rgba(139,92,246,0.045);bottom:-150px;left:-200px; }
.o3 { width:350px;height:350px;background:rgba(20,184,166,0.035);top:45%;left:25%; }

/* ── PAGE WRAP ── */
.pw { position:relative;z-index:1;padding:40px 0 100px; }

/* ── TOP BAR ── */
.topbar {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    margin-bottom: 0px;
    padding-bottom: 0px;
}

/* ── BRAND HEADER (centered) ── */
.brand-header {
    text-align: center;
    padding: 32px 0 20px;
    margin-bottom: 8px;
}
.brand {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(3rem, 8vw, 5.5rem);
    color: #ffffff;
    letter-spacing: -2px;
    line-height: 1;
    margin-bottom: 8px;
}
.brand span { color: #7c3aed; }
.brand-sub {
    font-size: 0.72rem;
    letter-spacing: 3px;
    text-transform: uppercase;
    color: rgba(124,58,237,0.75);
    margin-bottom: 20px;
    font-weight: 500;
}
.hero-desc {
    font-size: 0.97rem;
    color: rgba(221,225,240,0.5);
    line-height: 1.8;
    font-weight: 300;
    max-width: 520px;
    margin: 0 auto 0;
}

/* ── STATS ── */
.stats {
    display: grid;
    grid-template-columns: repeat(3,1fr);
    gap: 10px;
    margin-bottom: 44px;
    margin-top: 36px;
}
.stat {
    padding: 22px 12px;
    background: rgba(255,255,255,0.025);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 20px;
    text-align: center;
}
.stat-n {
    font-family: 'DM Serif Display', serif;
    font-size: 2.2rem;
    color: #fff;
    line-height: 1;
    margin-bottom: 6px;
}
.stat-n em { font-style: normal; color: #7c3aed; }
.stat-l { font-size: 0.7rem; color: rgba(221,225,240,0.35); letter-spacing: 0.5px; }

/* ── STEP PILL ── */
.spill {
    display: flex;
    align-items: center;
    gap: 4px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 100px;
    padding: 5px;
    width: fit-content;
    margin: 0 auto 44px;
}
.si {
    display: flex; align-items: center; gap: 8px;
    padding: 9px 22px; border-radius: 100px;
    font-size: 0.78rem; font-weight: 500;
    color: rgba(255,255,255,0.28);
    transition: all 0.3s;
    white-space: nowrap;
}
.si.active { background: linear-gradient(135deg,#7c3aed,#a855f7); color:#fff; box-shadow:0 4px 20px rgba(124,58,237,0.3); }
.si.done { color: #a855f7; }
.sn {
    width:20px;height:20px;border-radius:50%;
    border:1.5px solid currentColor;
    display:flex;align-items:center;justify-content:center;
    font-size:0.62rem;flex-shrink:0;
}
.si.active .sn { background:rgba(255,255,255,0.22);border-color:white; }

/* ── FORM LABEL ── */
.fl {
    font-size: 0.68rem; font-weight: 600;
    letter-spacing: 1.5px; text-transform: uppercase;
    color: rgba(221,225,240,0.35); margin-bottom: 10px; display: block;
}

/* ── INPUT ── */
.stTextInput > div > div > input {
    background: #ffffff !important;
    border: 1.5px solid rgba(255,255,255,0.08) !important;
    border-radius: 16px !important;
    color: #000000 !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 1.05rem !important;
    padding: 18px 22px !important;
    height: auto !important;
    transition: all 0.25s !important;
    caret-color: #7c3aed !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(168,85,247,0.45) !important;
    background: rgba(124,58,237,0.04) !important;
    box-shadow: 0 0 0 4px rgba(124,58,237,0.08) !important;
    outline: none !important;
}
.stTextInput > div > div > input::placeholder { color: rgba(221,225,240,0.18) !important; }
.stTextInput label { display: none !important; }

/* ── MULTISELECT ── */
.stMultiSelect > div > div {
    background: rgba(255,255,255,0.04) !important;
    border: 1.5px solid rgba(255,255,255,0.08) !important;
    border-radius: 16px !important;
    min-height: 58px !important;
    transition: all 0.25s !important;
}
.stMultiSelect > div > div:focus-within {
    border-color: rgba(168,85,247,0.45) !important;
    box-shadow: 0 0 0 4px rgba(124,58,237,0.08) !important;
}
.stMultiSelect span[data-baseweb="tag"] {
    background: rgba(124,58,237,0.15) !important;
    border: 1px solid rgba(168,85,247,0.3) !important;
    border-radius: 10px !important;
    color: #c4b5fd !important;
    font-size: 0.8rem !important;
}
[data-baseweb="select"] input { color: rgba(221,225,240,0.5) !important; font-family: 'Sora',sans-serif !important; }
[data-baseweb="menu"] {
    background: #111420 !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 16px !important;
    box-shadow: 0 20px 60px rgba(0,0,0,0.5) !important;
}
[data-baseweb="option"] { color: rgba(221,225,240,0.7) !important; font-family: 'Sora',sans-serif !important; }
[data-baseweb="option"]:hover { background: rgba(124,58,237,0.1) !important; color: #fff !important; }
.stMultiSelect label { display: none !important; }

/* ── BUTTONS — base reset ── */
.stButton > button {
    font-family: 'Sora', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    border-radius: 14px !important;
    padding: 15px 28px !important;
    border: none !important;
    transition: all 0.25s ease !important;
    height: auto !important;
    letter-spacing: 0.3px !important;
    width: 100% !important;
}

/* Back button — ghost */
div[data-testid="column"]:first-child .stButton > button {
    background: rgba(255,255,255,0.05) !important;
    color: rgba(221,225,240,0.6) !important;
    border: 1.5px solid rgba(255,255,255,0.1) !important;
}
div[data-testid="column"]:first-child .stButton > button:hover {
    background: rgba(255,255,255,0.09) !important;
    color: rgba(221,225,240,0.9) !important;
}

/* Primary CTA */
div[data-testid="column"]:last-child .stButton > button {
    background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
    color: #fff !important;
    box-shadow: 0 8px 32px rgba(124,58,237,0.35) !important;
}
div[data-testid="column"]:last-child .stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 14px 44px rgba(124,58,237,0.48) !important;
}

/* Single full-width primary (step 1) */
div[data-testid="stVerticalBlock"] > div > div > div > div > div:only-child .stButton > button {
    background: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%) !important;
    color: #fff !important;
    box-shadow: 0 8px 32px rgba(124,58,237,0.35) !important;
}

/* ── LANGUAGE SELECTBOX — top right ── */
.lang-wrap { display: flex; justify-content: flex-end; margin-bottom: 16px; }
.lang-wrap .stSelectbox > div > div {
    background: rgba(124,58,237,0.1) !important;
    border: 1.5px solid rgba(168,85,247,0.3) !important;
    border-radius: 100px !important;
    color: #c4b5fd !important;
    font-family: 'Sora', sans-serif !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
    min-height: unset !important;
    padding: 0 !important;
    width: 160px !important;
    cursor: pointer !important;
}
.lang-wrap .stSelectbox > div > div > div {
    padding: 8px 18px !important;
    color: #c4b5fd !important;
}
.lang-wrap .stSelectbox svg { fill: #c4b5fd !important; }
.lang-wrap .stSelectbox label { display: none !important; }
[data-baseweb="popover"] [data-baseweb="menu"] {
    background: #1a1030 !important;
    border: 1px solid rgba(168,85,247,0.25) !important;
    border-radius: 14px !important;
}
[data-baseweb="popover"] [data-baseweb="option"] { color: #c4b5fd !important; font-size: 0.85rem !important; }
[data-baseweb="popover"] [data-baseweb="option"]:hover { background: rgba(124,58,237,0.15) !important; color: #fff !important; }

/* ── GREETING ── */
.greet {
    display:flex;align-items:center;gap:16px;
    padding:20px 24px;
    background:rgba(124,58,237,0.06);
    border:1px solid rgba(168,85,247,0.12);
    border-radius:18px;margin-bottom:28px;
}
.av {
    width:50px;height:50px;border-radius:50%;flex-shrink:0;
    background:linear-gradient(135deg,#7c3aed,#a855f7);
    display:flex;align-items:center;justify-content:center;
    font-family:'DM Serif Display',serif;font-size:1.3rem;color:#fff;
}
.gn { font-weight:600;color:#fff;font-size:1rem; }
.gs { font-size:0.82rem;color:rgba(221,225,240,0.4);margin-top:3px; }

/* ── SECTION HEADING ── */
.sec-head {
    font-size:0.68rem;font-weight:600;
    letter-spacing:2px;text-transform:uppercase;
    color:rgba(221,225,240,0.3);margin-bottom:22px;
}

/* ── RESULT CARDS ── */
.dc {
    padding:26px 30px;border-radius:20px;margin-bottom:14px;
    border:1px solid rgba(255,255,255,0.06);
    background:rgba(255,255,255,0.022);
    position:relative;overflow:hidden;
}
.dc::before {
    content:'';position:absolute;left:0;top:0;bottom:0;
    width:3px;border-radius:3px 0 0 3px;
}
.dc.r1::before{background:linear-gradient(180deg,#7c3aed,#a855f7);}
.dc.r2::before{background:rgba(168,85,247,0.45);}
.dc.r3::before{background:rgba(148,163,184,0.25);}
.drl{font-size:0.65rem;font-weight:600;letter-spacing:1.8px;text-transform:uppercase;margin-bottom:6px;}
.r1 .drl{color:#c4b5fd;} .r2 .drl{color:rgba(168,85,247,0.8);} .r3 .drl{color:rgba(148,163,184,0.5);}
.dn{font-family:'DM Serif Display',serif;font-size:1.55rem;color:#fff;margin-bottom:8px;line-height:1.2;}
.dd{font-size:0.85rem;color:rgba(221,225,240,0.4);line-height:1.75;font-weight:300;margin-bottom:16px;}
.cr{display:flex;align-items:center;gap:14px;}
.cbw{flex:1;height:3px;background:rgba(255,255,255,0.06);border-radius:3px;overflow:hidden;}
.cb{height:100%;background:linear-gradient(90deg,#7c3aed,#a855f7);border-radius:3px;}
.cl{font-size:0.78rem;font-weight:700;color:#c4b5fd;min-width:44px;text-align:right;}

/* ── SHAP ── */
.shap-box {
    background:rgba(255,255,255,0.022);
    border:1px solid rgba(255,255,255,0.06);
    border-radius:20px;padding:28px 30px;
}
.sh{display:flex;align-items:center;gap:12px;margin-bottom:20px;padding-bottom:16px;border-bottom:1px solid rgba(255,255,255,0.05);}
.si2{width:34px;height:34px;border-radius:10px;background:rgba(124,58,237,0.12);display:flex;align-items:center;justify-content:center;font-size:1rem;}
.st2{font-size:0.88rem;font-weight:500;color:rgba(221,225,240,0.55);}
.pw2{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:18px;}
.pill{padding:7px 18px;border-radius:100px;font-size:0.78rem;font-weight:500;letter-spacing:0.3px;}
.pp{background:rgba(20,184,166,0.1);border:1px solid rgba(20,184,166,0.22);color:#2dd4bf;}
.pn{background:rgba(239,68,68,0.07);border:1px solid rgba(239,68,68,0.18);color:#f87171;}
.leg{display:flex;flex-wrap:wrap;gap:20px;font-size:0.72rem;color:rgba(221,225,240,0.3);}
.ld{width:7px;height:7px;border-radius:50%;display:inline-block;margin-right:6px;vertical-align:middle;}

/* ── DISCLAIMER ── */
.disc{font-size:0.75rem;color:rgba(221,225,240,0.22);line-height:1.7;
    padding:14px 18px;background:rgba(255,255,255,0.018);
    border-radius:12px;border:1px solid rgba(255,255,255,0.04);margin-top:12px;}

/* ── PROGRESS / SPINNER / ALERT ── */
.stProgress>div>div{background:rgba(255,255,255,0.04)!important;border-radius:4px!important;}
.stProgress>div>div>div{background:linear-gradient(90deg,#7c3aed,#a855f7)!important;border-radius:4px!important;}
.stSpinner>div{border-top-color:#a855f7!important;}
.stAlert{background:rgba(239,68,68,0.07)!important;border:1px solid rgba(239,68,68,0.18)!important;border-radius:14px!important;color:#f87171!important;}
</style>
""", unsafe_allow_html=True)

# ── Load artifacts ─────────────────────────────────────
@st.cache_resource
def load_artifacts():
    model     = joblib.load("models/logreg_model.joblib")
    tfidf     = joblib.load("models/tfidf_vectorizer.joblib")
    label_map = joblib.load("models/label_map.joblib")
    desc_df   = pd.read_csv("data/raw/symptom_Description.csv")
    desc_df.columns = desc_df.columns.str.strip()
    desc_map  = dict(zip(desc_df["Disease"].str.strip(), desc_df["Description"].str.strip()))
    return model, tfidf, label_map, desc_map

model, tfidf, label_map, desc_map = load_artifacts()

# ── BG orbs ────────────────────────────────────────────
st.markdown('<div class="orb o1"></div><div class="orb o2"></div><div class="orb o3"></div><div class="pw">', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
# TOP BAR — Brand (center) + Language (right)
# ══════════════════════════════════════════════════════
col_title, col_lang = st.columns([5, 1])
with col_title:
    s = st.session_state.step
    # Only show big brand on step 1
    if s == 1:
        st.markdown(f"""
        <div class="brand-header">
            <div class="brand">Medi<span>Scan</span></div>
            <div class="brand-sub">{tx['tagline']}</div>
            <p class="hero-desc">{tx['hero_sub']}</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="text-align:center; padding: 20px 0 8px;">
            <div style="font-family:'DM Serif Display',serif; font-size:1.8rem; color:#fff; letter-spacing:-1px;">
                Medi<span style="color:#7c3aed">Scan</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

with col_lang:
    st.markdown('<div class="lang-wrap">', unsafe_allow_html=True)
    lang_choice = st.selectbox(
        "lang",
        options=["English", "தமிழ்"],
        index=0 if st.session_state.lang == "en" else 1,
        label_visibility="collapsed",
        key="lang_select"
    )
    new_lang = "en" if lang_choice == "English" else "ta"
    if new_lang != st.session_state.lang:
        st.session_state.lang = new_lang
        st.rerun()
    st.markdown('</div>', unsafe_allow_html=True)

# refresh after possible rerun
lang = st.session_state.lang
tx = T[lang]
s = st.session_state.step

def sc(n):
    if s > n: return "done"
    if s == n: return "active"
    return ""

# ══════════════════════════════════════════════════════
# STEP 1 — Name
# ══════════════════════════════════════════════════════
if s == 1:
    # Stats
    st.markdown(f"""
    <div class="stats">
        <div class="stat"><div class="stat-n">41<em>+</em></div><div class="stat-l">{tx['stat1_label']}</div></div>
        <div class="stat"><div class="stat-n">132<em>+</em></div><div class="stat-l">{tx['stat2_label']}</div></div>
        <div class="stat"><div class="stat-n">99<em>%</em></div><div class="stat-l">{tx['stat3_label']}</div></div>
    </div>
    """, unsafe_allow_html=True)

    # Step pill
    st.markdown(f"""
    <div class="spill">
        <div class="si {sc(1)}"><div class="sn">1</div>{tx['step1']}</div>
        <div class="si {sc(2)}"><div class="sn">2</div>{tx['step2']}</div>
        <div class="si {sc(3)}"><div class="sn">3</div>{tx['step3']}</div>
    </div>
    """, unsafe_allow_html=True)

    # Form
    st.markdown(f'<span class="fl">{tx["name_label"]}</span>', unsafe_allow_html=True)
    name = st.text_input("n", placeholder=tx["name_placeholder"], label_visibility="collapsed", key="name_field")
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col2:
        if st.button(tx["continue"] + "  →", key="btn1"):
            if not name.strip():
                st.warning(tx["warn_name"])
            else:
                st.session_state.name = name.strip()
                st.session_state.step = 2
                st.rerun()
    st.markdown(f'<div class="disc">{tx["disclaimer"]}</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
# STEP 2 — Age
# ══════════════════════════════════════════════════════
elif s == 2:
    initials = ''.join([w[0].upper() for w in st.session_state.name.split()[:2]])

    st.markdown(f"""
    <div class="spill">
        <div class="si {sc(1)}"><div class="sn">✓</div>{tx['step1']}</div>
        <div class="si {sc(2)}"><div class="sn">2</div>{tx['step2']}</div>
        <div class="si {sc(3)}"><div class="sn">3</div>{tx['step3']}</div>
    </div>
    <div class="greet">
        <div class="av">{initials}</div>
        <div>
            <div class="gn">{tx['welcome']} {st.session_state.name}</div>
            <div class="gs">{tx['profile_sub']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<span class="fl">{tx["age_label"]}</span>', unsafe_allow_html=True)
    age = st.text_input("a", placeholder=tx["age_placeholder"], label_visibility="collapsed", key="age_field")
    st.markdown("<br>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        if st.button(tx["back"], key="back2"):
            st.session_state.step = 1
            st.rerun()
    with col2:
        if st.button(tx["continue"] + "  →", key="btn2"):
            if not age.strip() or not age.strip().isdigit():
                st.warning(tx["warn_age"])
            else:
                st.session_state.age = age.strip()
                st.session_state.step = 3
                st.rerun()
    st.markdown(f'<div class="disc">{tx["disclaimer"]}</div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════
# STEP 3 — Symptoms + Results
# ══════════════════════════════════════════════════════
elif s == 3:
    initials = ''.join([w[0].upper() for w in st.session_state.name.split()[:2]])

    st.markdown(f"""
    <div class="spill">
        <div class="si done"><div class="sn">✓</div>{tx['step1']}</div>
        <div class="si done"><div class="sn">✓</div>{tx['step2']}</div>
        <div class="si active"><div class="sn">3</div>{tx['step3']}</div>
    </div>
    <div class="greet">
        <div class="av">{initials}</div>
        <div>
            <div class="gn">{st.session_state.name} · {st.session_state.age} {tx['step2'].lower()}</div>
            <div class="gs">{tx['symptom_greeting_sub']}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<span class="fl">{tx["symptom_label"]}</span>', unsafe_allow_html=True)

    # Show Tamil labels in multiselect when Tamil is selected
    selected_display = st.multiselect(
        "sym",
        options=SYMPTOM_DISPLAY_LIST,
        placeholder=tx["symptom_placeholder"],
        label_visibility="collapsed",
        key="sym_field"
    )

    # Map display labels back to English keys for the model
    if lang == "ta":
        selected_en = [SYMPTOM_OPTIONS[d] for d in selected_display]
    else:
        selected_en = selected_display

    symptoms_input = " ".join(selected_en)
    st.markdown("<br>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        if st.button(tx["back"], key="back3"):
            st.session_state.step = 2
            st.rerun()
    with col2:
        analyse = st.button(tx["analyse"] + "  →", key="analyse")

    st.markdown(f'<div class="disc" style="margin-top:20px">{tx["disclaimer"]}</div>', unsafe_allow_html=True)

    if analyse:
        if not selected_display:
            st.warning(tx["warn_symptom"])
        else:
            with st.spinner(""):
                X     = tfidf.transform([symptoms_input])
                probs = model.predict_proba(X)[0]
                top3  = np.argsort(probs)[::-1][:3]

            ranks  = [tx["diag1"], tx["diag2"], tx["diag3"]]
            medals = [tx["rank1"], tx["rank2"], tx["rank3"]]
            rclass = ["r1", "r2", "r3"]

            st.markdown(f'<div class="sec-head">{tx["results_header"]} {st.session_state.name}</div>', unsafe_allow_html=True)

            for i, idx in enumerate(top3):
                disease = label_map[idx]
                conf    = probs[idx] * 100
                desc    = desc_map.get(disease, tx["no_desc"])
                st.markdown(f"""
                <div class="dc {rclass[i]}">
                    <div class="drl">{medals[i]} · {ranks[i]}</div>
                    <div class="dn">{disease}</div>
                    <div class="dd">{desc}</div>
                    <div class="cr">
                        <div class="cbw"><div class="cb" style="width:{int(conf)}%"></div></div>
                        <div class="cl">{conf:.1f}%</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

            # SHAP
            disease_shap, top_words = explain(symptoms_input)
            pills_html = '<div class="pw2">'
            for word, score in top_words:
                cls   = "pp" if score >= 0 else "pn"
                arrow = "↑" if score >= 0 else "↓"
                display_word = SYMPTOM_TA.get(word, word.replace("_", " ")) if lang == "ta" else word.replace("_", " ")
                pills_html += f'<span class="pill {cls}">{arrow} {display_word}</span>'
            pills_html += '</div>'

            st.markdown(f"""
            <div class="shap-box">
                <div class="sh">
                    <div class="si2">🔬</div>
                    <div class="st2">{tx['shap_title']} — <strong style="color:#fff">{disease_shap}</strong></div>
                </div>
                {pills_html}
                <div class="leg">
                    <span><span class="ld" style="background:#2dd4bf"></span>{tx['legend_pos']}</span>
                    <span><span class="ld" style="background:#f87171"></span>{tx['legend_neg']}</span>
                </div>
            </div>
            """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)