import matplotlib.pyplot as plt
from mne.time_frequency import tfr_multitaper

def plot_spectrogram(subjects, freqs, n_cycles, time_bandwidth):
    fig, axes = plt.subplots(len(subjects), 1, figsize=(15, 20))  # Adjusted to number of subplots

    # Compute and plot spectrograms for each subject
    for i, (title, raw) in enumerate(subjects):
        power = tfr_multitaper(raw, freqs=freqs, n_cycles=n_cycles,
                               time_bandwidth=time_bandwidth, return_itc=False)
        power.plot([0], baseline=(None, 0), mode='logratio', axes=axes[i], show=False)
        axes[i].set_title(f'Spectrogram - {title}', fontsize=14)  # Set title for each subplot

    # Adjust layout to avoid overlap and ensure titles and axes are visible
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.subplots_adjust(hspace=0.5)
    plt.show()