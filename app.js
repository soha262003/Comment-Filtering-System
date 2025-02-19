import React, { useState } from "react";
import axios from "axios";

function App() {
    const [comment, setComment] = useState("");
    const [isAllowed, setIsAllowed] = useState(true);
    const [message, setMessage] = useState("");

    const checkComment = async (text) => {
        try {
            const response = await axios.post("http://localhost:5000/check-comment", { text });

            console.log("API Response:", response.data);  // ✅ Debugging line

            setIsAllowed(response.data.allowed);
            setMessage(response.data.message);
        } catch (error) {
            console.error("Error checking comment:", error);
            setIsAllowed(false);  // If there's an error, disable the button
            setMessage("Error checking comment.");
        }
    };

    const handleChange = (e) => {
        const text = e.target.value;
        setComment(text);
        checkComment(text);
    };

    return (
        <div style={{ textAlign: "center", marginTop: "50px" }}>
            <h2>Comment Filter</h2>
            <textarea
                value={comment}
                onChange={handleChange}
                placeholder="Write your comment..."
                rows="5"
                cols="50"
            />
            <br />
            <button disabled={!isAllowed} style={{ marginTop: "10px", padding: "10px 20px" }}>
                Send
            </button>
            <p style={{ color: isAllowed ? "green" : "red" }}>{message}</p>
        </div>
    );
}

export default App;
