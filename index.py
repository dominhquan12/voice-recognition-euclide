import ExtractMFCC
# phân tích cú pháp các đối số dòng lệnh
import argparse
# lấy đường dẫn âm thanh
import glob

# Tạo trình phân tích cú pháp đối số để phân tích cú pháp các đối số
ap = argparse.ArgumentParser()

# Chuyển sang đường dẫn đến thư mục ảnh
ap.add_argument("-d","--dataset", required = True , help = "Path to directory that contains images")
ap.add_argument("-i","--index", required = True , help = "Path to where the index will be stored")
args = vars(ap.parse_args())

# mở file để ghi
output = open(args["index"], "w")

# sử dụng glob để lấy các đường dẫn âm thanh và lặp lại chúng
for audioPath in glob.glob(args["dataset"] + "/*.wav"):
	# trích xuất ID âm thanh (tức là tên tệp duy nhất) từ âm thanh
	# đường dẫn và tải âm thanh của chính nó
	audioID = audioPath[audioPath.rfind("\\") + 1:]
	# trích rút đặc trưng
	features = ExtractMFCC.get_features(audioPath)
	# ghi đặc trưng vào file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (audioID, ",".join(features)))
# đóng file
output.close()

# input
# python index.py -d dataset -i index.csv