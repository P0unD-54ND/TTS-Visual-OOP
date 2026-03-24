# -*- coding: utf-8 -*-
# ==============================================================================
# [FILE]: main.py
# [TITLE]: Local Coqui XTTS-v2 OOP Project Manager (Forensic Stopwatch Edition)
# [SECURITY PROTOCOL]: Local Execution Only - Workspace Level D: Drive
# [FORENSIC STRATEGY]: Dynamic Timestamping | Execution Benchmarking.
# Copyright (c) 2026 Dennis Sayer. All Rights Reserved. Written Mar-24-2026 11:05.
# ==============================================================================

# // REASONING: System-level interface for stream redirection and logging.
import sys
# // REASONING: Time module for generating unique, chronological file signatures.
from datetime import datetime
# // REASONING: Core time module for establishing absolute execution benchmarks.
import time

# // REASONING: Importing the linguistic workstation class from the local module.
from theological_parser import TheologicalParser
# // REASONING: Importing the hardware rendering workstation class from the local module.
from video_engine import VideoEngine

# // REASONING:
# // [INPUT DEFINITION BLOCK]: ForensicLogger (Class)
# // [PURPOSE]: Captures terminal output and mirrors it to a physical log file on the D: drive.
class ForensicLogger:
    
    # // REASONING:
    # // [INPUT DEFINITION BLOCK]: __init__
    # // [VARIABLE]: self | [TYPE]: Object | [PURPOSE]: Initializes internal stream state.
    # // [VARIABLE]: filename | [TYPE]: String | [PURPOSE]: The target path for the log file.
    def __init__(self, filename):
        # // REASONING: Capturing the original standard output handle.
        self.terminal = sys.stdout
        # // REASONING: Opening the log file in append/write mode with UTF-8 support.
        self.log = open(filename, "w", encoding="utf-8")
    # // REASONING: Closing the initialization method.

    # // REASONING:
    # // [INPUT DEFINITION BLOCK]: write
    # // [VARIABLE]: self | [TYPE]: Object | [PURPOSE]: Accesses internal stream state.
    # // [VARIABLE]: message | [TYPE]: String | [PURPOSE]: The text payload to mirror.
    def write(self, message):
        # // REASONING: Writing output to the standard console.
        self.terminal.write(message)
        # // REASONING: Writing output to the persistent file.
        self.log.write(message)
        # // REASONING: Forcing disk commit to prevent cache loss on termination.
        self.log.flush()
    # // REASONING: Closing the write method.

    # // REASONING:
    # // [INPUT DEFINITION BLOCK]: flush
    # // [VARIABLE]: self | [TYPE]: Object | [PURPOSE]: Accesses internal stream state.
    def flush(self):
        # // REASONING: Synchronizing the terminal buffer.
        self.terminal.flush()
        # // REASONING: Synchronizing the file buffer.
        self.log.flush()
    # // REASONING: Closing the flush method.
# // REASONING: Closing the ForensicLogger class.

# // REASONING: Verifying the script is running as the primary execution thread.
if __name__ == "__main__":
    
    # // REASONING: Extracting the current system time formatted as YYYY-MM-DD_HHMM.
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M")
    
    # // REASONING: Establishing the shared prefix for the session's outputs.
    base_filename = f"Sermon_Export_{timestamp}"
    
    # // REASONING: Constructing the physical path for the diagnostic log.
    log_filepath = f"{base_filename}_log.txt"
    
    # // REASONING: Constructing the physical path for the final MP4 video.
    video_filepath = f"{base_filename}.mp4"

    # // REASONING: Rerouting global standard output to the dynamically named session logger.
    sys.stdout = ForensicLogger(log_filepath)
    # // REASONING: Rerouting global standard error to capture fatal tracebacks in the same log.
    sys.stderr = sys.stdout
    
    # // REASONING: Logging the start of the Object-Oriented initialization.
    print("--- System Initialization: OOP Architecture Active ---")
    # // REASONING: Confirming the dynamic binding to the console.
    print(f"--- Dynamic Archiving: Locked to [{base_filename}] ---")
    
    # // REASONING: Instantiating the Linguistic Workstation to handle text processing.
    parser_module = TheologicalParser()
    
    # // REASONING: Instantiating the Hardware Workstation, injecting the parser dependency.
    render_engine = VideoEngine(parser=parser_module, speaker_name="Aaron Dreschner")
    
    # // REASONING: Capturing the precise Unix epoch timestamp immediately before hardware spin-up.
    start_time = time.time()
    
    # // REASONING: Firing the primary rendering sequence with the timestamped output target.
    render_engine.execute_render(text_file="source_manuscript.txt", output_mp4=video_filepath)
    
    # // REASONING: Capturing the precise Unix epoch timestamp immediately after successful muxing.
    end_time = time.time()
    
    # // REASONING: Calculating total elapsed rendering time in pure seconds.
    elapsed_seconds = end_time - start_time
    
    # // REASONING: Structuring elapsed time into whole minutes.
    elapsed_minutes = int(elapsed_seconds // 60)
    
    # // REASONING: Structuring the residual elapsed time into seconds.
    residual_seconds = int(elapsed_seconds % 60)
    
    # // REASONING: Injecting the final performance benchmark into the forensic log.
    print(f"--- Session Terminated: Total Render Time: {elapsed_minutes}m {residual_seconds}s ---")
# // REASONING: Closing the main execution block.