import React, { useState, useEffect } from 'react';
import PageHeader from '../components/PageHeader';
import SongList from '../components/SongList';
// import DropDown from '../components/DropDown';

const ChartContainer = ({genres}) => {
    const [songs, setSongs] = useState([]);

    useEffect(() => {
        getSongs(categories[0].url)
    }, [genres])

    const getSongs = function (url) {
        fetch(url)
            .then(res => res.json())
            .then(songs => setSongs(songs.feed.entry))
    };

    const handleSelectChange = event => {
        getSongs(event.target.value);
    }

    return (
        <div>
            <PageHeader title="UK Top 20 Songs" handleSelectChange={handleSelectChange} genres={genres} />
            {/* <DropDown categories={categories} onCategorySelect={onCategorySelect} /> */}
            {currentCategory ? <SongList songs={songs} url={genres[0].url} handleSelectChange={handleSelectChange} /> : null}
        </div>
    );
}

export default ChartContainer;