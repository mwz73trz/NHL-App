import "./App.css";
import { Component } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import HomePage from "./pages/HomePage";
import LeagueStandingsPage from "./pages/LeagueStandingsPage";

class App extends Component {
  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route
              path="/leagues/:leagueId"
              element={<LeagueStandingsPage />}
            />
          </Routes>
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
