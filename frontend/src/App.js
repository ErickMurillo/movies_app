import React, { Component } from 'react'
import Movies from './components/movies'
import axios from "axios";
import './App.css';

class App extends Component {
  render() {
    return (
      <Movies movies={this.state.movies} />
    )
  }

  state = {
    movies: []
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    axios
      .get("http://127.0.0.1:8000/api/movie/")
      .then((res) => this.setState({ movies: res.data }))
      .catch((err) => console.log(err));
  };

  renderDetail = (item) => {
    axios.get('http://127.0.0.1:8000/api/movie/${item.id}/');
  }

}

export default App;
