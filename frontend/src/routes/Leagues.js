import { Link } from "react-router-dom";
import nhlAPI from "../api/nhlAPI";

export default function Leagues() {
  let leaguesData = nhlAPI.getLeagues();
  let leagues = [leaguesData];

  console.log("This is the leagues:", leagues);
  return (
    <div style={{ display: "flex" }}>
      <nav style={{ borderRight: "solid 1px", padding: "1rem" }}>
        {leagues.map((league) => (
          <Link
            style={{ display: "block", margin: "1rem 0" }}
            to={`/leagues/${league.id}`}
            key={`league-${league.id}`}
          >
            {league.name}
          </Link>
        ))}
      </nav>
    </div>
  );
}
