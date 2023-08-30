if __name__ == '__main__':
    n = int(input())
    d = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        d[name] = scores
    query_name = input()
    for i,j in d.items():
       if i == query_name:
           avg = sum(j)/len(j)
           float_conversion = f"{avg:.2f}"
           print(float_conversion)