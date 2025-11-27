# **Name Matcher AI 🔍**

A Streamlit web application that matches names against a database of 500,000+ entries using Fuzzy String Matching (Levenshtein Distance).

Deployed Website Link :\- [https://namematcherjanardan.streamlit.app/](https://namematcherjanardan.streamlit.app/)

Public GitHub Repository Link :- https://github.com/Janardan3satpathy/Name\_Matcher

## **Features**

* **Instant Search:** Finds similar names (e.g., "Gita" matches "Geetha").  
* **Large Dataset:** Includes standard English names and a massive variation of Indian names.  
* **Ranked Results:** Shows confidence scores for every match.

## **How to Run Locally**

1. Clone the repository.  
2. Install dependencies:  
   pip install \-r requirements.txt

3. Run the app:  
   streamlit run NameMatcher.py

## **Dataset**

The project uses combined\_names.csv. If this file is missing, the app defaults to a small sample list for demonstration purposes.

\# Name Matching System

This project implements a fuzzy string matching system that identifies the most similar names from a dataset based on user input. It uses the Levenshtein distance algorithm to calculate similarity scores.

\#\# Prerequisites

\- \*\*OS:\*\* Windows, Linux, or macOS.

\- \*\*Language:\*\* Python 3.6 or higher.

\- \*\*Package Manager:\*\* \`pip\` (included with standard Python installations).

\#\# Installation

1\. Open your terminal (Linux/Mac) or Command Prompt/PowerShell (Windows).

2\. Navigate to the project directory.

3\. Install the required dependencies:

   \`\`\`bash

   pip install \-r requirements.txt

**Scenario 1: Exact Match variation** *Input:* `Geeta` *Dataset contains:* `Geetha, Gita, Gitu, Geeta`

**Output:**

Plaintext

✅ Best Match: Geeta (Score: 100%)

📋 Ranked List of Similar Names:

Name            | Similarity Score

\-----------------------------------

Geeta           | 100% \<--

Geetha          | 91%

Gita            | 89%

Gitu            | 67%

\-----------------------------------

**Scenario 2: Spelling Error / Phonetic Match** *Input:* `Kathrin` *Dataset contains:* `Catherine, Katherine, Kathryn`

**Output:**

Plaintext

✅ Best Match: Kathryn (Score: 86%)

📋 Ranked List of Similar Names:

Name            | Similarity Score

\-----------------------------------

Kathryn         | 86% \<--

Katherine       | 75%

Catherine       | 62%

\-----------------------------------

