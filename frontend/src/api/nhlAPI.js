const BASE_URL = "http://localhost:8000/";

const getInit = () => {
  return {
    headers: {
      "Content-Type": "application/json",
    },
  };
};

const tryCatchFetch = async (url, init) => {
  try {
    let response = await fetch(url, init);
    if (response.ok) {
      if (response.status !== 204) {
        let data = response.json();
        return data;
      } else {
        return { success: true };
      }
    }
  } catch (error) {
    console.error(":ERR:", error);
    return null;
  }
};

const getLeagues = async () => {
  let url = `${BASE_URL}api/leagues/`;
  return await tryCatchFetch(url, getInit());
};

const getLeagueById = async (leagueId) => {
  let url = `${BASE_URL}api/leagues/${leagueId}/`;
  return await tryCatchFetch(url, getInit());
};

const myExports = {
  getLeagues,
  getLeagueById,
};

export default myExports;
