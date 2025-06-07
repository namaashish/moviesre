
# 🎬 Movie Recommendation System  
An interactive recommendation engine that suggests similar movies based on content features like genres, keywords, cast, and crew using NLP and cosine similarity. Built using Python, Pandas, Scikit-learn, and Streamlit.

---

## 🚀 Features  
🍿 **Movie Recommendations** – Get 5 similar movie suggestions for any selected movie  
🧠 **Content-Based Filtering** – Powered by TF-IDF-style tags and cosine similarity  
📚 **NLP Pipeline** – Text cleaning, stemming, and vectorization  
📊 **Data Processing** – Parsed JSON-style strings using `ast`, handled missing data  
🧵 **Streamlined Tags Column** – Combined overview, genre, cast, keywords, crew  
📦 **Pickle Persistence** – Preprocessed data and similarity matrix stored in `.pkl` files  
🎨 **Simple Streamlit UI** – Fast and responsive UI ready for deployment

---

## 🧠 Tech Stack  
| Layer         | Technologies                                  |
|---------------|-----------------------------------------------|
| Frontend      | Streamlit                                     |
| Backend       | Python, Pandas, NumPy                         |
| NLP           | NLTK (PorterStemmer), CountVectorizer         |
| ML Similarity | Scikit-learn (cosine similarity)              |
| Deployment    | Streamlit Cloud / Heroku (Procfile provided)  |

---

## 📂 Project Structure  
```
.
├── app.py                   # Main Streamlit app
├── dataprocessor.py         # Preprocessing logic (optional module)
├── movies_dict.pkl          # Dictionary of movie data for recommendation
├── movies.pkl               # Pickled preprocessed DataFrame
├── similarity.pkl           # Pickled cosine similarity matrix
├── tmdb_5000_credits.csv    # TMDb credits dataset
├── tmdb_5000_movies.csv     # TMDb movies dataset
├── requirements.txt         # Python dependencies
├── setup.sh                 # Setup script for deployment
├── Procfile                 # Heroku deployment config
└── .gitignore               # Git ignored files
```

---

## ▶️ How to Run  

### 🔧 Setup  
```bash
git clone https://github.com/namaashish/Movie-Recommendation-System.git
pip install -r requirements.txt
```

### ▶️ Launch App  
```bash
streamlit run app.py
```
Then open your browser at [http://localhost:8501](http://localhost:8501)

---

## 📊 How It Works  
1. Load and merge movie metadata and credits from TMDb  
2. Extract relevant columns: `genres`, `keywords`, `cast`, `crew`, `overview`  
3. Convert JSON-style strings using `ast.literal_eval`  
4. Keep top 3 cast members, and extract the director from the crew  
5. Combine all selected attributes into a `tags` column  
6. Apply lowercase conversion, whitespace removal, and stemming  
7. Vectorize the tags using `CountVectorizer` (max 5000 words, no stopwords)  
8. Compute pairwise cosine similarity matrix  
9. Recommend 5 most similar movies when a title is selected  

---

## 🔮 Future Enhancements  
- 🎯 Add collaborative filtering with user ratings  
- 🌐 Integrate TMDb API for real-time recommendations  
- 💾 Add user login and favorites functionality  
- 🎨 UI enhancements and movie posters  
- 📱 Responsive layout for mobile devices  

---

## 👨‍💻 Author  
**Ashish Nama**  
 • 🐍 Python | 🎞️ ML | 🎨 Streamlit  




