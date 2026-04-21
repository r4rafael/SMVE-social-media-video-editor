"""
SMVE - Social Media Video Editor
Main entry point for the application
"""

import os
from pathlib import Path

# Project root
PROJECT_ROOT = Path(__file__).parent.absolute()

def main():
    """Main application entry point"""
    print("🎬 SMVE - Social Media Video Editor")
    print("=" * 50)
    print("Starting application...")
    
    # Check dependencies
    try:
        import moviepy
        import librosa
        import cv2
        print("✅ All dependencies installed!")
    except ImportError as e:
        print(f"❌ Missing dependency: {e}")
        print("Run: pip install -r requirements.txt")
        return
    
    print("\nTo start the Streamlit app, run:")
    print("streamlit run ui/app.py")

if __name__ == "__main__":
    main()