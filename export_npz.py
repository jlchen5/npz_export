
import numpy as np
data = np.load('/results.npz')
data.files
matrix = data['matrix']
labels = data['labels']
matrix
