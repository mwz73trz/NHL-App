import "./App.css";
import { Component } from "react";
import { BrowserRouter, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import LeagueStandingsPage from "./pages/LeagueStandingsPage";

class App extends Component {
  render() {
    return (
      <div className="App">
        <BrowserRouter>
          <Route path="/" exact component={HomePage} />
          <Route
            path="/leagues/:leagueId"
            exact
            component={LeagueStandingsPage}
          />
        </BrowserRouter>
      </div>
    );
  }
}

export default App;
