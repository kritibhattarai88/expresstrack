# Adjacency matrix for locations
# Adjacency matrix in dictionary format
adj_matrix = {
    "Kathmandu": {
        "Kathmandu": 0,
        "Pokhara": 200,
        "Biratnagar": 400,
        "Birgunj": 300,
        "Butwal": 300,
        "Nepalgunj": 500,
        "Dhangadhi": 800,
        "Itahari": 300,
        "Hetauda": 130,
        "Janakpur": 225,
        "Dharan": 110,
        "Tansen": 250,
        "Ghorahi": 275,
        "Lamjung": 130,
        "Besisahar": 225,
    },
    "Pokhara": {
        "Kathmandu": 200,
        "Pokhara": 0,
        "Biratnagar": 400,
        "Birgunj": 300,
        "Butwal": 150,
        "Nepalgunj": 500,
        "Dhangadhi": 800,
        "Itahari": 300,
        "Hetauda": 140,
        "Janakpur": 225,
        "Dharan": 140,
        "Tansen": 275,
        "Ghorahi": 300,
        "Lamjung": 150,
        "Besisahar": 225,
    },
    "Biratnagar": {
        "Kathmandu": 400,
        "Pokhara": 400,
        "Biratnagar": 0,
        "Birgunj": 200,
        "Butwal": 450,
        "Nepalgunj": 600,
        "Dhangadhi": 800,
        "Itahari": 100,
        "Hetauda": 400,
        "Janakpur": 700,
        "Dharan": 200,
        "Tansen": 600,
        "Ghorahi": 650,
        "Lamjung": 400,
        "Besisahar": 400,
    },
    "Birgunj": {
        "Kathmandu": 300,
        "Pokhara": 300,
        "Biratnagar": 200,
        "Birgunj": 0,
        "Butwal": 350,
        "Nepalgunj": 500,
        "Dhangadhi": 700,
        "Itahari": 200,
        "Hetauda": 350,
        "Janakpur": 650,
        "Dharan": 150,
        "Tansen": 450,
        "Ghorahi": 500,
        "Lamjung": 300,
        "Besisahar": 300,
    },
    "Butwal": {
        "Kathmandu": 300,
        "Pokhara": 150,
        "Biratnagar": 450,
        "Birgunj": 350,
        "Butwal": 0,
        "Nepalgunj": 400,
        "Dhangadhi": 700,
        "Itahari": 300,
        "Hetauda": 160,
        "Janakpur": 250,
        "Dharan": 200,
        "Tansen": 200,
        "Ghorahi": 250,
        "Lamjung": 150,
        "Besisahar": 200,
    },
    "Nepalgunj": {
        "Kathmandu": 500,
        "Pokhara": 500,
        "Biratnagar": 600,
        "Birgunj": 500,
        "Butwal": 400,
        "Nepalgunj": 0,
        "Dhangadhi": 300,
        "Itahari": 500,
        "Hetauda": 400,
        "Janakpur": 600,
        "Dharan": 450,
        "Tansen": 450,
        "Ghorahi": 300,
        "Lamjung": 500,
        "Besisahar": 500,
    },
    "Dhangadhi": {
        "Kathmandu": 800,
        "Pokhara": 800,
        "Biratnagar": 800,
        "Birgunj": 700,
        "Butwal": 700,
        "Nepalgunj": 300,
        "Dhangadhi": 0,
        "Itahari": 800,
        "Hetauda": 600,
        "Janakpur": 700,
        "Dharan": 700,
        "Tansen": 700,
        "Ghorahi": 200,
        "Lamjung": 800,
        "Besisahar": 800,
    },
    "Itahari": {
        "Kathmandu": 300,
        "Pokhara": 300,
        "Biratnagar": 100,
        "Birgunj": 200,
        "Butwal": 300,
        "Nepalgunj": 500,
        "Dhangadhi": 800,
        "Itahari": 0,
        "Hetauda": 300,
        "Janakpur": 500,
        "Dharan": 200,
        "Tansen": 300,
        "Ghorahi": 350,
        "Lamjung": 300,
        "Besisahar": 300,
    },
    "Hetauda": {
        "Kathmandu": 130,
        "Pokhara": 140,
        "Biratnagar": 400,
        "Birgunj": 350,
        "Butwal": 160,
        "Nepalgunj": 400,
        "Dhangadhi": 600,
        "Itahari": 300,
        "Hetauda": 0,
        "Janakpur": 300,
        "Dharan": 100,
        "Tansen": 180,
        "Ghorahi": 200,
        "Lamjung": 150,
        "Besisahar": 180,
    },
    "Janakpur": {
        "Kathmandu": 225,
        "Pokhara": 225,
        "Biratnagar": 700,
        "Birgunj": 650,
        "Butwal": 250,
        "Nepalgunj": 600,
        "Dhangadhi": 700,
        "Itahari": 500,
        "Hetauda": 300,
        "Janakpur": 0,
        "Dharan": 300,
        "Tansen": 250,
        "Ghorahi": 300,
        "Lamjung": 225,
        "Besisahar": 250,
    },
    "Dharan": {
        "Kathmandu": 110,
        "Pokhara": 140,
        "Biratnagar": 200,
        "Birgunj": 150,
        "Butwal": 200,
        "Nepalgunj": 450,
        "Dhangadhi": 700,
        "Itahari": 200,
        "Hetauda": 100,
        "Janakpur": 300,
        "Dharan": 0,
        "Tansen": 150,
        "Ghorahi": 200,
        "Lamjung": 150,
        "Besisahar": 150,
    },
    "Tansen": {
        "Kathmandu": 250,
        "Pokhara": 275,
        "Biratnagar": 600,
        "Birgunj": 450,
        "Butwal": 200,
        "Nepalgunj": 450,
        "Dhangadhi": 700,
        "Itahari": 300,
        "Hetauda": 180,
        "Janakpur": 250,
        "Dharan": 150,
        "Tansen": 0,
        "Ghorahi": 150,
        "Lamjung": 275,
        "Besisahar": 275,
    },
    "Ghorahi": {
        "Kathmandu": 275,
        "Pokhara": 300,
        "Biratnagar": 650,
        "Birgunj": 500,
        "Butwal": 250,
        "Nepalgunj": 300,
        "Dhangadhi": 200,
        "Itahari": 350,
        "Hetauda": 200,
        "Janakpur": 300,
        "Dharan": 200,
        "Tansen": 150,
        "Ghorahi": 0,
        "Lamjung": 275,
        "Besisahar": 275,
    },
    "Lamjung": {
        "Kathmandu": 130,
        "Pokhara": 150,
        "Biratnagar": 400,
        "Birgunj": 300,
        "Butwal": 150,
        "Nepalgunj": 500,
        "Dhangadhi": 800,
        "Itahari": 300,
        "Hetauda": 150,
        "Janakpur": 225,
        "Dharan": 150,
        "Tansen": 275,
        "Ghorahi": 275,
        "Lamjung": 0,
        "Besisahar": 150,
    },
    "Besisahar": {
        "Kathmandu": 225,
        "Pokhara": 225,
        "Biratnagar": 400,
        "Birgunj": 300,
        "Butwal": 200,
        "Nepalgunj": 500,
        "Dhangadhi": 800,
        "Itahari": 300,
        "Hetauda": 180,
        "Janakpur": 250,
        "Dharan": 150,
        "Tansen": 275,
        "Ghorahi": 275,
        "Lamjung": 150,
        "Besisahar": 0,
    }
}


def floyd_warshall():
    dist = dict(adj_matrix)  # Copy of adjacency matrix
    next_node = {i: {j: j for j in adj_matrix[i]} for i in adj_matrix}  # Store next nodes

    for k in adj_matrix:
        for i in adj_matrix:
            for j in adj_matrix[i]:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]

    return dist, next_node

def construct_path(next_node, start, end):
    if next_node[start][end] is None:
        return []
    path = [start]
    while start != end:
        start = next_node[start][end]
        path.append(start)
    return path