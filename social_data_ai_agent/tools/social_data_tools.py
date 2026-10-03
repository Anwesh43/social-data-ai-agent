from services.social_data_service import SocialDataService 

sds = SocialDataService()



def getUserProfile(userName : str):
    print(f"Calling getUserProfile for {userName}")
    return sds.getUserProfile(username=userName)

def getVerifiedFollowers(userId : str, cursorId : str = ''):
    print(f"Calling getVerifiedFollowers tool for {userId}")
    return sds.getVerifiedUserFollowers(userId, cursorId=cursorId)

def getUserFollowings(userId : str, cursorId : str = ''):
    print(f"Calling getUserFollowings for {userId}")
    return sds.getUserFollowings(userId=userId, cursorId = cursorId)

def getUserTweets(userId : str, cursorId : str = ''):
    print(f"Calling getUserTweets tool for {userId}")
    return sds.getUserTweets(userId=userId, cursorId=cursorId)

def searchForTweets(query : str, cursorId : str = '', type : str = 'Latest'):
    print(f"Calling searchQuery tool {query} and {cursorId}")
    return sds.getTopSearchResults(query = query, cursorId=cursorId, type = type)

def getThread(threadId : str, cursorId : str = '')
    print(f"Calling getThread for {threadId} and {cursorId}")
    return sds.getThread(threadId=threadId, cursorId=cursorId)

def getArticleDetails(articleId : str):
    print(f"Calling getArticleDetails for {articleId}")
    return sds.getArticle(articleId=articleId)