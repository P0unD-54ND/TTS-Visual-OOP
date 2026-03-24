# -*- coding: utf-8 -*-
# ==============================================================================
# [FILE]: video_engine.py
# [TITLE]: Local Coqui XTTS-v2 Hardware & Rendering Engine (Light Mode Memory Pipe)
# [SECURITY PROTOCOL]: Local Execution Only - Workspace Level D: Drive
# [FORENSIC STRATEGY]: RGB Inversion | Raw RGB Streaming | Absolute Traceability.
# Copyright (c) 2026 Dennis Sayer. All Rights Reserved. Written Mar-24-2026 11:30.
# ==============================================================================

# // REASONING: Standard library for filesystem manipulation and path management.
import os

# // REASONING: Formatting manuscript text to maintain visual 16:9 margins.
import textwrap

# // REASONING: Orchestrating FFmpeg/FFprobe hardware-accelerated binaries via data pipes.
import subprocess

# // REASONING: Core interface for RTX 4060 CUDA memory management.
import torch

# // REASONING: Managing high-level directory tree removals.
import shutil

# // REASONING: Pattern matching to identify and delete orphaned chunk fragments.
import glob

# // REASONING: Visual generation module for the video frames in system RAM.
from PIL import Image

# // REASONING: Canvas manipulation for imprinting text onto memory frames.
from PIL import ImageDraw

# // REASONING: Font loading interface for typography management.
from PIL import ImageFont

# // REASONING: Local neural engine wrapper for Coqui synthesis.
from TTS.api import TTS

# // REASONING: Applying the PyTorch 2.6 security override for weight loading.
_original_torch_load = torch.load

# // REASONING:
# // [INPUT DEFINITION BLOCK]: _patched_torch_load
# // [VARIABLE]: *args | [TYPE]: Tuple | [PURPOSE]: Positional arguments for model load.
# // [VARIABLE]: **kwargs | [TYPE]: Dictionary | [PURPOSE]: Keyword arguments for model load.
def _patched_torch_load(*args, **kwargs):
    # // REASONING: Explicitly allowing local model weight ingestion.
    kwargs['weights_only'] = False
    
    # // REASONING: Returning the execution to the core loader.
    return _original_torch_load(*args, **kwargs)
# // REASONING: Closing _patched_torch_load function.

# // REASONING: Applying the patch to the active Torch instance.
torch.load = _patched_torch_load

# // REASONING:
# // [INPUT DEFINITION BLOCK]: VideoEngine (Class)
# // [PURPOSE]: Encapsulates all hardware rendering, CUDA management, and FFmpeg operations.
class VideoEngine:

    # // REASONING:
    # // [INPUT DEFINITION BLOCK]: __init__
    # // [VARIABLE]: self | [TYPE]: Object | [PURPOSE]: Initializes internal rendering state.
    # // [VARIABLE]: parser | [TYPE]: Object | [PURPOSE]: The Linguistic Workstation instance.
    # // [VARIABLE]: speaker_name | [TYPE]: String | [PURPOSE]: The default fallback XTTS voice profile.
    def __init__(self, parser, speaker_name):
        # // REASONING: Storing the linguistic parser object for text transformations.
        self.parser = parser
        
        # // REASONING: Storing the default voice profile.
        self.speaker_name = speaker_name
        
        # // REASONING: Establishing video resolution width.
        self.width = 1280
        
        # // REASONING: Establishing video resolution height.
        self.height = 720
        
        # // REASONING: Setting standard framerate target.
        self.fps = 30
        
        # // REASONING: Establishing the audio start delay.
        self.lead_in = 1.0
        
        # // REASONING: Establishing the trailing visual hold buffer.
        self.post_roll = 3.0
    # // REASONING: Closing the initialization method.

    # // REASONING:
    # // [INPUT DEFINITION BLOCK]: pre_flight_purge
    # // [VARIABLE]: self | [TYPE]: Object | [PURPOSE]: Accesses execution context.
    def pre_flight_purge(self):
        # // REASONING: Logging the start of the purge sequence.
        print("--- Forensic Action: Initiating Pre-Flight Purge ---")
        
        # // REASONING: Locating orphaned audio chunks using wildcard search.
        orphaned_chunks = glob.glob("chunk_*.aac")
        
        # // REASONING: Iterating through orphaned files found in the directory.
        for f in orphaned_chunks:
            # // REASONING: Deleting the individual audio chunk from the disk.
            os.remove(f)
        # // REASONING: Closing orphaned file iteration loop.
        
        # // REASONING: Evaluating if any orphans existed to log the removal.
        if orphaned_chunks:
            # // REASONING: Logging the total number of chunks removed.
            print(f" > Purged: {len(orphaned_chunks)} orphaned audio chunks.")
        # // REASONING: Closing the orphan check block.
        
        # // REASONING: Defining static temporary compilation files as a list.
        temp_files = ["concat_list.txt", "full_sermon.m4a"]
        
        # // REASONING: Iterating through the temporary files array.
        for f in temp_files:
            # // REASONING: Checking if the specific file currently exists on disk.
            if os.path.exists(f):
                # // REASONING: Deleting the target file.
                os.remove(f)
                
                # // REASONING: Logging the specific deletion action.
                print(f" > Purged: {f}")
            # // REASONING: Closing the file existence conditional check.
        # // REASONING: Closing the temp file loop.
    # // REASONING: Closing the pre_flight_purge method.

    # // REASONING:
    # // [INPUT DEFINITION BLOCK]: execute_render
    # // [VARIABLE]: self | [TYPE]: Object | [PURPOSE]: Accesses internal hardware parameters.
    # // [VARIABLE]: text_file | [TYPE]: String | [PURPOSE]: Path to the manuscript text file.
    # // [VARIABLE]: output_mp4 | [TYPE]: String | [PURPOSE]: Target output filename for the video.
    def execute_render(self, text_file, output_mp4):
        # // REASONING: Triggering the workspace sanitization sequence before rendering.
        self.pre_flight_purge()
        
        # // REASONING: Verifying the physical manuscript file exists on the D: drive.
        if not os.path.exists(text_file):
            # // REASONING: Emitting failure state to the log.
            print(f"ERROR: {text_file} not found. Workspace state invalid.")
            
            # // REASONING: Aborting execution safely because input is missing.
            return
        # // REASONING: Closing the file verification block.
        
        # // REASONING: Opening manuscript file in read mode with UTF-8 encoding.
        with open(text_file, 'r', encoding='utf-8') as f:
            # // REASONING: Loading the full payload to memory.
            file_content = f.read()
            
            # // REASONING: Structuring text into physical paragraph arrays, ignoring empty lines.
            raw_paragraphs = [p.strip() for p in file_content.split('\n') if p.strip()]
        # // REASONING: Closing file stream automatically via the 'with' context manager.
        
        # // REASONING: Announcing primary sequence start with Light Mode notation.
        print(f"SESSION START: {output_mp4} initiated (Light Mode Active).")
        
        # // REASONING: Engaging Coqui engine on the local RTX 4060 CUDA core.
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to("cuda")
        
        # // REASONING: Announcing the start of the acoustic synthesis phase.
        print("--- Phase 1: Phonetic Audio Synthesis ---")
        
        # // REASONING: Creating tracking array for physical audio chunk files.
        chunk_files = []
        
        # // REASONING: Creating a clean array for the visual render phase to prevent tags on screen.
        visual_manuscript = []
        
        # // REASONING: Iterating over manuscript paragraphs by index and content.
        for idx, p in enumerate(raw_paragraphs):
            
            # // REASONING: Extracting voice tag, checking for clone status, and stripping from string.
            clean_text, current_speaker, is_clone = self.parser.extract_voice_info(text=p, default_voice=self.speaker_name)
            
            # // REASONING: Failsafe evaluation to prevent hardware crash if reference WAV is missing.
            if is_clone and not os.path.exists(current_speaker):
                # // REASONING: Alerting the log to the missing physical file.
                print(f"WARNING: Reference audio '{current_speaker}' not found. Reverting to default.")
                
                # // REASONING: Demoting the current speaker back to the fallback profile.
                current_speaker = self.speaker_name
                
                # // REASONING: Disabling the clone flag to prevent parameter routing errors.
                is_clone = False
            # // REASONING: Closing the failsafe logic block.
            
            # // REASONING: Appending the sanitized string to the visual tracking array.
            visual_manuscript.append(clean_text)
            
            # // REASONING: Offloading linguistic translation to the injected Parser object.
            audio_ready_text = self.parser.normalize_text(text=clean_text)
            
            # // REASONING: Offloading boundary chunking to the Parser object.
            sub_chunks = self.parser.split_text(text=audio_ready_text)
            
            # // REASONING: Iterating over individual phonetic chunks.
            for s_idx, chunk in enumerate(sub_chunks):
                # // REASONING: Calculating absolute final sequence flag based on indices.
                is_last = (idx == len(raw_paragraphs) - 1) and (s_idx == len(sub_chunks) - 1)
                
                # // REASONING: Offloading terminal anchoring to the Parser object.
                processed_chunk = self.parser.stabilize_chunk(text=chunk, is_last=is_last)
                
                # // REASONING: Formatting the physical target filename for the chunk.
                fname = f"chunk_{idx}_{s_idx}.aac"
                
                # // REASONING: Checking the active clone flag to determine hardware parameter routing.
                if is_clone:
                    # // REASONING: Printing current synthesis payload and physical WAV target to log.
                    print(f"DEBUG: [CLONE: {current_speaker}] Processing chunk {idx}_{s_idx}")
                    
                    # // REASONING: Instructing GPU to extract vocal characteristics from the physical WAV file.
                    tts.tts_to_file(text=processed_chunk, speaker_wav=current_speaker, language="en", file_path=fname)
                # // REASONING: Handling standard internal voice dictionaries.
                else:
                    # // REASONING: Printing current synthesis payload and internal voice dictionary target to log.
                    print(f"DEBUG: [{current_speaker}] Processing chunk {idx}_{s_idx}")
                    
                    # // REASONING: Instructing GPU to synthesize string using the internal voice dictionary profile.
                    tts.tts_to_file(text=processed_chunk, speaker=current_speaker, language="en", file_path=fname)
                # // REASONING: Closing the parameter routing logic block.
                
                # // REASONING: Appending successful file to the tracking array.
                chunk_files.append(fname)
            # // REASONING: Closing the inner chunk loop.
            
            # // REASONING: Explicitly purging CUDA VRAM to prevent GPU bottlenecks between paragraphs.
            torch.cuda.empty_cache()
        # // REASONING: Closing the outer paragraph synthesis loop.
        
        # // REASONING: Opening the FFmpeg directive text file in write mode.
        with open("concat_list.txt", "w") as f:
            # // REASONING: Iterating tracked files in the array.
            for cf in chunk_files:
                # // REASONING: Appending specific FFmpeg syntax for file concatenation.
                f.write(f"file '{cf}'\n")
            # // REASONING: Closing the tracking iteration loop.
        # // REASONING: Closing the FFmpeg directive file automatically.
        
        # // REASONING: Defining intermediate master audio file path.
        audio_path = "full_sermon.m4a"
        
        # // REASONING: Executing external FFmpeg process to stitch AAC tracks together.
        subprocess.run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', 'concat_list.txt', '-c:a', 'aac', '-b:a', '64k', '-ac', '1', '-ar', '22050', audio_path], check=True)
        
        # // REASONING: Iterating over the temporary phonetic chunks to sweep them from the drive.
        for cf in chunk_files:
            # // REASONING: Unlinking the physical file.
            os.remove(cf)
        # // REASONING: Closing the sweep loop.
        
        # // REASONING: Unlinking the FFmpeg directive text file.
        os.remove("concat_list.txt")
        
        # // REASONING: Querying hardware for precise absolute temporal length using ffprobe.
        res = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'default=noprint_wrappers=1:nokey=1', audio_path], capture_output=True, text=True)
        
        # // REASONING: Casting terminal duration string to float primitive.
        audio_duration = float(res.stdout)
        
        # // REASONING: Calculating maximum sequential frame target for the video loop.
        TOTAL_FRAMES = int((audio_duration + self.lead_in + self.post_roll) * self.fps)
        
        # // REASONING: Calculating temporal freeze marker for post-roll buffer.
        AUDIO_END_FRAME = int((audio_duration + self.lead_in) * self.fps)
        
        # // REASONING: Initializing TrueType typography engine.
        font = ImageFont.truetype("C:/Windows/Fonts/arialbd.ttf", 45)
        
        # // REASONING: Initializing visual data structures for the pre-calculation.
        wrapped_paragraphs = []
        
        # // REASONING: Tracking absolute Y-axis height for the scrolling algorithm.
        total_text_height = 0
        
        # // REASONING: Setting standard visual padding integer between paragraphs.
        padding = 70
        
        # // REASONING: Extracting display geometry from the sanitized visual manuscript.
        for p in visual_manuscript:
            # // REASONING: Formatting line-breaks for 16:9 boundaries.
            p_text = "\n".join(textwrap.wrap(text=p, width=42))
            
            # // REASONING: Establishing virtual bounding box constraints to calculate pixel height.
            bbox = ImageDraw.Draw(Image.new('RGB', (self.width, self.height))).multiline_textbbox((0, 0), p_text, font=font)
            
            # // REASONING: Calculating geometric difference to find pure pixel height.
            p_h = bbox[3] - bbox[1]
            
            # // REASONING: Storing structured visual data as a tuple.
            wrapped_paragraphs.append((p_text, p_h))
            
            # // REASONING: Incrementing master scrolling height.
            total_text_height += p_h + padding
        # // REASONING: Closing the geometric extraction loop.
        
        # // REASONING: Building NVENC hardware argument block expecting raw RGB binary stream via standard input.
        ffmpeg_cmd = [
            'ffmpeg', '-y', 
            '-f', 'rawvideo', '-vcodec', 'rawvideo',
            '-s', f'{self.width}x{self.height}', '-pix_fmt', 'rgb24', '-r', str(self.fps),
            '-i', '-', 
            '-i', audio_path, 
            '-af', f'adelay={int(self.lead_in*1000)}|{int(self.lead_in*1000)}', 
            '-c:v', 'h264_nvenc', '-preset', 'p4', 
            '-c:a', 'aac', '-b:a', '64k', '-ac', '1', '-ar', '22050',
            '-pix_fmt', 'yuv420p', '-b:v', '4M',
            output_mp4
        ]
        
        # // REASONING: Firing background execution thread for NVENC compiler, opening standard input for binary writing.
        ffmpeg_process = subprocess.Popen(ffmpeg_cmd, stdin=subprocess.PIPE)
        
        # // REASONING: Calculating constant scroll speed based on duration and geometric height.
        pixels_per_frame = total_text_height / (audio_duration * self.fps)
        
        # // REASONING: Assigning mid-point display coordinate for the start of the scroll.
        start_y = self.height / 2 
        
        # // REASONING: Commencing Phase 2 & 3 simultaneous rendering notation.
        print(f"--- Phase 2 & 3: Rendering {TOTAL_FRAMES} Frames (Light Mode / Memory Pipe) ---")
        
        # // REASONING: Executing absolute frame mapping sequence in volatile system memory.
        for i in range(TOTAL_FRAMES):
            # // REASONING: LIGHT MODE: Initializing RGB canvas container to White (255, 255, 255).
            img = Image.new('RGB', (self.width, self.height), color=(255, 255, 255))
            
            # // REASONING: Engaging draw engine on the white canvas target.
            draw = ImageDraw.Draw(img)
            
            # // REASONING: Calculating dynamic vertical offset, locked by the terminal hold marker.
            current_scroll_y = start_y - (pixels_per_frame * (min(i, AUDIO_END_FRAME)))
            
            # // REASONING: Mapping offset reference for iteration.
            temp_y = current_scroll_y
            
            # // REASONING: Iterating over calculated display blocks.
            for p_text, p_h in wrapped_paragraphs:
                # // REASONING: Discarding coordinates outside of visible render plane to conserve CPU.
                if -800 < temp_y < 800:
                    # // REASONING: LIGHT MODE: Inverting text glyphs to Black (0, 0, 0).
                    draw.multiline_text((self.width/2, temp_y), p_text, font=font, fill=(0, 0, 0), anchor="ma", align="center", spacing=8)
                # // REASONING: Closing the boundary check.
                
                # // REASONING: Pushing coordinate down for the subsequent paragraph.
                temp_y += p_h + padding
            # // REASONING: Closing the paragraph draw sequence loop.
            
            # // REASONING: Streaming the raw bytes of the frame directly into the GPU pipe.
            ffmpeg_process.stdin.write(img.tobytes())
        # // REASONING: Closing the total sequence map loop.
        
        # // REASONING: Sealing the standard input pipe to instruct FFmpeg the video stream is concluded.
        ffmpeg_process.stdin.close()
        
        # // REASONING: Forcing the primary Python thread to halt until the GPU finishes writing the final MP4 container.
        ffmpeg_process.wait()
        
        # // REASONING: Unlinking the final intermediary audio construct from the drive.
        os.remove(audio_path)
        
        # // REASONING: Confirming complete modular success to the environment.
        print(f"SUCCESS: {output_mp4} finalized with Inverted Palette.")
    # // REASONING: Closing the execute_render method.
# // REASONING: Closing the VideoEngine class.