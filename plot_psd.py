import matplotlib.pyplot as plt

def plot_psd(raw_data, titles):
    fig, axes = plt.subplots(len(raw_data), 1, figsize=(15, 24))  # Adjusted to number of subplots

    for i, raw in enumerate(raw_data):
        raw.plot_psd(fmin=1, fmax=40, ax=axes[i], show=False)
        axes[i].set_title(titles[i], fontsize=14)
        axes[i].set_xlabel('Frequency (Hz)', fontsize=10)
        axes[i].set_ylabel('Power (dB µV²/Hz)', fontsize=10)
        axes[i].axvspan(0.5, 4, color='lightgray', alpha=0.3, label='Delta Band (0.5-4 Hz)')
        axes[i].axvspan(4, 8, color='orange', alpha=0.3, label='Theta Band (4-8 Hz)')
        axes[i].axvspan(8, 13, color='lightblue', alpha=0.3, label='Alpha Band (8-13 Hz)')
        axes[i].axvspan(13, 30, color='lightgreen', alpha=0.3, label='Beta Band (13-30 Hz)')
        axes[i].legend(loc='lower left')
        axes[i].grid(True)

    # Adjust layout to avoid overlap and ensure titles and axes are visible
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.subplots_adjust(hspace=0.5)
    plt.show()