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

def prompt_tool1_thought(i, scenario, tools, files, questions):
    return f"""
You are solving a Blue Team Labs Online (BTLO)-style cybersecurity investigation challenge using Ubuntu terminal commands.

Scenario:
{scenario}

Available Tools:
{', '.join(tools)}

Target File(s):
{', '.join(files)}

Question:
{questions[i]}

Instructions:
- Think step-by-step about how you would approach answering the question.
- Consider which tools or files might be relevant.
- Do not give a command yet.

Respond in this format only:
<your reasoning about what to do next>

Important:
- Do not provide any commands.
- Focus only on explaining your reasoning.
- Be concise and precise.
"""


def prompt_tool1_action(i, scenario, tools, files, questions, thought):
    return f"""
You are solving a Blue Team Labs Online (BTLO)-style cybersecurity investigation challenge using Ubuntu terminal commands.

Scenario:
{scenario}

Available Tools:
{', '.join(tools)}

Target File(s):
{', '.join(files)}

Question:
{questions[i]}

Your previous reasoning:
{thought}

Instructions:
- Based on your reasoning above and the full context, generate the **first Ubuntu terminal command** you would execute to begin solving the question.

Respond in this format only:
<your Ubuntu terminal command>

Important:
- Only provide one command.
- Do not answer the question.
- Do not include any explanation.
- Be precise and relevant to the question and your thought.
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

def prompt_tool2_thought(i, scenario, tools, files, questions):
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

Context:
You have access to previous reasoning steps (thoughts), the Ubuntu terminal commands generated (actions), and their corresponding command outputs. Use this organized history to guide your reasoning.

Instructions:
- Think step by step about what should be done next based on the question, the provided files and tools, and previous steps taken.
- You may conclude that the answer is already present in previous command outputs.
- If so, clearly state that the answer appears to be known based on prior outputs, but do NOT state the answer itself.
- Do NOT generate any commands at this stage.

Respond only in this format:
<your reasoning about what to do next>

Important:
- Do NOT include any command.
- Do NOT output the final answer.
- Be concise and precise.
"""

def prompt_tool2_action(i, scenario, tools, files, questions, thought):
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

Your previous reasoning:
{thought}

Note:
You also have access to the full context from previous thoughts, actions, and command outputs.

Instructions:
- Based strictly on the current question, your latest reasoning above, and the previous command outputs, decide the next step.

Respond in ONE of the following formats ONLY:

1. If the reasoning indicates that the answer is already known from a previous command output:
   final answer: <your answer>

2. If further investigation is needed:
   <your next Ubuntu terminal command>

Important:
- Do NOT explain or justify.
- Return only one response in the correct format.
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

def prompt_manual_thought(i, scenario, tools, files, questions, history):
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

History of Previous Steps:
{'\n'.join(str(h) for h in history) if history else '[No previous steps yet — this is the first question.]'}

Context:
You have access to organized previous steps, including:
- Reasoning/thoughts
- Ubuntu terminal commands executed
- Their respective command outputs

{'This is the first step, so no previous thoughts or actions exist yet.' if not history else 'Use the history to reason your next step effectively.'}

Instructions:
- Think step by step about what to do next, given the question, available tools, files, and prior steps.
- Use logical deduction to decide what direction to explore next.
- If the previous command output clearly reveals the final answer, you can note that—but DO NOT reveal the answer.
- Do NOT return any command or final answer in this step.

Respond only in this format:
<your internal reasoning about what should be done next>

Important:
- Do NOT explain or justify your response.
- Be concise and direct.
"""

def prompt_manual_action(i, scenario, tools, files, questions, history, thought):
    return f"""
You are solving a Blue Team Labs Online (BTLO)-style cybersecurity investigation challenge using Ubuntu terminal commands.

Scenario:
{scenario}

Available Tools:
{', '.join(tools)}

Target File(s):
{', '.join(files)}

Question:
{questions[i]}

History of Previous Steps:
{'\n'.join(str(h) for h in history) if history else '[No previous steps yet — this is the first question.]'}

Previous Reasoning (Thought):
{thought}

Context:
You have access to organized previous steps, including:
- Reasoning/thoughts
- Terminal commands executed
- Their respective command outputs

Instructions:
Based on your reasoning and the current state of the investigation, you must choose **only one** of the following responses:

Respond only in one of these formats:
1. If more investigation is needed:
   command: <your Ubuntu terminal command>

2. If the answer is already known:
   final answer: <the extracted answer>

Important:
- Base your response strictly on the reasoning and available information.
- Do NOT explain or justify your response.
- Be concise and direct.
"""

