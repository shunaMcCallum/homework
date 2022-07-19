import React from 'react'

const PageHeader = ({title, handleSelectChange, genres}) => {
    return (
        <div>
        <h1>{title}</h1>
        <select onChange={handleSelectChange}>
            {genres.map(genre => {
          return <option key={genre.name} value={genre.url}>{genre.name}</option>
            })}
            </select>
        </div>
    );
}

export default PageHeader;