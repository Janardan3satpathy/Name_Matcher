import streamlit as st
import pandas as pd
import os
from thefuzz import process, fuzz

# --- Configuration ---
DATASET_FILE = "combined_names.csv"
PAGE_TITLE = "Name Matcher AI"
ICON = "🔍"

# --- Page Setup ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=ICON, layout="centered")

# --- CSS Styling ---
st.markdown("""
    <style>
    .main {
        background-color: #f9f9f9;
    }
    .stButton>button {
        width: 100%;
        background-color: #ff4b4b;
        color: white;
    }
    .result-card {
        padding: 20px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 10px;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# --- Functions ---

@st.cache_data
def load_data():
    """
    Loads the dataset. Using cache_data ensures we only load the huge CSV once
    per session, making the app much faster.
    """
    # 1. Check if the CSV exists
    if os.path.exists(DATASET_FILE):
        try:
            df = pd.read_csv(DATASET_FILE)
            # Convert the first column to a list of strings
            return df.iloc[:, 0].astype(str).tolist()
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            return []
    
    # 2. Fallback: If CSV is missing (e.g., first time on GitHub before upload)
    # We provide the small manual list so the app doesn't crash.
    else:
        st.warning(f"'{DATASET_FILE}' not found. Using small fallback dataset.")
        return [
            "Geetha", "Gita", "Geeta", "Rahul", "Raahul", 
            "Mohammed", "Mohd", "Deepak", "Dipak", "Priya", 
            "Amit", "Anjali", "Vikram", "Suresh", "Aditi", 
            "Rohan", "Meera", "Catherine", "Katherine", 
            "John", "Jon", "Steven", "Stephen"
        ]

def find_matches(name, dataset, limit=5):
    # Using token_sort_ratio for robust partial matching
    return process.extract(
        name, 
        dataset, 
        scorer=fuzz.token_sort_ratio, 
        limit=limit
    )

# --- Main UI ---

st.title(f"{ICON} {PAGE_TITLE}")
st.write("Enter a name to find its most similar matches from the database.")

# Load Data
with st.spinner("Loading Database..."):
    dataset = load_data()
    st.success(f"Database Active: {len(dataset):,} names loaded.", icon="✅")

# Input Section
col1, col2 = st.columns([3, 1])
with col1:
    user_input = st.text_input("Input Name", placeholder="e.g. Rames", label_visibility="collapsed")
with col2:
    search_clicked = st.button("Search")

# Search Logic
if search_clicked or user_input:
    if not user_input.strip():
        st.warning("Please enter a name first.")
    else:
        with st.spinner(f"Searching for matches for '{user_input}'..."):
            matches = find_matches(user_input, dataset, limit=10)

        if matches:
            best_name, best_score = matches[0]

            # --- Best Match Display ---
            st.markdown("### 🏆 Top Result")
            st.markdown(f"""
            <div class="result-card">
                <h2 style='color: #2e7bcf; margin:0;'>{best_name}</h2>
                <p style='font-size: 1.2rem; color: #555;'>Confidence: <b>{best_score}%</b></p>
            </div>
            """, unsafe_allow_html=True)

            # --- Other Matches Table ---
            st.markdown("### 📋 Other Candidates")
            
            # Prepare data for cleaner table display
            results_data = [{"Name": n, "Similarity Score": f"{s}%"} for n, s in matches[1:]]
            st.table(results_data)
        else:
            st.info("No close matches found.")

# --- Sidebar ---
with st.sidebar:
    st.header("About")
    st.markdown("""
    This system uses **Levenshtein Distance** to find phonetic and spelling similarities.
    
    **Dataset:** Combined General & Indian Names.
    **Library:** `thefuzz` + `python-Levenshtein`.
    """)
    st.divider()
    st.caption("Built with Streamlit")