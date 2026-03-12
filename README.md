# 🏋️ AI Fitness Coach

A multi-agent AI fitness coaching system. Get personalized workout plans, nutrition guidance, and progress tracking from specialized AI agents working together.

## Features

- **🤖 Multi-Agent Architecture** - A main fitness coach routes your requests to specialized agents
- **💪 Workout Plans** - Customized exercise routines based on your goals and equipment
- **🥗 Nutrition Guidance** - Personalized meal plans and dietary advice
- **📊 Progress Tracking** - BMI calculation and fitness journey monitoring
- **💬 Interactive Chat** - Natural conversation with follow-up questions for personalization

## Agents

| Agent | Purpose |
|-------|---------|
| `fitness_coach` | Main coordinator that assesses your needs and routes to specialists |
| `workout_agent` | Creates personalized workout routines and exercise plans |
| `nutrition_agent` | Provides dietary guidance and meal planning |
| `tracker_agent` | Tracks progress and calculates health metrics (BMI) |


## Installation

```bash
# Clone the repository
git clone <repository-url>
cd fitness_coach

# Install dependencies with uv
uv sync

# Or with pip
pip install -e .
```

## Usage

### Interactive Mode

Run the fitness coach in interactive chat mode:

```bash
# Using uv
uv run python -m fitness_coach.main

# Or using the installed command
uv run fitness-coach
```

### Example Conversation

```
🏋️ Welcome to your AI Fitness Coach!
I'm here to help you achieve your fitness goals.

You: I want to lose weight and build muscle

fitness_coach: Great goals! Let me connect you with the right specialist.
To get started, what's your current fitness level and do you have
any specific health conditions I should know about?

[Hands off to workout_agent or nutrition_agent based on your response]
```

## Tools

### `calculate_bmi`

Calculate Body Mass Index with health category and guidance.

```
Parameters:
  - weight_kg: Weight in kilograms
  - height_cm: Height in centimeters

Returns:
  - bmi: Calculated BMI value
  - category: Underweight/Normal/Overweight/Obese
  - guidance: Health recommendations
```

## Project Structure

```
fitness_coach/
├── pyproject.toml              # Project configuration and dependencies
├── README.md                   # This file
└── src/fitness_coach/
    ├── __init__.py             # Package exports
    ├── main.py                 # Main fitness_coach agent + entry point
    ├── workout_agent.py        # Workout planning specialist
    ├── nutrition_agent.py      # Nutrition guidance specialist
    └── tracker_agent.py        # Progress tracking + BMI tool
```

## Development

```bash
# Install in development mode
uv sync --dev

# Run with hot reload (if using watchfiles)
uv run python -m fitness_coach.main
```

## How It Works

1. **Initial Assessment** - The `fitness_coach` gathers information about your goals, fitness level, and preferences
2. **Specialist Handoff** - Based on your needs, you're routed to the appropriate specialist:
   - Workout questions → `workout_agent`
   - Nutrition questions → `nutrition_agent`
   - Progress/BMI → `tracker_agent`
3. **Personalized Response** - The specialist provides tailored advice and asks a follow-up question
4. **Continuous Support** - The conversation continues with sustainable, encouraging guidance

## Disclaimer

This AI fitness coach provides general guidance and should not replace professional medical advice. Consult with healthcare providers before starting any new fitness or nutrition program, especially if you have pre-existing health conditions.

## License

MIT License - see LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.
# fitness_coach
