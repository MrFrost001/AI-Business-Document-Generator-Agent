from google import genai
from dotenv import load_dotenv
import os
import time

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Local fallback content
MOCK_CONTENT = {
    "Analyze request":
    "The organization aims to improve customer relationship management and centralize customer interactions.",

    "Generate document":
    "The proposed CRM system will improve customer retention, sales visibility, and operational efficiency.",

    "Create sections":
    "Sections include Executive Summary, Problem Statement, Proposed Solution, ROI Analysis, and Timeline.",

    "Format content":
    "The proposal follows a professional business format with headings and structured sections.",

    "Finalize report":
    "The proposal concludes with implementation recommendations and next steps."
}

def ask_llm(prompt):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            error = str(e)

            print(error)

            # Quota fallback
            if "RESOURCE_EXHAUSTED" in error:

                print("Using fallback content")

                for key in MOCK_CONTENT:

                    if key in prompt:
                        return MOCK_CONTENT[key]

            time.sleep(2)

    return "Fallback business content generated."