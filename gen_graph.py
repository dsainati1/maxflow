import random
import sys

def output_results(size, graph, output_file):
  with open(output_file, 'w') as outfile:
    lst = range(0, size)
    outfile.write('source\n')
    for n in graph["source"]:
      outfile.write(n[0])
      outfile.write(":")
      outfile.write(str(n[1]))
      outfile.write(",")
    outfile.write("\nsink\n")
    outfile.write("---")
    for node in lst:
      outfile.write("\n")
      outfile.write(str(node))
      outfile.write("\n")
      if len(graph[str(node)]) == 0:
        outfile.write("---")
        continue
      else:
        for n in graph[str(node)]:
          outfile.write(n[0])
          outfile.write(":")
          outfile.write(str(n[1]))
          outfile.write(",")

def make_degree_graph(size, degree, cap):
  lst = range(0, size)
  graph = {}

  for node in lst:
    ns = []
    for i in range(0, degree):
      neighbor = random.randint(0, size)
      if neighbor == size:
        name = "sink"
      else:
        name = str(neighbor) 
      ns.append((name, random.randint(1,cap)))
    graph[str(node)] = ns

  src = []
  for i in range(0, degree):
      neighbor = random.randint(0, size-1)
      src.append((str(neighbor), random.randint(1,cap)))
  graph["source"] = src
  graph["sink"] = []
  return graph


def make_uniform_graph(size, prob, cap):
  lst = range(0, size)
  graph = {}

  for node in lst:
    ns = []
    for neighbor in lst:
      if node == neighbor:
        continue
      if random.random() <= prob:
        ns.append((str(neighbor), random.randint(1,cap)))
    if random.random() <= prob:
        ns.append(("sink", random.randint(1,cap)))
    graph[str(node)] = ns

  src = []
  for node in lst:
    if random.random() <= prob:
      src.append((str(node), random.randint(1,cap)))
  graph["source"] = src
  graph["sink"] = []
  return graph

def main():
  outfile = sys.argv[1]
  size = int(sys.argv[2])
  typ = sys.argv[4]
  cap = int(sys.argv[5])

  if typ == "uniform":
    prob = float(sys.argv[3])
    graph = make_uniform_graph(size, prob, cap)
  else:
    prob = int(sys.argv[3])
    graph = make_degree_graph(size, prob, cap)
  output_results(size, graph, outfile)  

if __name__ == "__main__":
    main()