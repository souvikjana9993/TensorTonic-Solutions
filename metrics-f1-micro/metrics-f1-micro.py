import numpy as np
def f1_micro(y_true, y_pred) -> float:
    """
    Compute micro-averaged F1 for multi-class integer labels.
    """
    y_true = np.array(y_true)
    y_pred = np.array(y_pred)
    tp = int(np.sum(np.where(y_true == y_pred,1,0)))
    mis = int(np.sum(np.where(y_true != y_pred,1,0)))
    fp = mis
    fn = mis

    return 2*tp/(2*tp +fp+fn)