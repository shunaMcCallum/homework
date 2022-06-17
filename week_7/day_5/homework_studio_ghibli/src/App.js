import React from 'react';
import FilmContainer from './containers/FilmContainer';
import './App.css';

function App() {


  return (
    <div className="app" style={{
      backgroundImage: `url(https://cdn.vox-cdn.com/thumbor/s2_cd1uqU2wT_uy6vx4-GRESV8k=/1400x1050/filters:format(jpeg)/cdn.vox-cdn.com/uploads/chorus_asset/file/19996673/Studio_Ghibli_Logo.jpg)`
    }}>
      <FilmContainer />
    </div>
  );
}

export default App;
