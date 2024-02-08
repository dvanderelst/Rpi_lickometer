class SeriesCounter:
    def __init__(self, max_zeros_in_series=0, max_series_length=float('inf')):
        self.max_zeros_in_series = max_zeros_in_series
        self.max_series_length = max_series_length
        self.count = 0
        self.in_series = False
        self.zeros_count = 0
        self.series_length = 0

    def feed_sample(self, sample):
        if sample == 1:
            if not self.in_series:
                self.in_series = True
                self.series_length = 1
                self.count += 1
            elif self.zeros_count > self.max_zeros_in_series or self.series_length >= self.max_series_length:
                self.in_series = True
                self.series_length = 1
                self.count += 1
            else:
                self.series_length += 1
        else:
            if self.in_series:
                self.zeros_count += 1
                if self.zeros_count > self.max_zeros_in_series:
                    self.in_series = False
                    self.zeros_count = 0
                    self.series_length = 0
            else:
                self.zeros_count = 0

    def get_series_count(self):
        return self.count

    def reset_count(self):
        self.count = 0


# # Example usage:
# counter = SeriesCounter(max_zeros_in_series=1, max_series_length=3)
# samples = [0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0]
#
# for sample in samples:
#     counter.feed_sample(sample)
#
# print("Number of continuous series of ones with at most 1 zero in between and maximum length of 3:",
#       counter.get_series_count())
#
# # Reset the count
# counter.reset_count()
#
