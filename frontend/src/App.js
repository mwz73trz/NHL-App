import "./App.css";
import { Component } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";

class App extends Component {
  render() {
    return (
      <div className="App">
        <Router>
          <Routes>
            <Route to="/" element={<App />} />
            <Route index element={<HomePage />} />
          </Routes>
        </Router>
      </div>
    );
  }
}

export default App;
