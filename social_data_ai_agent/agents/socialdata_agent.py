from pydantic_ai import Agent 
from tools.social_data_tools import getVerifiedFollowers, getUserFollowings, getArticleDetails, getThread, getUserProfile, getUserTweets, createPDFFromHTMLStr, getTweetDetails
from dotenv import load_dotenv 
from prompts.social_data_prompt import SYSTEM_PROMPT

load_dotenv()

agent = Agent(
    model = 'openai:gpt-5.2',
    tools = [getVerifiedFollowers, getUserFollowings, getArticleDetails, getThread, getUserProfile, getUserTweets, createPDFFromHTMLStr, getTweetDetails],
    system_prompt = SYSTEM_PROMPT
)

async def analyseSocialData(prompt : str):
    async with agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end = '')