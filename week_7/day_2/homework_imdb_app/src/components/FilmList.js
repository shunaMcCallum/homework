import React, { useState } from 'react';
import Film from './Film.js';

const FilmList = ({films}) => {
    
    const filmNodes = films.map((film) => {
        return (
            <Film film={film} key={film.id} />
        );
    });

    return (
        <>
            <div className="filmList">{filmNodes}</div>
            <div className="line" style={{ borderTop: "1px solid #c8c8c8", marginLeft: -27, marginRight: 10 }}></div>
        </>

    );

};

export default FilmList;