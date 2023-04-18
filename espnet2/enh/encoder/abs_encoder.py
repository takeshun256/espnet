from abc import ABC, abstractmethod
from typing import Tuple

import torch


class AbsEncoder(torch.nn.Module, ABC):
    @abstractmethod
    def forward(
        self,
        input: torch.Tensor,
        ilens: torch.Tensor,
    ) -> Tuple[torch.Tensor, torch.Tensor]:
        raise NotImplementedError

    @property
    @abstractmethod
    def output_dim(self) -> int:
        raise NotImplementedError

    @property
    def frame_size(self) -> int:
        raise NotImplementedError

    @property
    def hop_size(self) -> int:
        raise NotImplementedError

    def forward_streaming(self, input: torch.Tensor):
        raise NotImplementedError
