# Task 1: Refactor Word Counter using Counter

from collections import Counter

para = "The pairs figure skating competition at the 2002 Winter Olympics was held on February 9 and 11 at the Salt Lake Ice Center  Salt Lake City, Utah,  the United States. Originally, Elena Berezhnaya and Anton Sikharulidze of Russia won the gold, while Jamie Salé and David Pelletier of Canada won the silver, and Shen Xue and Zhao Hongbo of China won the bronze. However, allegations of misconduct led to one judge's scores being discarded; Salé  Pelletier were also awarded gold medals, while the Russians were allowed to keep theirs. In a joint press conference, the International Skating Union (ISU) and the International Olympic Committee announced that Marie-Reine Le Gougne, the French judge implicated in collusion, was guilty of misconduct and immediately suspended. In 2004, the ISU voted to retire the 6.0 judging system. As a result, the ISU Judging System was created, in which skaters are scored based on a technical evaluation of the required elements. (Full article...)"

p = para.split()
result = Counter(p)
print(result.most_common(3))


#---------------------------------------------------------
#Task 2: Graph Adjacency List using defaultdict

from collections import defaultdict

connections = [
    ("Ali", "Hamza"),
    ("Ali", "Huzaifa"),
    ("Hamza", "Azan"),
    ("Huzaifa", "Azan")
]

graph = defaultdict(list)
for u,v in connections:
    graph[u].append(v)
    graph[v].append(u)


for person,friend in graph.items():
    print(f"{person}:{friend}")


