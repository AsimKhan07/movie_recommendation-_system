# 🎬 Movie Recommendation System

## 📌 Overview
A **content-based movie recommendation system** that suggests similar movies based on genres, cast, crew, and plot overviews using **machine learning and NLP techniques**. Built using **The Movie Database (TMDB)** dataset, this system helps users discover new movies they might enjoy!

## 🚀 Features
✅ **Content-Based Filtering** – Recommends movies based on similarities.  
✅ **Natural Language Processing (NLP)** – Extracts and processes movie metadata.  
✅ **Machine Learning (ML)** – Uses **TF-IDF & Cosine Similarity** for recommendations.  
✅ **Easy Deployment** – Deployable as a **Streamlit web app**.  
✅ **User-Friendly Interface** – Simple, interactive, and effective UI.  

---

## 📂 Dataset
The system uses **TMDB 5000 Movie Dataset** from [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata), which includes:
- **tmdb_5000_movies.csv** – Contains movie metadata (title, genres, overview, etc.).
- **tmdb_5000_credits.csv** – Contains cast and crew information.

---

## 🔧 How It Works
1️⃣ **Data Processing** – Load and clean TMDB movie & credit data.  
2️⃣ **Feature Engineering** – Extract meaningful features (genres, cast, keywords).  
3️⃣ **Text Processing** – Use NLP (stemming, vectorization, tokenization).  
4️⃣ **Similarity Calculation** – Compute similarity using **Cosine Similarity**.  
5️⃣ **Recommendation System** – Suggest movies based on user input.  
6️⃣ **Deployment Ready** – Save processed data for **Streamlit app integration**.  

---

## 🛠️ Installation & Usage
### 🔹 Prerequisites
Make sure you have **Python 3.x** installed along with the following libraries:
```bash
pip install numpy pandas scikit-learn nltk streamlit
```

### 🔹 Running the Project
1️⃣ **Download Data** – Get the TMDB dataset from [Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata).  
2️⃣ **Run Jupyter Notebook** – Execute `movie-recommendation-system.ipynb`.  
3️⃣ **Deploy with Streamlit** – Run the command below to launch the app:
```bash
streamlit run app.py
```

---

## 📌 Deployment with Streamlit
This project can be **deployed as a web app** using **Streamlit**:
1️⃣ **Save Processed Data** – Use `pickle` to store preprocessed data.  
2️⃣ **Create a Streamlit App** – Build a UI to take movie input & display recommendations.  
3️⃣ **Run & Access the App** – Open in a browser using Streamlit.

---

## ⚠️ Copyright & License
🛑 **Copyright © [Mayana.Asim Ali Khan]. All Rights Reserved.** 🛑  
This project is protected under copyright law. Unauthorized reproduction, modification, or distribution is strictly prohibited. If you wish to use this project, please contact me for permission.

---

## 🤝 Contact & Contribution
📧 Have any questions or suggestions? Feel free to connect!  
🔗 **GitHub Profile** – [AsimKhan07] 
💡 Contributions are welcome! Fork this repo and submit a PR.  

---

⭐ **If you like this project, don't forget to give it a star!** ⭐

