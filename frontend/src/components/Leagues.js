import { Component } from "react";

class Leagues extends Component {
  render() {
    return (
      <span>
        <h3>{this.props.league.name}</h3>
      </span>
    );
  }
}

export default Leagues;
