class Solution:
    def largestWordCount(self, messages: List[str], senders: List[str]) -> str:
        count = collections.defaultdict(int)

        for idx, message in enumerate(messages):
            count[senders[idx]] += len(message.split(' '))
        
        h = [(-1 * value, key) for key, value in count.items()]
        heapq.heapify(h)
        p = heapq.heappop(h)
        # print(h)
        while h and h[0][0] == p[0]:
            p = heapq.heappop(h)
        return p[1]