from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Create an adjacency list for the graph
        graph = {i: [] for i in range(numCourses)}
        for dest, src in prerequisites:
            graph[src].append(dest)
        
        # State tracking: 0 = unvisited, 1 = visiting, 2 = visited
        state = [0] * numCourses
        
        # Helper function to perform DFS and detect cycle
        def dfs(course):
            if state[course] == 1:  # Cycle detected
                return False
            if state[course] == 2:  # Already fully processed
                return True
            
            # Mark the course as being visited
            state[course] = 1
            
            # Visit all the neighbors (prerequisites)
            for neighbor in graph[course]:
                if not dfs(neighbor):  # If any course cannot be completed, return False
                    return False
            
            # Mark the course as fully processed
            state[course] = 2
            return True
        
        # Check each course
        for course in range(numCourses):
            if state[course] == 0:  # If the course hasn't been visited
                if not dfs(course):  # Start DFS to check for cycles
                    return False
        
        return True
