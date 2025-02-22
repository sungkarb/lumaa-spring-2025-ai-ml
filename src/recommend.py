import pandas as pd
import sys, re, json 
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.preprocessing import MultiLabelBinarizer

MAX_ROW = 20000

def load(filename: str) -> pd.DataFrame:
    """Loads dataframe specified by the filename.

    Args:
        filename - name of the csv file to load
    Returns:
        Dataframe with decreased number of rows for training purposes
    """
    df = pd.read_csv(filename, low_memory=False)
    n = len(df)
    if n > MAX_ROW:
        step_size = n / MAX_ROW
        indxs = [step_size * i for i in range(MAX_ROW)]
        df = df.iloc[indxs, :]

    return df 

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Processes dataframe for ease of vectorization in the future

    Args:
        df - tabular dataframe
    Returns:
        Processed dataframe with selected columns and lowercased text
    """
    def _convert_to_str(s):
        try:
            result = str(s).lower()
        except:
            result = ""
        return result 
    
    def _unpack_genres(s):
        s = s.replace("'", "\"")
        pattern = "{[^{}]*}"
        result = []
        for match in re.findall(pattern, s):
            dic = json.loads(match)
            result.append(dic["name"].lower())
        return result


    result = df[["title", "overview", "genres"]].copy()
    result["overview"] = result["overview"].apply(_convert_to_str)
    result["genres"] = result["genres"].apply(_unpack_genres)
    return result 

def recommend(prompt: str, df: pd.DataFrame, N = 5, alpha = 0.7) -> list[str]:
    """Gives best titles (3 - 5) based on user prompt and movie corpus

    Args:
        prompt - user prompt describing his preferences
        df - processed movie dataset containing movie titles and their
             descriptions
        N - number of top matches to return
        alpha - controls the weight given to genre inferred from the prompt
    Returns:
        List of movies recommended by the system
    """
    prompt = prompt.lower()
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform(df["overview"])

    ## Infer genres from prompt
    mlb = MultiLabelBinarizer()
    genre_matrix = mlb.fit_transform(df["genres"])
    genre_sim = cosine_similarity(genre_matrix)
    inferred_genres = []
    for word in prompt.split(" "):
        if word in mlb.classes_:
            inferred_genres.append(word)
    
    ## Compute similarity score based on text description and genre similarity
    inferred_genres_vec = mlb.transform([inferred_genres])
    genre_sim = cosine_similarity(inferred_genres_vec, genre_matrix).flatten()
    prompt_vector = vectorizer.transform([prompt])
    overview_sim = cosine_similarity(tfidf_matrix, prompt_vector).flatten()

    ## Average the result using alpha parameter ()
    final_sim = alpha * overview_sim + (1 - alpha) * genre_sim
    top_matches = final_sim.argsort()[::-1][:N]
    return df.iloc[top_matches, :]["title"].to_list()

def main():
    ## Process user input
    argv = sys.argv
    n = len(argv)
    num_matches = 5
    if n < 2 or n > 3:
        print("Usage: [prompt] [#matches (optional)]")
        return 
    elif n == 2:
        prompt = argv[1]
    elif n == 3:
        prompt = argv[1]
        num_matches = int(argv[2])
    
    ## Load and preprocess dataset
    print("Loading dataset ...")
    df = load("../data/movies_metadata.csv")
    df = preprocess(df)

    ## Give recommendation
    recommendations = recommend(prompt, df, num_matches)
    print("Based on your preferences we found following movie titles")
    for movie_title in recommendations:
        print(movie_title)

if __name__ == "__main__":
    main()
