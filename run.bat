@echo off
(
    echo although this might look sketchy but believe me it isn't 
    set /p playlist=input playlist url:
    py ./spotify_dl/spotify_dl.py -l %playlist% -o ./songs 
)
