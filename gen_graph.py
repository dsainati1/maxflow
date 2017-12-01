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


def make_graph(size, prob):
  lst = range(0, size)
  graph = {}

  for node in lst:
    ns = []
    for neighbor in lst:
      if node == neighbor:
        continue
      if random.random() <= prob:
        ns.append((str(neighbor), random.randint(1,10)))
    if random.random() <= prob:
        ns.append(("sink", random.randint(1,10)))
    graph[str(node)] = ns

  src = []
  for node in lst:
    if random.random() <= prob:
      src.append((str(node), random.randint(1,10)))
  graph["source"] = src
  graph["sink"] = []
  return graph

def main():
  outfile = sys.argv[1]
  size = int(sys.argv[2])
  prob = float(sys.argv[3])

  graph = make_graph(size, prob)
  output_results(size, graph, outfile)  

if __name__ == "__main__":
    main()