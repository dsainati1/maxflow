open Graph 
open Flow_network 

let graph_type = ref "matrix"
let search_type = ref "bfs"
let file = ref ""

let options = 
	[("-g", Arg.Set_string graph_type, "Type of graph");
	 ("-s", Arg.Set_string search_type, "Type of search")]

(* Reads a graph in from a file, and parses commandline arguments 
   Graph files follow the format :
   <NODE_NAME> 
   <NEIGHBOR>:<CAPACITY>, <NEIGHBOR>:<CAPACITY>, ...
	
   If a node has no neighbors, put --- on the line after it

   There must be a sink node and a source node, but these will not be included in the output list 
   of nodes (although they may appear in the edge set)
*)
let read_input () :  (string list) * ((string * string * int) list) =
	let rec collect_edges node e : string list -> (string * string * int) list = function
		| [] -> e
		| h :: [] when h = "---" -> e
		| h :: t -> let spl = String.trim h  |> Str.split (Str.regexp ":") in
					let dest = List.hd spl in 
					let cap = List.nth spl 1 |> int_of_string in 
					collect_edges node ((node, dest, cap) ::e) t in
	let rec read_file (input : in_channel) (v, e) : (string list) * ((string * string * int) list) = 
		let node = try input_line input with End_of_file -> "EOF" in 
		if node = "EOF" then (v, e) else
			let v' = if node = "source" || node = "sink" then v else node :: v in 
			let e' = 
				(try input_line input with End_of_file -> failwith "Malformed graph file") |> 
				Str.split (Str.regexp ",") |> collect_edges node e  in 
			read_file input (v', e') in 
	Arg.parse options (fun f -> file := f) "Give graph and graph type";
	let infile = open_in !file in 
	let g = read_file infile ([],[]) in 
	close_in infile; 
	g

let _ = 
	if !Sys.interactive then () else
	let v, e = read_input () in
	let (module G) = 
		if !graph_type = "matrix" then (module MatrixGraph : Graph) else
		if !graph_type = "array" then (module ArrayGraph : Graph) else
		if !graph_type = "naive" then (module NaiveGraph : Graph) else
		failwith "improper graph type" in
	let (module S) = 
		if !search_type = "bfs" then 
			(module BFS (G) : PathSearch with type path = G.edge list and type graph = G.graph) 
		else if !search_type = "dfs" then 
			(module DFS (G) : PathSearch with type path = G.edge list and type graph = G.graph)
		else failwith "improper search type" in
	let (module N) = (module FlowNetworkMaker (G) (S) : FlowNetwork with type graph = G.graph) in
	let g = N.make_graph (List.rev v) e in 
	let tim = Sys.time () in
	N.max_flow g |> N.flow_capacity g |> Printf.printf "Max Flow Capacity: %d\n";
	Printf.printf "Compute time: %f\n" (Sys.time () -. tim)