import React, { useState, useEffect } from 'react';
import PageHeader from '../components/PageHeader';
import SongList from '../components/SongList';

const ChartContainer = () => {
    const [songs, setSongs] = useState([]);

    useEffect(() => {
        getSongs();
    }, [])

    const getSongs = function () {
        fetch('https://itunes.apple.com/gb/rss/topsongs/limit=20/json')
            .then(res => res.json())
            .then(songs => setSongs(songs.feed.entry))
    }

    return (
        <div>
            <PageHeader title="UK Top 20 Songs" />    
            <SongList songs={songs}/>
        </div>
    );
}

export default ChartContainer;