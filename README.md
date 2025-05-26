
# 🌐 Multimodal Internet Crawler + Question Answerer

A powerful multimodal system that **scrapes the web** to answer complex user queries using **text, images, and videos**. This project combines state-of-the-art AI models for captioning, transcription, retrieval, and summarization — producing structured, step-by-step guides with rich media.

---


## 🧠 Example Query

> **"Show me how to do a deadlift"**

✅ Google Search  
✅ Download and caption images  
✅ Transcribe tutorial YouTube videos  
✅ Extract and summarize instructional steps  
✅ Output a final guide with:  
- ✅ Text answer  
- 🖼️ Diagrams  
- 🎞️ Video summary  

---

## 🚀 Features

- 🔍 **Web Crawler** (Google, YouTube)
- 🖼️ **Image Captioning** (BLIP-2 / DINOv2)
- 🎧 **Video Transcription** (OpenAI Whisper)
- 📚 **Text Summarization & RAG** (LlamaIndex / LangChain)
- 🧠 **Multimodal Ranking** (CLIP/Text/Temporal)
- 📘 **Guide Generator** (Structured JSON/HTML)

---

## 🧱 Architecture

```
Query → Scraper → Media/Text Processor → Multimodal Ranker → Structured Guide
           |            |                        |
         Google       BLIP/Whisper            Fusion
         YouTube       + RAG Index         (Text + Visual)
```

---

## 🗂️ Project Structure

```
multimodal_qa/
├── app.py                          # Main pipeline orchestrator
├── crawler/
│   └── web_scraper.py              # Google + YouTube scraping & media downloading
├── processing/
│   ├── image_captioning.py         # BLIP-2 for image captions
│   ├── video_processor.py          # Whisper for video/audio
│   └── text_processor.py           # LangChain / LlamaIndex for RAG
├── aligner/
│   └── multimodal_ranker.py        # Align visual + textual info
├── generator/
│   └── guide_formatter.py          # Structured guide output
├── models/
│   └── load_models.py              # Shared model loading logic
├── data/                           # Media, transcripts, captions, outputs
└── requirements.txt
```

---

## 👥 Team Responsibilities

| Member         | Responsibilities                                                   |
|----------------|--------------------------------------------------------------------|
| **Aashutosh** | Pipeline orchestration, RAG integration, multimodal alignment, output formatting |
| **Qusai**     | Web crawler, Google/YouTube scraping, image/video downloading      |
| **Areef**     | Image captioning (BLIP-2), video transcription (Whisper), RAG indexing |

---

## 🧪 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/multimodal-qa.git
cd multimodal-qa
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
playwright install
```

### 3. Add Your API Keys

Set your OpenAI API Key:

```bash
export OPENAI_API_KEY="your-key"
```

(Optional) Create a `.env` file to store credentials.

---

## ▶️ Run the System

```bash
python app.py
```

This will:
- Scrape Google/YouTube for your query
- Caption images and transcribe videos
- Summarize all results into a structured multimodal guide

---

## 📌 TODO (Milestones)

- [] Web crawler with Playwright
- [] BLIP-2 captioning
- [] Whisper transcription
- [] LlamaIndex or LangChain RAG
- [] Multimodal ranking with CLIP
- [] Visual-text temporal alignment
- [] Streamlit or React front-end

---

## 📄 License

MIT License – open for academic or research use.

---

## 🤖 Built With

- [Playwright](https://playwright.dev/)
- [Transformers](https://huggingface.co)
- [OpenAI Whisper](https://github.com/openai/whisper)
- [LangChain](https://github.com/langchain-ai/langchain)
- [LlamaIndex](https://www.llamaindex.ai/)
- [BLIP-2](https://github.com/salesforce/LAVIS)

---

## 🙌 Acknowledgements

Inspired by the latest advances in **multimodal generative AI** and RAG pipelines.
