import React, { useState, useEffect } from 'react';
import PageHeader from '../components/PageHeader';
import SongList from '../components/SongList';
import DropDown from '../components/DropDown';

const ChartContainer = () => {
    const [songs, setSongs] = useState([]);
    const [categories, setCategories] = useState([
        { name: "All", url: "https://itunes.apple.com/gb/rss/topsongs/limit=20/json" },
        { name: "Rock", url: "https://itunes.apple.com/gb/rss/topsongs/limit=20/genre=21/json" },
        { name: "Dance", url: "https://itunes.apple.com/gb/rss/topsongs/limit=20/genre=17/json" },
        { name: "Country", url: "https://itunes.apple.com/gb/rss/topsongs/limit=20/genre=6/json" }
    ]);
    const [currentCategory, setCurrentCategory] = useState(null);

    // useEffect(() => {
    //     getSongs();
    // }, [])

    const getSongs = function () {
        fetch(currentCategory.url)
            .then(res => res.json())
            .then(songs => setSongs(songs.feed.entry))
    };


    const onCategorySelect = ((category) => {
        setCurrentCategory(category);
        getSongs();
    })

    return (
        <div>
            <PageHeader title="UK Top 20 Songs" />
            <DropDown categories={categories} onCategorySelect={onCategorySelect} />
            {currentCategory ? <SongList songs={songs} /> : null}
        </div>
    );
}

export default ChartContainer;