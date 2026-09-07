import streamlit as st
import streamlit.components.v1 as components

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

        #main-content {
            display: none;
            text-align: center;
            width: 100%;
            height: 100vh;
            position: relative;
            background: radial-gradient(circle, #1a001a 0%, #050510 100%);
            overflow: hidden;
        }

        .card-container {
            position: absolute;
            top: 45%;
            left: 50%;
            transform: translate(-50%, -50%);
            width: 300px;
            height: 380px;
            cursor: pointer;
        }

        .card {
            width: 100%;
            height: 100%;
            position: absolute;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(255,51,102,0.5);
            border: 4px solid #ff3366;
            background-color: #222;
            background-size: cover;
            background-position: center;
            display: flex;
            align-items: flex-end;
            justify-content: center;
            padding-bottom: 20px;
            transition: transform 0.3s ease;
        }

        .card:active {
            transform: scale(0.95);
        }

        .card-text {
            background: rgba(0, 0, 0, 0.8);
            color: white;
            padding: 8px 18px;
            border-radius: 15px;
            font-size: 16px;
            font-weight: bold;
            text-shadow: 0 0 5px #ff3366;
            border: 1px solid #ff3366;
        }

        .instruction {
            position: absolute;
            bottom: 40px;
            width: 100%;
            text-align: center;
            color: #ff99bb;
            font-size: 18px;
            animation: bounce 1.5s infinite;
        }

        @keyframes bounce {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-8px); }
        }
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

    <script>
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

        // قائمة الـ 13 صورة بامتداهم yassoX.jpeg مع رسائل رقيقة لكل صورة
        const memories = [
            { img: 'yasso1.jpeg', text: 'Happy Birthday Yasso ❤️' },
            { img: 'yasso2.jpeg', text: 'أحلى دني وأجمل صدفة 🌸' },
            { img: 'yasso3.jpeg', text: 'سنة حلوة تشبه عيونك ✨' },
            { img: 'yasso4.jpeg', text: 'دائماً منورة حياتي يا ياسو 💖' },
            { img: 'yasso5.jpeg', text: 'ضحكتك بالدنيا كلها 😍' },
            { img: 'yasso6.jpeg', text: 'ربنا يخليكي ليا دايماً 🧿' },
            { img: 'yasso7.jpeg', text: 'كل سنة وأنتِ أقرب لي قلبي 💞' },
            { img: 'yasso8.jpeg', text: 'يا أجمل ما شافته عيني ✨' },
            { img: 'yasso9.jpeg', text: 'سندريلا بتاعتي 👑' },
            { img: 'yasso10.jpeg', text: 'معاكِ الحياة أحلى كتير 🥰' },
            { img: 'yasso11.jpeg', text: 'ربنا ما يحرمني من وجودك 🤲' },
            { img: 'yasso12.jpeg', text: 'يا احلى فتاة في الكون 🌹' },
            { img: 'yasso13.jpeg', text: 'بحبك يا ياسو ❤️' }
        ];

        let currentIndex = 0;
        const currentCard = document.getElementById('currentCard');
        const cardText = document.getElementById('cardText');

        // تحميل أول صورة افتراضياً
        currentCard.style.backgroundImage = `url('${memories[0].img}')`;

        function nextCard() {
            currentIndex = (currentIndex + 1) % memories.length;
            currentCard.style.backgroundImage = `url('${memories[currentIndex].img}')`;
            cardText.innerText = memories[currentIndex].text;
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=750)