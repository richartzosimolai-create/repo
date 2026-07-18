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
        border-radius: 50%; 
        transition: all 0.3s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
    }
    .game-card { 
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
    .btn-main {
        background: #4CAF50 !important;
        color: white !important;
        border-radius: 30px !important;
        height: 50px !important;
    }
    .btn-main:hover {
        background: #45a049 !important;
    }
    .btn-danger {
        background: #f44336 !important;
        color: white !important;
        border-radius: 30px !important;
        height: 50px !important;
    }
    .btn-danger:hover {
        background: #d32f2f !important;
    }
    </style>
""", unsafe_allow_html=True)

GAMES = [
    {'id': 'hangman', 'name': 'Hangman', 'icon': '🔤', 'color': '#4CAF50', 'status': 'Aktif'},
    {'id': 'math', 'name': 'Quiz Matematika', 'icon': '📝', 'color': '#FF9800', 'status': 'Coming Soon'},
    {'id': 'vocab', 'name': 'Kosakata', 'icon': '📚', 'color': '#2196F3', 'status': 'Coming Soon'},
    {'id': 'science', 'name': 'Quiz Sains', 'icon': '🔬', 'color': '#9C27B0', 'status': 'Coming Soon'},
    {'id': 'history', 'name': 'Quiz Sejarah', 'icon': '🏛️', 'color': '#F44336', 'status': 'Coming Soon'},
    {'id': 'geo', 'name': 'Quiz Geografi', 'icon': '🌍', 'color': '#00BCD4', 'status': 'Coming Soon'},
]

WORDS = ['apel', 'kucing', 'buku', 'meja', 'kursi', 'lampu', 'pohon', 'bunga', 'mobil', 'sepatu', 'sekolah', 'kesehatan', 'perpustakaan']

# ============ GAMBAR HANGMAN ============
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
    """
       _______
      |/      |
      |      (_)
      |      /|\\
      |       |
      |      / \\
      |
    __|_________
    """
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
    st.title("🔤 Hangman")
    
    col1, col2, col3 = st.columns([1,5,1])
    with col2:
        if st.button("⬅️ Back", use_container_width=True):
            st.session_state.page = 'home'
            st.rerun()
    
    init_hangman()
    
    # Cek game over
    if '_' not in st.session_state.hangman_guessed:
        st.session_state.hangman_game_over = True
        st.balloons()
        st.markdown("""
            <div style='text-align:center;padding:30px;background:#d4edda;border-radius:20px;border:3px solid #4CAF50;'>
                <h1 style='color:#4CAF50;font-size:3em;'>🎉 SELAMAT!</h1>
                <h2 style='color:#155724;'>ANDA MENANG!</h2>
                <p style='font-size:1.5em;'>Kata: <strong>{}</strong></p>
            </div>
        """.format(st.session_state.hangman_word.upper()), unsafe_allow_html=True)
        
        if st.button("🔄 Play again", use_container_width=True):
            st.session_state.hangman_word = random.choice(WORDS)
            st.session_state.hangman_guessed = ['_'] * len(st.session_state.hangman_word)
            st.session_state.hangman_tries = 6
            st.session_state.hangman_used = []
            st.session_state.hangman_game_over = False
            st.rerun()
        return
    
    if st.session_state.hangman_tries == 0:
        st.session_state.hangman_game_over = True
        st.markdown("""
            <div style='text-align:center;padding:30px;background:#f8d7da;border-radius:20px;border:3px solid #f44336;'>
                <h1 style='color:#f44336;font-size:3em;'>💀 You lose!</h1>
                <h2 style='color:#721c24;'>Kata yang benar: <strong>{}</strong></h2>
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
        # TAMPILAN GAMBAR HANGMAN
        st.markdown("### 🎨 Status Hangman")
       st.code(HANGMAN_PICS[min(6 - st.session_state.hangman_tries, 5)], language='text')
    
    with col2:
        st.markdown("### 📝 Kata")
        display = ' '.join(st.session_state.hangman_guessed)
        st.markdown(f"<h1 style='text-align:center;letter-spacing:20px;font-size:3em;'>{display}</h1>", unsafe_allow_html=True)
        
        # Nyawa
        nyawa = '❤️' * st.session_state.hangman_tries
        st.markdown(f"<p style='text-align:center;font-size:22px;'>Nyawa: {nyawa}</p>", unsafe_allow_html=True)
        
        # Huruf terpakai
        if st.session_state.hangman_used:
            used = ', '.join(sorted(st.session_state.hangman_used)).upper()
            st.markdown(f"<p style='text-align:center;font-size:16px;color:#666;'>❌ Huruf terpakai: {used}</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p style='text-align:center;font-size:16px;color:#666;'>❌ Huruf terpakai: belum ada</p>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.markdown("### 🔤 Select a letter")
    
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
                st.success("✅ Correct!")
            else:
                st.session_state.hangman_tries -= 1
                st.error("❌ Incorrect")
            
            time.sleep(0.3)
            st.rerun()

def home_page():
    st.title("🎮 Ms oCha class")
    st.markdown("<p style='text-align:center;font-size:18px;color:#666;'>Pilih game dan jawab soal dengan seru!</p>", unsafe_allow_html=True)
    
    cols = st.columns(3)
    
    for idx, game in enumerate(GAMES):
        with cols[idx % 3]:
            with st.container():
                status_class = "badge-active" if game['status'] == 'Aktif' else "badge-coming"
                
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
                
                if game['status'] == 'Aktif':
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
            st.title("⏳ Dalam Pengembangan")
            st.markdown("<p style='text-align:center;font-size:20px;'>Game ini masih dalam pengembangan!</p>", unsafe_allow_html=True)
            if st.button("⬅️ Back"):
                st.session_state.page = 'home'
                st.rerun()

if __name__ == "__main__":
    main()
