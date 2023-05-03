import heapq

tasks = []
heapq.heapify(tasks)

num_tasks = int(input())

for i in range(num_tasks):
    task = input().split()

    if task[0] == 'N':
        task_id = int(task[1])
        difficulty = int(task[2])
        heapq.heappush(tasks, (-difficulty, task_id))
    elif task[0] == 'R':
        _, task_id = heapq.heappop(tasks)
        print(task_id)