import streamlit as st
import streamlit.components.v1 as components

# إعدادات صفحة ستريم ليت
st.set_page_config(page_title="Happy Birthday Yasso ❤️", layout="centered")

# إخفاء القوائم والعلامات المائية
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            .stApp {background-color: #050510;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

html_code = """
<!DOCTYPE html>
<html dir="rtl">
<head>
    <style>
        body {
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
        
        /* شاشة العد التنازلي */
        #countdown-screen {
            font-size: 5em;
            color: #ff3366;
            font-weight: bold;
            text-shadow: 0 0 30px rgba(255,51,102,0.8);
            animation: pulse 1s infinite alternate;
        }

        @keyframes pulse {
            0% { transform: scale(1); opacity: 0.8; }
            100% { transform: scale(1.1); opacity: 1; }
        }

        /* المحتوى الرئيسي للهدية */
        #main-content {
            display: none;
            text-align: center;
            width: 100%;
            height: 100vh;
            position: relative;
            background: radial-gradient(circle, #1a001a 0%, #050510 100%);
            overflow: hidden;
        }

        /* ستايل الكروت / الصور المتقاطعة أو المتحركة على شكل قلب */
        .card-container {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 320px;
            height: 400px;
            perspective: 1000px;
            cursor: pointer;
        }

        .card {
            width: 100%;
            height: 100%;
            position: absolute;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(255,51,102,0.4);
            border: 4px solid #ff3366;
            background-color: white;
            background-size: cover;
            background-position: center;
            transition: transform 0.6s ease;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            padding-bottom: 20px;
        }

        .card-text {
            background: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 8px 15px;
            border-radius: 15px;
            font-size: 16px;
            font-weight: bold;
            text-shadow: 0 0 5px #ff3366;
        }

        .instruction {
            position: absolute;
            bottom: 30px;
            width: 100%;
            text-align: center;
            color: #ff99bb;
            font-size: 18px;
            animation: bounce 1.5s infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
    </style>
</head>
<body>

    <!-- شاشة البداية والعد التنازلي زي الفيديو -->
    <div id="countdown-screen">3</div>

    <!-- المحتوى اللي هيظهر بعد العد -->
    <div id="main-content">
        <div class="card-container" id="cardContainer" onclick="nextCard()">
            <!-- سيتم تغيير الصور والرسائل هنا ديناميكياً -->
            <div class="card" id="currentCard" style="background-image: url('1.jpg');">
                <div class="card-text">Happy Birthday Yasso ❤️</div>
            </div>
        </div>
        <div class="instruction">اضغط على الكارت لتشوف الباقي ✨</div>
    </div>

    <script>
        // العد التنازلي زي الفيديو (3, 2, 1, HAPPY BIRTHDAY YASSO)
        let count = 3;
        const countdownEl = document.getElementById('countdown-screen');
        const mainContent = document.getElementById('main-content');

        const timer = setInterval(() => {
            count--;
            if (count > 0) {
                countdownEl.innerText = count;
            } else if (count === 0) {
                countdownEl.innerText = "HAPPY BIRTHDAY YASSO ✨";
                countdownEl.style.fontSize = "2.2em";
            } else {
                clearInterval(timer);
                countdownEl.style.display = 'none';
                mainContent.style.display = 'block';
            }
        }, 1000);

        // قائمة الصور والرسائل اللي بتظهر لما تقلب الكروت (تقدر تغير أسماء الصور والرسائل براحتك)
        const memories = [
            { img: '1.jpg', text: 'Happy Birthday Yasso ❤️' },
            { img: '2.jpg', text: 'أحلى دني وأجمل صدفة 🌸' },
            { img: '3.jpg', text: 'سنة حلوة تشبه عيونك ✨' },
            { img: '4.jpg', text: 'دائماً منورة حياتي يا ياسو 💖' }
        ];

        let currentIndex = 0;
        const currentCard = document.getElementById('currentCard');

        function nextCard() {
            currentIndex = (currentIndex + 1) % memories.length;
            
            // تأثير حركة خفيفة عند الضغط
            currentCard.style.transform = 'scale(0.9) rotate(5deg)';
            
            setTimeout(() => {
                currentCard.style.backgroundImage = `url('${memories[currentIndex].img}')`;
                currentCard.querySelector('.card-text').innerText = memories[currentIndex].text;
                currentCard.style.transform = 'scale(1) rotate(0deg)';
            }, 200);
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=750)