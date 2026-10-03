from services.base_http_client import BaseHTTPClient 
from dotenv import load_dotenv 
import os 
from typing import Dict 

load_dotenv()

class SocialDataService:
    def __init__(self):
        self.client = BaseHTTPClient(os.environ["SOCIALDATA_BASE_URL"])

    def _getHeaders(self):
        return {
            "Authorization": f"Bearer {os.environ["SOCIALDATA_API_KEY"]}"
        }

    def _handleError(self, e):
        print("Error", e)
        return {
            "status": "Error", 
            "message": str(e)
        }
    


    def _getUserResponse(self, response : Dict):
        try:
            users = response["users"]
            results = []
            finalResponse = {
                "nextCursorId": response["next_cursor"]
            }
            for user in users:
                userObj = {}
                userObj["tweetId"] = user["id_str"]
                userObj["name"] = user["name"]
                userObj["username"] = user["screen_name"]
                userObj["followersCount"] = user["followers_count"]
                results.append(userObj)

            finalResponse["results"] = results 
            return finalResponse
        except Exception as e:
            raise e 

    def _getTweetsResult(self, response):
        finalResponse = {}
        try:
            tweets = response["tweets"]
            finalResponse["next_cursor_id"] = response["next_cursor"]
            results = []
            for tweet in tweets:
                tweetObj = {}
                tweetObj["id"] = tweet["id_str"]
                tweetObj["fullText"] = tweet["full_text"]
                if "user" in tweet:
                    tweetObj["userId"] = tweet["user"]["id_str"]
                    tweetObj["userName"] = tweet["user"]["screen_name"]
                    tweetObj["fullName"] = tweet["user"]["name"]
                results.append(tweetObj)
            finalResponse["results"] = results
            return finalResponse
        except Exception as e:
            raise e 

    def getUserProfile(self, username : str):
        try: 
            response = self.client.getCall(f"user/{username}", qpParams={}, headers = self._getHeaders())
            return response
        except Exception as e:
            return self._handleError(e)

    def getVerifiedUserFollowers(self, userId : str, cursorId : str = ''):
        try:
            qpParams = {}
            if not(cursorId == ''):
                qpParams["cursor"] = cursorId

            response = self.client.getCall(f"user/{userId}/verified-followers", qpParams=qpParams, headers = self._getHeaders())
            return self._getUserResponse(response=response)
        except Exception as e:
            return self._handleError(e)      


    def getUserFollowings(self, userId : str, cursorId : str = ''):
        try:
            qpParams = {}
            if not(cursorId == ''):
                qpParams["cursor"] = cursorId
            response = self.client.getCall(f"user/{userId}/following", qpParams=qpParams, headers = self._getHeaders())
            return self._getUserResponse(response=response)
        except Exception as e:
            return self._handleError(e)

    def getUserTweets(self, userId : str, cursorId: str = ''):
        try:
            qpParams = {}
            if not(cursorId == ''):
                qpParams["cursor"] = cursorId 
            response = self.client.getCall(f"user/{userId}/tweets", qpParams=qpParams, headers = self._getHeaders())
            return self._getTweetsResult(response=response) 
        except Exception as e:
            return self._handleError(e)

    def getTopSearchResults(self, query : str, cursorId, type : str = 'Latest'):
        try:
            qpParams = {
                "query": query,
                "type": type 
            }
            if not(cursorId == ''):
                qpParams["cursor"] = cursorId
            response = self.client.getCall("search", qpParams=qpParams, headers = self._getHeaders())
            return self._getTweetsResult(response=response)
        except Exception as e:
            return self._handleError(e)

    def getThread(self, threadId : str, cursorId : str = ''):
        try:
            qpParams = {

            }
            if not(cursorId == ''):
                qpParams["cursor"] = cursorId
            response = self.client.getCall(f"thread/{threadId}", qpParams = qpParams, headers= self._getHeaders())
            return self._getTweetsResult(response=response)
        except Exception as e:
            return self._handleError(e)

    def getArticleDetails(self, articleId :str):
        try:
            response = self.client.getCall(f"article/{articleId}", qpParams={}, headers = self._getHeaders())
            return response 
        except Exception as e:
            return self._handleError(e)
        