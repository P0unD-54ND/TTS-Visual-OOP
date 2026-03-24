==============================================================================
[FILE]: readme.txt
[TITLE]: TTS-Visual-OOP: High-Velocity Media Rendering Engine
[STATUS]: Hardware-Accelerated | Domain-Agnostic | Forensic Standard
Copyright (c) 2026 Dennis Sayer. All Rights Reserved.
Written Mar-24-2026 12:47.

TTS-Visual-OOP: High-Velocity Media Rendering Engine
[STATUS]: Hardware-Accelerated | Domain-Agnostic | Forensic Standard

Project Objective
This module is a specialized Linguistic-to-Visual Pipeline designed to automate the production of high-quality, scrolling-text videos. It replaces manual video editing with a programmatic architecture optimized specifically for the NVIDIA RTX 4060 chipset and a D: Drive sandboxed environment.

Hardware Architecture (The "Memory Pipe")
Unlike standard video scripts that "thrash" local storage by saving thousands of temporary image frames, this engine utilizes a Raw RGB Memory Pipe to ensure forensic efficiency.

CPU: Draws text frames directly into system RAM using the PIL (Pillow) library.

Data Stream: Pipes raw binary pixel data directly into the encoder via a standard input (stdin) subprocess.

GPU: Uses the NVIDIA NVENC hardware chip to compress the stream into an H.264 MP4 in real-time.

Result: 90% reduction in Disk I/O and total elimination of the 55-minute duration limit found in standard file-based renders.

System Requirements & Dependencies

Hardware Specifications:

GPU: NVIDIA RTX 4060 (8GB+ VRAM required for XTTS-v2 stability).

Storage: D: Drive workspace (Redirected OneDrive environments supported).

Software Environment:

Core Engine: Python 3.10.x (Mandatory for XTTS-v2 C++ header compatibility).

External Binaries: FFmpeg (compiled with nvenc support) and FFprobe must be available in the Windows System PATH.

Python Installation Sequence:
To initialize the workspace and inject the required modules into the sandboxed directory, execute the following commands using the Python Launcher (py):

py -m pip install TTS
py -m pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
py -m pip install Pillow

Operating Protocol (User Instructions)

Step 1: Prepare the Manuscript

Navigate to the project root: D:\Python\TTS Visual OOP.

Locate the file named source_manuscript.txt.

Paste your raw text content.

Voice Markup: Use [[VOICE: Name]] for internal Coqui dictionary voices.

Clone Markup: Use [[CLONE: path/to/voice.wav]] to trigger the Zero-Shot cloning engine.

Save and close the file.

Step 2: System Execution
Open a PowerShell terminal and trigger the Project Manager (main.py):

cd "D:\Python\TTS Visual OOP"
py main.py

Step 3: Output Verification

Video: The rendered .mp4 appears in the root directory with a timestamped filename (e.g., Sermon_Export_20260324_1145.mp4).

Logs: A diagnostic .txt log file is generated, providing a forensic audit of the rendering velocity, hardware bottlenecks, and total stopwatch duration.

Visual Palette (Light Mode)
As of the current version, the engine is set to a High-Contrast Light Mode standard for maximum readability:

Background: Absolute White (255, 255, 255)

Typography: Absolute Black (0, 0, 0)

Resolution: 1280x720 (16:9 Aspect Ratio)

Note: This configuration is designed for maximum clarity on mobile devices and projectors.

==============================================================================
Copyright (c) 2026 Dennis Sayer. All Rights Reserved.