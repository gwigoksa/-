import streamlit as st
import networkx as nx

def is_eulerian_path_possible(graph):
    odd_degree_nodes = [node for node in graph.nodes if graph.degree[node] % 2 != 0]
    return len(odd_degree_nodes) in [0, 2], odd_degree_nodes

def find_eulerian_path(graph):
    try:
        path = list(nx.eulerian_path(graph))
        return path
    except nx.NetworkXError as e:
        return None

def main():
    st.title("한붓그리기 경로 찾기 프로그램")
    st.write("노드와 간선을 입력하면 한붓그리기 경로(Eulerian Path)를 계산합니다.")

    # 사용자 입력
    num_nodes = st.number_input("노드 개수 입력", min_value=1, step=1, value=4)
    edges = st.text_area("간선 입력 (예: 1,2 2,3 3,4 4,1)", value="1,2 2,3 3,4 4,1")

    if st.button("한붓그리기 경로 찾기"):
        try:
            # 그래프 생성
            graph = nx.Graph()
            graph.add_nodes_from(range(1, num_nodes + 1))

            # 간선 추가
            edge_list = [tuple(map(int, edge.split(','))) for edge in edges.split()]
            graph.add_edges_from(edge_list)

            # 한붓그리기 가능성 확인
            is_possible, odd_degree_nodes = is_eulerian_path_possible(graph)
            if not is_possible:
                st.error("한붓그리기 경로를 만들 수 없습니다.")
                st.write(f"홀수 차수의 노드: {odd_degree_nodes}")
            else:
                st.success("한붓그리기 경로를 만들 수 있습니다.")
                path = find_eulerian_path(graph)
                if path:
                    st.write("한붓그리기 경로:", " → ".join([f"{u}-{v}" for u, v in path]))
                else:
                    st.error("한붓그리기 경로를 계산하는 데 실패했습니다.")

            # 그래프 시각화
            st.write("입력한 그래프 시각화:")
            pos = nx.spring_layout(graph)
            nx.draw(graph, pos, with_labels=True, node_color="lightblue", node_size=500, edge_color="gray")
            st.pyplot()

        except Exception as e:
            st.error(f"입력 오류: {e}")

if __name__ == "__main__":
    main()