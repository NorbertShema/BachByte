from collections import deque

def blueprint_approval(blueprints):
    queue = deque(sorted(blueprints))  
    approved = []

    while queue:
        approved.append(queue.popleft()) 

    return approved
