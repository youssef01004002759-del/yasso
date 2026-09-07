import streamlit as st
import os

st.set_page_config(page_title="Happy Birthday Yasso ❤️", layout="centered")

# إخفاء واجهة ستريم ليت
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp {background-color: #050510;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# قائمة الرسائل الـ 13
messages = [
    'Happy Birthday Yasso ❤️',
    'أحلى دنيا وأجمل صدفة 🌸',
    'سنة حلوة تشبه عيونك ✨',
    'دائماً منورة حياتي يا ياسو 💖',
    'ضحكتك بالدنيا كلها 😍',
    'ربنا يخليكي ليا دايماً 🧿',
    'كل سنة وأنتِ أقرب لي قلبي 💞',
    'يا أجمل ما شافته عيني ✨',
    'سندريلا بتاعتي 👑',
    'معاكِ الحياة أحلى كتير 🥰',
    'ربنا ما يحرمني من وجودك 🤲',
    'يا أحلى فتاة في الكون 🌹',
    'بحبك يا ياسو ❤️'
]

if 'img_index' not in st.session_state:
    st.session_state.img_index = 0

# دالة ذكية للبحث عن الصورة بأي امتداد متاح (.jpeg أو .jpg أو .PNG) لعدم إظهار خطأ مفقودة
def find_image(base_name):
    for ext in ['.jpeg', '.jpg', '.JPG', '.JPEG', '.png', '.PNG']:
        full_path = base_name + ext
        if os.path.exists(full_path):
            return full_path
    return None

st.markdown("""
    <style>
    .caption-box {
        background: rgba(0, 0, 0, 0.85);
        color: white;
        padding: 10px 20px;
        border-radius: 15px;
        font-size: 16px;
        font-weight: bold;
        border: 1px solid #ff3366;
        margin-top: 15px;
        display: inline-block;
        text-shadow: 0 0 5px #ff3366;
    }
    </style>
""", unsafe_allow_html=True)

idx = st.session_state.img_index

if idx < 13:
    st.markdown("<h2 style='text-align: center; color: #ff3366; text-shadow: 0 0 10px #ff3366;'>Happy Birthday Yasso ❤️✨</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        img_file = find_image(f"yasso{idx + 1}")
        if img_file:
            st.image(img_file, use_container_width=True)
        else:
            st.error(f"تأكد من وجود الصورة yasso{idx + 1} في مجلد المشروع!")
            
        st.markdown(f"<div style='text-align:center;'><div class='caption-box'>{messages[idx]}</div></div>", unsafe_allow_html=True)
        
        st.write("")
        if st.button("✨ اضغط هنا لرؤية الذكرى التالية ✨", use_container_width=True):
            st.session_state.img_index += 1
            st.rerun()
else:
    # شاشة النهاية (تجميع الصور على شكل قلب)
    st.markdown("<h1 style='text-align: center; color: #ff3366; text-shadow: 0 0 15px #ff3366;'>كل سنة وأنتِ منورة حياتي يا ياسو ❤️✨</h1>", unsafe_allow_html=True)
    st.write("---")
    
    cols = st.columns(4)
    for i in range(13):
        img_file = find_image(f"yasso{i+1}")
        if img_file:
            with cols[i % 4]:
                st.image(img_file, use_container_width=True)
                
    st.write("")
    if st.button("🔄 إعادة العرض من جديد", use_container_width=True):
        st.session_state.img_index = 0
        st.rerun()