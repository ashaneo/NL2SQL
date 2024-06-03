import React, { useState } from "react";
import axios from "axios";

function DatabaseForm({ setDbCredentials }) {
  const [credentials, setCredentials] = useState({
    host: "",
    user: "",
    password: "",
    database: "",
  });

  const handleChange = (e) => {
    setCredentials({
      ...credentials,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:5000/api/db_credentials",
        credentials
      );
      setDbCredentials(credentials); // Store credentials in a parent component state
      alert("Database credentials saved!");
    } catch (error) {
      console.error("Failed to save credentials", error);
      alert("Failed to save database credentials.");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Enter Database Credentials</h2>
      <input
        type="text"
        name="host"
        placeholder="Host"
        value={credentials.host}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="user"
        placeholder="Username"
        value={credentials.user}
        onChange={handleChange}
        required
      />
      <input
        type="password"
        name="password"
        placeholder="Password"
        value={credentials.password}
        onChange={handleChange}
        required
      />
      <input
        type="text"
        name="database"
        placeholder="Database Name"
        value={credentials.database}
        onChange={handleChange}
        required
      />
      <button type="submit">Save Credentials</button>
    </form>
  );
}

export default DatabaseForm;
