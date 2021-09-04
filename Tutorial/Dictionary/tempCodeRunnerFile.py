a = {
    {"name":"hoa", "score": 10},
    {"name":"ha", "score": 7},
    {"name":"huy", "score": 9},
}
print(max(a.items(), key = lambda k : k[1]))