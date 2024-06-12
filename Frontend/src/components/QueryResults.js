import React from "react";
import "./styles/QueryResults.css"; 

function QueryResults({ results }) {
  return (
    <div className="query-results">
      <h2>Query Results</h2>
      {results && (
        <div>
          <p>
            <strong>SQL Query:</strong> {results.sqlQuery}
          </p>
        </div>
      )}
    </div>
  );
}

export default QueryResults;
