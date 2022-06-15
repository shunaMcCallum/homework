import React from 'react'

function Song({song}) {
    return (
        <li>{song["im:name"]["label"]} - {song["im:artist"]["label"]} </li>
    );
}

export default Song;