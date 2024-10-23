# Project Overview

This project focuses on developing a chatbot that provides insights into VALORANT esports, utilizing a large language model (LLM) powered by Amazon Bedrock. The model is designed to understand player dynamics, strategies, and team compositions from the game, offering users detailed responses based on their queries.

## Methodology

The LLM, specifically the "amazon.titan-text-express-v1," utilizes Amazon Bedrock to generate responses based on an expert context informed by historical data from VALORANT tournaments. This context includes knowledge of player roles, team strategies, and performance metrics. The chatbot also references player data from a CSV file containing esports statistics, allowing it to provide precise player and team information when queried.

## Data Sources

- **Esports Data CSV**: Contains player statistics, team names, regions, and player statuses.
- **Amazon Bedrock**: Utilizes LLMs trained on diverse datasets to enhance understanding of esports dynamics.

## Findings and Learnings

Throughout the project, it was noted that combining structured player data with the LLM's capabilities allows for nuanced responses to user prompts. This integration highlights the importance of expert knowledge in generating meaningful insights. I also learned how to effectively use Amazon Bedrock to deploy and manage a large language model. This experience deepened my understanding of integrating structured data with LLM capabilities, enhancing response quality. Additionally, I gained insights into optimizing interactions with AWS services like Boto3, which streamlined the data handling process. These skills have empowered me to create a more robust and responsive chatbot for VALORANT esports queries.

## Tooling

- **AWS Services**:
  - **Amazon Bedrock**: Provides the foundation for the LLM, enabling scalable model deployment.
  - **Boto3**: A Python SDK for AWS, used to interact with the Bedrock API and manage data transfer.
  
- **Gradio**: Used to create an interactive web interface for users to engage with the chatbot. Gradio simplifies the process of launching the chatbot, allowing users to submit queries and receive responses in real-time.

This architecture enables a seamless user experience while ensuring robust performance in understanding and responding to VALORANT-related queries.

## Usage

To run this project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
    ```
2. **Install Dependencies**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    pip install -r requirements.txt
    ```
3. **Download Esports Data from Google Drive**:

    [link text][https://drive.google.com/file/d/1Vxvnej6lL-8md8DLUFRX_d_VJTAI4m2v/view?usp=drive_link]

4. **Run the Chatbot**:

    ```bash
    python main.py
    ```
