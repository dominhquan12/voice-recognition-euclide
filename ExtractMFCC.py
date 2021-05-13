import os
import librosa
import numpy as np

#hàm trích rút đặc trưng của 1 file âm thanh
def get_features(file_name):

    # tín hiệu + tỉ lệ mẫu
    X, sample_rate = librosa.load(file_name, sr=None)

    # mfcc
    mfccs = librosa.feature.mfcc(y=X, n_mfcc=13, sr=sample_rate)
    # mfcc delta
    delta_mfccs = librosa.feature.delta(mfccs)
    # mfcc double delta
    delta2_mfccs = librosa.feature.delta(mfccs, order=2)

    # Nối thành mảng mfccs, delta_mfccs, double_delta_mfccs
    comprehensive_mfccs = np.concatenate((mfccs, delta_mfccs, delta2_mfccs))

    # Lấy 1 mảng trung bình cho 1 file âm thanh
    mfccs_scaled = np.mean(comprehensive_mfccs.T,axis=0)
    return mfccs_scaled

    
