import mne
import os
import numpy as np
import matplotlib.pyplot as plt
from plot_topomap import plot_alpha_band_topomap

# Load subject 06 edf files
subject_06_baseline = mne.io.read_raw_edf(os.path.join("data", "Subject06_1.edf"), preload=True)
subject_06_task = mne.io.read_raw_edf(os.path.join("data", "Subject06_2.edf"), preload=True)

# Load subject 07 edf files
subject_07_baseline = mne.io.read_raw_edf(os.path.join("data", "Subject07_1.edf"), preload=True)
subject_07_task = mne.io.read_raw_edf(os.path.join("data", "Subject07_2.edf"), preload=True)

# Clean up channels
raw_data = [subject_06_baseline, subject_06_task, subject_07_baseline, subject_07_task]
for raw in raw_data:
    raw.rename_channels({
        'EEG Fp1': 'Fp1', 'EEG Fp2': 'Fp2', 'EEG F3': 'F3', 'EEG F4': 'F4', 
        'EEG F7': 'F7', 'EEG F8': 'F8', 'EEG T3': 'T3', 'EEG T4': 'T4', 
        'EEG C3': 'C3', 'EEG C4': 'C4', 'EEG T5': 'T5', 'EEG T6': 'T6',
        'EEG P3': 'P3', 'EEG P4': 'P4', 'EEG O1': 'O1', 'EEG O2': 'O2',
        'EEG Fz': 'Fz', 'EEG Cz': 'Cz', 'EEG Pz': 'Pz', 'EEG A2-A1': 'A2', 
        'ECG ECG': 'ECG'
    })
    raw.set_channel_types({'ECG': 'ecg'})

    # Set the montage for the channel locations
    montage = mne.channels.make_standard_montage('standard_1020')
    raw.set_montage(montage)

# Define frequency range for alpha band
alpha_band = (8, 12)

# List of subjects and their corresponding data
subjects = [
    ('Subject 06 Baseline', subject_06_baseline),
    ('Subject 06 Task', subject_06_task),
    ('Subject 07 Baseline', subject_07_baseline),
    ('Subject 07 Task', subject_07_task)
]