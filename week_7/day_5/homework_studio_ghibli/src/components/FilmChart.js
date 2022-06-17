import React from 'react';
import { Chart } from 'react-google-charts';

const FilmChart = ({getFilmRatings, films}) => {

    const data = getFilmRatings(films)

    const options = {
        is3D: true,
        backgroundColor: "#f7f7f7",
        marginLeft: 50,
    };

    return (
        <div>

            <Chart 
                chartType="PieChart"
                data={data}
                options={options}
                width={"100%"}
                height={"250px"}
            />

        </div>
    );
}

export default FilmChart