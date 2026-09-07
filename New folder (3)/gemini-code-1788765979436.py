import streamlit as st

st.set_page_config(page_title="Happy Birthday Yasso ❤️", layout="centered")

# إخفاء واجهة Streamlit لتبدو الموقع كأنه صفحة ويب احترافية
st.markdown("""
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp {background-color: #050510;}
    .caption-box {
        background: rgba(0, 0, 0, 0.85);
        color: white;
        padding: 10px 20px;
        border-radius: 15px;
        font-size: 17px;
        font-weight: bold;
        border: 1px solid #ff3366;
        margin-top: 15px;
        display: inline-block;
        text-shadow: 0 0 5px #ff3366;
    }
    </style>
""", unsafe_allow_html=True)

# قائمة الرسائل المتوافقة مع الصور الـ 13 بالترتيب
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

# تخزين مؤشر الصورة الحالي في جلسة المستخدم
if 'img_index' not in st.session_state:
    st.session_state.img_index = 0

idx = st.session_state.img_index

if idx < 13:
    st.markdown("<h2 style='text-align: center; color: #ff3366; text-shadow: 0 0 10px #ff3366;'>Happy Birthday Yasso ❤️✨</h2>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        # استخدام اسم الصورة مباشرة دون تعقيد لضمان عملها 100%
        img_name = f"yasso{idx + 1}.jpeg"
        
        try:
            st.image(img_name, use_container_width=True)
        except Exception:
            st.error(f"تأكد من وجود الملف {img_name} في نفس المجلد بجانب ملف الكود.")
            
        st.markdown(f"<div style='text-align:center;'><div class='caption-box'>{messages[idx]}</div></div>", unsafe_allow_html=True)
        
        st.write("")
        if st.button("✨ اضغط هنا لرؤية الذكرى التالية ✨", use_container_width=True):
            st.session_state.img_index += 1
            st.rerun()
else:
    # شاشة النهاية (تجميع كل الصور في شبكة منسقة وجميلة)
    st.markdown("<h1 style='text-align: center; color: #ff3366; text-shadow: 0 0 15px #ff3366;'>كل سنة وأنتِ منورة حياتي يا ياسو ❤️✨</h1>", unsafe_allow_html=True)
    st.write("---")
    
    cols = st.columns(4)
    for i in range(13):
        p = f"yasso{i+1}.jpeg"
        with cols[i % 4]:
            try:
                st.image(p, use_container_width=True)
            except:
                pass
                
    st.write("")
    if st.button("🔄 إعادة العرض من جديد", use_container_width=True):
        st.session_state.img_index = 0
        st.rerun()