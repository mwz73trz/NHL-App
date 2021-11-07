import { Component } from "react";
import nhlAPI from "../api/nhlAPI";
import Leagues from "../components/Leagues";

class HomePage extends Component {
  state = {
    leagues: [],
  };

  getLeagues = async () => {
    try {
      let leaguesData = await nhlAPI.getLeagues();
      this.setState({ leagues: leaguesData });
    } catch (error) {
      console.log(error);
    }
  };

  componentDidMount() {
    this.getLeagues();
  }

  renderWelcome() {
    let leagueElements = this.state.leagues.map((league, index) => {
      return (
        <li key={`league-${index}`}>
          <Leagues league={league} />
        </li>
      );
    });
    return <ul style={{ listStyle: "none" }}>{leagueElements}</ul>;
  }

  render() {
    return (
      <div>
        <h1>Home Page</h1>
        {this.renderWelcome()}
      </div>
    );
  }
}

export default HomePage;
