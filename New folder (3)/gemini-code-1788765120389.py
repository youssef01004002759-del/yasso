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

# قائمة الرسائل
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

# استخدام حالة التطبيق (Session State) للقلب بين الصور بضغطة زرار احترافية وآمنة 100% في Streamlit
if 'page' not in st.session_state:
    st.session_state.page = 'countdown' # ممكن تبدأ بـ 'main' لو عايز تتخطى العد التنازلي فوراً

if 'img_index' not in st.session_state:
    st.session_state.img_index = 0

# تصميم الشاشة باستخدام عناصر Streamlit الخالصة لضمان عدم تلف الصور أبداً
st.markdown("""
    <style>
    .birthday-card {
        background-color: #111;
        border: 4px solid #ff3366;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        box-shadow: 0 10px 30px rgba(255,51,102,0.6);
        max-width: 350px;
        margin: 0 auto;
    }
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

# عرض الصور بالترتيب مع رسائلها
idx = st.session_state.img_index
img_path = f"yasso{idx + 1}.jpeg"

if idx < 13:
    st.markdown("<h2 style='text-align: center; color: #ff3366; text-shadow: 0 0 10px #ff3366;'>Happy Birthday Yasso ❤️✨</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if os.path.exists(img_path):
            st.image(img_path, use_container_width=True)
        else:
            st.error(f"الصورة {img_path} غير موجودة في المجلد!")
            
        st.markdown(f"<div style='text-align:center;'><div class='caption-box'>{messages[idx]}</div></div>", unsafe_allow_html=True)
        
        st.write("")
        if st.button("✨ اضغط هنا لرؤية الذكرى التالية ✨", use_container_width=True):
            st.session_state.img_index += 1
            st.rerun()
else:
    # شاشة النهاية (تجميع الصور على شكل شبكة قلب)
    st.markdown("<h1 style='text-align: center; color: #ff3366; text-shadow: 0 0 15px #ff3366;'>كل سنة وأنتِ منورة حياتي يا ياسو ❤️✨</h1>", unsafe_allow_html=True)
    st.write("---")
    
    # عرض الصور في شبكة منظمة وجميلة جداً
    cols = st.columns(4)
    for i in range(13):
        p = f"yasso{i+1}.jpeg"
        if os.path.exists(p):
            with cols[i % 4]:
                st.image(p, use_container_width=True)
                
    st.write("")
    if st.button("🔄 إعادة العرض من جديد", use_container_width=True):
        st.session_state.img_index = 0
        st.rerun()