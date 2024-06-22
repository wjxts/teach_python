data.x [num_nodes, node_feature_dim]
data.edge [num_edges, 2] # directed edges 
data.edge_feature [num_edges, edge_feature_dim]

to apply feature aggregation H'=AH, where A is adjacent / affinity matrix, H is node feature, H = [h_1, h_2, ..., h_n]^T
we use ** torch.index **
