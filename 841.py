class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        visited = []
        def dfs(currentRoom):
            if currentRoom in visited:
                return
            visited.append(currentRoom)

            for key in rooms[currentRoom]:
                dfs(key)
        
        dfs(0)

        return len(visited) == len(rooms)
