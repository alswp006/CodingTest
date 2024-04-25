from collections import deque

q = deque(input() * 2)
slice_q = deque(q.popleft() for i in range(q.count("a") // 2))
answer = slice_q.count("b")

while q and slice_q:
    slice_q.popleft()
    slice_q.append(q.popleft())
    answer = min(answer, slice_q.count("b"))

print(answer)