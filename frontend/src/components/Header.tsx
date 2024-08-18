import { useState, useEffect } from "react";
import SearchBar from "./SearchBar";
import LoginButton from "./user/LoginButton";


export default function Header() {

    return (
        <header className="w-full flex flex-row items-center justify-center space-x-9">
            <h1>Header</h1>
            <SearchBar />
            <LoginButton />
        </header>
    )
}
