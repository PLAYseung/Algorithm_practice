
import heapq

def solution(operations):
    answer = []
    heap = []
    
    for item in operations:
        if item.split()[0] == 'I':
            heapq.heappush(heap, int(item.split()[1]))
            continue
        elif len(heap):
            heap.pop(len(heap)-1) if item=='D 1' else heap.pop(0)
            
            
    if len(heap)<2:
        answer.extend([0,0])
    else:
        answer.extend([heap[-1],heap[0]])
    
    return answer
