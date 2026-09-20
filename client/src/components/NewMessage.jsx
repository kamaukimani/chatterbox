import React, { useState } from "react";

function NewMessage({ currentUser, onAddMessage }) {
  const [body, setBody] = useState("");
  const [username,setUsername]=useState("")

  function handleSubmit(e) {
    e.preventDefault();

    //fetch("http://127.0.0.1:4000/messages", {
    fetch("http://127.0.0.1:5555/messages/all",{
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      // body: JSON.stringify({
      //   username: currentUser.username,
      //   body: body,
      //   created_at:new Date(),
      // }),
      body:JSON.stringify({
        username,
        body
      })
    })
      .then((r) => r.json())
      .then((newMessage) => {
        onAddMessage(newMessage);
        setBody("");
        setUsername("");
      });
  }

  return (
    <form className="new-message" onSubmit={handleSubmit}>
      <label>
        Enter Username:
        <input
        type="text"
        name="username"
        value={username}
        onChange={e=>setUsername(e.target.value)}
        />
      </label><br/>
      <br/>
      <label>
        Enter Body:
        <input
        type="text"
        name="body"
        autoComplete="off"
        value={body}
        onChange={(e) => setBody(e.target.value)}
      />
      </label>
      <button type="submit">Send</button>
    </form>
  );
}

export default NewMessage;