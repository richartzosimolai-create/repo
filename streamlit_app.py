import streamlit as st
import random
import time

st.set_page_config(page_title="Ms Ocha Class", page_icon="🎮", layout="wide")

st.markdown("""
    <style>
   
.stButton > button { 
    width: 100%; 
    height: 60px; 
    font-size: 20px; 
    border-radius: 12px;  
    transition: all 0.3s;
}


.letter-btn {
    width: 100%;
    height: 50px;
    font-size: 18px;
    font-weight: bold;
    border-radius: 8px;
    border: 2px solid #667eea;
    background: white;
    color: #333;
    cursor: pointer;
    transition: all 0.2s;
}
.letter-btn:hover:not(:disabled) {
    background: #667eea;
    color: white;
    transform: scale(1.05);
}
.letter-btn:disabled {
    opacity: 0.4;
    cursor: not-allowed;
}
.letter-btn.correct {
    background: #4CAF50;
    color: white;
    border-color: #4CAF50;
}
.letter-btn.wrong {
    background: #f44336;
    color: white;
    border-color: #f44336;
}
    
    .game-card { 
        color: #000000;
        padding: 20px; 
        border-radius: 20px; 
        background: white; 
        box-shadow: 0 10px 30px rgba(0,0,0,0.2); 
        text-align: center; 
        margin: 10px;
        transition: all 0.3s;
    }
    .game-card:hover {
        transform: translateY(-10px);
    }
    .circle { 
        width: 150px; 
        height: 150px; 
        border-radius: 50%; 
        margin: 0 auto 15px; 
        display: flex; 
        align-items: center; 
        justify-content: center; 
        font-size: 4em; 
        color: white;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }
    .badge {
        display: inline-block;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 0.75em;
        font-weight: bold;
        color: white;
    }
    .badge-active { background: #4CAF50; }
    .badge-coming { background: #9E9E9E; }
    .hangman-art {
        font-size: 1.2em;
        font-family: monospace;
        text-align: center;
        background: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
        margin: 10px 0;
        white-space: pre;
    }

    /* Tombol Back panah di pojok kanan bawah */
    .back-btn-container {
        position: fixed;
        bottom: 80px;
        right: 20px;
        z-index: 999;
    }
    .back-btn-container .stButton > button {
        width: 60px !important;
        height: 60px !important;
        border-radius: 50% !important;
        background: #667eea !important;
        color: white !important;
        font-size: 28px !important;
        font-weight: bold !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        padding: 0 !important;
        display: flex !important;
        align-items: center !important;
        justify-content: center !important;
    }
    .back-btn-container .stButton > button:hover {
        background: #764ba2 !important;
        transform: scale(1.1) !important;
    }
    </style>
""", unsafe_allow_html=True)

GAMES = [
    {'id': 'hangman', 'name': 'Hangman', 'icon': '🪢', 'color': '#4CAF50', 'status': 'Active'},
    {'id': 'math', 'name': 'Victor', 'icon': '📝', 'color': '#FF9800', 'status': 'Coming Soon'},
    {'id': 'vocab', 'name': 'First', 'icon': '📚', 'color': '#2196F3', 'status': 'Coming Soon'},
    {'id': 'science', 'name': 'wong', 'icon': '🔬', 'color': '#9C27B0', 'status': 'Coming Soon'},
    {'id': 'history', 'name': 'yapping', 'icon': '🏛️', 'color': '#F44336', 'status': 'Coming Soon'},
    {'id': 'geo', 'name': '67', 'icon': '🌍', 'color': '#00BCD4', 'status': 'Coming Soon'},
]

WORDS = ['victor']

HANGMAN_PICS = [
    """
       _______
      |/      |
      |      
      |      
      |      
      |      
      |
    __|_________
    """,
    """
       _______
      |/      |
      |      (_)
      |      
      |      
      |      
      |
    __|_________
    """,
    """
       _______
      |/      |
      |      (_)
      |       |
      |       |
      |      
      |
    __|_________
    """,
    """
       _______
      |/      |
      |      (_)
      |      /|
      |       |
      |      
      |
    __|_________
    """,
    """
       _______
      |/      |
      |      (_)
      |      /|\\
      |       |
      |      
      |
    __|_________
    """,
    """
       _______
      |/      |
      |      (_)
      |      /|\\
      |       |
      |      / 
      |
    __|_________
    """,
]

if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'game' not in st.session_state:
    st.session_state.game = None

def init_hangman():
    if 'hangman_word' not in st.session_state:
        st.session_state.hangman_word = random.choice(WORDS)
        st.session_state.hangman_guessed = ['_'] * len(st.session_state.hangman_word)
        st.session_state.hangman_tries = 6
        st.session_state.hangman_used = []
        st.session_state.hangman_game_over = False

def play_hangman():
    # ===== TOMBOL BACK PANAH DI POJOK KANAN BAWAH =====
    st.markdown("""
        <div class="back-btn-container">
    """, unsafe_allow_html=True)
    if st.button("⬅️", key="back_btn_bottom"):
        st.session_state.hangman_word = random.choice(WORDS)
        st.session_state.hangman_guessed = ['_'] * len(st.session_state.hangman_word)
        st.session_state.hangman_tries = 6
        st.session_state.hangman_used = []
        st.session_state.hangman_game_over = False
        st.session_state.page = 'home'
        st.rerun()
    st.markdown("""
        </div>
    """, unsafe_allow_html=True)

    st.title("🔤 Hangman")

    init_hangman()

    # cek menang
    if '_' not in st.session_state.hangman_guessed and st.session_state.hangman_tries > 0:
        st.session_state.hangman_game_over = True
        st.balloons()
        st.markdown("""
            <div style='text-align:center;padding:30px;background:#d4edda;border-radius:20px;border:3px solid #4CAF50;'>
                <h1 style='color:#4CAF50;font-size:3em;'>🎉 Congratulation!</h1>
                <h2 style='color:#155724;'>You win the game!</h2>
                <p style='font-size:1.5em;'>The word: <strong>{}</strong></p>
            </div>
        """.format(st.session_state.hangman_word.upper()), unsafe_allow_html=True)

        if st.button("🔄 Play againn", use_container_width=True):
            st.session_state.hangman_word = random.choice(WORDS)
            st.session_state.hangman_guessed = ['_'] * len(st.session_state.hangman_word)
            st.session_state.hangman_tries = 6
            st.session_state.hangman_used = []
            st.session_state.hangman_game_over = False
            st.rerun()
        return

    # cek kalah
    if st.session_state.hangman_tries == 0:
        st.session_state.hangman_game_over = True
        st.markdown("""
            <div style='text-align:center;padding:30px;background:#f8d7da;border-radius:20px;border:3px solid #f44336;'>
                <h1 style='color:#f44336;font-size:3em;'>💀 You lose !</h1>
                <h2 style='color:#721c24;'>The correct word: <strong>{}</strong></h2>
            </div>
        """.format(st.session_state.hangman_word.upper()), unsafe_allow_html=True)

        if st.button("🔄 Try again", use_container_width=True):
            st.session_state.hangman_word = random.choice(WORDS)
            st.session_state.hangman_guessed = ['_'] * len(st.session_state.hangman_word)
            st.session_state.hangman_tries = 6
            st.session_state.hangman_used = []
            st.session_state.hangman_game_over = False
            st.rerun()
        return

    col1, col2 = st.columns([1, 1])

    with col1:
        st.markdown("### 🎨  Hangman")
        index = 6 - st.session_state.hangman_tries
        if index > 5:
            index = 5
        st.code(HANGMAN_PICS[index], language='text')

    with col2:
        st.markdown("### 📝 The word:")
        display = ' '.join(st.session_state.hangman_guessed)
        st.markdown(f"<h1 style='text-align:center;letter-spacing:20px;font-size:3em;'>{display}</h1>", unsafe_allow_html=True)

        nyawa = '❤️' * st.session_state.hangman_tries
        st.markdown(f"<p style='text-align:center;font-size:22px;'>Live: {nyawa}</p>", unsafe_allow_html=True)

        if st.session_state.hangman_used:
            used = ', '.join(sorted(st.session_state.hangman_used)).upper()
            st.markdown(f"<p style='text-align:center;font-size:16px;color:#666;'>❌ the letter that used: {used}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='text-align:center;font-size:16px;color:#666;'>❌ The letter that used: nothing</p>", unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("### 🔤 Choose a letter")

    cols = st.columns(7)
    letters = 'abcdefghijklmnopqrstuvwxyz'

    for i, letter in enumerate(letters):
        col = cols[i % 7]
        disabled = letter in st.session_state.hangman_used or st.session_state.hangman_tries == 0 or '_' not in st.session_state.hangman_guessed
        
        if col.button(letter.upper(), key=f"letter_{letter}", disabled=disabled, use_container_width=True):
            st.session_state.hangman_used.append(letter)
            
            if letter in st.session_state.hangman_word:
                for idx, char in enumerate(st.session_state.hangman_word):
                    if char == letter:
                        st.session_state.hangman_guessed[idx] = letter
                st.success("✅ correct!")
            else:
                st.session_state.hangman_tries -= 1
                st.error("❌ incorrect! -1❤️ ")
            
            time.sleep(0.3)
            st.rerun()

def home_page():
    st.title("🎮 Ms ocha Class")
    st.markdown("<p style='text-align:center;font-size:18px;color:#666;'>Choose a game and answer questions for fun!</p>", unsafe_allow_html=True)

    cols = st.columns(3)

    for idx, game in enumerate(GAMES):
        with cols[idx % 3]:
            with st.container():
                status_class = "badge-active" if game['status'] == 'Active' else "badge-coming"

                st.markdown(f"""
                    <div class="game-card">
                        <div class="circle" style="background:linear-gradient(135deg, {game['color']}, {game['color']}dd);">
                            {game['icon']}
                        </div>
                        <h3 style="margin:0;">{game['name']}</h3>
                        <p style="color:#666;margin:5px 0 10px 0;">{game['status']}</p>
                        <span class="badge {status_class}">{game['status']}</span>
                    </div>
                """, unsafe_allow_html=True)

                if game['status'] == 'Active':
                    if st.button(f"▶️ Play", key=f"btn_{game['id']}", use_container_width=True):
                        st.session_state.page = 'play'
                        st.session_state.game = game['id']
                        st.rerun()
                else:
                    st.button(f"⏳ Coming Soon", key=f"btn_{game['id']}_disabled", disabled=True, use_container_width=True)

def main():
    if st.session_state.page == 'home':
        home_page()
    elif st.session_state.page == 'play':
        if st.session_state.game == 'hangman':
            play_hangman()
        else:
            st.title("⏳ Victor")
            st.markdown("<p style='text-align:center;font-size:20px;'>Stay tuned!</p>", unsafe_allow_html=True)
            if st.button("⬅️ Back"):
                st.session_state.page = 'home'
                st.rerun()

if __name__ == "__main__":
    main()
