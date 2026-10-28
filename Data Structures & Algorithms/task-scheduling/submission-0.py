import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        time = 0
        queue = collections.deque()
        count = Counter(tasks)
        Maxheap = [ - cnt for cnt in count.values()]
        heapq.heapify(Maxheap)

        while Maxheap or queue:
            time +=1
            if Maxheap:
                value = heapq.heappop(Maxheap) + 1
                if value:
                    queue.append([value,time+n])

            if queue and queue[0][1] == time:
                heapq.heappush(Maxheap,queue.popleft()[0])

        return time


        