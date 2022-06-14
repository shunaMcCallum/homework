import React from 'react';

const Film = ({ film }) => {
  
    return (
        
        <li className="film"><a className="filmLink" href={film.url}>{film.name}</a></li>

    );

};

export default Film;