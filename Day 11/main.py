from input import puzzleinput
#from testinput import puzzleinput
import networkx as nx
import rustworkx as rx

#will require rework to access question part 1
question_part = 2

def input_to_graph(puzzleinput: str):
    str_list = puzzleinput.splitlines()
    node_list = []
    for str in str_list:
        name, connects_to = str.split(":") 
        edge_list = connects_to.split()
        G.add_node(name)
        for edge in edge_list:
            G.add_edge(name, edge)

G = nx.DiGraph(multigraph=False)
G.add_node("out")
input_to_graph(puzzleinput)
gnode_list = list(G.nodes)


#creating subgraphs to search in segments SVR -> FFT, FFT -> DAC, DAC - > OUT
svrfft_list = []
for node in gnode_list:
    try: 
        a = nx.shortest_path(G, "svr", node)
        b = nx.shortest_path(G, node, "fft")
        if a and b:
            svrfft_list.append(node)
    except:
        continue
fftdac_list = []
for node in gnode_list:
    try: 
        a = nx.shortest_path(G, "fft", node)
        b = nx.shortest_path(G, node, "dac")
        if a and b:
            fftdac_list.append(node)
    except:
        continue
dacout_list = []
for node in gnode_list:
    try: 
        a = nx.shortest_path(G, "dac", node)
        b = nx.shortest_path(G, node, "out")
        if a and b:
            dacout_list.append(node)
    except:
        continue
  
#subgraph
S1 = nx.subgraph(G, svrfft_list)
S2 = nx.subgraph(G, fftdac_list)
S3 = nx.subgraph(G, dacout_list)


#convert to rustworkx for faster processing
S1_rx: rx.PyDiGraph = rx.networkx_converter(S1, keep_attributes=True) # type: ignore
S2_rx: rx.PyDiGraph= rx.networkx_converter(S2, keep_attributes=True) # type: ignore
S3_rx: rx.PyDiGraph= rx.networkx_converter(S3, keep_attributes=True) # type: ignore

#using generations to find index of starting nodes (SVR, FFT2, DAC2) and ending nodes (FFT, DAC, OUT)
S1_gens = rx.topological_generations(S1_rx)
S2_gens = rx.topological_generations(S2_rx)
S3_gens = rx.topological_generations(S3_rx)

svr = S1_gens[0][0]
fft = S1_gens[-1][0]
fft2 = S2_gens[0][0]
dac = S2_gens[-1][0]
dac2 = S3_gens[0][0]
out = S3_gens[-1][0]


#Running all simple path calcs
svr_fft_paths = list(rx.all_simple_paths(S1_rx, svr, fft)) #10
print("SVR -> FFT paths: ", len(svr_fft_paths))
fft_dac_paths = list(rx.all_simple_paths(S2_rx, fft2, dac)) #17
print("FFT -> DAC paths: ",len(fft_dac_paths))
dac_out_paths = list(rx.all_simple_paths(S3_rx, dac2, out)) #9
print("DAC -> OUT paths: ",len(dac_out_paths))

svr_out_paths = len(svr_fft_paths) * len(fft_dac_paths) * len(dac_out_paths)

print ("SVR -> FFT -> DAC -> OUT paths: ", svr_out_paths)
