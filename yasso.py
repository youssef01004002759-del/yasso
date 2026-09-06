import streamlit as st
from datetime import datetime

# ==========================================

# إعدادات الصفحة

# ==========================================

st.set_page_config(
page_title="For Yasso ❤️",
page_icon="❤️",
layout="centered",
initial_sidebar_state="collapsed"
)

# ==========================================

# التصميم CSS

# ==========================================

st.markdown("""

<style>

    /* إخفاء عناصر Streamlit الافتراضية */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }


    /* الخلفية */
    .stApp {
        background: linear-gradient(135deg, #ffdde1, #ee9ca7);
        font-family: Arial, sans-serif;
    }


    /* حجم المحتوى */
    .block-container {
        padding-top: 3rem;
        padding-bottom: 3rem;
        max-width: 750px;
    }


    /* العناوين */
    h1 {
        text-align: center;
        color: white;
        font-size: 3rem;
        font-weight: bold;
        text-shadow: 2px 2px 12px rgba(0,0,0,0.15);
    }

    h2 {
        text-align: center;
        color: white;
    }

    h3 {
        text-align: center;
        color: white;
    }


    /* النصوص */
    p {
        color: white;
        font-size: 18px;
        text-align: center;
        line-height: 2;
        direction: rtl;
    }


    /* الكروت */
    .card {
        background: rgba(255,255,255,0.18);
        border: 1px solid rgba(255,255,255,0.3);
        padding: 25px;
        border-radius: 25px;
        margin: 20px 0;
        backdrop-filter: blur(10px);
        box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
    }


    /* الأزرار */
    .stButton > button {
        width: 100%;
        border-radius: 30px;
        border: none;
        padding: 14px 20px;
        font-size: 17px;
        font-weight: bold;
        background: white;
        color: #e75480;
        transition: all 0.3s ease;
        margin-top: 8px;
    }

    .stButton > button:hover {
        background: #e75480;
        color: white;
        transform: scale(1.03);
        border: none;
    }


    /* الصور */
    img {
        border-radius: 20px;
    }


    /* العداد */
    .counter {
        text-align: center;
        font-size: 40px;
        font-weight: bold;
        color: white;
    }


    /* النص الصغير */
    .small-text {
        font-size: 15px;
        opacity: 0.9;
    }

</style>

""", unsafe_allow_html=True)

# ==========================================

# التنقل بين الصفحات

# ==========================================

if "page" not in st.session_state:
st.session_state.page = "home"

def go_to(page):
st.session_state.page = page

# ==========================================

# الصفحة الرئيسية

# ==========================================

if st.session_state.page == "home":

```
st.markdown("<h1>For Yasso ❤️</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <p>

    يا ياسو ❤️<br><br>

    عملتلك المكان الصغير ده مخصوص ليكي.<br><br>

    مكان فيه شوية من ذكرياتنا،
    وكلام نفسي تفضلي فاكره،
    وحاجات صغيرة كلها بتفكرني بيكي.<br><br>

    فلو في يوم وحشتك،
    أو كنتي زعلانة،
    أو حتى حبيتي تبتسمي...<br><br>

    ارجعي هنا.<br><br>

    هتلاقيني سايبلك جزء مني ❤️

    </p>
</div>
""", unsafe_allow_html=True)


if st.button("ابدأي رحلتنا ❤️"):
    go_to("menu")
    st.rerun()
```

# ==========================================

# القائمة الرئيسية

# ==========================================

elif st.session_state.page == "menu":

```
st.markdown("<h1>أهلًا يا ياسو ❤️</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <p>

    ده عالمنا الصغير ❤️<br><br>

    اختاري أي حاجة وحاولي تكتشفيها...

    </p>
</div>
""", unsafe_allow_html=True)


if st.button("📸 ذكرياتنا"):
    go_to("memories")
    st.rerun()

if st.button("❤️ حاجات بحبها في ياسو"):
    go_to("reasons")
    st.rerun()

if st.button("💌 افتحي لما..."):
    go_to("openwhen")
    st.rerun()

if st.button("⏳ وقتنا سوا"):
    go_to("counter")
    st.rerun()

if st.button("🎁 رسالة من يوسف"):
    go_to("message")
    st.rerun()
```

# ==========================================

# صفحة الذكريات

# ==========================================

elif st.session_state.page == "memories":

```
st.markdown("<h1>ذكرياتنا 📸</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <p>

    كل صورة هنا وراها ذكرى.<br><br>

    وكل ذكرى معاكي
    هي واحدة من أحلى ذكرياتي ❤️

    </p>
</div>
""", unsafe_allow_html=True)


# ==========================================
# هنضيف الصور هنا بعدين
# ==========================================

# مثال:
# st.image("assets/images/photo1.jpg", use_container_width=True)

st.info("ذكرياتنا هتكون هنا قريب جدًا ❤️")


if st.button("⬅ رجوع لعالمنا"):
    go_to("menu")
    st.rerun()
```

# ==========================================

# حاجات بحبها فيها

# ==========================================

elif st.session_state.page == "reasons":

```
st.markdown("<h1>حاجات بحبها في ياسو ❤️</h1>", unsafe_allow_html=True)


reasons = [

    "ابتسامتك ممكن تصلح حتى أسوأ يوم ❤️",

    "الطريقة اللي بتفهميني بيها حتى وأنا مش عارف أشرح اللي جوايا.",

    "صوتك واحد من أكتر الأصوات اللي بحب أسمعها.",

    "معاكي حتى اللحظات العادية بتحس إنها مختلفة.",

    "بتضحكيني من غير حتى ما تحاولي.",

    "قلبك وطريقتك في الاهتمام بالناس اللي بتحبيهم.",

    "بتخليني دايمًا عايز أبقى نسخة أحسن من نفسي.",

    "حتى لما بتكوني رخمة جدًا... برضو بحبك 😂❤️",

    "عشان وجودك في حياتي مختلف.",

    "وعشان بكل بساطة... إنتي ياسو ❤️"

]


for reason in reasons:

    st.markdown(f"""
    <div class="card">
        <p>{reason}</p>
    </div>
    """, unsafe_allow_html=True)


if st.button("⬅ رجوع لعالمنا"):
    go_to("menu")
    st.rerun()
```

# ==========================================

# افتحي لما...

# ==========================================

elif st.session_state.page == "openwhen":

```
st.markdown("<h1>افتحي لما... 💌</h1>", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <p>

    مهما كان إحساسك دلوقتي،
    هتلاقي هنا حاجة مخصوص ليكي ❤️

    </p>
</div>
""")


# ==========================================
# لما تكوني زعلانة
# ==========================================

if st.button("😢 لما تكوني زعلانة"):

    st.markdown("""
    <div class="card">
        <p>

        يا ياسو ❤️<br><br>

        لو فتحتي الرسالة دي وإنتي زعلانة،
        فعايزك تعرفي حاجة.<br><br>

        إنتي أقوى بكتير من اللي إنتي متخيلاه.<br><br>

        وعديتي بحاجات كتير قبل كده،
        وحاجات يمكن وقتها كنتي فاكرة إنك مش هتقدري تعديها...
        بس عدت.<br><br>

        ومهما حصل،
        متنسيش إنك مش لوحدك.<br><br>

        في حد هنا بيحب يشوفك مبسوطة،
        وابتسامتك فارقة معاه أكتر ما تتخيلي ❤️

        </p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# لما أكون واحشك
# ==========================================

if st.button("🥺 لما أكون واحشك"):

    st.markdown("""
    <div class="card">
        <p>

        لو وحشتك في أي وقت...<br><br>

        افتحي الرسالة دي وافتكري إن المسافات،
        والانشغال،
        وأي حاجة بتحصل في يومنا...
        عمرها ما بتغير مكانتك عندي.<br><br>

        وممكن جدًا في نفس اللحظة دي
        تكوني وحشاني أنا كمان ❤️<br><br>

        فابتسمي شوية...
        وافتكري إننا أكيد هنتكلم قريب.

        </p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# لما تكوني زعلانة مني
# ==========================================

if st.button("😡 لما تكوني زعلانة مني"):

    st.markdown("""
    <div class="card">
        <p>

        طبعًا لو فتحتي دي،
        يبقى أنا غالبًا عملت مصيبة 😂<br><br>

        وممكن أكون غلطان فعلًا،
        وممكن أستاهل إنك تكوني زعلانة مني.<br><br>

        بس وسط كل ده،
        عايزك تفتكري حاجة واحدة بس...<br><br>

        إني بحبك.<br><br>

        حتى وإحنا مختلفين.<br>
        حتى وإنتي متعصبة مني.<br>
        وحتى لما تقولي مش هكلمك تاني 😂❤️<br><br>

        هنفضل نحل الموضوع...
        عشان وجودك يستاهل.

        </p>
    </div>
    """, unsafe_allow_html=True)


# ==========================================
# لما متعرفيش تنامي
# ==========================================

if st.button("🌙 لما متعرفيش تنامي"):

    st.markdown("""
    <div class="card">
        <p>

        يا ياسو 🌙❤️<br><br>

        اقفلي عينيكي شوية...<br><br>

        خدي نفس عميق.<br><br>

        وانسي كل اللي مضايقك،
        وكل حاجة مستنياكي بكرة.<br><br>

        وتخيلي إني جنبك،
        بنتكلم في أي كلام عشوائي،
        وبنضحك على حاجات ملهاش لازمة،
        لحد ما تنامي 😂❤️<br><br>

        تصبحين على خير يا أحلى ياسو 🌙❤️

        </p>
    </div>
    """, unsafe_allow_html=True)


if st.button("⬅ رجوع لعالمنا"):
    go_to("menu")
    st.rerun()
```

# ==========================================

# عداد الوقت

# ==========================================

elif st.session_state.page == "counter":

```
st.markdown("<h1>وقتنا سوا ⏳</h1>", unsafe_allow_html=True)


# ==========================================
# غير التاريخ ده بتاريخ بداية علاقتكم
# الصيغة:
# سنة، شهر، يوم
# ==========================================

start_date = datetime(2025, 1, 1)


now = datetime.now()

difference = now - start_date

days = difference.days
hours = difference.seconds // 3600
minutes = (difference.seconds % 3600) // 60


st.markdown(f"""
<div class="card">

    <h2>Youssef ❤️ Yasso</h2>

    <p>بقالنا سوا</p>

    <div class="counter">
        {days} يوم ❤️
    </div>

    <br>

    <h3>
    و {hours} ساعة و {minutes} دقيقة
    </h3>

    <p class="small-text">

    ولسه قدامنا ذكريات كتير نعملها سوا ❤️

    </p>

</div>
""", unsafe_allow_html=True)


if st.button("⬅ رجوع لعالمنا"):
    go_to("menu")
    st.rerun()
```

# ==========================================
# الرسالة الأخيرة
# ==========================================

elif st.session_state.page == "message":

    st.markdown(
        "<h1>رسالة من يوسف ❤️</h1>",
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="card">

        <p>

        يا ياسو ❤️<br><br>

        مش عارف إذا كان الكلام ممكن في يوم
        يوصف فعلًا إنتي بالنسبالي إيه.<br><br>

        بس أنا حبيت أعملك المكان الصغير ده،
        حاجة تكون مخصوص ليكي.<br><br>

        مكان فيه شوية مننا،
        وشوية ذكريات،
        وكلام ممكن ترجعي تقريه في أي وقت.<br><br>

        عايز أشكرك على كل ضحكة،
        وكل مكالمة،
        وكل لحظة،
        وكل ذكرى عملناها سوا.<br><br>

        وجودك عمل فرق،
        ويمكن أنا مش دايمًا بعرف أقول ده بالطريقة الصح،
        بس إنتي شخص مميز جدًا بالنسبالي.<br><br>

        ولو في يوم نسيتي ده...<br><br>

        ارجعي هنا ❤️<br><br>

        واقري الكلام ده تاني.<br><br>

        وافتكري إن في حد
        أخد وقت من حياته وعمل عالم صغير مخصوص ليكي.<br><br>

        عشان بكل بساطة...<br><br>

        إنتي تستاهلي ❤️<br><br>

        بحبك يا ياسو ❤️

        </p>

    </div>
    """
        st.rerun()
