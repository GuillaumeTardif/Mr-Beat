from audiostream import get_output

from audio_source_mixer import AudioSourceMixer
from audio_source_one_shot import AudioSourceOneShot
from audio_source_track import AudioSourceTrack


class AudioEngine:
    NB_CHANNELS = 1
    SAMPLE_RATE = 44100
    BUFFER_SIZE = 1024

    def __init__(self):
        self.outputstream = get_output(channels=self.NB_CHANNELS,
                                       rate=self.SAMPLE_RATE,
                                       buffersize=self.BUFFER_SIZE)
        self.audio_source_one_shot = AudioSourceOneShot(self.outputstream)
        self.audio_source_one_shot.start()

    def play_sound(self, wav_samples):
        self.audio_source_one_shot.set_wav_samples(wav_samples)

    def create_track(self, wav_samples, bpm):
        source_track = AudioSourceTrack(self.outputstream, wav_samples, bpm, self.SAMPLE_RATE)
        # source_track.set_steps((0, 0, 0, 0))
        source_track.start()
        return source_track

    def create_mixer(self, all_waves_samples, bpm, nb_steps, on_current_step_changed, min_bpm):
        source_mixer = AudioSourceMixer(self.outputstream, all_waves_samples, bpm, self.SAMPLE_RATE, nb_steps, on_current_step_changed, min_bpm)
        source_mixer.start()
        return source_mixer
        # créer le mixer
        # starter
        # return


