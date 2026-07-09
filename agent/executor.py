from services.llm import ask_llm

def execute_tasks(tasks):

    outputs=[]

    for task in tasks[:5]:

        if isinstance(task, dict):

            task_text = task.get(
                "name",
                str(task)
            )

        else:

            task_text = str(task)

        print(
            f"Running: {task_text}"
        )

        result = ask_llm(
            f"""
            Create detailed professional business content for:

            {task_text}

            Keep it concise but useful.
            """
        )

        outputs.append({
            "task":task_text,
            "result":result
        })

    return outputs