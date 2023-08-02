# source: https://gist.github.com/bossjones/d8363d03ac83780b9c70

brew install portaudio portmidi libsndfile liblo jack

brew link portaudio portmidi libsndfile liblo

cd ~/Sites/tmp

svn checkout http://pyo.googlecode.com/svn/trunk/ pyo-read-only

cd pyo-read-only

python setup.py install --use-coreaudio --use-jack --use-double

cd ../

sudo rm -r pyo-read-only