import numpy as np
import csv
import math

class Searcher:
    def __init__(self, indexPath):
        # lưu trữ đường dẫn chỉ mục 
        self.indexPath = indexPath

    def search(self, queryFeatures, limit=10):
        # khởi tạo từ điển kết quả 
        results = {}
        # mở tệp chỉ mục để đọc
        with open(self.indexPath) as f:
            # khởi tạo trình đọc CSV
            reader = csv.reader(f)
            # lặp qua các hàng trong chỉ mục
            for row in reader:
                # phân tích cú pháp ID hình ảnh và các tính năng, 
                # sau đó tính toán khoảng cách euclide giữa các tính năng trong chỉ mục  
                # và các tính năng truy vấn
                features = [float(x) for x in row[1:]]
                d = self.euclide_distance(features, queryFeatures)
                # có khoảng cách giữa hai vectơ đặc trưng,
                # cập nhật từ điển kết quả - khóa là ID hình ảnh hiện tại trong chỉ mục 
                # và giá trị là khoảng cách vừa tính toán, 
                # thể hiện mức độ 'tương tự' của âm thanh trong chỉ mục là truy vấn
                results[row[0]] = d
            # đóng file
            f.close()
        # sắp xếp kết quả để khoảng cách nhỏ hơn 
        # (tức là các âm thanh có liên quan hơn nằm ở đầu danh sách)
        results = sorted([(v, k) for (k, v) in results.items()])
        # trả lại kết quả (có giới hạn)
        return results[:limit]

    # function euclide distance
    def euclide_distance(self, pointA, pointB):
        distance = math.sqrt(sum([(a - b) ** 2 for a, b in zip(pointA, pointB)]))
        return distance
