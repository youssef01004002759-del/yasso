import streamlit as st
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title="Happy Birthday Yasso ❤️", layout="centered")

hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp {background-color: #050510;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# دالة لقراءة الـ 13 صورة وتحويلها برمجياً لداخل المتصفح مباشرة لضمان ظهورها
def get_image_base64(path):
    if os.path.exists(path):
        with open(path, "rb") as img_file:
            encoded = base64.b64encode(img_file.read()).decode()
            return f"data:image/jpeg;base64,{encoded}"
    return ""

# تجهيز الـ 13 صورة
images_list = []
for i in range(1, 14):
    img_b64 = get_image_base64(f"yasso{i}.jpeg")
    if img_b64:
        images_list.append(img_b64)

# تحويل الليست لـ JavaScript Array بشكل صحيح وخالٍ من الأخطاء
js_array = '["' + '", "'.join(images_list) + '"]'

html_code = f"""
<!DOCTYPE html>
<html dir="rtl">
<head>
    <style>
        body {{
            background-color: #050510;
            margin: 0;
            padding: 0;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
            height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
        }
        
        /* شاشة العد التنازلي (3, 2, 1) */
        #countdown-screen {{
            font-size: 4.5em;
            color: #ff3366;
            font-weight: bold;
            text-shadow: 0 0 30px rgba(255,51,102,0.8);
            animation: pulse 1s infinite alternate;
            text-align: center;
        }}

        @keyframes pulse {{
            0% {{ transform: scale(1); opacity: 0.8; }}
            100% {{ transform: scale(1.08); opacity: 1; }}
        }}

        #main-content {{
            display: none;
            text-align: center;
            width: 100%;
            height: 100vh;
            position: relative;
            background: radial-gradient(circle, #1a001a 0%, #050510 100%);
            overflow: hidden;
        }}

        /* حاوية الكروت التفاعلية */
        .card-container {{
            position: absolute;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 280px;
            height: 370px;
            cursor: pointer;
        }}

        .card {{
            width: 100%;
            height: 100%;
            position: absolute;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(255,51,102,0.6);
            border: 4px solid #ff3366;
            background-color: #111;
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            padding-bottom: 20px;
            transition: transform 0.2s ease;
        }}

        .card:active {{
            transform: scale(0.96);
        }}

        .card-text {{
            background: rgba(0, 0, 0, 0.85);
            color: white;
            padding: 8px 18px;
            border-radius: 15px;
            font-size: 15px;
            font-weight: bold;
            text-shadow: 0 0 5px #ff3366;
            border: 1px solid #ff3366;
        }}

        .instruction {{
            position: absolute;
            bottom: 30px;
            width: 100%;
            text-align: center;
            color: #ff99bb;
            font-size: 17px;
            animation: bounce 1.5s infinite;
        }}

        @keyframes bounce {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-8px); }}
        }}

        /* شاشة النهاية (تجميع الصور على شكل قلب) */
        #heart-screen {{
            display: none;
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            background: #050510;
            align-items: center;
            justify-content: center;
            flex-direction: column;
            padding: 10px;
            box-sizing: border-box;
        }}

        .heart-grid {{
            display: grid;
            grid-template-columns: repeat(4, 65px);
            gap: 8px;
            justify-content: center;
            align-content: center;
            animation: fadeIn 1.2s ease;
        }}

        .heart-grid img {{
            width: 65px;
            height: 65px;
            object-fit: cover;
            border-radius: 12px;
            border: 2px solid #ff3366;
            box-shadow: 0 0 10px rgba(255,51,102,0.5);
        }}
    </style>
</head>
<body>

    <div id="countdown-screen">3</div>

    <div id="main-content">
        <div class="card-container" onclick="nextCard()">
            <div class="card" id="currentCard">
                <div class="card-text" id="cardText">Happy Birthday Yasso ❤️</div>
            </div>
        </div>
        <div class="instruction">اضغط على الكارت لتشوف الذكريات ✨</div>
    </div>

    <div id="heart-screen">
        <h2 style="color: #ff3366; margin-bottom: 12px; font-size: 1.5em; text-shadow: 0 0 10px #ff3366; text-align:center;">
            كل سنة وأنتِ أقرب لي قلبي يا ياسو ❤️✨
        </h2>
        <div class="heart-grid" id="heartGrid"></div>
    </div>

    <script>
        const images = {js_array};
        
        let count = 3;
        const countdownEl = document.getElementById('countdown-screen');
        const mainContent = document.getElementById('main-content');

        // تسلسل العد التنازلي تماماً مثل الفيديو
        const timer = setInterval(() => {{
            count--;
            if (count === 2) {{
                countdownEl.innerText = "2";
            }} else if (count === 1) {{
                countdownEl.innerText = "1";
            }} else if (count === 0) {{
                countdownEl.innerText = "HAPPY\\nBIRTHDAY\\nYASSO ✨";
                countdownEl.style.fontSize = "2.5em";
                countdownEl.style.whiteSpace = "pre-line";
            }} else {{
                clearInterval(timer);
                countdownEl.style.display = 'none';
                mainContent.style.display = 'block';
            }}
        }}, 1000);

        const messages = [
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
            'يا احلى فتاة في الكون 🌹',
            'بحبك يا ياسو ❤️'
        ];

        let currentIndex = 0;
        const currentCard = document.getElementById('currentCard');
        const cardText = document.getElementById('cardText');

        if (images.length > 0) {{
            currentCard.style.backgroundImage = `url('${{images[0]}}')`;
        }}

        function nextCard() {{
            currentIndex++;
            if (currentIndex < images.length) {{
                currentCard.style.backgroundImage = `url('${{images[currentIndex]}}')`;
                cardText.innerText = messages[currentIndex] || 'Happy Birthday Yasso ❤️';
            }} else {{
                // عند الانتهاء من عرض الـ 13 صورة، يتم إظهار شاشة شبكة القلب الرومانسية
                mainContent.style.display = 'none';
                const heartScreen = document.getElementById('heart-screen');
                const heartGrid = document.getElementById('heartGrid');
                heartScreen.style.display = 'flex';
                
                heartGrid.innerHTML = '';
                images.forEach(imgUrl => {{
                    const imgElem = document.createElement('img');
                    imgElem.src = imgUrl;
                    heartGrid.appendChild(imgElem);
                }});
            }}
        }}
    </script>
</body>
</html>
"""

components.html(html_code, height=750)