# GPT3-Turbo AI Agent

This is a project for building an AI agent using GPT3-Turbo.

## Architecture

The architecture for this project is as follows:

| Component           | Technology     | Purpose                                                    |
|---------------------|----------------|------------------------------------------------------------|
| Web server          | Flask          | Serves API requests                                        |
| API Gateway         | AWS ELB        | Load balances requests to multiple servers                 |
| Database            | PostgreSQL     | Stores data for the application                            |
| GPT3-Turbo client   | OpenAI API      | Interacts with the GPT3-Turbo AI engine                     |
| Deployment platform | AWS Fargate    | Hosts the web server in a containerized environment         |

## File Directory Tree

```
.
├── api
│   ├── app.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── .dockerignore
├── scripts
│   └── initialize_db.py
├── models
│   └── gpt3.py
├── tests
│   └── test_gpt3.py
├── README.md
├── .gitignore
├── docker-compose.yml
└── config.ini
```

# Context Storage

Provide me with a prompt that will summarize our work so far including the files and any other relevant info to refresh your memory and proceed forward.

> Sure! Here's a summary of the work we've done so far:
>
> We have designed the architecture for an AI chatbot using Python, GPT3-Turbo, AWS Fargate, and PostgreSQL.
> We have created a file directory tree for the project, including all necessary files such as Dockerfile, app.py, chatbot.py, and requirements.txt.
> We have written the code for initializing the PostgreSQL database and created a schema for storing chat history.
> We have implemented the functionality for generating a response from the GPT-3 API and for storing chat history in the database.
> We have created a loop in chatbot.py to allow the user to have a conversation with the AI agent.
> Next, we could focus on improving the AI agent's ability to generate relevant responses. We could use the chat history stored in the database to train the AI agent and improve its ability to understand the user's queries and generate helpful responses. We could also implement other features, such as the ability to handle user requests for specific types of information, like weather or news.

## Developer Setup

To get started with developing the AI chatbot, follow these steps:

1. Install [Docker](https://www.docker.com/get-started).
2. Clone this repository to your local machine.
3. Navigate to the project directory in your terminal.
4. Build the Docker image with the following command:
    ```
    docker build -t chatbot .
    ```
5. Start the Docker container with the following command:
    ```
    docker run -p 5000:5000 chatbot
    ```
6. Open your web browser and navigate to `http://localhost:5000` to see the chatbot in action.

### Prerequisites

You will need to set up a GPT-3 API key and a PostgreSQL database in order to use the full functionality of the chatbot. Be sure to update the `app.py` file with your API key and database credentials.

The GPT-3 API key needs to be added to the app.py file, specifically in the openai.api_key line:

You can obtain your GPT-3 API key by signing up for an OpenAI account and creating a new API key. Once you have your key, replace "YOUR_API_KEY_HERE" with your actual API key.

As for the database credentials, you will need to update the DATABASE_URL variable in the db.py file with the URL for your PostgreSQL database. The format for the URL is:

```
postgresql://<username>:<password>@<hostname>:<port>/<database-name>
```

Replace `<username>`, `<password>`, `<hostname>`, `<port>`, and `<database-name>` with your own values.


