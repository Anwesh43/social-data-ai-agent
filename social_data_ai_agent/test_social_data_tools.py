from tools.social_data_tools import getThread, getUserFollowings, searchForTweets, getArticleDetails, getUserProfile, getUserTweets, getVerifiedFollowers
from typing import Dict 
import json 

def writeFile(fileName : str, data : Dict):
    with open(fileName, "w") as f:
        f.write(json.dumps(data))
    print(f"Writing data to {fileName}")


if __name__ == "__main__":
    userProfile = getUserProfile("elonmusk")
    writeFile("test_user_profile.json", userProfile)
    
    writeFile("test_user_followers.json", getVerifiedFollowers(userProfile["id_str"]))
    writeFile("test_user_followings.json", getUserFollowings(userProfile["id_str"]))
    writeFile("test_thread_status.json", getThread("2104139753998188961"))
    writeFile("test_article.json", getArticleDetails("2102762406204076532"))