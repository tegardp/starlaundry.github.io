#!/usr/bin/env python3
"""
Star Laundry Reel #1 Assembly Script
=====================================
Assembles all generated clips, voiceover, text overlays, and background music
into the final 1080x1920 vertical reel using ffmpeg.

Requirements:
    - Python 3.8+
    - ffmpeg installed (brew install ffmpeg)
    - All clips generated and placed in the clips/ directory
    - Voiceover audio in audio/ directory

Usage:
    cd /Users/tegardp/Code/starlaundry
    python3 marketing/shortform/production/assemble-reel-01.py

Output:
    marketing/shortform/production/REEL-01-FINAL.mp4
"""

import os
import subprocess
import sys
from pathlib import Path

# ============================================================
# CONFIGURATION
# ============================================================

BASE_DIR = Path("/Users/tegardp/Code/starlaundry/marketing/shortform/production")
ASSETS_DIR = Path("/Users/tegardp/Code/starlaundry/marketing/assets/images")
CLIPS_DIR = BASE_DIR / "clips"
AUDIO_DIR = BASE_DIR / "audio"
GRAPHICS_DIR = BASE_DIR / "graphics"
TEMP_DIR = BASE_DIR / "temp"
OUTPUT_FILE = BASE_DIR / "REEL-01-FINAL.mp4"

# Video settings
WIDTH = 1080
HEIGHT = 1920
FPS = 30
DURATION_TOTAL = 30  # seconds

# Brand colors for text overlays (ffmpeg uses hex without #)
COLOR_WHITE = "white"
COLOR_YELLOW = "0xFBB818"
COLOR_BLUE = "0x2AADE0"
COLOR_BLACK = "black"

# Background music volume (0.0 to 1.0, keep low so voiceover is clear)
BG_MUSIC_VOLUME = 0.15

# Scene definitions: (clip_file, start_time, duration, overlay_text)
SCENES = [
    {
        "clip": CLIPS_DIR / "clip-3a-suitcase-open.mp4",
        "duration": 5.0,
        "text": "Baru pulang mudik?",
        "text_color": COLOR_WHITE,
    },
    {
        "clip": CLIPS_DIR / "clip-2a-dirty-laundry.mp4",
        "duration": 5.0,
        "text": "Males nyuci sendiri...",
        "text_color": COLOR_WHITE,
    },
    {
        "clip": CLIPS_DIR / "clip-2b-machines-running.mp4",
        "duration": 4.0,
        "text": "Star Laundry BUKA LAGI!",
        "text_color": COLOR_YELLOW,
    },
    {
        "clip": ASSETS_DIR / "Mesin.mp4",
        "duration": 4.0,
        "text": "Tinggal drop off, beres!",
        "text_color": COLOR_WHITE,
    },
    {
        "clip": CLIPS_DIR / "clip-2c-folding-clothes.mp4",
        "duration": 3.0,
        "text": "Bersih Wangi Rapi",
        "text_color": COLOR_WHITE,
    },
    {
        "clip": ASSETS_DIR / "Orang lagi lipat pakaian.mp4",
        "duration": 3.0,
        "text": "Tinggal pakai lagi!",
        "text_color": COLOR_WHITE,
    },
    {
        "clip": CLIPS_DIR / "clip-2d-clean-shelves.mp4",
        "duration": 4.0,
        "text": "Tinggal ambil!",
        "text_color": COLOR_WHITE,
    },
    {
        "clip": GRAPHICS_DIR / "cta-endcard.png",
        "duration": 2.0,
        "text": "",  # CTA card already has text
        "text_color": COLOR_WHITE,
        "is_image": True,
    },
]

VOICEOVER = AUDIO_DIR / "reel-01-voiceover.mp3"
BG_MUSIC = AUDIO_DIR / "background-music.mp3"  # Optional: provide your own


def check_ffmpeg():
    """Check if ffmpeg is installed."""
    try:
        subprocess.run(
            ["ffmpeg", "-version"],
            capture_output=True,
            check=True,
        )
        print("[OK] ffmpeg is installed")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[ERROR] ffmpeg is not installed. Install it with: brew install ffmpeg")
        sys.exit(1)


def check_files():
    """Check which required files exist."""
    missing = []
    available = []

    for i, scene in enumerate(SCENES):
        clip_path = scene["clip"]
        if clip_path.exists():
            available.append(f"  Scene {i+1}: {clip_path.name}")
        else:
            missing.append(f"  Scene {i+1}: {clip_path.name}")

    if VOICEOVER.exists():
        available.append(f"  Voiceover: {VOICEOVER.name}")
    else:
        missing.append(f"  Voiceover: {VOICEOVER.name}")

    if BG_MUSIC.exists():
        available.append(f"  Background music: {BG_MUSIC.name}")
    else:
        available.append(f"  Background music: {BG_MUSIC.name} (OPTIONAL - will skip)")

    print("\n[FILES AVAILABLE]")
    for f in available:
        print(f)

    if missing:
        print("\n[FILES MISSING]")
        for f in missing:
            print(f)
        print(
            "\nSome files are missing. Generate them using the tools described in"
            " REEL-01-ENHANCED.md first."
        )
        response = input("\nContinue with available files only? (y/n): ")
        if response.lower() != "y":
            sys.exit(0)

    return missing


def prepare_directories():
    """Create necessary directories."""
    for d in [CLIPS_DIR, AUDIO_DIR, GRAPHICS_DIR, TEMP_DIR]:
        d.mkdir(parents=True, exist_ok=True)
    print("[OK] Directories ready")


def prepare_clip(scene_index, scene):
    """
    Prepare a single clip: scale to 1080x1920, set duration, add text overlay.
    Returns the path to the prepared temp clip.
    """
    clip_path = scene["clip"]
    duration = scene["duration"]
    text = scene["text"]
    text_color = scene["text_color"]
    is_image = scene.get("is_image", False)
    output_path = TEMP_DIR / f"scene-{scene_index:02d}.mp4"

    if not clip_path.exists():
        # Create a blue placeholder for missing clips
        print(f"  Creating placeholder for missing Scene {scene_index + 1}...")
        cmd = [
            "ffmpeg", "-y",
            "-f", "lavfi",
            "-i", f"color=c=0x2AADE0:s={WIDTH}x{HEIGHT}:d={duration}:r={FPS}",
            "-f", "lavfi",
            "-i", f"anullsrc=r=44100:cl=stereo",
            "-t", str(duration),
            "-vf", (
                f"drawtext=text='{text or 'Scene ' + str(scene_index + 1)}':"
                f"fontsize=48:fontcolor=white:"
                f"x=(w-text_w)/2:y=(h-text_h)/2:"
                f"borderw=3:bordercolor=black"
            ),
            "-c:v", "libx264",
            "-preset", "fast",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-shortest",
            str(output_path),
        ]
        subprocess.run(cmd, capture_output=True, check=True)
        return output_path

    if is_image:
        # Convert static image to video clip
        print(f"  Converting image to {duration}s clip: {clip_path.name}...")
        cmd = [
            "ffmpeg", "-y",
            "-loop", "1",
            "-i", str(clip_path),
            "-f", "lavfi",
            "-i", f"anullsrc=r=44100:cl=stereo",
            "-t", str(duration),
            "-vf", (
                f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=decrease,"
                f"pad={WIDTH}:{HEIGHT}:(ow-iw)/2:(oh-ih)/2:color=0x2AADE0,"
                f"fps={FPS}"
            ),
            "-c:v", "libx264",
            "-preset", "fast",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-shortest",
            str(output_path),
        ]
    else:
        # Process video clip: scale, crop/pad to 1080x1920, trim, add text
        print(f"  Processing clip: {clip_path.name} ({duration}s)...")

        # Build video filter
        vf_parts = [
            f"scale={WIDTH}:{HEIGHT}:force_original_aspect_ratio=decrease",
            f"pad={WIDTH}:{HEIGHT}:(ow-iw)/2:(oh-ih)/2:color=0x2AADE0",
            f"fps={FPS}",
        ]

        # Add text overlay if specified
        if text:
            # Escape special characters for ffmpeg drawtext
            escaped_text = text.replace("'", "\\'").replace(":", "\\:")
            vf_parts.append(
                f"drawtext=text='{escaped_text}':"
                f"fontsize=48:"
                f"fontcolor={text_color}:"
                f"x=(w-text_w)/2:"
                f"y=h-text_h-200:"
                f"borderw=3:"
                f"bordercolor=black"
            )

        vf = ",".join(vf_parts)

        cmd = [
            "ffmpeg", "-y",
            "-i", str(clip_path),
            "-t", str(duration),
            "-vf", vf,
            "-af", f"apad=whole_dur={duration}",
            "-c:v", "libx264",
            "-preset", "fast",
            "-pix_fmt", "yuv420p",
            "-c:a", "aac",
            "-ar", "44100",
            "-ac", "2",
            str(output_path),
        ]

    subprocess.run(cmd, capture_output=True, check=True)
    return output_path


def add_crossfade(clip_paths):
    """
    Concatenate clips with short crossfade transitions.
    Returns path to the concatenated video (no audio mix yet).
    """
    if len(clip_paths) == 0:
        print("[ERROR] No clips to concatenate")
        sys.exit(1)

    if len(clip_paths) == 1:
        return clip_paths[0]

    # Use concat demuxer for simplicity (no crossfade, just clean cuts)
    # Crossfade can cause timing issues; clean cuts are more reliable
    concat_file = TEMP_DIR / "concat-list.txt"
    with open(concat_file, "w") as f:
        for path in clip_paths:
            f.write(f"file '{path}'\n")

    output = TEMP_DIR / "concatenated.mp4"
    cmd = [
        "ffmpeg", "-y",
        "-f", "concat",
        "-safe", "0",
        "-i", str(concat_file),
        "-c:v", "libx264",
        "-preset", "fast",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-ar", "44100",
        str(output),
    ]
    print("\n[CONCATENATING] Joining all scenes...")
    subprocess.run(cmd, capture_output=True, check=True)
    return output


def mix_audio(video_path):
    """
    Mix voiceover and optional background music onto the concatenated video.
    Returns path to the final output.
    """
    has_voiceover = VOICEOVER.exists()
    has_bg_music = BG_MUSIC.exists()

    if not has_voiceover and not has_bg_music:
        print("[AUDIO] No voiceover or music found. Using video as-is.")
        return video_path

    print("\n[AUDIO] Mixing audio tracks...")

    inputs = ["-i", str(video_path)]
    filter_parts = []
    audio_inputs = ["[0:a]"]  # video's own audio (silent from our processing)

    input_index = 1

    if has_voiceover:
        inputs.extend(["-i", str(VOICEOVER)])
        filter_parts.append(f"[{input_index}:a]volume=1.0[vo]")
        audio_inputs.append("[vo]")
        input_index += 1
        print(f"  Added voiceover: {VOICEOVER.name}")

    if has_bg_music:
        inputs.extend(["-i", str(BG_MUSIC)])
        # Get video duration for fade-out
        filter_parts.append(
            f"[{input_index}:a]volume={BG_MUSIC_VOLUME},"
            f"afade=t=out:st=28:d=2[bg]"
        )
        audio_inputs.append("[bg]")
        input_index += 1
        print(f"  Added background music at {int(BG_MUSIC_VOLUME*100)}% volume")

    # Mix all audio streams
    n_audio = len(audio_inputs)
    mix_input = "".join(audio_inputs)
    filter_parts.append(
        f"{mix_input}amix=inputs={n_audio}:duration=longest:dropout_transition=2[aout]"
    )

    filter_complex = ";".join(filter_parts)

    output = TEMP_DIR / "with-audio.mp4"
    cmd = [
        "ffmpeg", "-y",
        *inputs,
        "-filter_complex", filter_complex,
        "-map", "0:v",
        "-map", "[aout]",
        "-c:v", "copy",
        "-c:a", "aac",
        "-ar", "44100",
        "-t", str(DURATION_TOTAL),
        str(output),
    ]

    subprocess.run(cmd, capture_output=True, check=True)
    return output


def finalize(assembled_path):
    """Copy final file to output location."""
    print(f"\n[FINALIZING] Writing output to {OUTPUT_FILE}...")

    cmd = [
        "ffmpeg", "-y",
        "-i", str(assembled_path),
        "-c:v", "libx264",
        "-preset", "slow",
        "-crf", "18",
        "-pix_fmt", "yuv420p",
        "-c:a", "aac",
        "-b:a", "192k",
        "-movflags", "+faststart",
        str(OUTPUT_FILE),
    ]
    subprocess.run(cmd, capture_output=True, check=True)


def cleanup():
    """Remove temporary files."""
    import shutil
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)
    print("[OK] Cleaned up temporary files")


def main():
    print("=" * 60)
    print("  Star Laundry Reel #1 Assembly Script")
    print("  Output: 1080x1920, 30fps, ~30 seconds")
    print("=" * 60)

    check_ffmpeg()
    prepare_directories()
    missing = check_files()

    # Step 1: Prepare each scene clip
    print("\n[STEP 1] Preparing individual scene clips...")
    prepared_clips = []
    for i, scene in enumerate(SCENES):
        try:
            clip_path = prepare_clip(i, scene)
            prepared_clips.append(clip_path)
            print(f"  [OK] Scene {i+1} ready")
        except subprocess.CalledProcessError as e:
            print(f"  [ERROR] Scene {i+1} failed: {e}")
            print(f"  stderr: {e.stderr.decode() if e.stderr else 'none'}")
            sys.exit(1)

    # Step 2: Concatenate all clips
    concatenated = add_crossfade(prepared_clips)
    print("[OK] All scenes concatenated")

    # Step 3: Mix audio (voiceover + background music)
    try:
        with_audio = mix_audio(concatenated)
        print("[OK] Audio mixed")
    except subprocess.CalledProcessError as e:
        print(f"[WARNING] Audio mixing failed, using video without mixed audio")
        print(f"  stderr: {e.stderr.decode() if e.stderr else 'none'}")
        with_audio = concatenated

    # Step 4: Final encode
    try:
        finalize(with_audio)
        print("[OK] Final video encoded")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] Final encoding failed: {e}")
        print(f"  stderr: {e.stderr.decode() if e.stderr else 'none'}")
        sys.exit(1)

    # Step 5: Cleanup
    cleanup()

    # Summary
    if OUTPUT_FILE.exists():
        size_mb = OUTPUT_FILE.stat().st_size / (1024 * 1024)
        print("\n" + "=" * 60)
        print(f"  DONE! Final reel saved to:")
        print(f"  {OUTPUT_FILE}")
        print(f"  File size: {size_mb:.1f} MB")
        print("=" * 60)
    else:
        print("\n[ERROR] Output file was not created.")
        sys.exit(1)


if __name__ == "__main__":
    main()
