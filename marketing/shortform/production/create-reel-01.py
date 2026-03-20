#!/usr/bin/env python3
"""
Star Laundry — Reel #1: "Buka Lagi! Tumpukan Baju Mudik"
Generates a 30-second vertical reel (1080x1920) using real shop assets.
"""

import subprocess
import os
import sys

BASE = "/Users/tegardp/Code/starlaundry/marketing/assets/images"
STATIC = "/Users/tegardp/Code/starlaundry/static/images"
OUT_DIR = "/Users/tegardp/Code/starlaundry/marketing/shortform/production/output"
OUTPUT = f"{OUT_DIR}/reel-01-buka-lagi.mp4"
os.makedirs(OUT_DIR, exist_ok=True)

TUMPUKAN = f"{BASE}/Tumpukan baju.jpeg"
MESIN_IMG = f"{BASE}/Mesin dan interior.jpeg"
MESIN_VID = f"{BASE}/Mesin.mp4"
LIPAT_VID = f"{BASE}/Orang lagi lipat pakaian.mp4"
RAK_IMG = f"{BASE}/rak Laundry 2.jpeg"
TOKO_IMG = f"{BASE}/Toko.jpeg"
LOGO = f"{STATIC}/logo.png"

FONT = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
FONT_REG = "/System/Library/Fonts/Supplemental/Arial.ttf"
W, H, FPS = 1080, 1920, 30


def run_ff(args, label):
    """Run ffmpeg and print stderr on failure."""
    r = subprocess.run(["ffmpeg"] + args, capture_output=True)
    if r.returncode != 0:
        print(f"  FAILED: {label}")
        print(r.stderr.decode()[-1000:])
        sys.exit(1)
    print(f"  {label} done")


def img_to_video(img, out, duration, texts, darken=0.7):
    """Convert image to video with Ken Burns zoom and text overlays.
    Images are 1200x1600 (3:4). We scale up and crop to 9:16."""
    d = int(duration * FPS)

    # Build text filter chain
    text_filters = ""
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
        f"[0:v]scale=-1:2400,crop=1350:2400:(iw-1350)/2:0,"
        f"scale={W}:{H},format=yuv420p,"
        f"colorlevels=rimax={darken}:gimax={darken}:bimax={darken}"
        f"{text_filters}"
    )

    run_ff([
        "-y", "-loop", "1", "-i", img,
        "-filter_complex", filt,
        "-t", str(duration), "-r", str(FPS),
        "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        out
    ], f"Image scene ({os.path.basename(img)})")


def vid_to_scene(vid, bg_img, out, duration, texts):
    """Convert landscape video to 9:16 with bg image and text overlays."""
    text_filters = ""
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
        # Background from image, blurred
        f"[1:v]scale=-1:2400,crop=1350:2400:(iw-1350)/2:0,"
        f"scale={W}:{H},format=yuv420p,gblur=sigma=15,colorlevels=rimax=0.4:gimax=0.4:bimax=0.4[bg];"
        # Video scaled to fit width
        f"[0:v]scale={W}:-1[vid];"
        # Overlay video on blurred bg, centered vertically
        f"[bg][vid]overlay=0:(H-h)/2:format=auto"
        f"{text_filters}"
    )

    run_ff([
        "-y", "-i", vid, "-loop", "1", "-i", bg_img,
        "-filter_complex", filt,
        "-t", str(duration), "-r", str(FPS),
        "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        "-an", out
    ], f"Video scene ({os.path.basename(vid)})")


def build():
    scenes = []

    # SCENE 1: HOOK (5s) — Dirty laundry baskets
    s1 = f"{OUT_DIR}/s1.mp4"
    img_to_video(TUMPUKAN, s1, 5, [
        {"text": "BARU PULANG MUDIK?", "y": "(h/2)-80", "size": 72, "start": 0.3},
        {"text": "Isi koper pasti kayak gini...", "y": "(h/2)+30", "size": 46,
         "font": FONT_REG, "bw": 2, "start": 1.0},
    ], darken=0.65)
    scenes.append(s1)

    # SCENE 2: PROBLEM (5s) — Same image, dramatic text
    s2 = f"{OUT_DIR}/s2.mp4"
    img_to_video(TUMPUKAN, s2, 5, [
        {"text": "TUMPUKAN", "y": "(h/2)-100", "size": 96,
         "color": "0xFBB818", "bw": 4, "start": 0.3},
        {"text": "BAJU KOTOR", "y": "(h/2)+30", "size": 96,
         "color": "0xFBB818", "bw": 4, "start": 0.6},
        {"text": "Males banget nyuci sendiri...", "y": "(h/2)+170", "size": 42,
         "font": FONT_REG, "bw": 2, "start": 1.2},
    ], darken=0.55)
    scenes.append(s2)

    # SCENE 3: SOLUTION (8s) — Machine video + "BUKA LAGI!"
    s3 = f"{OUT_DIR}/s3.mp4"
    vid_to_scene(MESIN_VID, MESIN_IMG, s3, 8, [
        {"text": "STAR LAUNDRY", "y": "280", "size": 84,
         "color": "0xFBB818", "bc": "0x2AADE0", "bw": 4, "start": 0.5},
        {"text": "BUKA LAGI!", "y": "380", "size": 96,
         "bc": "0x2AADE0", "bw": 4, "start": 0.8},
        {"text": "Mulai 24 Maret 2026", "y": "500", "size": 48,
         "color": "0xFBB818", "bw": 2, "start": 1.2},
        {"text": "Tinggal drop off, beres!", "y": str(H-350), "size": 48,
         "font": FONT_REG, "bw": 2, "start": 1.8},
    ])
    scenes.append(s3)

    # SCENE 4: TRANSFORMATION (6s) — Staff folding + "Bersih Wangi Rapi"
    s4 = f"{OUT_DIR}/s4.mp4"
    vid_to_scene(LIPAT_VID, RAK_IMG, s4, 6, [
        {"text": "BERSIH", "y": "300", "size": 88,
         "color": "0xFBB818", "bw": 4, "start": 0.5},
        {"text": "WANGI", "y": "420", "size": 88,
         "color": "0xFBB818", "bw": 4, "start": 1.2},
        {"text": "PASTI RAPI!", "y": "540", "size": 88,
         "bc": "0x2AADE0", "bw": 4, "start": 1.9},
    ])
    scenes.append(s4)

    # SCENE 5: RESULT (4s) — Clean laundry shelves
    s5 = f"{OUT_DIR}/s5.mp4"
    img_to_video(RAK_IMG, s5, 4, [
        {"text": "Cucian kamu aman di sini!", "y": str(H-400), "size": 56,
         "bc": "0x2AADE0", "start": 0.5},
        {"text": "Rapi, terlabel, siap diambil", "y": str(H-320), "size": 40,
         "color": "0xFBB818", "font": FONT_REG, "bw": 2, "start": 1.0},
    ], darken=0.75)
    scenes.append(s5)

    # SCENE 6: CTA (2s) — Blue bg + logo + info
    s6 = f"{OUT_DIR}/s6.mp4"
    filt = (
        f"[1:v]format=yuva420p,scale=500:-1[logo];"
        f"[0:v][logo]overlay=(W-w)/2:400"
        f",drawtext=fontfile='{FONT}':text='Star Laundry Boyolali':fontsize=52:fontcolor=white"
        f":x=(w-text_w)/2:y=850"
        f",drawtext=fontfile='{FONT}':text='WA 0822-2567-2756':fontsize=56:fontcolor=0xFBB818"
        f":x=(w-text_w)/2:y=1050"
        f",drawtext=fontfile='{FONT_REG}':text='Buka 07.00 - 21.00':fontsize=44:fontcolor=white"
        f":x=(w-text_w)/2:y=1150"
        f",drawtext=fontfile='{FONT_REG}':text='Jl. Jambu, Boyolali':fontsize=40:fontcolor=white"
        f":x=(w-text_w)/2:y=1230"
        f",drawtext=fontfile='{FONT}':text='Bersih Wangi, Pasti Rapi':fontsize=44:fontcolor=0xFBB818"
        f":x=(w-text_w)/2:y=1400"
    )
    run_ff([
        "-y",
        "-f", "lavfi", "-i", f"color=c=0x2AADE0:s={W}x{H}:d=2:r={FPS}",
        "-i", LOGO,
        "-filter_complex", filt,
        "-t", "2", "-r", str(FPS),
        "-pix_fmt", "yuv420p", "-c:v", "libx264", "-preset", "fast", "-crf", "23",
        s6
    ], "CTA end card")
    scenes.append(s6)

    # CONCAT
    concat_file = f"{OUT_DIR}/concat.txt"
    with open(concat_file, "w") as f:
        for s in scenes:
            f.write(f"file '{s}'\n")

    print("\n  Concatenating...")
    run_ff([
        "-y", "-f", "concat", "-safe", "0", "-i", concat_file,
        "-c:v", "libx264", "-preset", "medium", "-crf", "20",
        "-pix_fmt", "yuv420p", "-r", str(FPS),
        "-movflags", "+faststart", OUTPUT
    ], "Final concat")

    for s in scenes:
        os.remove(s)
    os.remove(concat_file)
    return OUTPUT


if __name__ == "__main__":
    print("Creating Reel #1: Buka Lagi! Tumpukan Baju Mudik")
    print(f"Output: {W}x{H}, {FPS}fps, ~30s\n")

    for a in [TUMPUKAN, MESIN_IMG, MESIN_VID, LIPAT_VID, RAK_IMG, LOGO]:
        if not os.path.exists(a):
            print(f"MISSING: {a}")
            sys.exit(1)
    print("All assets found.\n")

    output = build()
    dur = subprocess.check_output([
        "ffprobe", "-v", "quiet", "-show_entries", "format=duration", "-of", "csv=p=0", output
    ]).decode().strip()
    mb = os.path.getsize(output) / (1024 * 1024)

    print(f"\nReel created:")
    print(f"  File: {output}")
    print(f"  Duration: {float(dur):.1f}s")
    print(f"  Size: {mb:.1f}MB")
    print(f"\nNext: Import into CapCut → add voiceover + music → export → upload!")
