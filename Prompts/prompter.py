def prompt_tool1_zero_shot(i, scenario, tools, files, questions):
    return f"""
You are tasked with solving a Blue Team Labs Online (BTLO)-style cybersecurity investigation challenge using Ubuntu terminal commands.

Scenario:
{scenario}

Available Tools:
{', '.join(tools)}

Target File(s):
{', '.join(files)}

Question:
{questions[i]}

Instructions:
Based on the question above, generate the **first Ubuntu terminal command** you would execute to begin solving the question.

Respond in this format only:
<your Ubuntu terminal command>

Important:
- Do not answer the question.
- Do not include any explanation.
- Only provide one command.
- Be precise and relevant to the question.
"""

def prompt_tool2_zero_shot(i, scenario, tools, files, questions):
    return f"""
You are assisting in solving a Blue Team Labs Online (BTLO)-style cybersecurity investigation challenge using Ubuntu terminal commands.

Scenario:
{scenario}

Available Tools:
{', '.join(tools)}

Target File(s):
{', '.join(files)}

Question:
{questions[i]}


Instructions:
Based strictly on the previous commands and their outputs and the question:

1. If the answer is **clearly** present in the last output, respond with:
   final answer: <your answer>

2. If the answer is **not yet clear**, and you need to explore further, respond with:
   <your next Ubuntu terminal command>

Important:
- Do **not** include explanations or justifications.
- Only give **one** response per turn, using the correct format.
- Decide carefully whether the answer is present or more steps are needed.
"""

def prompt_zero_shot(i, scenario, tools, file, questions):
    return f"""
You are tasked with solving a Blue Team Labs Online (BTLO)-style cybersecurity investigation challenge using Ubuntu terminal commands.

Scenario:
{scenario}

Available Tools:
{', '.join(tools)}

Target File(s):
{', '.join(file)}

Question:
{questions[i]}

Instructions:
You are assisting in a live investigation and must analyze the provided file(s) to answer the question using the tools listed.

There are two types of responses you can give, based on the current situation:

1. If the answer to the question is not yet known and more data must be extracted:
   Respond with:
   command: <your Ubuntu terminal command>

   - This can be your first step after seeing the question.
   - It can also be used **after** reviewing the user's previous command output if it did not contain the answer or needs further processing.

2. If the output provided by the user clearly contains the answer:
   Respond with:
   final answer: <your answer based strictly on the output>

Important Notes:
- Think step by step when needed — especially for complex questions.
- Only provide **one** response per turn, in one of the two formats above.
- Do not include any explanation, justification, or text outside the specified format.
- Always base your decision (whether to give a command or final answer) on what has already been seen and whether the question can be conclusively answered.

Your goal is to be precise, methodical, and efficient.
"""