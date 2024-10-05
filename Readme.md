# EEG Data Analysis Project

## Overview
This project involves the analysis of EEG data from two subjects (Subject 06 and Subject 07) under two different conditions: baseline and task. The data was collected using 16 EEG channels and 1 ECG channel, recorded from two separate .edf files for each subject.

## Data Cleaning
The data was cleaned by renaming the channels to standard 10-20 system and setting the ECG channel type to 'ecg'.

## Data Analysis
The data was analyzed by computing the average power spectral density (PSD) for each condition and plotting the alpha band (8-12 Hz) PSD topomap for each subject and condition.

## Results
The results are stored in the `analysis` folder.