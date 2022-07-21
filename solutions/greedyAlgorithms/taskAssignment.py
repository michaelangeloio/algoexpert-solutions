#simple

def taskAssignment(k, tasks):
    # Write your code here.
    sortedTask = sorted(list(enumerate(tasks)), key = lambda x: x[1])
    taskTuples = []
    for i in range(k):
        taskTuples.append((sortedTask[i][0], sortedTask[len(tasks)-1-i][0]))
    return taskTuples
