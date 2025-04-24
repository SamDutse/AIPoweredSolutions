# 🎓 AI Career & Course Advisor (Nigerian Edition)

This is an AI-powered web application designed to help Nigerian students receive personalized course and career guidance based on their interests and academic background (WAEC subjects and UTME scores).

## 🌍 Why This Matters

Many Nigerian students struggle with choosing the right course of study due to lack of guidance, limited access to counselors, or insufficient understanding of their own interests. This project leverages **free, open-source AI models from Hugging Face** to provide real-time suggestions tailored to the user's input.

By democratizing access to career advice, this app can:
- Assist final-year secondary school students in making informed choices.
- Reduce course mismatch in tertiary institutions.
- Empower guidance counselors in under-resourced schools.
- Enable self-assessment for students in rural areas with internet access.

---

## 🧠 Features

- **AI-Powered Career Matching**: Uses the `facebook/bart-large-mnli` zero-shot classifier to recommend Nigerian-relevant courses and careers based on interests.
- **User-Friendly Interface**: Built with [Streamlit](https://streamlit.io) for a fast, interactive experience.
- **Token-Based Access**: Securely integrates with Hugging Face models using a personal access token stored in a `.env` file.

---

## 🚀 Getting Started

### 1. Clone this Repository

```bash
git clone https://github.com/yourusername/ai-career-advisor.git
cd ai-career-advisor
```

### 2. Set Up the Environment

```bash
conda create -n career_advisor python=3.10 -y
conda activate career_advisor
pip install -r requirements.txt
```

### 3. Add Your Hugging Face Token

Create a `.env` file in the root directory with:

```
HF_TOKEN=your_huggingface_token_here
```

You can get a token for free at [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).

### 4. Run the App

```bash
streamlit run app.py
```

---

## 📚 Example Inputs

- Interests: _"I enjoy solving problems with technology and love mathematics."_
- WAEC Subjects: _"Math, Physics, English, Chemistry"_
- UTME Score: _280_

### Output:
- Computer Science → Software Developer  
- Mechanical Engineering → Automobile Engineer  
- ...and more

---

## 🛠 Tech Stack

- **Python**
- **Streamlit**
- **Transformers (Hugging Face)**
- **facebook/bart-large-mnli** model
- **dotenv** for token security

---

## 🤝 Contributing

Feel free to fork this repo, make improvements, and submit pull requests! Suggestions for new features or datasets are welcome.

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.
