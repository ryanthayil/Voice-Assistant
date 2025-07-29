# AI VOICE ASSISTANT
his project integrates a **multilingual voice assistant** with real-time **object detection** to enable a humanoid robot to interact naturally with its environment. The assistant uses speech recognition, text-to-speech, and contextual conversation via OpenAI's API to understand and respond to user queries in multiple languages.

## Features

- **Voice Interaction**: Speak to the assistant in supported languages.
- **Multilingual Support**: Handles English, Hindi, and other languages.
- **Contextual Conversations**: Uses OpenAI to generate intelligent, context-aware replies.
- **Real-Time Object Detection**: YOLO-based object detection from the robot's camera feed.
- **Noise Cancellation**: Improved audio processing using Silero plugins.
- **LiveKit Integration**: Manages real-time media and voice routing.

## Architecture Overview

1. User speaks → Audio captured via microphone.
2. Noise-cancelled audio → Transcribed via LiveKit/OpenAI plugins.
3. Transcription → Sent to OpenAI GPT for reply generation.
4. Optional: Object detection module uses webcam and YOLO to describe visual scene.
5. Response → Converted to speech and spoken via robot’s speaker.
   
## SETUP
- Create a [LiveKit](https://cloud.livekit.io/login?r=%2F) API key
- Create openai API key
- Dupicate `.env.template` and rename to `.env` and fill in the environment variables
- Install python dependencies
  ```bash
    pip install requirements.txt
  ```
- To start the agent
  ```bash
    python main.py console
  ```
