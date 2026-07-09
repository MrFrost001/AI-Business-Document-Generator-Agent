from services.llm import ask_llm
import json
import re

def create_plan(user_request):

    prompt = f"""
    You are an autonomous planning agent.

    User request:
    {user_request}

    Break the request into ONLY 5 concise TODO tasks.

    Return ONLY valid JSON:

    {{
        "tasks":[
            "Task 1",
            "Task 2",
            "Task 3",
            "Task 4",
            "Task 5"
        ]
    }}
    """

    result = ask_llm(prompt)

    print("Raw LLM response:")
    print(result)

    # Remove markdown code blocks
    cleaned = re.sub(
        r"```(?:json)?",
        "",
        result
    )

    cleaned = cleaned.replace(
        "```",
        ""
    ).strip()

    print("Cleaned response:")
    print(cleaned)

    try:
        parsed = json.loads(cleaned)
        return parsed

    except Exception as e:

        print(
            "JSON parsing error:",
            e
        )

        return {
            "tasks":[
                "Analyze request",
                "Generate document",
                "Create sections",
                "Format content",
                "Finalize report"
            ]
        }