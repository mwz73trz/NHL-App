import { Component } from "react";
import nhlAPI from "../api/nhlAPI";

class LeagueStandings extends Component {
  state = {
    id: this.props.match.params.id,
    league: null,
  };

  getLeague = async () => {
    try {
      let leagueId = this.state.id;
      let leagueData = await nhlAPI.getLeagueById(leagueId);
      if (leagueData) {
        this.setState({ league: leagueData });
      }
    } catch (error) {
      console.log(error);
    }
  };

  componentDidMount() {
    this.getLeague();
  }

  renderTeams() {
    let teamElements = this.state.league.teams.map((team, index) => {
      return <li key={`team-${index}`}>{team.name}</li>;
    });
    return <ul>{teamElements}</ul>;
  }

  renderLeague() {
    if (!this.league) {
      return <p>No Teams Found!</p>;
    }
    return (
      <div>
        <h1>{this.state.league.name}</h1>
        {this.renderTeams()}
      </div>
    );
  }

  render() {
    return (
      <div>
        <h1>League Standings</h1>
        {this.renderLeague()}
      </div>
    );
  }
}

export default LeagueStandings;
