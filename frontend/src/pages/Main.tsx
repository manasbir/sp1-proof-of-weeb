import { useEffect, useState } from "react";
import Loading from "./Loading";
import axios from "axios";


export default function Main() {
    let token = new URLSearchParams(window.location.search).get('code')

    const [userData, setUserData] = useState<any | null>(null);
    const [code, setCode] = useState<string | null>(null);

    const handleLogin = async () => {
        login(setCode);
    };

    useEffect(() => {
        setCode(localStorage.getItem("codeChallenge"));
    }, [])

    useEffect(() => {
        if (token == null || code == null) {
            return;
        }
        getUserData(token, code, setUserData)
    }, [token, code])

    if (token !== null) {
        localStorage.setItem("token", token);
    } else {
        token = localStorage.getItem("token");
    }

    if (token === null) {
        if (localStorage.getItem("token") === null) {
            return (
                <div>
                    <h1>React + Vite + Tailwind CSS</h1>
                    <button onClick={handleLogin}>Login</button>
                    <h2>{randomPenis()}</h2>    
                </div>
            )
        }
    } else {
        return (
            <>
                {userData == null ? <div><p>{code}</p><p>{token}</p><Loading /></div> : <h1>{window.location.origin + "/user/" + userData.data.username}</h1>}
            </>
        )
    }
}
