
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

if __name__=='__main__':
    print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
    print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))