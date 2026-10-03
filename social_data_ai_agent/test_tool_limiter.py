from tools.social_data_tools import getVerifiedFollowers
import time 

userId = "44196397"

cursorId = ""

for i in range(1, 100):
    print(f"Calling {i}")
    verifiedFollowers = getVerifiedFollowers(userId=userId, cursorId=cursorId)
    print("RESPONSE", verifiedFollowers)
    if "status" in verifiedFollowers and verifiedFollowers["status"] == "Error":
        print("TOOLCALL LIMIT REACHED")
        break 
    cursorId = verifiedFollowers["nextCursorId"]
    time.sleep(2)
