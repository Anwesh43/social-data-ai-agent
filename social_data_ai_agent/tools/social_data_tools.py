from services.social_data_service import SocialDataService 
from tools.tool_limiter import ToolLimiter

sds = SocialDataService()

toolCallLimiter = ToolLimiter()



def getUserProfile(userName : str):
    print(f"Calling getUserProfile for {userName}")
    return sds.getUserProfile(username=userName)

def getVerifiedFollowers(userId : str, cursorId : str = ''):
    print(f"Calling getVerifiedFollowers tool for {userId}")
    toolName = f"verifiedFollowers_{userId}"
    if not(toolCallLimiter.isKeyPresent(toolName=toolName)):
        toolCallLimiter.setToolCalLimit(toolName=toolName, limit=5)
        
    if toolCallLimiter.isLimitReached(toolName):
        return {
            "status": "Error", 
            "message": f"tool call limit for getVerifiedFollowers has reached for {userId}"
        }
    toolCallLimiter.incrementToolCall(toolName=toolName)
    return sds.getVerifiedUserFollowers(userId, cursorId=cursorId)

def getUserFollowings(userId : str, cursorId : str = ''):
    print(f"Calling getUserFollowings for {userId}")
    toolName = f"userFollowings_{userId}"

    if not(toolCallLimiter.isKeyPresent(toolName=toolName)):
        toolCallLimiter.setToolCalLimit(toolName=toolName, limit=5)
    if toolCallLimiter.isLimitReached(toolName):
        return {
            "status": "Error", 
            "message": f"tool call limit for getUserFollowings has reached for {userId}"
        }
    toolCallLimiter.incrementToolCall(toolName=toolName)
    return sds.getUserFollowings(userId=userId, cursorId = cursorId)

def getUserTweets(userId : str, cursorId : str = ''):
    print(f"Calling getUserTweets tool for {userId}")
    toolName = f"userTweets_{userId}"
    if not(toolCallLimiter.isKeyPresent(toolName=toolName)):
        toolCallLimiter.setToolCalLimit(toolName=toolName, limit=5)

    if toolCallLimiter.isLimitReached(toolName):
        return {
            "status": "Error", 
            "message": f"tool call limit for getUserTweets has reached for {userId}"
        }
    toolCallLimiter.incrementToolCall(toolName=toolName)
    return sds.getUserTweets(userId=userId, cursorId=cursorId)


def searchForTweets(query : str, cursorId : str = '', type : str = 'Latest'):
    print(f"Calling searchQuery tool {query} and {cursorId}")
    toolName = f"searchForTweets_{query}"
    if not(toolCallLimiter.isKeyPresent(toolName=toolName)):
        toolCallLimiter.setToolCalLimit(toolName=toolName, limit=5)
    if toolCallLimiter.isLimitReached(toolName):
        return {
            "status": "Error", 
            "message": f"tool call limit for searchForTweets has reached for {query}"
        }
    toolCallLimiter.incrementToolCall(toolName=toolName)    
    return sds.getTopSearchResults(query = query, cursorId=cursorId, type = type)

def getThread(threadId : str, cursorId : str = ''):
    print(f"Calling getThread for {threadId} and {cursorId}")
    return sds.getThread(threadId=threadId, cursorId=cursorId)

def getArticleDetails(articleId : str):
    print(f"Calling getArticleDetails for {articleId}")
    return sds.getArticleDetails(articleId=articleId)