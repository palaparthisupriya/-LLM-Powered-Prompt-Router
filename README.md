# AI Intent Router using Prompt Engineering

## Overview

This project implements an **AI prompt routing system** that intelligently directs user requests to specialized expert personas. Instead of using a single large prompt, the system first detects the user's intent and then routes the request to an appropriate AI expert such as a coding assistant, data analyst, writing coach, or career advisor.

This architecture improves response quality and efficiency by using **intent-based routing** and **specialized prompts**.

---

## Architecture

The system follows a **two-step pipeline**:

1. **Intent Classification**

   * The system analyzes the user's message.
   * It classifies the message into one of the supported intents:

     * `code`
     * `data`
     * `writing`
     * `career`
     * `unclear`

2. **Prompt Routing**

   * Based on the detected intent, the request is routed to a specific expert persona.
   * Each persona has a specialized system prompt designed for that task.
   * The AI then generates the final response.

---

## Features

* Intent classification system
* Multiple expert AI personas
* Prompt routing architecture
* Graceful error handling for malformed JSON responses
* Logging of all requests and routing decisions
* Modular project structure

---

## Project Structure

```
ai_router_project
│
├── app.py            # Main application entry point
├── classifier.py     # Intent classification logic
├── router.py         # Routing and response generation
├── prompts.py        # Expert persona prompts
├── logger.py         # Request logging system
└── route_log.jsonl   # Log file storing routing history
```

---

## Expert Personas

The system includes the following specialized personas:

### Code Expert

Provides technical programming help with clean and production-quality code solutions.

### Data Analyst

Analyzes datasets and explains patterns using statistical concepts and visualization suggestions.

### Writing Coach

Provides feedback to improve writing clarity, tone, grammar, and structure without rewriting the text.

### Career Advisor

Offers actionable career advice and asks clarifying questions before providing recommendations.

---

## How to Run the Project

### Step 1: Navigate to the project folder

```
cd ai_router_project
```

### Step 2: Run the application

```
python app.py
```

### Step 3: Interact with the system

Example input:

```
how do i sort a list in python
```

Example output:

```
Detected Intent: code
Confidence: 0.91
Response: Generated response for: how do i sort a list in python
```

Type `exit` to stop the program.

---

## Logging

Every request is logged to **route_log.jsonl**.

Each entry contains:

* intent
* confidence score
* user message
* final response

Example log entry:

```
{"intent":"code","confidence":0.91,"user_message":"how do i sort list in python","final_response":"Generated response for: how do i sort list in python"}
```

---

## Testing Examples

You can test the system using inputs like:

```
how do i sort a list of objects in python?
I'm preparing for a job interview, any tips?
This paragraph sounds awkward, can you help me fix it?
what's the average of these numbers: 12, 45, 23, 67, 34
hey
```

---

## Technologies Used

* Python
* Prompt Engineering
* JSON Logging
* Intent-Based AI Routing Architecture
