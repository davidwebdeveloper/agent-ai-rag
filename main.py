from dotenv import load_dotenv
import os
import pandas as pd
from llama_index.experimental.query_engine import PandasQueryEngine
from prompts import new_prompt, instruction_str, context
from note_engine import note_engine
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai import OpenAI
# from pdf import india_engine

load_dotenv()

population_path = os.path.join('data', 'population.csv')
population_df = pd.read_csv(population_path)

population_query_engine = PandasQueryEngine(df=population_df, verbose=True, instruction_str=instruction_str)
population_query_engine.update_prompts({"pandas_prompt": new_prompt})


population_query_engine.query("What is the population of india?")

tools = [
    note_engine,
    QueryEngineTool(query_engine=population_query_engine, metadata=ToolMetadata(name="population_query_engine", description="Query the population data"),),
    # QueryEngineTool(query_engine=india_engine, metadata=ToolMetadata(name="india_data", description="This gives the information about the india the country"),)

]


llm = OpenAI(model="gpt-4o-mini-2024-07-18")

agent = ReActAgent.from_tools(tools=tools, llm=llm, verbose=True, context=context)

while (prompt := input("Enter a prompt: ")) != "exit":
    result = agent.query(prompt)
    print(result)

