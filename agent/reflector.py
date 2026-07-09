from services.llm import ask_llm

def review(content):

    prompt=f"""
    Review this output.

    Check:
    - missing sections
    - inconsistencies
    - completeness

    Improve if needed.

    Content:
    {content}
    """

    return ask_llm(prompt)