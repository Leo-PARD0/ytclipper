# ✂️ Live Cutter — Documentation (EN)

> ⚠️ **Language note**  
> English is not my first language.  
> This document aims to be clear and technically accurate, even if the wording is not perfect.

---

## Introduction

**Live Cutter** is a local application designed for content creators who need to **mark and extract specific segments from YouTube videos** in a simple and controlled way.

The project runs **locally in the browser**, using **Flask** as the backend and **HTML/JavaScript** on the frontend.  
It does not operate as an online service, does not host content, and does not perform remote processing.

This repository documents the **current state of the project**, its existing features, and its known limitations.  
Development is incremental and experimental, with room for discussion, feedback, and community contributions.

---

## Current features

Live Cutter provides a simple, continuous flow for marking and processing video segments locally.

### Usage flow

1. The user provides a YouTube video URL.
2. The video is loaded into an embedded player.
3. During playback, the user marks a **start** and **end** time.
4. Each cut is sent **automatically and individually** to the backend.
5. Cuts are processed locally, one at a time.

### Current behavior

- Cuts are processed **sequentially**.
- No manual “send” action is required.
- Each cut’s status is reflected in the interface.
- The application runs entirely in the user’s local environment.

---

## Project architecture

Live Cutter is organized into simple layers, with clear separation between **interface**, **control flow**, **processing**, and **local data**.

> The structure below reflects the development repository.  
> The final executable structure differs from this layout.

```
├── 🐍 app.py # Flask backend entry point
├── 📁 templates
│   └── 🌐 index.html # Interface structure
├── 📁 static
│   ├── 📄 script.js # Frontend logic
│   └── 🎨 style.css # Interface styles
├── 📁 engine
│   ├── 🐍 __init__.py
│   └── 🐍 ytfastcut.py # Video cutting engine
├── 📁 core
│   └── 🐍 app_path.py # Path and directory management
├── 📁 cutter
│   ├── 📁 data # Locally generated data
│   │   ├── 📁 cut # cut output
│   │   │   ├── 📁 fast
│   │   │   └── 📁 slow
│   │   └── 📁 tmp # Temporary downloads
│   │       ├── 📁 fast
│   │       └── 📁 slow
│   │   
│   ├── 📁 essentials # Essentials modules - DO NOT ERASE IT!
│   │   └── 📁 bin
├── 📁 assets
│   └── 📁 screenshots # Documentation images
├── 📁 licenses
│   ├── 📄 LICENSE # Project license
│   └── 📁 Third_Party # Third-party licenses
│       └── 📄 yt-dlp.LICENCE
├── 📝 README.MD
├── 📝 README.en.md
└── 📝 README.pt-br.md
```


Each layer has a well-defined responsibility:

- **Interface (`templates/` + `static/`)**  
  Visual structure and browser-side interaction logic.

- **Backend (`app.py`)**  
  Starts the local server, exposes simple routes, and delegates processing.

- **Processing engine (`engine/ytfastcut.py`)**  
  Performs the actual video cutting.

- **Path management (`core/app_path.py`)**  
  Centralizes directory structure and path rules.

- **Local data (`cutter/data/`)**  
  Stores generated files and temporary data.

---

## Frontend logic (`static/script.js`)

All frontend behavior lives in `script.js`, including:

- application state;
- cut queue management;
- automatic communication with the backend.

Cuts are queued locally and processed **one at a time**, without parallel execution or persistent state.

### Supported YouTube URL format

Currently, only the standard YouTube URL format is supported:

https://www.youtube.com/watch?v=VIDEO_ID


Other formats (short links, embeds, shorts, or URLs with additional parameters) are **not supported yet**, even though they are technically possible to handle.

This limitation exists because the `video_id` is extracted using simple string operations, prioritizing readability over robustness.

---

## Local processing (`engine/ytfastcut.py`)

The processing engine performs the actual video cutting using `yt-dlp`.

It:
- creates temporary directories;
- executes the cutting command;
- waits for completion;
- moves the final file to the output directory.

Processing is synchronous and explicit, with no parallel execution or advanced fallback logic.

The engine depends directly on the compatibility between `yt-dlp` and YouTube.  
There is currently **no automatic update mechanism** for this dependency.

---

## Limitations and project stance

Live Cutter is an evolving project focused on clarity, learning, and experimentation.

### Known limitations

- Local-only execution.
- Sequential processing.
- No persistent state.
- Limited YouTube URL support.
- Direct dependency on `yt-dlp`.
- No automatic dependency updates.

### Project stance

Live Cutter:
- does not host content;
- does not distribute videos;
- does not operate as an online service;
- does not validate usage intent;
- does not moderate or inspect content.

Usage is the responsibility of the user.  
The project is provided **“as is”**, without explicit or implied warranties.

---

## 💡 Open ideas

This section lists ideas and directions for discussion, not implementation commitments.

- Support for additional YouTube URL formats.
- Responsive iframe-based player.
- Optional automatic updates for `yt-dlp`.
- Frontend state persistence.
- Improved visual feedback for errors and processing.
- Revisions to the processing architecture.

Constructive feedback and discussion are welcome, especially if they help keep the project simple and understandable.

---

## Support the project

Live Cutter is an independent, open-source project developed incrementally.

If this project has been useful to you — as a tool or as a technical reference — you may choose to support its development.

### 🌍 International support

## Support the project

Live Cutter is an independent, open-source project developed incrementally.

If this project has been useful to you — whether as a tool or as a technical reference — you may choose to support its development.

### 🌍 International support

International support is available via **Buy Me a Coffee**:

- ☕ https://buymeacoffee.com/LeoPardo

Support is optional and not associated with promises, features, priority support, or guarantees.

Community discussion, feedback, and constructive criticism are just as valuable as financial support.

---

## License

This project is distributed under the **MIT License**.

- [`licenses/LICENSE`](licenses/LICENSE)

Third-party components are documented separately:

- [`licenses/Third_Party/`](licenses/Third_Party/)
