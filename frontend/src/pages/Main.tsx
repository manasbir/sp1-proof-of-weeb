import axios from "axios";
import { useState } from "react";


export default function Main() {
    const code = new URLSearchParams(window.location.search).get('code')

    if (code === null) {
    return (
        <div>
            <h1>React + Vite + Tailwind CSS</h1>
            <button onClick={login}>Login</button>
            <h2>{randomPenis()}</h2>
        </div>
    )
    } else {
    return (
        <div>
            <h1>React + Vite + Tailwind CSS</h1>
            <button onClick={verify}>Verify</button>
        </div>
    )
    }
}


function login() {
    const clientId = '';
    const codeChallenge = randomPenis();

    const authUrl = `https://myanimelist.net/v1/oauth2/authorize?response_type=code&client_id=${clientId}&code_challenge=${codeChallenge}&code_challenge_method=plain`;

    window.open(authUrl).focus();

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