import os

#import pandas as pd
import torch
import torch.nn as nn
import torch.nn.functional as F

from sklearn.metrics import confusion_matrix, roc_curve, auc
from sklearn.metrics import f1_score
import numpy as np
from sklearn.metrics import roc_curve, auc, accuracy_score


def AUC (scores, targets):

    pred = np.reshape(scores, (-1))
    lab = np.reshape(targets, (-1))
    '''idx = np.where(lab != 0)
    pred = pred[idx]
    lab = lab[idx]'''
    fpr, tpr, thresholds = roc_curve(y_true=lab, y_score=pred, pos_label=1)
    roc_auc = auc(fpr, tpr)
    return roc_auc


def accuracy(scores, targets):
    pred = np.reshape(scores, (-1))
    lab = np.reshape(targets, (-1))
    return accuracy_score(lab, pred)


def balanced_acc(scores, targets):
    pred = np.reshape(scores, (-1))
    lab = np.reshape(targets, (-1))
    return balanced_acc(lab, pred)


def MAE(scores, targets):
    MAE = F.l1_loss(scores, targets)
    MAE = MAE.detach().item()
    return MAE


