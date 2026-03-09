"""Tracker agent for monitoring progress and calculating BMI."""

from agents import Agent, function_tool


@function_tool
def calculate_bmi(weight_kg: float, height_cm: float) -> dict:
    """Calculate Body Mass Index (BMI) and provide interpretation.
    
    Args:
        weight_kg: Weight in kilograms
        height_cm: Height in centimeters
        
    Returns:
        Dictionary with BMI value, category, and health guidance
    """
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
        guidance = "Consider consulting a healthcare provider about healthy weight gain strategies."
    elif bmi < 25:
        category = "Normal weight"
        guidance = "Great! Maintain your current lifestyle with balanced nutrition and regular activity."
    elif bmi < 30:
        category = "Overweight"
        guidance = "Focus on gradual weight loss through calorie deficit and increased physical activity."
    else:
        category = "Obese"
        guidance = "Consult a healthcare provider for a personalized weight management plan."
    
    return {
        "bmi": round(bmi, 1),
        "category": category,
        "guidance": guidance,
    }


tracker_agent = Agent(
    name="tracker_agent",
    instructions="""You are a specialized tracker agent helping users monitor their fitness progress.
    Calculate BMI, track workout progress, and help users understand their fitness journey.
    Use the calculate_bmi tool when users provide weight and height.
    Encourage users to track measurements beyond scale weight (e.g., energy levels, strength gains, how clothes fit).
    Ask one follow-up question to help with tracking (e.g., 'Would you like to log your current measurements?' or 'How often would you like to check in?').
    Be supportive and remind users that progress isn't always linear.""",
    tools=[calculate_bmi],
)
