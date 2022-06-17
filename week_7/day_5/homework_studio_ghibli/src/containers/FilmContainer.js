import React, { useState, useEffect } from 'react';
import FilmSelect from '../components/FilmSelect';
import FilmDetails from '../components/FilmDetails';
import './FilmContainer.css';


const FilmContainer = () => {

    const [films, setFilms] = useState([]);
    const [people, setPeople] = useState([])
    const [selectedFilm, setSelectedFilm] = useState(null);

    useEffect(() => {
        fetch('https://ghibliapi.herokuapp.com/films')
            .then(res => res.json())
            .then(data => setFilms(data));
    }, [])

    const handleFilmSelect = (film) => {
        setSelectedFilm(film);
    }

    // useEffect(() => {
    //     fetch(url)
    //         .then(res => res.json())
    //         .then(data => setSelectedFilm(data));
    //         .then(() => {
    //             const allPeoplePromises = [];
    //             for (const personUrl of film.people) {
    //                 allPeoplePromises.push(fetch(personUrl))
    //             }

    //             Promise.all(allPeoplePromises)
    //             .then(res => res.json())
    //             .then(data => console.log(data))
    //         })
    // }, [])

    return (
        <div className="film-box">
            <header className="page-header">
                <img id="header-image" src="https://www.pngitem.com/pimgs/m/83-834494_studio-ghibli-logo-vector-hd-png-download.png"></img>
                <h1 id="header-text">Studio Ghibli Films</h1>
            </header>
            <FilmSelect films={films} onFilmSelect={handleFilmSelect} />
            <div>
                {selectedFilm ? <FilmDetails film={selectedFilm} /> : null}
            </div>
        </div>
    );
}

export default FilmContainer;