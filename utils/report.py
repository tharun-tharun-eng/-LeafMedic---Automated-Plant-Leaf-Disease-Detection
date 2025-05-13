# utils/report.py

# Dictionary mapping class folder names to human-readable descriptions and treatments
disease_info = {
    "Apple___Black_rot": {
        "description": (
            "Black rot is a fungal disease caused by Botryosphaeria obtusa. "
            "It produces dark, circular lesions on leaves, fruit, and bark."
        ),
        "treatment": (
            "Remove and destroy infected leaves and fruit immediately. "
            "Prune affected branches and apply fungicides such as captan or thiophanate-methyl."
        )
    },
    "Tomato___Early_blight": {
        "description": (
            "Early blight is caused by Alternaria solani. It appears as brown spots "
            "with concentric rings on older leaves."
        ),
        "treatment": (
            "Use disease-free seeds. Apply fungicides like chlorothalonil or mancozeb. "
            "Rotate crops and avoid overhead irrigation."
        )
    },
    "Potato___Late_blight": {
        "description": (
            "Late blight is caused by Phytophthora infestans. It creates large, "
            "dark, water-soaked lesions on leaves and stems."
        ),
        "treatment": (
            "Apply copper-based fungicides. Remove and destroy infected plants. "
            "Improve air circulation and avoid wet foliage."
        )
    },
    "Tomato___healthy": {
        "description": (
            "The leaf appears healthy with no visible signs of disease or pest infestation."
        ),
        "treatment": (
            "No treatment needed. Continue regular care, provide balanced nutrition, "
            "and monitor for early signs of any disease."
        )
    }
    # Add additional entries for each class folder name in your dataset
}

def generate_disease_report(label: str, confidence: float) -> str:
    """
    Build a detailed, human-readable report based on predicted class and confidence.

    Args:
      label:      The class key (folder name) predicted by the model.
      confidence: Confidence score between 0 and 1.

    Returns:
      A multiline string containing:
        - Disease name
        - Confidence percentage
        - Description
        - Recommended treatment
    """
    # Convert folder-style name to readable form
    name = label.replace("___", " – ").replace("_", " ")
    
    # Lookup disease info or fallback
    info = disease_info.get(label, {
        "description": "No description available for this class.",
        "treatment":   "No treatment recommendation available."
    })

    # Build report text
    report = (
        f"📝 Disease Report\n"
        f"──────────────────────────\n"
        f"Predicted: {name}\n"
        f"Confidence: {confidence * 100:.1f}%\n\n"
        f"📖 Description:\n{info['description']}\n\n"
        f"💊 Recommended Treatment:\n{info['treatment']}"
    )
    return report
