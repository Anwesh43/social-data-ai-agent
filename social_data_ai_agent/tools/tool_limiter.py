class ToolLimiter:
    def __init__(self):
        self.toolCallMap = {
        }

    def setToolCalLimit(self, toolName : str, limit : int):
        self.toolCallMap[toolName] = {
            "limit": limit,
            "count": 0
        }
    
    def incrementToolCall(self, toolName: str):
        if toolName in self.toolCallMap:
            count = self.toolCallMap[toolName]["count"]
            self.toolCallMap[toolName]["count"] = count + 1

    def isLimitReached(self, toolName : str):
        if toolName in self.toolCallMap:
            return self.toolCallMap[toolName]["count"] >= self.toolCallMap[toolName]["limit"]
        return False 

    def isKeyPresent(self, toolName : str):
        return toolName in self.toolCallMap