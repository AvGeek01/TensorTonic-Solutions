import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if not seqs:
        return np.array([])
    if max_len is None:
        max_len=max(len(seq) for seq in seqs)
    padded=[]
    for seq in seqs:
        if len(seq)>max_len:
            seq=seq[:max_len]
        pad_len=max_len-len(seq)
        new_seq=seq+[pad_value]*pad_len
        padded.append(new_seq)
    return np.array(padded)
    pass