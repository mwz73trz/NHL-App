import { Component } from "react";
import { Link, Outlet } from "react-router-dom";
import nhlAPI from "../api/nhlAPI";

class Leagues extends Component {
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
        <Link
          style={{ display: "block", margin: "1rem 0" }}
          to={`/leagues/${league.id}`}
          key={`league-${index}`}
        >
          {league.name}
        </Link>
      );
    });
    return (
      <div style={{ display: "flex" }}>
        <nav style={{ borderRight: "solid 1px", padding: "1rem" }}>
          {leagueElements}
        </nav>
        <Outlet />
      </div>
    );
  }

  render() {
    return <div>{this.renderWelcome()}</div>;
  }
}

export default Leagues;
