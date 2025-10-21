# 🧠 AI Agent Project

## 📌 Overview
This project demonstrates an **AI Agent** that can automatically scan blogs, articles, or videos and **repurpose content** into new formats such as summaries, LinkedIn posts, tweets, or scripts.

## 🚀 Features
- Extracts content from existing text or video transcripts  
- Summarizes and reformats into multiple styles (post, tweet, script)  
- Uses **free Hugging Face and OpenAI API alternatives**  
- Lightweight and efficient — runs locally without paid models

## 🛠️ Setup Instructions
1. Clone the repository  
   ```bash
   git clone https://github.com/indrakiran7b/AI-Agent.git
   cd AI-Agent
   ```

2. Create and activate a virtual environment  
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Run the AI Agent  
   ```bash
   python main.py
   ```

## 🧩 How It Works
The AI Agent:
1. Takes input text or URLs.  
2. Parses and extracts content using BeautifulSoup.  
3. Uses a local or free model (e.g., Hugging Face transformers) for summarization.  
4. Repurposes into various formats (LinkedIn post, tweet, etc.).  

## 📦 Requirements
- Python 3.9+  
- transformers  
- beautifulsoup4  
- requests  

## 🧠 Example Output
Input: Blog article about “AI in Healthcare”  
Output:  
> “AI is revolutionizing healthcare by improving diagnosis speed and accuracy. Here’s how technology is shaping the future of medicine. 🧬💡”

## 👨‍💻 Author
**Bhavanam Indra Kiran Reddy**  
GitHub: [indrakiran7b](https://github.com/indrakiran7b)  
LinkedIn: [linkedin.com/in/indrakiran7b](https://linkedin.com/in/indrakiran7b)

## 📄 License
This project is open source under the MIT License.
