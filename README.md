Traccar Proximity Alert System
An intelligent location monitoring system that tracks two devices via Traccar and sends instant push notifications through Bark when they come within 3 kilometers of each other.
✨ Features

Real-time proximity monitoring - Continuously tracks distance between two devices
Instant notifications - Push alerts via Bark app when devices are within 3km
Lightweight & efficient - Minimal resource usage with Python requests
Cross-platform - Works on iOS and Android through Bark app

🚀 Quick Start
Prerequisites

Traccar server with API access
Bark app installed on your mobile device
Python 3.7+ installed on your system

Installation

Clone the repository
bashgit clone https://github.com/sobanbackup1/location-get.git
cd location-get

Set up Python environment (recommended)
bash# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

Install dependencies
bashpip install requests

Install Bark app

iOS: Download from App Store
Android: Download from GitHub Releases



📱 Setup & Configuration

Configure your Traccar API credentials
Set up device IDs for monitoring
Add your Bark notification key
Adjust proximity threshold if needed (default: 3km)

🔧 Usage
Run the proximity monitor:
python3 getloc.py
The script will continuously monitor your devices and send notifications when they're nearby!

Built with ❤️ for seamless location tracking 
