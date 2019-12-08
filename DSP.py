# EC601 Mini Project 3 -- DSP visualization
# Fengxu Tu fengxutu@bu.edu


import numpy as np
import librosa
import librosa.display
from scipy.io import wavfile
from scipy.fftpack import fft, ifft
import wave
import matplotlib.pyplot as plt


def visualization(filename):
  WAVE = wave.open(filename)
  x, sr = librosa.load(filename)
  X = librosa.stft(x)
  Xdb = librosa.amplitude_to_db(abs(X))
  plt.figure(figsize=(14, 5))
  librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
  plt.colorbar()
  plt.show()
  # for item in enumerate(WAVE.getparams()):
  #     print(item)
  # a = WAVE.getparams().nframes
  # f = WAVE.getparams().framerate
  # sample_time = 1 / f
  # time = a / f
  # sample_frequency, audio_sequence = wavfile.read(filename)
  # print(audio_sequence)
  # x_seq = np.arange(0, time, sample_time)
  # y_seq = abs(fft(audio_sequence))
  # plt.subplot(221)
  # plt.plot(x_seq, audio_sequence, 'blue')
  # plt.xlabel("time (s)")
  # plt.ylabel("amplitude")
  # plt.title("Time domain signal")
  # plt.subplot(222)
  # plt.plot(y_seq, abs(audio_sequence), 'red')
  # plt.xlabel("frequency (Hz)")
  # plt.title("Frequency domain signal")
  # plt.show()

if __name__ == '__main__':
  file_music = 'Canon.wav'
  visualization(file_music)

  file_ring = 'Ring.wav'
  visualization(file_ring)
