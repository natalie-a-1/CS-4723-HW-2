import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt

def bandpass_filter(data, sfreq, low_freq, high_freq):
    nyquist = 0.5 * sfreq
    low = low_freq / nyquist
    high = high_freq / nyquist
    b, a = butter(N=4, Wn=[low, high], btype='band')
    return filtfilt(b, a, data)

def plot_alpha_band(subjects):
    # Create a figure with subplots for each condition
    fig, axes = plt.subplots(len(subjects), 1, figsize=(15, 20))

    # Loop through each subject and condition
    for i, (title, raw) in enumerate(subjects):
        # Get data and sampling frequency
        sfreq = raw.info['sfreq']  # Sampling frequency
        data, _ = raw[:]

        # Apply bandpass filter to extract the alpha band (8-12 Hz)
        alpha_data = bandpass_filter(data[0], sfreq, 8, 12)

        # Define a time vector for plotting (using the first 10 seconds)
        time = np.arange(len(alpha_data)) / sfreq

        # Use a subset to make the plot clearer (e.g., first 10 seconds)
        time_subset = time[:int(10 * sfreq)]
        alpha_data_subset = alpha_data[:int(10 * sfreq)]

        # Plot the time domain signal for Alpha band
        axes[i].plot(time_subset, alpha_data_subset, color='blue' if 'Baseline' in title else 'green')
        axes[i].set_title(f'Alpha Band Signal (8-12 Hz) - {title}', fontsize=14)
        axes[i].set_xlabel('Time (s)', fontsize=10)
        axes[i].set_ylabel('Amplitude (µV)', fontsize=10)
        axes[i].grid(True)

    # Adjust layout to avoid overlap and ensure titles and axes are visible
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.subplots_adjust(hspace=0.7)
    plt.show()