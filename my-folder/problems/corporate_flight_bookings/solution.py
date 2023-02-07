class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        cnt = [0] * (n + 2)

        for start, end, cost in bookings:
            cnt[start] += cost
            cnt[end + 1] += - 1 * cost
        return accumulate(cnt[1:-1])