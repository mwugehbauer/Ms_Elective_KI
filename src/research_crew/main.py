#!/usr/bin/env python
# src/research_crew/main.py
import os
import sys
from research_crew.crew import ResearchCrew

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

# Codespaces secrets bypass .env entirely, so .env.example's MODEL default never applies there — set it here instead.
os.environ.setdefault('MODEL', 'groq/llama-3.3-70b-versatile')

REQUIRED_ENV_VARS = {
    'GROQ_API_KEY': 'powers the LLM behind every agent (get one free at https://console.groq.com/keys)',
    'SERPER_API_KEY': "powers the researcher agent's web search tool (get one free at https://serper.dev)",
    'GEMINI_API_KEY': 'powers embeddings for knowledge/memory features (get one free at https://ai.google.dev)',
}

# A copy-pasted secret with a trailing newline produces an "Illegal header value" error deep inside
# litellm that's hard to diagnose — strip whitespace defensively before anything reads these.
for _key in REQUIRED_ENV_VARS:
    _value = os.getenv(_key)
    if _value is not None:
        os.environ[_key] = _value.strip()

def check_setup():
    """Fail fast with a clear message instead of a deep crewai stack trace."""
    missing = [name for name in REQUIRED_ENV_VARS if not os.getenv(name)]
    if not missing:
        return
    print("\nSetup incomplete — missing required API key(s):\n")
    for name in missing:
        print(f"  {name}: {REQUIRED_ENV_VARS[name]}")
    print(
        "\nIf you're in a Codespace, add these as Codespaces secrets in your GitHub "
        "account settings (Settings -> Codespaces -> Secrets) and restart the codespace.\n"
        "If you're running locally, copy .env.example to .env and fill them in.\n"
    )
    sys.exit(1)

def run():
    """
    Run the research crew.
    """
    check_setup()

    inputs = {
        'topic': 'Artificial Intelligence in Healthcare'
    }

    # Create and run the crew
    result = ResearchCrew().crew().kickoff(inputs=inputs)

    # Print the result
    print("\n\n=== FINAL REPORT ===\n\n")
    print(result.raw)

    print("\n\nReport has been saved to output/report.md")

if __name__ == "__main__":
    run()