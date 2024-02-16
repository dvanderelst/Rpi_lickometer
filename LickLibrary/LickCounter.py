class LickCounter:
    def __init__(self, min_lick_length, max_lick_length, max_bout_gap, min_licks_per_bout):
        self.min_lick_length = min_lick_length
        self.max_lick_length = max_lick_length
        self.max_bout_gap = max_bout_gap
        self.lick_threshold = min_licks_per_bout
        self.lick_count = 0
        self.lick_length = 0
        self.zeros_count = 0
        self.bout_count = 0
        self.sample_history = []
        self.lick_count_history = []
        self.bout_count_history = []
        self.lick_length_history = []

    def process_samples(self, samples):
        for sample in samples:
            self.process_sample(sample)

    def process_sample(self, sample):
        if sample == 1:
            self.lick_length += 1
            self.zeros_count = 0
        else:
            self.zeros_count += 1
            if self.zeros_count > self.max_bout_gap:
                if self.lick_count >= self.lick_threshold:
                    self.bout_count += 1
                self.lick_count = 0
                self.lick_length = 0
            elif self.lick_length > self.max_lick_length:
                self.lick_length = 0  # Reset lick length if exceeds max length

        if sample == 0:
            if self.min_lick_length <= self.lick_length <= self.max_lick_length:
                self.lick_count += 1
            self.lick_length = 0

        self.sample_history.append(sample)
        self.lick_count_history.append(self.get_lick_count())
        self.bout_count_history.append(self.get_bout_count())
        self.lick_length_history.append(self.lick_length)

    def reset_bout_count(self):
        self.bout_count = 0

    def get_lick_count(self):
        return self.lick_count

    def get_bout_count(self):
        return self.bout_count

    def print_state(self):
        print("Number of licks:", self.get_lick_count())
        print("Number of bouts:", self.get_bout_count())
        print("Current lick length:", self.lick_length)

    def plot_history(self):
        import matplotlib.pyplot as plt

        fig, axs = plt.subplots(4, 1, sharex=True, figsize=(10, 8))

        axs[0].plot(self.sample_history, '.-', label='Sample')
        axs[0].legend()
        axs[0].set_ylabel('Sample')

        axs[1].plot(self.lick_length_history, '.-', color='red')
        axs[1].set_ylabel('Lick Length')

        axs[2].plot(self.lick_count_history, '.-', color='orange')
        axs[2].set_ylabel('Lick Count')

        axs[3].plot(self.bout_count_history, '.-', color='green')
        axs[3].set_ylabel('Bout Count')
        axs[3].set_xlabel('Time')

        plt.show()