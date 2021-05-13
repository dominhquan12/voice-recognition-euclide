import ExtractMFCC
from searcher import Searcher
import argparse

# xây dựng trình phân tích cú pháp đối số và phân tích cú pháp đối số
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-q", "--query", required = True,
	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

# tải âm thanh truy vấn và mô tả nó
query = args["query"]
features = ExtractMFCC.get_features(query)

# thực hiện tìm kiếm
searcher = Searcher(args["index"])
results = searcher.search(features)

# hiển thị truy vấn
print("file âm thanh truy vấn:")
print(query)

# lặp lại các kết quả
print("file âm thanh nhận được:")
for (score, resultID) in results:
	# tải âm thanh kết quả và hiển thị nó
	result = args["result_path"] + "/" + resultID
	print(result)

# input
# python search.py -i index.csv -q dataset\"child (1).wav" -r dataset
# python search.py -i index.csv -q filetest\"child (36).wav" -r dataset