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
