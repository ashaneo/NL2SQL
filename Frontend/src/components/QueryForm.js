import React, { useState } from "react";
import axios from "axios";
import "./styles/QueryForm.css"; // Make sure the path to the CSS file is correct

function QueryForm({ dbCredentials, setQueryResults }) {
  const [question, setQuestion] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    setMessage("Submitting your query...");
    try {
      const response = await axios.post("http://localhost:5000/api/question", {
        question,
      });
      setQueryResults(response.data);
      setMessage("Query submitted successfully and results fetched.");
    } catch (error) {
      console.error("Failed to submit query or fetch results", error);
      setMessage("Failed to submit query. Please try again.");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit} className="query-form">
        <h2>Ask a Question</h2>
        <textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          required
          placeholder="Type your SQL-related question here..."
          className="query-textarea"
        />
        <button type="submit" className="query-submit-button">
          Submit Question
        </button>
      </form>
      {message && <p className="message">{message}</p>}
    </div>
  );
}

export default QueryForm;
