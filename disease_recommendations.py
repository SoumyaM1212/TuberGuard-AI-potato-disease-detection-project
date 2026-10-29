
"""
Company: Crevavi Technologies
Project: Potato Disease Detection
Step: Disease Treatment and Fertilizer Recommendations
"""

recommendations = {
    "Black Scurf": {
        "treatment": [
            "Use certified disease-free seed potatoes.",
            "Remove heavily infected tubers before planting.",
            "Rotate potatoes with suitable non-host crops.",
            "Avoid planting in poorly drained soil."
        ],
        "fertilizer": (
            "No fertilizer cures this disease. Use balanced potato "
            "fertilizer according to a soil test."
        ),
        "prevention": (
            "Use healthy seed tubers and maintain good soil drainage."
        )
    },

    "Blackleg": {
        "treatment": [
            "Remove infected plants and tubers.",
            "Clean tools and equipment.",
            "Avoid waterlogged soil and excessive irrigation.",
            "Use certified disease-free seed potatoes."
        ],
        "fertilizer": (
            "Fertilizer does not cure this bacterial disease. "
            "Apply nutrients only according to soil-test results."
        ),
        "prevention": (
            "Use healthy seed potatoes and prevent prolonged wet conditions."
        )
    },

    "Common Scab": {
        "treatment": [
            "Use scab-free seed potatoes.",
            "Maintain adequate soil moisture during tuber formation.",
            "Rotate potatoes with suitable non-host crops.",
            "Check soil pH before applying soil amendments."
        ],
        "fertilizer": (
            "Do not apply sulfur or acidifying fertilizer blindly. "
            "Soil amendments may help in some soils, but the amount "
            "must depend on soil pH and local agricultural advice."
        ),
        "prevention": (
            "Avoid moisture stress during tuber formation and use healthy seed."
        )
    },

    "Dry Rot": {
        "treatment": [
            "Separate rotting potatoes from healthy stored potatoes.",
            "Remove severely affected tubers.",
            "Avoid bruising and cuts during harvesting.",
            "Use healthy seed potatoes for future planting."
        ],
        "fertilizer": (
            "Fertilizer cannot cure rot in harvested potatoes. "
            "Use balanced fertilizer for the next crop based on a soil test."
        ),
        "prevention": (
            "Handle tubers carefully and store them in suitable, "
            "well-ventilated conditions."
        )
    },

    "Healthy Potatoes": {
        "treatment": [
            "No disease treatment is indicated by this prediction.",
            "Continue monitoring the crop for unusual symptoms."
        ],
        "fertilizer": (
            "Use a balanced potato fertilizer based on soil testing, "
            "crop growth stage, and local agricultural recommendations."
        ),
        "prevention": (
            "Use healthy seed, maintain suitable irrigation, "
            "and monitor the crop regularly."
        )
    },

    "Miscellaneous": {
        "treatment": [
            "The model detected an unspecified or miscellaneous category.",
            "Inspect the potato for visible symptoms.",
            "Ask an agricultural expert to confirm the problem."
        ],
        "fertilizer": (
            "Do not select a fertilizer based on this category alone. "
            "Obtain a soil test and confirm the problem first."
        ),
        "prevention": (
            "Keep affected potatoes separate until the condition is identified."
        )
    },

    "Pink Rot": {
        "treatment": [
            "Remove severely rotted tubers.",
            "Improve soil drainage.",
            "Avoid excessive irrigation and prolonged waterlogging.",
            "Use healthy seed potatoes."
        ],
        "fertilizer": (
            "No fertilizer cures pink rot. Use balanced fertilizer "
            "according to a soil test and avoid excessive irrigation."
        ),
        "prevention": (
            "Maintain good drainage and avoid harvesting or storing "
            "damaged, rotting tubers."
        )
    }
}


def get_recommendation(disease_name):
    """Return advice for the predicted potato condition."""

    return recommendations.get(
        disease_name,
        recommendations["Miscellaneous"]
    )
