import React from 'react';

const FilmBoxHeader = ({title}) => {

    return (
        <>
            <h3 className="filmBoxHeader">{title}</h3>
            <div style={{ borderTop: "1px solid #c8c8c8", marginLeft: -27, marginRight: 10 }}></div>
        </>
    );

};

export default FilmBoxHeader;