import { Component } from "react";
import nhlAPI from "../api/nhlAPI";

class LeagueStandingsPage extends Component {
  state = {
    league: null,
  };

  getLeague = async () => {
    try {
      let leagueId = this.props.match.params.leagueId;
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
      return (
        <tbody key={`team-${index}`}>
          <tr>
            <td>{team.name}</td>
            <td>{team.gp}</td>
            <td>{team.wins}</td>
            <td>{team.losses}</td>
            <td>{team.ot}</td>
            <td>{team.points}</td>
          </tr>
        </tbody>
      );
    });
    return (
      <table border="1">
        <thead>
          <tr>
            <th>Team</th>
            <th>Games Played</th>
            <th>Wins</th>
            <th>Losses</th>
            <th>Overtimes</th>
            <th>Points</th>
          </tr>
        </thead>
        {teamElements}
      </table>
    );
  }

  renderLeague() {
    if (!this.state.league) {
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
        <h1>League Standings Page</h1>
        {this.renderLeague()}
      </div>
    );
  }
}

export default LeagueStandingsPage;
