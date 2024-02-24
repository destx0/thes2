def find_closest_clusters_test(cluster_list, broken_mst):
    cluster_connected = copy.deepcopy(broken_mst)
    curr = cluster_list[0]
    visited_id = set(curr[0])
    no_of_clusters = len(cluster_list)
    cluster_dict = {id : vals for }

    for _ in range(no_of_clusters) : 
        for cluster in cluster_list:
            if cluster[0] in visited_id:
                continue
            min_dis, close_point, close_point2 = dis_btw_clusters(curr[1], cluster[1])


    