# 🛡️ Oracle-CLI: Local AI Auto-Debugger

A high-performance, privacy-first Python wrapper that intercepts terminal errors and provides instant, offline fixes using local LLMs.

![Python](https://img.shields.io/badge/python-3.14-blue.svg)
![Ollama](https://img.shields.io/badge/AI-Ollama-orange.svg)
![GPU](https://img.shields.io/badge/Hardware-RTX%205070-green.svg)

## 📖 Overview
Oracle-CLI solves the "context-switching" problem. Instead of manually copying errors into a browser, this tool monitors your shell, catches non-zero exit codes, and uses a local **Qwen-2.5-Coder** model to diagnose and fix the issue.

## ✨ Key Features
- **Data Sovereignty:** 100% offline. No code or logs ever leave your machine, making it safe for enterprise/proprietary work.
- **Hardware Accelerated:** Optimized for **NVIDIA RTX 50-series** GPUs for near-zero latency inference.
- **Cross-Platform Intelligence:** Automatically translates Linux/Unix commands for Windows environments and vice-versa.
- **VRAM Efficient:** Uses the `keep_alive: 0` protocol to ensure zero GPU memory footprint when idle.

## 🛠️ Installation & Setup
1. **Install Ollama:** Download from [ollama.com](https://ollama.com).
2. **Download the Model:**
   ```bash
   ollama run qwen2.5-coder:7b
