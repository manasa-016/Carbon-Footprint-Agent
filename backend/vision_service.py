# vision_service.py - fallback lightweight mock analyzer

import random

# Mock crisis reference store
STORE = {
    "Flood": {"desc": "High water anomaly in satellite image"},
    "Heatwave": {"desc": "Persistent land surface temp rise"},
    "Wildfire": {"desc": "Vegetation burn + smoke plume"},
}

def analyze_image_mock(file_bytes: bytes):
    """
    Fake ViT one-shot analyzer (no heavy model).
    Randomly classifies input as one of the crises.
    """
    crisis = random.choice(list(STORE.keys()))
    confidence = round(random.uniform(0.7, 0.95), 2)
    explanation = STORE[crisis]["desc"]

    return {
        "crisis": crisis,
        "confidence": confidence,
        "explanation": explanation,
    }
