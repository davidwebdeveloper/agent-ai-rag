
from llama_index.core.prompts.base import PromptTemplate

instruction_str = """
    1. Convert the query to executable python code using Pandas. 
    2. The final line of "should by a python expression that be called with the `eval()` function.
    3. The code should represent the solution to the query.
    4. PRINT ONLY THE EXPRESSION, NOT THE RESULT.
    5. Do not quote the expression."""


new_prompt = PromptTemplate(
    """
    You are wwoking with a Pandas DataFrame  in python.
    The name of the DataFrame is `df`.
    This is the result of `print(df.head())`:
    {df_str}

    Follow these instructions to complete the task:
    {instruction_str}
    Query: {query_str}


    Expression: """
)


context = """   
Purpose: The primary role of this agent is to assist users by providing accurate information about the world population statistics and dettails about a country. 
"""