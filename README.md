# 🌟 Chat With YouTube Videos 🌟

## Introduction 🚀
Hey there, awesome coders! 🎉 I'm super thrilled to introduce our latest Python project that's going to blow your minds! 🤯 Imagine chatting with YouTube videos - yes, you heard that right! 📹💬 We're merging the power of Large Language Models (LLMs) with the magic of YouTube, allowing you to interact with video content like never before. 🌈✨

## What's Cooking? 🍳
Our project uses a mix of cool tech to make this possible:
- **Ollama / HuggingFace LLMs**: We're harnessing these AI giants to understand and respond to the content of YouTube videos. 🧠🤖
- **Pythonic YouTube Transcribe Package**: This nifty tool transcribes YouTube videos, turning spoken words into text. 🎙️➡️📝
- **LiteLLM**: This is our secret sauce for managing LLM completion queries, ensuring smooth and intelligent responses. 🌟🔧

## How It Works? 🧐
1. **Transcribe**: First, our Python script transcribes the YouTube video. 📼🔠
2. **Contextualize**: The transcribed text is then used to provide context to our LLMs. 📖🌍
3. **Chat Away**: You ask questions or make comments, and our LLMs, fueled by the video's context, respond as if you're having a conversation with the video itself! 🗨️💬

## Features 📚
- **Interactive Video Experience**: Feel like you're having a real conversation with your favorite YouTube videos. 🎥👥
- **Diverse LLM Support**: Thanks to Ollama and HuggingFace, our responses are smart, relevant, and incredibly engaging. 🧠✨
- **Easy-to-Use**: Simple setup, user-friendly interface. Perfect for both beginners and pros! 🙌💻

## Installation 🛠️
```bash
pip install -r requirements.txt
```
A single command and you're all set to go! 🚀

## Configuration ⚙️
Head over to `config/ai_models.json`. You can add / remove existing configuration as you wish, just make sure that the
URLs that you're using match the expectations.
Example config for a local ollama deployment:
```json
{
  "Ollama Mistral": {
    "model": "ollama/mistral",
    "base_api": "http://localhost:11434",
    "resolver_type": "ollama"
  }
}
```

## Contribute 🤝
Got ideas? Bugs? Want to contribute? Join us on this exciting journey to revolutionize how we interact with digital content! 🌍❤️

## Stay Tuned 📢
Follow us for updates, tips, and much more. Let's make YouTube conversations the next big thing! 🚀🎉

---

Made with ❤️ and a dash of Python magic! 🐍✨

**#ChatWithYouTube #PythonProject #AIConversations**

p.s: you guessed right, an LLM wrote this README 😂