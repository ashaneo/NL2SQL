import React, { useState } from "react";
import axios from "axios";

function QueryForm({ dbCredentials, setQueryResults }) {
  const [question, setQuestion] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post("/api/query", {
        dbCredentials,
        question,
      });
      setQueryResults(response.data); // Assuming the response contains both the SQL query and results
      alert("Query submitted and results fetched!");
    } catch (error) {
      console.error("Failed to submit query or fetch results", error);
      alert("Failed to submit query.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Ask a Question</h2>
      <textarea
        value={question}
        onChange={(e) => setQuestion(e.target.value)}
        required
      />
      <button type="submit">Submit Question</button>
    </form>
  );
}

export default QueryForm;
