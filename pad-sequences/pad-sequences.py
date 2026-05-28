import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    seqs = np.asarray(seqs, dtype=object)
    max_row = len(seqs)
    if max_row == 0:
        return np.empty((0, max_len or 0))
        
    if max_len is not None:
        max_col = max_len
    else:
        max_col = 0
        for seq in seqs:
            if len(seq) > max_col:
                max_col = len(seq)
                
    result = np.full((max_row, max_col), pad_value)

    for i, seq in enumerate(seqs):
        end_idx = min(len(seq), max_col)
        result[i, :end_idx] = seq[:end_idx]
    return result