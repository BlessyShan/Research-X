# Research-X

## Autonomous Research Agent

Research-X is an AI-powered autonomous research system that decomposes
a research topic into subtasks, searches the web, collects evidence,
analyzes sources, verifies findings, and generates a structured research
report.

## Features

- AI-powered research planning
- Autonomous subtask generation
- Web search
- Webpage content extraction
- Source deduplication
- Evidence analysis
- Claim verification
- Confidence scoring
- Markdown report generation

## Architecture

User Topic
    ↓
Planning Agent
    ↓
Research Agent
    ↓
Web Search
    ↓
Source Collection
    ↓
Analysis Agent
    ↓
Verification Agent
    ↓
Reporting Agent
    ↓
Research Report

## Technologies

- Python
- Google Gemini API
- Pydantic
- Requests
- BeautifulSoup
- python-dotenv

## Installation

```bash
git clone <repository-url>
cd Research-X

python -m venv venv

# Windows
venv\Scripts\activate

pip install -r requirements.txt