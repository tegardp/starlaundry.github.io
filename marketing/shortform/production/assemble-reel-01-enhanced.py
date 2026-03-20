#!/usr/bin/env python3
"""
Star Laundry — Reel #1 Enhanced Assembly
Combines Kling AI clips, Nano Banana clips, Canva CTA, and ElevenLabs voiceover.

Usage:
  1. Generate all clips using prompts in REEL-01-VIDEO-PROMPTS.md
  2. Place files in output/ folder with the expected names
  3. Run: python3 assemble-reel-01-enhanced.py
  4. Import result into CapCut to add music + auto-captions
"""

import subprocess, os, sys

OUT = "/Users/tegardp/Code/starlaundry/marketing/shortform/production/output"
FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
W, H, FPS = 1080, 1920, 30

# Expected input files
CLIPS = {
    "nano_koper":    f"{OUT}/nano-01-koper.mp4",
    "kling_tumpukan": f"{OUT}/kling-01-tumpukan.mp4",
    "kling_toko":    f"{OUT}/kling-05-toko.mp4",
    "kling_mesin":   f"{OUT}/kling-02-mesin.mp4",
    "nano_transisi": f"{OUT}/nano-02-transformasi.mp4",
    "kling_lipat":   f"{OUT}/kling-03-lipat.mp4",
    "kling_rak":     f"{OUT}/kling-04-rak.mp4",
}
CTA_IMG = f"{OUT}/canva-cta.png"
VOICEOVER = f"{OUT}/voiceover-reel-01.mp3"
OUTPUT = f"{OUT}/reel-01-enhanced-final.mp4"


def run_ff(args, label):
    r = subprocess.run(["ffmpeg"] + args, capture_output=True)
    if r.returncode != 0:
        print(f"  FAILED: {label}")
        print(r.stderr.decode()[-800:])
        sys.exit(1)
    print(f"  {label}")


def scale_clip(input_path, output_path, duration, texts=None):
    """Scale any video clip to 1080x1920 with optional text overlays."""
    text_filters = ""
    if texts:
        for t in texts:
            text_filters += (
                f",drawtext=fontfile='{t.get('font', FONT)}':"
                f"text='{t['text']}':"
                f"fontsize={t.get('size', 64)}:"
                f"fontcolor={t.get('color', 'white')}:"
                f"borderw={t.get('bw', 3)}:bordercolor={t.get('bc', 'black')}:"
                f"x={t.get('x', '(w-text_w)/2')}:y={t['y']}:"
                f"enable='between(t,{t.get('start', 0.3)},{duration})'"
            )

    filt = (
        f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
        f"crop={W}:{H},setsar=1,format=yuv420p"
        f"{text_filters}"
    )

    run_ff([
        "-y", "-i", input_path,
        "-filter_complex", filt,
        "-t", str(duration), "-r", str(FPS),
        "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-an", output_path
    ], os.path.basename(input_path))


def img_to_clip(img_path, output_path, duration, texts=None):
    """Convert static image to video clip."""
    text_filters = ""
    if texts:
        for t in texts:
            text_filters += (
                f",drawtext=fontfile='{t.get('font', FONT)}':"
                f"text='{t['text']}':"
                f"fontsize={t.get('size', 64)}:"
                f"fontcolor={t.get('color', 'white')}:"
                f"borderw={t.get('bw', 3)}:bordercolor={t.get('bc', 'black')}:"
                f"x={t.get('x', '(w-text_w)/2')}:y={t['y']}:"
                f"enable='between(t,{t.get('start', 0.3)},{duration})'"
            )

    filt = (
        f"[0:v]scale={W}:{H}:force_original_aspect_ratio=increase,"
        f"crop={W}:{H},setsar=1,format=yuv420p"
        f"{text_filters}"
    )

    run_ff([
        "-y", "-loop", "1", "-i", img_path,
        "-filter_complex", filt,
        "-t", str(duration), "-r", str(FPS),
        "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        output_path
    ], os.path.basename(img_path))


def build():
    temp_clips = []

    # Scene 1: Hook — suitcase (0:00-0:03)
    c1 = f"{OUT}/tmp_s1.mp4"
    scale_clip(CLIPS["nano_koper"], c1, 3, [
        {"text": "BARU PULANG MUDIK?", "y": "(h/2)-60", "size": 72,
         "color": "white", "bw": 3, "start": 0.2},
    ])
    temp_clips.append(c1)

    # Scene 2: Problem — dirty laundry baskets (0:03-0:06)
    c2 = f"{OUT}/tmp_s2.mp4"
    scale_clip(CLIPS["kling_tumpukan"], c2, 3, [
        {"text": "Isi koper pasti kayak gini...", "y": "(h/2)+20", "size": 48,
         "font": FONT_REG, "bw": 2, "start": 0.2},
    ])
    temp_clips.append(c2)

    # Scene 3: Problem cont — same clip zoomed (0:06-0:10)
    c3 = f"{OUT}/tmp_s3.mp4"
    scale_clip(CLIPS["kling_tumpukan"], c3, 4, [
        {"text": "TUMPUKAN", "y": "(h/2)-80", "size": 96,
         "color": "0xFBB818", "bw": 4, "start": 0.2},
        {"text": "BAJU KOTOR", "y": "(h/2)+40", "size": 96,
         "color": "0xFBB818", "bw": 4, "start": 0.5},
        {"text": "Males banget nyuci sendiri...", "y": "(h/2)+170", "size": 42,
         "font": FONT_REG, "bw": 2, "start": 1.0},
    ])
    temp_clips.append(c3)

    # Scene 4: Solution — storefront (0:10-0:15)
    c4 = f"{OUT}/tmp_s4.mp4"
    scale_clip(CLIPS["kling_toko"], c4, 5, [
        {"text": "STAR LAUNDRY", "y": "300", "size": 84,
         "color": "0xFBB818", "bc": "0x2AADE0", "bw": 4, "start": 0.5},
        {"text": "BUKA LAGI!", "y": "400", "size": 96,
         "bc": "0x2AADE0", "bw": 4, "start": 0.8},
        {"text": "Mulai 24 Maret 2026", "y": "520", "size": 48,
         "color": "0xFBB818", "bw": 2, "start": 1.2},
    ])
    temp_clips.append(c4)

    # Scene 5: Solution — machines running (0:15-0:18)
    c5 = f"{OUT}/tmp_s5.mp4"
    scale_clip(CLIPS["kling_mesin"], c5, 3, [
        {"text": "Tinggal drop off, beres!", "y": str(H-350), "size": 52,
         "font": FONT_REG, "bw": 2, "start": 0.3},
    ])
    temp_clips.append(c5)

    # Scene 6: Transformation — dirty to clean (0:18-0:21)
    c6 = f"{OUT}/tmp_s6.mp4"
    scale_clip(CLIPS["nano_transisi"], c6, 3, [
        {"text": "BERSIH", "y": "350", "size": 88,
         "color": "0xFBB818", "bw": 4, "start": 0.3},
        {"text": "WANGI", "y": "460", "size": 88,
         "color": "0xFBB818", "bw": 4, "start": 0.8},
        {"text": "PASTI RAPI!", "y": "570", "size": 88,
         "bc": "0x2AADE0", "bw": 4, "start": 1.3},
    ])
    temp_clips.append(c6)

    # Scene 7: Staff folding (0:21-0:24)
    c7 = f"{OUT}/tmp_s7.mp4"
    scale_clip(CLIPS["kling_lipat"], c7, 3, [
        {"text": "Tinggal pakai lagi!", "y": str(H-350), "size": 52,
         "color": "0xFBB818", "bw": 3, "start": 0.3},
    ])
    temp_clips.append(c7)

    # Scene 8: Clean shelves (0:24-0:28)
    c8 = f"{OUT}/tmp_s8.mp4"
    scale_clip(CLIPS["kling_rak"], c8, 4, [
        {"text": "Cucian kamu aman di sini!", "y": str(H-400), "size": 56,
         "bc": "0x2AADE0", "bw": 3, "start": 0.3},
        {"text": "Rapi, terlabel, siap diambil", "y": str(H-320), "size": 40,
         "color": "0xFBB818", "font": FONT_REG, "bw": 2, "start": 0.8},
    ])
    temp_clips.append(c8)

    # Scene 9: CTA end card (0:28-0:30)
    c9 = f"{OUT}/tmp_s9.mp4"
    if os.path.exists(CTA_IMG):
        img_to_clip(CTA_IMG, c9, 2)
    else:
        # Fallback: generate CTA with ffmpeg
        filt = (
            f"color=c=0x2AADE0:s={W}x{H}:d=2:r={FPS},format=yuv420p"
            f",drawtext=fontfile='{FONT}':text='Star Laundry Boyolali':fontsize=52:fontcolor=white"
            f":x=(w-text_w)/2:y=700"
            f",drawtext=fontfile='{FONT}':text='WA 0822-2567-2756':fontsize=60:fontcolor=0xFBB818"
            f":x=(w-text_w)/2:y=900"
            f",drawtext=fontfile='{FONT_REG}':text='Buka 07.00 - 21.00':fontsize=44:fontcolor=white"
            f":x=(w-text_w)/2:y=1000"
            f",drawtext=fontfile='{FONT_REG}':text='Jl. Jambu, Boyolali':fontsize=40:fontcolor=white"
            f":x=(w-text_w)/2:y=1080"
            f",drawtext=fontfile='{FONT}':text='Bersih Wangi, Pasti Rapi':fontsize=48:fontcolor=0xFBB818"
            f":x=(w-text_w)/2:y=1250"
        )
        run_ff([
            "-y", "-f", "lavfi", "-i", filt,
            "-t", "2", "-r", str(FPS),
            "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "fast", "-crf", "22",
            c9
        ], "CTA fallback")
    temp_clips.append(c9)

    # Concat all clips
    concat_file = f"{OUT}/concat_enhanced.txt"
    with open(concat_file, "w") as f:
        for c in temp_clips:
            f.write(f"file '{c}'\n")

    concat_vid = f"{OUT}/tmp_concat.mp4"
    run_ff([
        "-y", "-f", "concat", "-safe", "0", "-i", concat_file,
        "-c:v", "libx264", "-preset", "fast", "-crf", "22",
        "-pix_fmt", "yuv420p", "-r", str(FPS),
        concat_vid
    ], "Concat all scenes")

    # Add voiceover audio
    if os.path.exists(VOICEOVER):
        run_ff([
            "-y", "-i", concat_vid, "-i", VOICEOVER,
            "-filter_complex",
            f"[1:a]adelay=500|500,apad=pad_dur=6[vo]",
            "-map", "0:v", "-map", "[vo]",
            "-c:v", "copy", "-c:a", "aac", "-b:a", "192k",
            "-shortest",
            "-movflags", "+faststart",
            OUTPUT
        ], "Add voiceover")
    else:
        os.rename(concat_vid, OUTPUT)
        print("  (No voiceover found, output is video-only)")

    # Cleanup
    for c in temp_clips:
        if os.path.exists(c):
            os.remove(c)
    if os.path.exists(concat_file):
        os.remove(concat_file)
    if os.path.exists(concat_vid):
        os.remove(concat_vid)

    return OUTPUT


if __name__ == "__main__":
    print("Assembling Reel #1 Enhanced")
    print(f"Output: {W}x{H}, {FPS}fps\n")

    # Check what we have
    missing = []
    for name, path in CLIPS.items():
        status = "OK" if os.path.exists(path) else "MISSING"
        if status == "MISSING":
            missing.append(name)
        print(f"  [{status}] {name}: {os.path.basename(path)}")

    print(f"  [{'OK' if os.path.exists(CTA_IMG) else 'MISSING (will use fallback)'}] CTA image")
    print(f"  [{'OK' if os.path.exists(VOICEOVER) else 'MISSING (video-only)'}] Voiceover")

    if missing:
        print(f"\nMissing {len(missing)} clips: {', '.join(missing)}")
        print("Generate them using prompts in REEL-01-VIDEO-PROMPTS.md")
        print("Place files in output/ folder with the expected names.")
        sys.exit(1)

    print()
    output = build()

    dur = subprocess.check_output([
        "ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", output
    ]).decode().strip()
    mb = os.path.getsize(output) / (1024 * 1024)

    print(f"\nDone!")
    print(f"  File: {output}")
    print(f"  Duration: {float(dur):.1f}s")
    print(f"  Size: {mb:.1f}MB")
    print(f"\nNext steps:")
    print(f"  1. Import into CapCut")
    print(f"  2. Add background music (search 'upbeat happy')")
    print(f"  3. Enable auto-captions (Bahasa Indonesia)")
    print(f"  4. Export and upload to IG Reels + TikTok")
