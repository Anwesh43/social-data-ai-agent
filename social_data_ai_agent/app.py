from agents.socialdata_agent import analyseSocialData
import sys 
import asyncio 

if __name__ == "__main__" and len(sys.argv) > 1:
    prompt = " ".join(sys.argv[1:])
    asyncio.run(analyseSocialData(prompt=prompt))
    