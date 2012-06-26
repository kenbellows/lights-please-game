class Action:
    def __init__(self, id, num_steps, step_duration=5):
        self.id = id
        self.num_steps = num_steps
        self.curr_step = -1
        self.step_duration = step_duration
    
    def next(self):
        self.curr_step = (self.curr_step + 1) % (self.num_steps * self.step_duration)
        return int(self.curr_step/self.step_duration)
    
    def reset(self):
        self.curr_step = -1
