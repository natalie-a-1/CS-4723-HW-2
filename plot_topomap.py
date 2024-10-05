import numpy as np
import matplotlib.pyplot as plt
import mne

def plot_alpha_band_topomap(subjects, alpha_band=(8, 12)):
    """
    Plots the alpha band (8-12 Hz) PSD topomap for each subject and condition.

    Parameters:
    - subjects: List of tuples containing subject title and raw data.
    - alpha_band: Tuple defining the frequency range for the alpha band.
    """
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))  # 2x2 grid for 4 plots

    # Loop through each subject and condition
    for i, (title, raw) in enumerate(subjects):
        # Compute average PSD for each condition
        psd, freqs = raw.compute_psd(method='welch', fmin=alpha_band[0], fmax=alpha_band[1], n_fft=2048).get_data(return_freqs=True)

        # Average the PSD across the frequency range for the alpha band
        alpha_psd = np.mean(psd[:, (freqs >= alpha_band[0]) & (freqs <= alpha_band[1])], axis=1)

        # Determine subplot position
        row, col = divmod(i, 2)

        # Create topomap
        im, cn = mne.viz.plot_topomap(alpha_psd, raw.info, axes=axes[row, col], show=False, contours=8, cmap='viridis')
        axes[row, col].set_title(f'Alpha Band (8-12 Hz) PSD Topomap - {title}', fontsize=14)
        axes[row, col].grid(True)

    # Add color bar
    cbar_ax = fig.add_axes([0.92, 0.15, 0.02, 0.7])
    fig.colorbar(im, cax=cbar_ax, orientation='vertical', label='Power (dB)')

    plt.tight_layout(rect=[0, 0, 0.9, 1])
    plt.show()