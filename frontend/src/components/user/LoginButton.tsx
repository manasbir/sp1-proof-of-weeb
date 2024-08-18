import axios from "axios";
import { useEffect, useState } from "react";


export default function LoginButton() {

    const code = new URLSearchParams(window.location.search).get('code')

    const handleLogin = async () => {
        login();
    };

    const [jwt, setJWT] = useState<string | null>(getJWTToken());

    if (jwt) {
        return (
            <h1>Logged in</h1>
        )

    } else if (code) {
        getUuid(code, setJWT);
        return (
            <h1>Loading</h1>
        )
    } else {
        return (
            <button onClick={handleLogin}>Login</button>
        )
    }

}


function getJWTToken() {
    return localStorage.getItem('jwt');
}

function login() {
    const clientId = import.meta.env.VITE_CLIENT_ID;
    const codeChallenge = randomPenis();
    localStorage.setItem("codeChallenge", codeChallenge);

    const authUrl = `https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id=${clientId}&code_challenge=${codeChallenge}&code_challenge_method=plain`;

    window.open(authUrl)!.focus();

    localStorage.setItem("codeChallenge", codeChallenge);
}


function randomPenis() {
    const penis_variants = [
        "penis",
        "p3nis",
        "pen1s",
        "pen15",
        "p3n1s",
        "p3n15",
        "-",
        ".",
        "_",
        "~",
    ]
    const length = Math.floor(Math.random() * 83) + 44;
    let str = "";

    while (str.length < length) {
        const option = penis_variants[Math.floor(Math.random() * penis_variants.length)];
        for (let i = 0; i < option.length && str.length < length; i ++) {
            const char = Math.random() < 0.5 ? option[i] : option[i].toUpperCase();
            str += Math.random() < 0.05 ? ["-", ".", "_", "~", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"][Math.floor(Math.random() * 14)] : char;
        }
    }
    return str;
}

async function getUuid(code, setFn) {
    const codeChallenge = localStorage.getItem("codeChallenge")

    try {
        const response = await axios.post("http://localhost:3000/", {
            code: code,
            codeChallenge: codeChallenge!
        });
        
        console.log(response.data)

        setFn(response.data.jwt)

    } catch {
        localStorage.removeItem("codeChallenge")
        alert("Failed Login")
    }
}