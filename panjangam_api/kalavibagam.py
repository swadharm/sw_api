from nazhigai_calc import *
from time_convert import *



# start : daytime
# end : daytime
# vibagam: int
# no_vibagam : int

class kalavibagam:
    def __init__(self,start,end,vibagam,no_vibagam):
        self.start = start
        self.end = end
        self.no_vibagam = no_vibagam
        self.alavu = end - start
        self.vibagam = self.alavu/vibagam
        self.vibagam_tr = timedelta(seconds=self.vibagam.seconds) # time rounded
        no_v = self.no_vibagam-1
        self.start_time = self.start + self.vibagam_tr*no_v
        self.end_time = self.start_time + self.vibagam_tr
        return

