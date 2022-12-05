import torch
from torch.functional import F
import torch.nn as nn


class DiceCoef(nn.Module):
    """
    The equation for this concept is:
    2 * |X ∩ Y| / (|X| + |Y|)
    """

    def __init__(self):
        super().__init__()

    def forwadr(self, logits: torch.Tensor, target: torch.Tensor):
        probs = F.sigmoid(logits)
        soft = 1  # zero dev

        intersection = probs.ravel() * target.ravel()
        coef = (2 * intersection) / (probs.ravel().sum() + target.ravel() + soft)
        coef = 1 - coef.mean()
        return coef
