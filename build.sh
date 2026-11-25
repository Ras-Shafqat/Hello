#!/usr/bin/env bash
set -e

echo "=== Step 1: Running Tests ==="
python3 -m unittest test_app.py || python -m unittest test_app.py

echo "=== Step 2: Packaging Build Artifact ==="
mkdir -p build
echo "Build Artifact - Hello App v1.0.0" > build/app-release.apk
echo "Timestamp: $(date)" >> build/app-release.apk
echo "Commit: ${GIT_COMMIT:-local}" >> build/app-release.apk

echo "=== Build Complete: Artifact created at build/app-release.apk ==="
