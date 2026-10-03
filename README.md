# Social Data AI Agent

An AI agent that analyses X (Twitter) data. It uses [Pydantic AI](https://ai.pydantic.dev/) with an OpenAI model and calls the [SocialData API](https://socialdata.tools/) to fetch profiles, followers, followings, tweets, threads and articles. It can also write its analysis to a PDF report.

## Features

The agent can call these tools (defined in `social_data_ai_agent/tools/social_data_tools.py`):

| Tool | Description |
| --- | --- |
| `getUserProfile` | Fetch a user's profile by username |
| `getVerifiedFollowers` | List a user's verified followers (paginated) |
| `getUserFollowings` | List accounts a user follows (paginated) |
| `getUserTweets` | Fetch a user's tweets (paginated) |
| `getTweetDetails` | Fetch details for a single tweet |
| `getThread` | Fetch all tweets in a thread (paginated) |
| `getArticleDetails` | Fetch an X article |
| `createPDFFromHTMLStr` | Render an HTML string to an A4 PDF with Playwright |

Paginated tools are capped at 5 calls per user/query by `ToolLimiter`, so the agent can't page through results forever.

## Project structure

```
social_data_ai_agent/
├── app.py                  # CLI entry point
├── agents/
│   └── socialdata_agent.py # Pydantic AI agent definition and streaming runner
├── prompts/
│   └── social_data_prompt.py  # System prompt
├── services/
│   ├── base_http_client.py    # Thin wrapper around requests
│   └── social_data_service.py # SocialData API client
└── tools/
    ├── social_data_tools.py   # Tools exposed to the agent
    └── tool_limiter.py        # Per-tool call limits
```

## Requirements

- Python 3.14+
- [Poetry](https://python-poetry.org/)
- An OpenAI API key
- A SocialData API key

## Setup

1. Install dependencies:

   ```bash
   poetry install
   poetry run playwright install chromium
   ```

2. Create a `.env` file in the project root:

   ```env
   OPENAI_API_KEY=your-openai-key
   SOCIALDATA_API_KEY=your-socialdata-key
   SOCIALDATA_BASE_URL=https://api.socialdata.tools/twitter
   ```

## Usage

Modules are imported relative to the `social_data_ai_agent` directory, so run the app from there and pass your prompt as arguments:

```bash
cd social_data_ai_agent
poetry run python app.py "Analyse the latest tweets from @username and create a PDF report"
```

The agent's response streams to the terminal. Any PDF it generates is written to the current working directory.

## Tests

The `test_*.py` scripts in `social_data_ai_agent/` exercise individual tools and the tool limiter. Run them from the same directory, for example:

```bash
cd social_data_ai_agent
poetry run python test_tool_limiter.py
```
