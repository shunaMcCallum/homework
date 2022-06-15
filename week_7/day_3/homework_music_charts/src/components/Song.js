import React from 'react'

function Song({song}) {
    return (
        <li>{song["im:name"]["label"]} - {song["im:artist"]["label"]} <img src={song["im:image"][1]["label"]}></img> </li>
    );
}

export default Song;