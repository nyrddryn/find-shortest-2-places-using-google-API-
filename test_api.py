import googlemaps
from queue import PriorityQueue
import lo2cord
# Khai báo API key của Google Maps
api_key = 'AIzaSyD33vGmY4G4vlB1m4HNCcWPQ1uMGSZd3QI'

# Khởi tạo client của Google Maps
gmaps = googlemaps.Client(key=api_key)

# Tính toán khoảng cách giữa hai điểm trên bản đồ
def distance(point1, point2):
    result = gmaps.distance_matrix(point1, point2, mode='walking')
    return result['rows'][0]['elements'][0]['distance']['value']

# Tìm đường đi giữa hai điểm trên bản đồ bằng giải thuật A*
def find_path(start, end):
    # Khởi tạo hàng đợi ưu tiên và tập đỉnh đã duyệt
    queue = PriorityQueue()
    visited = set()

    # Khởi tạo đỉnh bắt đầu và đặt nó vào hàng đợi ưu tiên
    start_node = (start, 0, distance(start, end), None)
    queue.put(start_node)

    # Duyệt các đỉnh trong hàng đợi     while not queue.empty():
        # Lấy đỉnh có giá trị f nhỏ nhất từ hàng đợi ưu tiên
    current_node = queue.get()

        # Nếu đỉnh đó là điểm kết thúc, ta đã tìm được đường đi tối ưu
    if current_node[0] == end:
        path = []
        while current_node is not None:
            path.append(current_node[0])
            current_node = current_node[3]
        return path[::-1]

        # Nếu đỉnh đó chưa được duyệt, ta duyệt các đỉnh kề với nó
    if current_node[0] not in visited:
        visited.add(current_node[0])
        location = lo2cord.geocode(current_node[0])
        # print(location)
        neighbors = gmaps.places_nearby(location, radius=500, type='point_of_interest')
        for neighbor in neighbors['results']:
            neighbor_node = (neighbor['geometry']['location'], current_node[1] + distance(current_node[0], neighbor['geometry']['location']), distance(neighbor['geometry']['location'], end), current_node)
            print(neighbor_node[0])
            queue.put(neighbor_node)
        

    # Nếu không tìm thấy đường đi, trả về None
    return None

# Tìm đường đi giữa hai điểm trên bản đồ
start = 'ThanhXuân, Hà Đông, Hà Nội'
end = 'Bách Khoa, Hai Bà Trưng, Hà Nội'
path = find_path(start, end)
print(path)