import json
import boto3
import pandas as pd
import gradio as gr
from langchain.chains import LLMChain
from langchain.llms.bedrock import Bedrock
from langchain.prompts import PromptTemplate

# Set AWS credentials if necessary (make sure they are properly configured)
# os.environ["AWS_PROFILE"] = "your_profile"

# Initialize Amazon Bedrock client
bedrock_client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1"
)

# Define the model ID and parameters for Bedrock LLM
modelID = "amazon.titan-text-express-v1"  # Update with actual model ID

# Instantiate the Bedrock LLM with the required parameters
llm = Bedrock(
    model_id=modelID,
    client=bedrock_client,
    model_kwargs={"maxTokenCount": 2000, "temperature": 0.7}
)

# Load CSV file into a pandas dataframe
player_data = pd.read_csv('esports_data.csv')

# Expert context to prime the model
EXPERT_PROMPT = """
You are a VALORANT esports expert and data scientist for a professional team. You have in-depth knowledge of VALORANT players, teams, and strategies from tournaments like VCT International, VCT Challengers, and VCT Game Changers. You provide professional advice on team compositions, player roles, and strategies in competitive matches. Be detailed in your answers and use your knowledge of the game to provide strategic insights.
"""

# Function to search player/team info from CSV
def search_player_data(query):
    # Check if the query matches a player or team in the CSV
    player_info = player_data[
        player_data['handle'].str.contains(query, case=False, na=False) | 
        player_data['team_name'].str.contains(query, case=False, na=False)
    ]
    
    if not player_info.empty:
        result = player_info.to_dict(orient='records')[0]  # Get the first match
        return f"Player: {result['handle']}, Team: {result['team_name']}, Status: {result['player_status']}, Region: {result['region']}"
    else:
        return None

# Function to generate the chatbot response using LangChain
def my_chatbot(user_input):
    # Define the prompt template for LangChain
    prompt = PromptTemplate(
        input_variables=["expert_prompt", "user_input"],
        template="""
        {expert_prompt}
        User prompt: {user_input}
        """
    )

    # Create the LangChain with the Bedrock LLM and prompt
    bedrock_chain = LLMChain(llm=llm, prompt=prompt)

    # Create the full prompt with expert context and user input
    response = bedrock_chain({
        "expert_prompt": EXPERT_PROMPT,
        "user_input": user_input
    })

    return response['text']

# Define function for chatbot responses
def chatbot(user_prompt):
    if not user_prompt.strip():
        return "Please enter a valid prompt."
    
    # First, check if the user is asking about a player or team from the CSV
    csv_result = search_player_data(user_prompt)
    
    if csv_result:
        return f"**Player Data:** {csv_result}"
    
    # If no match in CSV, proceed with the Bedrock response using LangChain
    bot_response = my_chatbot(user_prompt)
    return f"**Response:** {bot_response}"

# Define Gradio Interface
def gradio_interface():
    # Create Gradio interface components
    gr_interface = gr.Interface(
        fn=chatbot,
        inputs=gr.Textbox(lines=4, label="Enter Your Custom VALORANT Esports Prompt"),
        outputs="text",
        title="VCTAI",
        description="Ask any question about VALORANT esports, players, team compositions, strategies, and roles.",
        theme="default"
    )
    
    # Launch the Gradio app
    gr_interface.launch()

if __name__ == '__main__':
    gradio_interface()
