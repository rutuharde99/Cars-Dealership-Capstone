import React from "react";

export default function Register() {
  const handleSubmit = (event) => {
    event.preventDefault();
    alert("Registration form submitted");
  };

  const fields = [
    { label: "Username", name: "username", type: "text" },
    { label: "First Name", name: "first_name", type: "text" },
    { label: "Last Name", name: "last_name", type: "text" },
    { label: "Email", name: "email", type: "email" },
    { label: "Password", name: "password", type: "password" },
  ];

  return (
    <main style={{ maxWidth: "420px", margin: "40px auto", padding: "24px" }}>
      <h1>Sign-up</h1>
      <form onSubmit={handleSubmit}>
        {fields.map((field) => (
          <div key={field.name} style={{ marginBottom: "16px" }}>
            <label htmlFor={field.name}>{field.label}</label>
            <input
              id={field.name}
              name={field.name}
              type={field.type}
              required
              style={{
                display: "block",
                width: "100%",
                padding: "10px",
                marginTop: "6px",
                boxSizing: "border-box",
              }}
            />
          </div>
        ))}
        <button type="submit">Register</button>
      </form>
    </main>
  );
}
