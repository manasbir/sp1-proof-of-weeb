import axios from "axios";
import { useEffect, useState } from "react";


export default function LoginButton() {

    const code = new URLSearchParams(window.location.search).get('code')

    const handleLogin = async () => {
        login();
    };

    const [jwt, setJWT] = useState<string | null>(getJWTToken());

    useEffect(() => {
        const getUuid = async (code: string, setJWT: (jwt: string) => void) => {
            const codeChallenge = localStorage.getItem("codeChallenge");
            const clientId = import.meta.env.VITE_CLIENT_ID;

            const response = await axios.post("https://myanimelist.net/v1/oauth2/token", {
                grant_type: "authorization_code",
                client_id: clientId,
                code: code,
                code_verifier: codeChallenge,
            });

            const jwt = response.data.jwt;
            const username = response.data.username;


            localStorage.setItem("jwt", jwt);
            setJWT(jwt);
            
            window.open(window.location.origin + "/user/@self");
        
        }

        if (code) {
            getUuid(code, setJWT);
        }
    })

    if (jwt) {
        return (
            <h1>Logged in</h1>
        )

    } else if (code) {
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