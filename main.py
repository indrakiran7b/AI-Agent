import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Step 1: Extract content from a blog URL
def extract_blog_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = [p.get_text() for p in soup.find_all("p")]
    return " ".join(paragraphs[:20])  # Limit to first 20 paragraphs

# Step 2: Initialize summarizer and text generation models
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=-1)
generator = pipeline("text-generation", model="gpt2", device=-1)

# Step 3: Define helper functions
def summarize_content(content):
    summary = summarizer(content, max_length=130000, min_length=40, do_sample=False)
    return summary[0]['summary_text']

def create_linkedin_post(content):
    prompt = f"Write a professional LinkedIn post (100-150 words) based on this content:\n\n{content}"
    post = generator(prompt, max_length=200000, num_return_sequences=1)[0]['generated_text']
    return post

def create_tweet_thread(content):
    prompt = f"Convert this into a tweet thread (3-5 short tweets):\n\n{content}"
    tweets = generator(prompt, max_length=2500000, num_return_sequences=1)[0]['generated_text']
    return tweets

# Step 4: Run the AI agent
def run_ai_agent(url):
    content = extract_blog_content(url)
    print("✅ Extracted content!\n")

    summary = summarize_content(content)
    linkedin_post = create_linkedin_post(content)
    tweet_thread = create_tweet_thread(content)

    print("🧾 Summary:\n", summary)
    print("\n💼 LinkedIn Post:\n", linkedin_post)
    print("\n🐦 Tweet Thread:\n", tweet_thread)

# Example:
if __name__ == "__main__":
    blog_url = input("Enter a blog URL: ")
    run_ai_agent(blog_url)
