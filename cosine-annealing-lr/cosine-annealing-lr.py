import math

def cosine_annealing_schedule(base_lr: float, min_lr: float, total_steps: int, current_step: int) -> float:
    """
    Returns the cosine-annealed learning rate for the requested step.
    """
    lr=min_lr+(base_lr-min_lr)/2*(1+math.cos(math.pi*current_step/total_steps))
    return float(lr)
    pass