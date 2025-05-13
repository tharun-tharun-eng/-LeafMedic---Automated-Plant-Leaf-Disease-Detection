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
    "Tomato_Early_blight": {
        "description": (
            "Early blight is caused by Alternaria solani. It appears as brown spots "
            "with concentric rings on older leaves. The disease typically starts on the lower, "
            "older leaves and progresses upward. Affected leaves may turn yellow around the spots "
            "and eventually wither."
        ),
        "treatment": (
            "1. Remove and destroy infected leaves to reduce spread.\n"
            "2. Apply fungicides like chlorothalonil, mancozeb, or copper-based products.\n"
            "3. Rotate crops and avoid planting tomatoes in the same location for 3-4 years.\n"
            "4. Use drip irrigation instead of overhead watering to keep foliage dry.\n"
            "5. Mulch around plants to prevent soil-borne spores from splashing onto leaves."
        )
    },
    "Potato_Late_blight": {
        "description": (
            "Late blight is caused by Phytophthora infestans, the same pathogen that caused the Irish potato famine. "
            "It creates large, dark, water-soaked lesions on leaves and stems. Under humid conditions, "
            "white fuzzy growth may appear on the undersides of leaves. The disease can spread rapidly "
            "in cool, wet weather and can destroy entire fields within days if not controlled."
        ),
        "treatment": (
            "1. Apply preventative fungicides before symptoms appear when conditions favor disease.\n"
            "2. Use fungicides containing chlorothalonil, mancozeb, or copper compounds.\n"
            "3. Remove and destroy infected plants immediately to prevent spread.\n"
            "4. Improve air circulation by proper plant spacing.\n"
            "5. Plant resistant varieties when available.\n"
            "6. Avoid irrigation late in the day to reduce leaf wetness overnight."
        )
    },
    "Tomato_healthy": {
        "description": (
            "The leaf appears healthy with no visible signs of disease or pest infestation. "
            "Healthy tomato leaves are typically medium to dark green, slightly fuzzy, and have "
            "a distinctive aroma. The leaf structure is compound with serrated leaflets."
        ),
        "treatment": (
            "No treatment needed. Continue regular care with these best practices:\n"
            "1. Water at the base of plants, avoiding wetting the foliage.\n"
            "2. Provide balanced nutrition with phosphorus and potassium for fruit production.\n"
            "3. Ensure good air circulation between plants.\n"
            "4. Monitor regularly for early signs of pests or disease.\n"
            "5. Apply preventative treatments during high-risk periods."
        )
    },
    "Pepper_bell_Bacterial_spot": {
        "description": (
            "Bacterial spot is caused by Xanthomonas species bacteria. It appears as small, water-soaked "
            "spots on leaves that enlarge and turn brown with yellow halos. In severe cases, leaves may "
            "drop prematurely. The disease can also affect stems and fruit, causing raised scab-like lesions "
            "on fruit surfaces that reduce marketability."
        ),
        "treatment": (
            "1. Use disease-free seeds and transplants from reputable sources.\n"
            "2. Apply copper-based bactericides early when symptoms first appear.\n"
            "3. Rotate crops, avoiding planting peppers or tomatoes in the same area for 2-3 years.\n"
            "4. Remove and destroy infected plant debris after harvest.\n"
            "5. Avoid working with plants when they're wet to prevent spreading bacteria.\n"
            "6. Use drip irrigation rather than overhead sprinklers."
        )
    },
    "Pepper_bell_healthy": {
        "description": (
            "The bell pepper leaf appears healthy with no visible signs of disease or pest damage. "
            "Healthy pepper leaves are typically smooth, glossy, and medium to dark green in color. "
            "The leaves have a simple, oval to lanceolate shape with smooth margins."
        ),
        "treatment": (
            "No treatment needed. Maintain plant health with these practices:\n"
            "1. Provide consistent moisture, avoiding drought stress.\n"
            "2. Apply balanced fertilizer with adequate calcium to prevent blossom end rot.\n"
            "3. Maintain proper spacing for good air circulation.\n"
            "4. Monitor for pests regularly, especially aphids and spider mites.\n"
            "5. Apply mulch to conserve moisture and reduce weed competition."
        )
    },
    "Potato_Early_blight": {
        "description": (
            "Early blight in potatoes is caused by the fungus Alternaria solani. It appears as dark brown "
            "to black lesions with concentric rings, creating a target-like pattern. The disease typically "
            "starts on lower leaves and moves upward. Severe infections can cause significant defoliation, "
            "reducing tuber size and yield."
        ),
        "treatment": (
            "1. Apply fungicides containing chlorothalonil, azoxystrobin, or pyraclostrobin.\n"
            "2. Begin applications when plants are 6-8 inches tall or when symptoms first appear.\n"
            "3. Practice crop rotation, avoiding potatoes or related crops for 2-3 years in the same area.\n"
            "4. Ensure proper plant spacing for good air circulation.\n"
            "5. Remove volunteer potato plants that may harbor disease.\n"
            "6. Use certified disease-free seed potatoes."
        )
    },
    "Potato_healthy": {
        "description": (
            "The potato leaf appears healthy with no visible signs of disease or pest damage. "
            "Healthy potato leaves are compound with oval leaflets, medium to dark green in color. "
            "The plant shows vigorous growth with no yellowing, spots, or abnormal growth patterns."
        ),
        "treatment": (
            "No treatment needed. Maintain plant health with these practices:\n"
            "1. Hill soil around plants as they grow to prevent greening of tubers.\n"
            "2. Provide consistent moisture, especially during tuber formation.\n"
            "3. Apply balanced fertilizer, avoiding excessive nitrogen which promotes foliage at the expense of tubers.\n"
            "4. Monitor for Colorado potato beetles and aphids regularly.\n"
            "5. Consider preventative fungicide applications during periods favorable for late blight."
        )
    },
    "Tomato_Bacterial_spot": {
        "description": (
            "Bacterial spot in tomatoes is caused by Xanthomonas species. It appears as small, water-soaked, "
            "circular spots on leaves, stems, and fruit. As the disease progresses, spots become angular, "
            "turn dark brown to black, and may have yellow halos. Severely affected leaves may turn yellow "
            "and drop. On fruit, spots appear as raised, scabby lesions that reduce quality and marketability."
        ),
        "treatment": (
            "1. Apply copper-based bactericides early in the season before symptoms appear.\n"
            "2. Rotate with non-solanaceous crops for at least 2 years.\n"
            "3. Use disease-free seeds and transplants.\n"
            "4. Remove and destroy infected plant debris after harvest.\n"
            "5. Avoid overhead irrigation and working with plants when wet.\n"
            "6. Space plants properly to promote air circulation and faster drying of foliage."
        )
    },
    "Tomato_Late_blight": {
        "description": (
            "Late blight in tomatoes is caused by Phytophthora infestans. It appears as pale green, water-soaked "
            "spots that rapidly enlarge to become brown-black, greasy-looking lesions. Under humid conditions, "
            "white fuzzy growth (sporangia) may appear on the undersides of leaves. The disease can spread rapidly "
            "in cool, wet weather, affecting leaves, stems, and fruit. Infected fruit develop large, firm, brown lesions."
        ),
        "treatment": (
            "1. Apply protective fungicides containing chlorothalonil, mancozeb, or copper compounds.\n"
            "2. Remove and destroy infected plants immediately to prevent spread to other plants.\n"
            "3. Improve air circulation by proper spacing and pruning.\n"
            "4. Avoid overhead irrigation and working with plants when wet.\n"
            "5. Plant resistant varieties when available.\n"
            "6. Monitor weather forecasts and increase fungicide applications during cool, wet periods."
        )
    },
    "Tomato_Leaf_Mold": {
        "description": (
            "Leaf mold is caused by the fungus Passalora fulva (formerly Fulvia fulva or Cladosporium fulvum). "
            "It appears as pale green to yellow spots on upper leaf surfaces with corresponding olive-green to "
            "grayish-purple fuzzy growth on the undersides. The disease is favored by high humidity and moderate "
            "temperatures. Severe infections can cause significant defoliation, reducing yield and fruit quality."
        ),
        "treatment": (
            "1. Improve greenhouse ventilation to reduce humidity below 85%.\n"
            "2. Space plants properly to improve air circulation.\n"
            "3. Apply fungicides containing chlorothalonil, mancozeb, or copper compounds.\n"
            "4. Remove and destroy infected leaves and plant debris.\n"
            "5. Use drip irrigation instead of overhead watering.\n"
            "6. Plant resistant varieties when available."
        )
    },
    "Tomato_Septoria_leaf_spot": {
        "description": (
            "Septoria leaf spot is caused by the fungus Septoria lycopersici. It appears as small, circular spots "
            "with dark borders and light gray centers, usually 2-3mm in diameter. Tiny black fruiting bodies (pycnidia) "
            "may be visible in the center of older spots. The disease typically starts on lower leaves and progresses "
            "upward. Severe infections can cause significant defoliation, reducing yield and fruit quality."
        ),
        "treatment": (
            "1. Apply fungicides containing chlorothalonil, mancozeb, or copper compounds when symptoms first appear.\n"
            "2. Remove and destroy infected leaves to reduce spread.\n"
            "3. Practice crop rotation, avoiding tomatoes in the same area for 2-3 years.\n"
            "4. Mulch around plants to prevent soil-borne spores from splashing onto leaves.\n"
            "5. Avoid overhead irrigation and working with plants when wet.\n"
            "6. Space plants properly to improve air circulation."
        )
    },
    "Tomato_Spider_mites_Two_spotted_spider_mite": {
        "description": (
            "Two-spotted spider mites (Tetranychus urticae) are tiny arachnids that feed on plant cells, causing "
            "stippling or small yellow/white spots on leaves. Severe infestations cause leaves to turn yellow, "
            "bronze, or brown and may be covered with fine webbing. The mites are barely visible to the naked eye "
            "but can be seen with a magnifying glass on the undersides of leaves. Hot, dry conditions favor rapid "
            "population growth."
        ),
        "treatment": (
            "1. Spray plants forcefully with water to dislodge mites and reduce populations.\n"
            "2. Apply insecticidal soap or horticultural oil to all plant surfaces, especially leaf undersides.\n"
            "3. For severe infestations, use miticides specifically labeled for spider mites.\n"
            "4. Introduce predatory mites such as Phytoseiulus persimilis for biological control.\n"
            "5. Increase humidity around plants, as spider mites prefer dry conditions.\n"
            "6. Remove and destroy heavily infested plants to prevent spread."
        )
    },
    "Tomato_Target_spot": {
        "description": (
            "Target spot is caused by the fungus Corynespora cassiicola. It appears as small, dark brown spots "
            "that enlarge to form circular lesions with concentric rings, resembling a target. The disease affects "
            "leaves, stems, and fruit. Severe infections can cause significant defoliation and fruit spotting, "
            "reducing yield and quality."
        ),
        "treatment": (
            "1. Apply fungicides containing chlorothalonil, mancozeb, or azoxystrobin when symptoms first appear.\n"
            "2. Remove and destroy infected leaves and fruit to reduce spread.\n"
            "3. Practice crop rotation, avoiding tomatoes in the same area for 2-3 years.\n"
            "4. Improve air circulation by proper spacing and pruning.\n"
            "5. Use drip irrigation instead of overhead watering to keep foliage dry.\n"
            "6. Mulch around plants to prevent soil-borne spores from splashing onto leaves."
        )
    },
    "Tomato_YellowLeaf_Curl_virus": {
        "description": (
            "Tomato Yellow Leaf Curl Virus (TYLCV) is transmitted by whiteflies. Infected plants show upward "
            "curling and yellowing of leaf edges, reduced leaf size, and stunted growth. Leaves may appear crumpled "
            "and have a cupped appearance. Plants infected early may produce few or no fruit. The virus cannot be "
            "cured once a plant is infected."
        ),
        "treatment": (
            "1. Remove and destroy infected plants immediately to prevent spread.\n"
            "2. Control whitefly populations using insecticidal soaps, neem oil, or approved insecticides.\n"
            "3. Use reflective mulches to repel whiteflies.\n"
            "4. Install fine mesh screens on greenhouse vents to exclude whiteflies.\n"
            "5. Plant resistant varieties (look for TYLCV resistance in seed catalogs).\n"
            "6. Maintain a whitefly-free period by avoiding continuous tomato production."
        )
    },
    "Tomato_mosaic_virus": {
        "description": (
            "Tomato mosaic virus (ToMV) and Tobacco mosaic virus (TMV) cause similar symptoms including mottled "
            "light and dark green patterns on leaves, leaf distortion, and stunted growth. Fruit may show yellow "
            "or brown rings or spots. The viruses are highly stable and can persist in plant debris and on tools "
            "for years. They are primarily spread through mechanical transmission and infected seed."
        ),
        "treatment": (
            "1. Remove and destroy infected plants immediately to prevent spread.\n"
            "2. Wash hands thoroughly with soap and water before handling plants.\n"
            "3. Disinfect tools with 10% bleach solution or 70% alcohol between plants.\n"
            "4. Use virus-free certified seeds and transplants.\n"
            "5. Control weeds that may harbor the virus.\n"
            "6. Plant resistant varieties (look for TMV or ToMV resistance in seed catalogs).\n"
            "7. Practice crop rotation, avoiding tomatoes and tobacco family plants in the same area."
        )
    }
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
        - Additional notes or warnings if applicable
    """
    # Convert folder-style name to readable form
    name = label.replace("___", " – ").replace("_", " ")
    
    # Lookup disease info or fallback
    info = disease_info.get(label, {
        "description": "No description available for this class.",
        "treatment":   "No treatment recommendation available."
    })
    
    # Determine severity level based on confidence
    severity = "High" if confidence > 0.85 else "Medium" if confidence > 0.70 else "Low"
    
    # Add warning for low confidence predictions
    warning = ""
    if confidence < 0.70:
        warning = (
            "⚠️ Note: This prediction has low confidence. Consider:\n"
            "• Taking clearer photos in good lighting\n"
            "• Capturing multiple angles of the affected leaves\n"
            "• Consulting with a plant pathologist for confirmation\n\n"
        )
    
    # Build report text with improved formatting
    report = (
        f"📝 DISEASE REPORT\n"
        f"══════════════════════════════════════\n"
        f"🔍 DIAGNOSIS\n"
        f"  Predicted Condition: {name}\n"
        f"  Confidence: {confidence * 100:.1f}%\n"
        f"  Severity Level: {severity}\n\n"
        f"{warning}"
        f"📖 DESCRIPTION\n"
        f"{info['description']}\n\n"
        f"💊 RECOMMENDED TREATMENT\n"
        f"{info['treatment']}\n\n"
        f"🌱 PREVENTION TIPS\n"
        f"• Practice crop rotation to break disease cycles\n"
        f"• Ensure proper plant spacing for good air circulation\n"
        f"• Use drip irrigation to keep foliage dry\n"
        f"• Remove plant debris at the end of the growing season\n"
        f"• Monitor plants regularly for early detection of problems"
    )
    return report
